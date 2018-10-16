# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import collections
import contextlib
import copy
import functools
import inspect
import logging

from future.utils import raise_with_traceback

from mobly import controller_manager
from mobly import expects
from mobly import records
from mobly import runtime_test_info
from mobly import signals
from mobly import utils

# Macro strings for test result reporting.
TEST_CASE_TOKEN = '[Test]'
RESULT_LINE_TEMPLATE = TEST_CASE_TOKEN + ' %s %s'

TEST_STAGE_BEGIN_LOG_TEMPLATE = '[{parent_token}]#{child_token} >>> BEGIN >>>'
TEST_STAGE_END_LOG_TEMPLATE = '[{parent_token}]#{child_token} <<< END <<<'

# Names of execution stages, in the order they happen during test runs.
STAGE_NAME_SETUP_GENERATED_TESTS = 'setup_generated_tests'
STAGE_NAME_SETUP_CLASS = 'setup_class'
STAGE_NAME_SETUP_TEST = 'setup_test'
STAGE_NAME_TEARDOWN_TEST = 'teardown_test'
STAGE_NAME_TEARDOWN_CLASS = 'teardown_class'


class Error(Exception):
    """Raised for exceptions that occured in BaseTestClass."""


class BaseTestClass(object):
    """Base class for all test classes to inherit from.

    This class gets all the controller objects from test_runner and executes
    the tests requested within itself.

    Most attributes of this class are set at runtime based on the configuration
    provided.

    The default logger in logging module is set up for each test run. If you
    want to log info to the test run output file, use `logging` directly, like
    `logging.info`.

    Attributes:
        tests: A list of strings, each representing a test method name.
        TAG: A string used to refer to a test class. Default is the test class
            name.
        results: A records.TestResult object for aggregating test results from
            the execution of tests.
        controller_configs: dict, controller configs provided by the user via
            test bed config.
        current_test_name: [Deprecated, use `self.current_test_info.name`]
            A string that's the name of the test method currently being
            executed. If no test is executing, this should be None.
        current_test_info: RuntimeTestInfo, runtime information on the test
            currently being executed.
        log_path: string, specifies the root directory for all logs written
            by a test run.
        test_bed_name: string, the name of the test bed used by a test run.
        user_params: dict, custom parameters from user, to be consumed by
            the test logic.
    """

    TAG = None

    def __init__(self, configs):
        """Constructor of BaseTestClass.

        The constructor takes a config_parser.TestRunConfig object and which has
        all the information needed to execute this test class, like log_path
        and controller configurations. For details, see the definition of class
        config_parser.TestRunConfig.

        Args:
            configs: A config_parser.TestRunConfig object.
        """
        self.tests = []
        self._class_name = self.__class__.__name__
        if configs.test_class_name_suffix and self.TAG is None:
            self.TAG = '%s_%s' % (self._class_name,
                                  configs.test_class_name_suffix)
        elif self.TAG is None:
            self.TAG = self._class_name
        # Set params.
        self.log_path = configs.log_path
        self.test_bed_name = configs.test_bed_name
        self.user_params = configs.user_params
        self.results = records.TestResult()
        self.summary_writer = configs.summary_writer
        # Deprecated, use `self.current_test_info.name`.
        self.current_test_name = None
        self._generated_test_table = collections.OrderedDict()
        self._controller_manager = controller_manager.ControllerManager(
            class_name=self.TAG, controller_configs=configs.controller_configs)
        self.controller_configs = self._controller_manager.controller_configs

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self._safe_exec_func(self.clean_up)

    def unpack_userparams(self,
                          req_param_names=None,
                          opt_param_names=None,
                          **kwargs):
        """An optional function that unpacks user defined parameters into
        individual variables.

        After unpacking, the params can be directly accessed with self.xxx.

        If a required param is not provided, an exception is raised. If an
        optional param is not provided, a warning line will be logged.

        To provide a param, add it in the config file or pass it in as a kwarg.
        If a param appears in both the config file and kwarg, the value in the
        config file is used.

        User params from the config file can also be directly accessed in
        self.user_params.

        Args:
            req_param_names: A list of names of the required user params.
            opt_param_names: A list of names of the optional user params.
            **kwargs: Arguments that provide default values.
                e.g. unpack_userparams(required_list, opt_list, arg_a='hello')
                self.arg_a will be 'hello' unless it is specified again in
                required_list or opt_list.

        Raises:
            Error: A required user params is not provided.
        """
        req_param_names = req_param_names or []
        opt_param_names = opt_param_names or []
        for k, v in kwargs.items():
            if k in self.user_params:
                v = self.user_params[k]
            setattr(self, k, v)
        for name in req_param_names:
            if hasattr(self, name):
                continue
            if name not in self.user_params:
                raise Error('Missing required user param "%s" in test '
                            'configuration.' % name)
            setattr(self, name, self.user_params[name])
        for name in opt_param_names:
            if hasattr(self, name):
                continue
            if name in self.user_params:
                setattr(self, name, self.user_params[name])
            else:
                logging.warning('Missing optional user param "%s" in '
                                'configuration, continue.', name)

    def register_controller(self, module, required=True, min_number=1):
        """Loads a controller module and returns its loaded devices.

        A Mobly controller module is a Python lib that can be used to control
        a device, service, or equipment. To be Mobly compatible, a controller
        module needs to have the following members:

        ```
        def create(configs):
            [Required] Creates controller objects from configurations.

            Args:
                configs: A list of serialized data like string/dict. Each
                    element of the list is a configuration for a controller
                    object.

            Returns:
                A list of objects.

        def destroy(objects):
            [Required] Destroys controller objects created by the create
            function. Each controller object shall be properly cleaned up
            and all the resources held should be released, e.g. memory
            allocation, sockets, file handlers etc.

            Args:
                A list of controller objects created by the create function.

        def get_info(objects):
            [Optional] Gets info from the controller objects used in a test
            run. The info will be included in test_summary.yaml under
            the key 'ControllerInfo'. Such information could include unique
            ID, version, or anything that could be useful for describing the
            test bed and debugging.

            Args:
                objects: A list of controller objects created by the create
                    function.

            Returns:
                A list of json serializable objects, each represents the
                info of a controller object. The order of the info object
                should follow that of the input objects.
        ```

        Registering a controller module declares a test class's dependency the
        controller. If the module config exists and the module matches the
        controller interface, controller objects will be instantiated with
        corresponding configs. The module should be imported first.

        Args:
            module: A module that follows the controller module interface.
            required: A bool. If True, failing to register the specified
                controller module raises exceptions. If False, the objects
                failed to instantiate will be skipped.
            min_number: An integer that is the minimum number of controller
                objects to be created. Default is one, since you should not
                register a controller module without expecting at least one
                object.

        Returns:
            A list of controller objects instantiated from controller_module, or
            None if no config existed for this controller and it was not a
            required controller.

        Raises:
            ControllerError:
                * The controller module has already been registered.
                * The actual number of objects instantiated is less than the
                * `min_number`.
                * `required` is True and no corresponding config can be found.
                * Any other error occurred in the registration process.
        """
        return self._controller_manager.register_controller(
            module, required, min_number)

    def _record_controller_info(self):
        # Collect controller information and write to test result.
        for record in self._controller_manager.get_controller_info_records():
            self.results.add_controller_info_record(record)
            self.summary_writer.dump(
                record.to_dict(), records.TestSummaryEntryType.CONTROLLER_INFO)

    def _setup_generated_tests(self):
        """Proxy function to guarantee the base implementation of
        setup_generated_tests is called.

        Returns:
            True if setup is successful, False otherwise.
        """
        stage_name = STAGE_NAME_SETUP_GENERATED_TESTS
        record = records.TestResultRecord(stage_name, self.TAG)
        record.test_begin()
        self.current_test_info = runtime_test_info.RuntimeTestInfo(
            stage_name, self.log_path, record)
        try:
            with self._log_test_stage(stage_name):
                self.setup_generated_tests()
                return True
        except Exception as e:
            logging.exception('%s failed for %s.', stage_name, self.TAG)
            record.test_error(e)
            self.results.add_class_error(record)
            self.summary_writer.dump(record.to_dict(),
                                     records.TestSummaryEntryType.RECORD)
            return False

    def setup_generated_tests(self):
        """Preprocesses that need to be done before setup_class.

        This phase is used to do pre-test processes like generating tests.
        This is the only place `self.generate_tests` should be called.

        If this function throws an error, the test class will be marked failure
        and the "Requested" field will be 0 because the number of tests
        requested is unknown at this point.
        """

    def _setup_class(self):
        """Proxy function to guarantee the base implementation of setup_class
        is called.

        Returns:
            If `self.results` is returned instead of None, this means something
            has gone wrong, and the rest of the test class should not execute.
        """
        # Setup for the class.
        class_record = records.TestResultRecord(STAGE_NAME_SETUP_CLASS,
                                                self.TAG)
        class_record.test_begin()
        self.current_test_info = runtime_test_info.RuntimeTestInfo(
            STAGE_NAME_SETUP_CLASS, self.log_path, class_record)
        expects.recorder.reset_internal_states(class_record)
        try:
            with self._log_test_stage(STAGE_NAME_SETUP_CLASS):
                self.setup_class()
        except signals.TestAbortSignal:
            # Throw abort signals to outer try block for handling.
            raise
        except Exception as e:
            # Setup class failed for unknown reasons.
            # Fail the class and skip all tests.
            logging.exception('Error in %s#setup_class.', self.TAG)
            class_record.test_error(e)
            self.results.add_class_error(class_record)
            self._exec_procedure_func(self._on_fail, class_record)
            class_record.update_record()
            self.summary_writer.dump(class_record.to_dict(),
                                     records.TestSummaryEntryType.RECORD)
            self._skip_remaining_tests(e)
            return self.results
        if expects.recorder.has_error:
            self._exec_procedure_func(self._on_fail, class_record)
            class_record.test_error()
            class_record.update_record()
            self.summary_writer.dump(class_record.to_dict(),
                                     records.TestSummaryEntryType.RECORD)
            self.results.add_class_error(class_record)
            self._skip_remaining_tests(
                class_record.termination_signal.exception)
            return self.results

    def setup_class(self):
        """Setup function that will be called before executing any test in the
        class.

        To signal setup failure, use asserts or raise your own exception.

        Errors raised from `setup_class` will trigger `on_fail`.

        Implementation is optional.
        """

    def _teardown_class(self):
        """Proxy function to guarantee the base implementation of
        teardown_class is called.
        """
        stage_name = STAGE_NAME_TEARDOWN_CLASS
        record = records.TestResultRecord(stage_name, self.TAG)
        record.test_begin()
        self.current_test_info = runtime_test_info.RuntimeTestInfo(
            stage_name, self.log_path, record)
        expects.recorder.reset_internal_states(record)
        try:
            with self._log_test_stage(stage_name):
                self.teardown_class()
        except signals.TestAbortAll as e:
            setattr(e, 'results', self.results)
            raise
        except Exception as e:
            logging.exception('Error encountered in %s.', stage_name)
            record.test_error(e)
            record.update_record()
            self.results.add_class_error(record)
            self.summary_writer.dump(record.to_dict(),
                                     records.TestSummaryEntryType.RECORD)
        else:
            if expects.recorder.has_error:
                record.update_record()
                self.results.add_class_error(record)
                self.summary_writer.dump(record.to_dict(),
                                         records.TestSummaryEntryType.RECORD)
        finally:
            # Write controller info and summary to summary file.
            self._record_controller_info()
            self._controller_manager.unregister_controllers()

    def teardown_class(self):
        """Teardown function that will be called after all the selected tests in
        the test class have been executed.

        Errors raised from `teardown_class` do not trigger `on_fail`.

        Implementation is optional.
        """

    @contextlib.contextmanager
    def _log_test_stage(self, stage_name):
        """Logs the begin and end of a test stage.

        This context adds two log lines meant for clarifying the boundary of
        each execution stage in Mobly log.

        Args:
            stage_name: string, name of the stage to log.
        """
        parent_token = self.current_test_info.name
        # If the name of the stage is the same as the test name, in which case
        # the stage is class-level instead of test-level, use the class's
        # reference tag as the parent token instead.
        if parent_token == stage_name:
            parent_token = self.TAG
        logging.debug(
            TEST_STAGE_BEGIN_LOG_TEMPLATE.format(
                parent_token=parent_token, child_token=stage_name))
        yield
        logging.debug(
            TEST_STAGE_END_LOG_TEMPLATE.format(
                parent_token=parent_token, child_token=stage_name))

    def _setup_test(self, test_name):
        """Proxy function to guarantee the base implementation of setup_test is
        called.
        """
        self.current_test_name = test_name
        with self._log_test_stage(STAGE_NAME_SETUP_TEST):
            self.setup_test()

    def setup_test(self):
        """Setup function that will be called every time before executing each
        test method in the test class.

        To signal setup failure, use asserts or raise your own exception.

        Implementation is optional.
        """

    def _teardown_test(self, test_name):
        """Proxy function to guarantee the base implementation of teardown_test
        is called.
        """
        with self._log_test_stage(STAGE_NAME_TEARDOWN_TEST):
            self.teardown_test()

    def teardown_test(self):
        """Teardown function that will be called every time a test method has
        been executed.

        Implementation is optional.
        """

    def _on_fail(self, record):
        """Proxy function to guarantee the base implementation of on_fail is
        called.

        Args:
            record: records.TestResultRecord, a copy of the test record for
                    this test, containing all information of the test execution
                    including exception objects.
        """
        self.on_fail(record)

    def on_fail(self, record):
        """A function that is executed upon a test failure.

        User implementation is optional.

        Args:
            record: records.TestResultRecord, a copy of the test record for
                this test, containing all information of the test execution
                including exception objects.
        """

    def _on_pass(self, record):
        """Proxy function to guarantee the base implementation of on_pass is
        called.

        Args:
            record: records.TestResultRecord, a copy of the test record for
                this test, containing all information of the test execution
                including exception objects.
        """
        msg = record.details
        if msg:
            logging.info(msg)
        self.on_pass(record)

    def on_pass(self, record):
        """A function that is executed upon a test passing.

        Implementation is optional.

        Args:
            record: records.TestResultRecord, a copy of the test record for
                this test, containing all information of the test execution
                including exception objects.
        """

    def _on_skip(self, record):
        """Proxy function to guarantee the base implementation of on_skip is
        called.

        Args:
            record: records.TestResultRecord, a copy of the test record for
                this test, containing all information of the test execution
                including exception objects.
        """
        logging.info('Reason to skip: %s', record.details)
        logging.info(RESULT_LINE_TEMPLATE, record.test_name, record.result)
        self.on_skip(record)

    def on_skip(self, record):
        """A function that is executed upon a test being skipped.

        Implementation is optional.

        Args:
            record: records.TestResultRecord, a copy of the test record for
                this test, containing all information of the test execution
                including exception objects.
        """

    def _exec_procedure_func(self, func, tr_record):
        """Executes a procedure function like on_pass, on_fail etc.

        This function will alter the 'Result' of the test's record if
        exceptions happened when executing the procedure function, but
        prevents procedure functions from altering test records themselves
        by only passing in a copy.

        This will let signals.TestAbortAll through so abort_all works in all
        procedure functions.

        Args:
            func: The procedure function to be executed.
            tr_record: The TestResultRecord object associated with the test
                executed.
        """
        func_name = func.__name__
        procedure_name = func_name[1:] if func_name[0] == '_' else func_name
        with self._log_test_stage(procedure_name):
            try:
                # Pass a copy of the record instead of the actual object so that it
                # will not be modified.
                func(copy.deepcopy(tr_record))
            except signals.TestAbortSignal:
                raise
            except Exception as e:
                logging.exception(
                    'Exception happened when executing %s for %s.',
                    procedure_name, self.current_test_name)
                tr_record.add_error(procedure_name, e)

    def record_data(self, content):
        """Record an entry in test summary file.

        Sometimes additional data need to be recorded in summary file for
        debugging or post-test analysis.

        Each call adds a new entry to the summary file, with no guarantee of
        its position among the summary file entries.

        The content should be a dict. If absent, timestamp field is added for
        ease of parsing later.

        Args:
            content: dict, the data to add to summary file.
        """
        if 'timestamp' not in content:
            content['timestamp'] = utils.get_current_epoch_time()
        self.summary_writer.dump(content,
                                 records.TestSummaryEntryType.USER_DATA)

    def exec_one_test(self, test_name, test_method, args=(), **kwargs):
        """Executes one test and update test results.

        Executes setup_test, the test method, and teardown_test; then creates a
        records.TestResultRecord object with the execution information and adds
        the record to the test class's test results.

        Args:
            test_name: Name of the test.
            test_method: The test method.
            args: A tuple of params.
            kwargs: Extra kwargs.
        """
        tr_record = records.TestResultRecord(test_name, self.TAG)
        tr_record.test_begin()
        self.current_test_info = runtime_test_info.RuntimeTestInfo(
            test_name, self.log_path, tr_record)
        expects.recorder.reset_internal_states(tr_record)
        logging.info('%s %s', TEST_CASE_TOKEN, test_name)
        # Did teardown_test throw an error.
        teardown_test_failed = False
        try:
            try:
                try:
                    self._setup_test(test_name)
                except signals.TestFailure as e:
                    raise_with_traceback(
                        signals.TestError(e.details, e.extras))
                if args or kwargs:
                    test_method(*args, **kwargs)
                else:
                    test_method()
            except signals.TestPass:
                raise
            except Exception:
                logging.exception('Exception occurred in %s.',
                                  self.current_test_name)
                raise
            finally:
                before_count = expects.recorder.error_count
                try:
                    self._teardown_test(test_name)
                except signals.TestAbortSignal:
                    raise
                except Exception as e:
                    logging.exception(e)
                    tr_record.test_error()
                    tr_record.add_error(STAGE_NAME_TEARDOWN_TEST, e)
                    teardown_test_failed = True
                else:
                    # Check if anything failed by `expects`.
                    if before_count < expects.recorder.error_count:
                        teardown_test_failed = True
        except (signals.TestFailure, AssertionError) as e:
            tr_record.test_fail(e)
        except signals.TestSkip as e:
            # Test skipped.
            tr_record.test_skip(e)
        except signals.TestAbortSignal as e:
            # Abort signals, pass along.
            tr_record.test_fail(e)
            raise e
        except signals.TestPass as e:
            # Explicit test pass.
            tr_record.test_pass(e)
        except Exception as e:
            # Exception happened during test.
            tr_record.test_error(e)
        else:
            # No exception is thrown from test and teardown, if `expects` has
            # error, the test should fail with the first error in `expects`.
            if expects.recorder.has_error and not teardown_test_failed:
                tr_record.test_fail()
            # Otherwise the test passed.
            elif not teardown_test_failed:
                tr_record.test_pass()
        finally:
            tr_record.update_record()
            try:
                if tr_record.result in (
                        records.TestResultEnums.TEST_RESULT_ERROR,
                        records.TestResultEnums.TEST_RESULT_FAIL):
                    self._exec_procedure_func(self._on_fail, tr_record)
                elif tr_record.result == records.TestResultEnums.TEST_RESULT_PASS:
                    self._exec_procedure_func(self._on_pass, tr_record)
                elif tr_record.result == records.TestResultEnums.TEST_RESULT_SKIP:
                    self._exec_procedure_func(self._on_skip, tr_record)
            finally:
                logging.info(RESULT_LINE_TEMPLATE, tr_record.test_name,
                             tr_record.result)
                self.results.add_record(tr_record)
                self.summary_writer.dump(tr_record.to_dict(),
                                         records.TestSummaryEntryType.RECORD)
                self.current_test_info = None
                self.current_test_name = None

    def _assert_function_name_in_stack(self, expected_func_name):
        """Asserts that the current stack contains the given function name."""
        current_frame = inspect.currentframe()
        caller_frames = inspect.getouterframes(current_frame, 2)
        for caller_frame in caller_frames[2:]:
            if caller_frame[3] == expected_func_name:
                return
        raise Error('"%s" cannot be called outside of %s' %
                    (caller_frames[1][3], expected_func_name))

    def generate_tests(self, test_logic, name_func, arg_sets):
        """Generates tests in the test class.

        This function has to be called inside a test class's
        `self.setup_generated_tests` function.

        Generated tests are not written down as methods, but as a list of
        parameter sets. This way we reduce code repetition and improve test
        scalability.

        Args:
            test_logic: function, the common logic shared by all the generated
                tests.
            name_func: function, generate a test name according to a set of
                test arguments. This function should take the same arguments as
                the test logic function.
            arg_sets: a list of tuples, each tuple is a set of arguments to be
                passed to the test logic function and name function.
        """
        self._assert_function_name_in_stack(STAGE_NAME_SETUP_GENERATED_TESTS)
        for args in arg_sets:
            test_name = name_func(*args)
            if test_name in self.get_existing_test_names():
                raise Error(
                    'Test name "%s" already exists, cannot be duplicated!' %
                    test_name)
            test_func = functools.partial(test_logic, *args)
            self._generated_test_table[test_name] = test_func

    def _safe_exec_func(self, func, *args):
        """Executes a function with exception safeguard.

        This will let signals.TestAbortAll through so abort_all works in all
        procedure functions.

        Args:
            func: Function to be executed.
            args: Arguments to be passed to the function.

        Returns:
            Whatever the function returns.
        """
        try:
            return func(*args)
        except signals.TestAbortAll:
            raise
        except:
            logging.exception('Exception happened when executing %s in %s.',
                              func.__name__, self.TAG)

    def get_existing_test_names(self):
        """Gets the names of existing tests in the class.

        A method in the class is considered a test if its name starts with
        'test_*'.

        Note this only gets the names of tests that already exist. If
        `setup_generated_test` has not happened when this was called, the
        generated tests won't be listed.

        Returns:
            A list of strings, each is a test method name.
        """
        test_names = []
        for name, _ in inspect.getmembers(self, inspect.ismethod):
            if name.startswith('test_'):
                test_names.append(name)
        return test_names + list(self._generated_test_table.keys())

    def _get_test_methods(self, test_names):
        """Resolves test method names to bound test methods.

        Args:
            test_names: A list of strings, each string is a test method name.

        Returns:
            A list of tuples of (string, function). String is the test method
            name, function is the actual python method implementing its logic.

        Raises:
            Error: The test name does not follow naming convention 'test_*'.
                This can only be caused by user input.
        """
        test_methods = []
        for test_name in test_names:
            if not test_name.startswith('test_'):
                raise Error('Test method name %s does not follow naming '
                            'convention test_*, abort.' % test_name)
            if hasattr(self, test_name):
                test_method = getattr(self, test_name)
            elif test_name in self._generated_test_table:
                test_method = self._generated_test_table[test_name]
            else:
                raise Error('%s does not have test method %s.' % (self.TAG,
                                                                  test_name))
            test_methods.append((test_name, test_method))
        return test_methods

    def _skip_remaining_tests(self, exception):
        """Marks any requested test that has not been executed in a class as
        skipped.

        This is useful for handling abort class signal.

        Args:
            exception: The exception object that was thrown to trigger the
                skip.
        """
        for test_name in self.results.requested:
            if not self.results.is_test_executed(test_name):
                test_record = records.TestResultRecord(test_name, self.TAG)
                test_record.test_skip(exception)
                self.results.add_record(test_record)
                self.summary_writer.dump(test_record.to_dict(),
                                         records.TestSummaryEntryType.RECORD)

    def run(self, test_names=None):
        """Runs tests within a test class.

        One of these test method lists will be executed, shown here in priority
        order:

        1. The test_names list, which is passed from cmd line. Invalid names
           are guarded by cmd line arg parsing.
        2. The self.tests list defined in test class. Invalid names are
           ignored.
        3. All function that matches test method naming convention in the test
           class.

        Args:
            test_names: A list of string that are test method names requested in
                cmd line.

        Returns:
            The test results object of this class.
        """
        # Executes pre-setup procedures, like generating test methods.
        if not self._setup_generated_tests():
            return self.results
        logging.info('==========> %s <==========', self.TAG)
        # Devise the actual test methods to run in the test class.
        if not test_names:
            if self.tests:
                # Specified by run list in class.
                test_names = list(self.tests)
            else:
                # No test method specified by user, execute all in test class.
                test_names = self.get_existing_test_names()
        self.results.requested = test_names
        self.summary_writer.dump(self.results.requested_test_names_dict(),
                                 records.TestSummaryEntryType.TEST_NAME_LIST)
        tests = self._get_test_methods(test_names)
        try:
            setup_class_result = self._setup_class()
            if setup_class_result:
                return setup_class_result
            # Run tests in order.
            for test_name, test_method in tests:
                self.exec_one_test(test_name, test_method)
            return self.results
        except signals.TestAbortClass as e:
            e.details = 'Test class aborted due to: %s' % e.details
            self._skip_remaining_tests(e)
            return self.results
        except signals.TestAbortAll as e:
            e.details = 'All remaining tests aborted due to: %s' % e.details
            self._skip_remaining_tests(e)
            # Piggy-back test results on this exception object so we don't lose
            # results from this test class.
            setattr(e, 'results', self.results)
            raise e
        finally:
            self._teardown_class()
            logging.info('Summary for test class %s: %s', self.TAG,
                         self.results.summary_str())

    def clean_up(self):
        """A function that is executed upon completion of all tests selected in
        the test class.

        This function should clean up objects initialized in the constructor by
        user.
        """
