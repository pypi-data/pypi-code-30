# Copyright (c) 2014 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import re

import ast
import six

oslo_namespace_imports_dot = re.compile(r"import[\s]+oslo[.][^\s]+")
oslo_namespace_imports_from_dot = re.compile(r"from[\s]+oslo[.]")
oslo_namespace_imports_from_root = re.compile(r"from[\s]+oslo[\s]+import[\s]+")
mock_imports_directly = re.compile(r"import[\s]+mock")
mock_imports_direclty_from = re.compile(r"from[\s]+mock[\s]+import[\s]+")


def check_oslo_namespace_imports(logical_line):
    if re.match(oslo_namespace_imports_from_dot, logical_line):
        msg = ("O323: '%s' must be used instead of '%s'.") % (
            logical_line.replace('oslo.', 'oslo_'),
            logical_line)
        yield(0, msg)
    elif re.match(oslo_namespace_imports_from_root, logical_line):
        msg = ("O323: '%s' must be used instead of '%s'.") % (
            logical_line.replace('from oslo import ', 'import oslo_'),
            logical_line)
        yield(0, msg)
    elif re.match(oslo_namespace_imports_dot, logical_line):
        msg = ("O323: '%s' must be used instead of '%s'.") % (
            logical_line.replace('import', 'from').replace('.', ' import '),
            logical_line)
        yield(0, msg)


def check_mock_imports(logical_line):
    if re.match(mock_imports_directly, logical_line):
        msg = ("O324: '%s' must be used instead of '%s'.") % (
            logical_line.replace('import mock', 'from six.moves import mock'),
            logical_line)
        yield(0, msg)
    elif re.match(mock_imports_direclty_from, logical_line):
        msg = "O324: Use mock from six.moves."
        yield(0, msg)


class BaseASTChecker(ast.NodeVisitor):
    """Provides a simple framework for writing AST-based checks.

    Subclasses should implement visit_* methods like any other AST visitor
    implementation. When they detect an error for a particular node the
    method should call ``self.add_error(offending_node)``. Details about
    where in the code the error occurred will be pulled from the node
    object.

    Subclasses should also provide a class variable named CHECK_DESC to
    be used for the human readable error message.

    """

    def __init__(self, tree, filename):
        """This object is created automatically by pep8.

        :param tree: an AST tree
        :param filename: name of the file being analyzed
                         (ignored by our checks)
        """
        self._tree = tree
        self._errors = []

    def run(self):
        """Called automatically by pep8."""
        self.visit(self._tree)
        return self._errors

    def add_error(self, node, message=None):
        """Add an error caused by a node to the list of errors for pep8."""
        message = message or self.CHECK_DESC
        error = (node.lineno, node.col_offset, message, self.__class__)
        self._errors.append(error)


