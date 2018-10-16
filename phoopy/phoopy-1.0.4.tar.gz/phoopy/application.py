# -*- coding: utf-8 -*-

from cleo import Application as BaseApplication
from cleo.inputs.input import Input
from cleo.exceptions import MissingArguments
from cleo.inputs.input_option import InputOption
from .proxy_command import ProxyCommand


class ApplicationException(Exception):
    pass


class Application(BaseApplication):
    def __init__(self, kernel):
        super(Application, self).__init__()
        self.__kernel = kernel
        self.__kernel.boot()
        self.__container = kernel.get_container()

    def run(self, input_=None, output_=None):
        self.monkeypatch_validation()
        return super(Application, self).run(input_, output_)

    def do_run(self, input_, output_):
        self.setup_application(input_)

        for command in self.__container.get('command.tag'):
            self.add_command_proxy(command['class_instance'], command['key'])

        return super(Application, self).do_run(input_, output_)

    def add_command_proxy(self, command, service_key):
        self.add(ProxyCommand(command, service_key, self.__container))

    def get_default_input_definition(self):
        definition = super(Application, self).get_default_input_definition()
        definition.add_option(InputOption('--env', None, InputOption.VALUE_OPTIONAL, 'Application environment'))
        return definition

    def setup_application(self, input_):
        # self.setup_environment(input_)
        self.setup_logging()

    # def setup_environment(self, input_):
    #     env = input_.get_parameter_option('--env', None)
    #     if not env:
    #         return
    #     service_path = path.join(s, env, 'services.py')
    #     if not path.exists(service_path):
    #         raise UsageException('Environment services.py not found at: {}'.format(service_path))
    #     module = self.import_module_by_path(service_path)
    #     if not hasattr(module, 'dependencies'):
    #         raise UsageException('Environment services.py does not contains dependencies')
    #     for key in module.dependencies:
    #         self.__container[key] = module.dependencies[key]

    # def import_module_by_path(self, path):
    #     path_backup = sys.path[:]
    #     sys.path = [os.path.dirname(path)] + sys.path
    #     module_name = os.path.basename(path).split('.py')[0]
    #     module = __import__(module_name, globals(), locals(), [], 0)
    #     sys.path = path_backup
    #     return module

    def setup_logging(self):
        self.logger = self.__container['logger']

    def monkeypatch_validation(self):
        #  Temporary monkey patching
        def validate(self):
            missing_args = []
            given_args = self.get_arguments()
            for argument in self.definition.get_arguments():
                if argument.is_required() and \
                        given_args.get(argument.get_name()) is None:
                    missing_args.append(argument.get_name())
            if len(missing_args):
                raise MissingArguments(
                    'Missing required arguments: {}'.format(','.join(missing_args))
                )

            self.validate_arguments()
            self.validate_options()

        Input.validate = validate

    def render_exception(self, e, output_):
        super(Application, self).render_exception(e, output_)
        if self.logger and 'cleo.exceptions' not in e.__class__.__module__ and e.__class__ is not ApplicationException:
            self.logger.exception('Exception')