class CheckForLoggingIssues(BaseASTChecker):

    DEBUG_CHECK_DESC = 'O324 Using translated string in debug logging'
    NONDEBUG_CHECK_DESC = 'O325 Not using translating helper for logging'
    EXCESS_HELPER_CHECK_DESC = 'O326 Using hints when _ is necessary'
    LOG_MODULES = ('logging')
    I18N_MODULES = (
        'oslo_messaging._i18n._',
        'oslo_messaging._i18n._LI',
        'oslo_messaging._i18n._LW',
        'oslo_messaging._i18n._LE',
        'oslo_messaging._i18n._LC',
    )
    TRANS_HELPER_MAP = {
        'debug': None,
        'info': '_LI',
        'warn': '_LW',
        'warning': '_LW',
        'error': '_LE',
        'exception': '_LE',
        'critical': '_LC',
    }

    def __init__(self, tree, filename):
        super(CheckForLoggingIssues, self).__init__(tree, filename)

        self.logger_names = []
        self.logger_module_names = []
        self.i18n_names = {}

        # NOTE(dstanek): this kinda accounts for scopes when talking
        # about only leaf node in the graph
        self.assignments = {}

    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        item._parent = node
                        self.visit(item)
            elif isinstance(value, ast.AST):
                value._parent = node
                self.visit(value)

    def _filter_imports(self, module_name, alias):
        """Keeps lists of logging and i18n imports."""
        if module_name in self.LOG_MODULES:
            self.logger_module_names.append(alias.asname or alias.name)
        elif module_name in self.I18N_MODULES:
            self.i18n_names[alias.asname or alias.name] = alias.name

    def visit_Import(self, node):
        for alias in node.names:
            self._filter_imports(alias.name, alias)
        return super(CheckForLoggingIssues, self).generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            full_name = '%s.%s' % (node.module, alias.name)
            self._filter_imports(full_name, alias)
        return super(CheckForLoggingIssues, self).generic_visit(node)

    def _find_name(self, node):
        """Return the fully qualified name or a Name or Attribute."""
        if isinstance(node, ast.Name):
            return node.id
        elif (isinstance(node, ast.Attribute)
                and isinstance(node.value, (ast.Name, ast.Attribute))):
            method_name = node.attr
            obj_name = self._find_name(node.value)
            if obj_name is None:
                return None
            return obj_name + '.' + method_name
        elif isinstance(node, six.string_types):
            return node
        else:  # could be Subscript, Call or many more
            return None

    def visit_Assign(self, node):
        """Look for 'LOG = logging.getLogger'

        This handles the simple case:
          name = [logging_module].getLogger(...)

          - or -

          name = [i18n_name](...)

        And some much more comple ones:
          name = [i18n_name](...) % X

          - or -

          self.name = [i18n_name](...) % X

        """
        attr_node_types = (ast.Name, ast.Attribute)

        if (len(node.targets) != 1
                or not isinstance(node.targets[0], attr_node_types)):
            # say no to: "x, y = ..."
            return super(CheckForLoggingIssues, self).generic_visit(node)

        target_name = self._find_name(node.targets[0])

        if (isinstance(node.value, ast.BinOp) and
                isinstance(node.value.op, ast.Mod)):
            if (isinstance(node.value.left, ast.Call) and
                    isinstance(node.value.left.func, ast.Name) and
                    node.value.left.func.id in self.i18n_names):
                # NOTE(dstanek): this is done to match cases like:
                # `msg = _('something %s') % x`
                node = ast.Assign(value=node.value.left)

        if not isinstance(node.value, ast.Call):
            # node.value must be a call to getLogger
            self.assignments.pop(target_name, None)
            return super(CheckForLoggingIssues, self).generic_visit(node)

        # is this a call to an i18n function?
        if (isinstance(node.value.func, ast.Name)
                and node.value.func.id in self.i18n_names):
            self.assignments[target_name] = node.value.func.id
            return super(CheckForLoggingIssues, self).generic_visit(node)

        if (not isinstance(node.value.func, ast.Attribute)
                or not isinstance(node.value.func.value, attr_node_types)):
            # function must be an attribute on an object like
            # logging.getLogger
            return super(CheckForLoggingIssues, self).generic_visit(node)

        object_name = self._find_name(node.value.func.value)
        func_name = node.value.func.attr

        if (object_name in self.logger_module_names
                and func_name == 'getLogger'):
            self.logger_names.append(target_name)

        return super(CheckForLoggingIssues, self).generic_visit(node)

    def visit_Call(self, node):
        """Look for the 'LOG.*' calls."""
        # obj.method
        if isinstance(node.func, ast.Attribute):
            obj_name = self._find_name(node.func.value)
            if isinstance(node.func.value, ast.Name):
                method_name = node.func.attr
            elif isinstance(node.func.value, ast.Attribute):
                obj_name = self._find_name(node.func.value)
                method_name = node.func.attr
            else:  # could be Subscript, Call or many more
                return super(CheckForLoggingIssues, self).generic_visit(node)

            # if dealing with a logger the method can't be "warn"
            if obj_name in self.logger_names and method_name == 'warn':
                msg = node.args[0]  # first arg to a logging method is the msg
                self.add_error(msg, message=self.USING_DEPRECATED_WARN)

            # must be a logger instance and one of the support logging methods
            if (obj_name not in self.logger_names
                    or method_name not in self.TRANS_HELPER_MAP):
                return super(CheckForLoggingIssues, self).generic_visit(node)

            # the call must have arguments
            if not node.args:
                return super(CheckForLoggingIssues, self).generic_visit(node)

            if method_name == 'debug':
                self._process_debug(node)
            elif method_name in self.TRANS_HELPER_MAP:
                self._process_non_debug(node, method_name)

        return super(CheckForLoggingIssues, self).generic_visit(node)

    def _process_debug(self, node):
        msg = node.args[0]  # first arg to a logging method is the msg

        # if first arg is a call to a i18n name
        if (isinstance(msg, ast.Call)
                and isinstance(msg.func, ast.Name)
                and msg.func.id in self.i18n_names):
            self.add_error(msg, message=self.DEBUG_CHECK_DESC)

        # if the first arg is a reference to a i18n call
        elif (isinstance(msg, ast.Name)
                and msg.id in self.assignments
                and not self._is_raised_later(node, msg.id)):
            self.add_error(msg, message=self.DEBUG_CHECK_DESC)

    def _process_non_debug(self, node, method_name):
        msg = node.args[0]  # first arg to a logging method is the msg

        # if first arg is a call to a i18n name
        if isinstance(msg, ast.Call):
            try:
                func_name = msg.func.id
            except AttributeError:
                # in the case of logging only an exception, the msg function
                # will not have an id associated with it, for instance:
                # LOG.warning(six.text_type(e))
                return

            # the function name is the correct translation helper
            # for the logging method
            if func_name == self.TRANS_HELPER_MAP[method_name]:
                return

            # the function name is an alias for the correct translation
            # helper for the loggine method
            if (self.i18n_names[func_name] ==
                    self.TRANS_HELPER_MAP[method_name]):
                return

            self.add_error(msg, message=self.NONDEBUG_CHECK_DESC)

        # if the first arg is not a reference to the correct i18n hint
        elif isinstance(msg, ast.Name):

            # FIXME(dstanek): to make sure more robust we should be checking
            # all names passed into a logging method. we can't right now
            # because:
            # 1. We have code like this that we'll fix when dealing with the %:
            #       msg = _('....') % {}
            #       LOG.warning(msg)
            # 2. We also do LOG.exception(e) in several places. I'm not sure
            #    exactly what we should be doing about that.
            if msg.id not in self.assignments:
                return

            helper_method_name = self.TRANS_HELPER_MAP[method_name]
            if (self.assignments[msg.id] != helper_method_name
                    and not self._is_raised_later(node, msg.id)):
                self.add_error(msg, message=self.NONDEBUG_CHECK_DESC)
            elif (self.assignments[msg.id] == helper_method_name
                    and self._is_raised_later(node, msg.id)):
                self.add_error(msg, message=self.EXCESS_HELPER_CHECK_DESC)

    def _is_raised_later(self, node, name):

        def find_peers(node):
            node_for_line = node._parent
            for _field, value in ast.iter_fields(node._parent._parent):
                if isinstance(value, list) and node_for_line in value:
                    return value[value.index(node_for_line) + 1:]
                continue
            return []

        peers = find_peers(node)
        for peer in peers:
            if isinstance(peer, ast.Raise):
                if six.PY3:
                    exc = peer.exc
                else:
                    exc = peer.type
                if (isinstance(exc, ast.Call) and
                        len(exc.args) > 0 and
                        isinstance(exc.args[0], ast.Name) and
                        name in (a.id for a in exc.args)):
                    return True
                else:
                    return False
            elif isinstance(peer, ast.Assign):
                if name in (t.id for t in peer.targets if hasattr(t, 'id')):
                    return False


def factory(register):
    register(CheckForLoggingIssues)
    register(check_oslo_namespace_imports)
    register(check_mock_imports)
