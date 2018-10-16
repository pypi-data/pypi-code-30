# xml DOM https://docs.oracle.com/javase/8/docs/api/org/w3c/dom/Node.html

from .Writer import Writer
from .Function import Function
from .Class import Class
from .Object import Object
from .DataStorageCreators import DataStoragePhpXml
from .DataStorageCreators import DataStoragePhpJson
from .Error import Error
from .Object import AccessSpecifier
import re

SERIALIZATION = 0
DESERIALIZATION = 1


def convertInitializeValue(value):
    if value is None:
        value = 'null'
    if value == '0.0':
        value = '0.0f'
    return value


class WriterJava(Writer):

    def __init__(self, parser, serialize_format):
        self.functions_cache = {}
        self.save_visitors = False
        Writer.__init__(self, parser, serialize_format)

    def save_generated_classes(self, out_directory):
        Writer.save_generated_classes(self, out_directory)
        self.create_factory()
        self.create_visitor_acceptors()

    def write_class(self, cls, flags):
        global _pattern_file
        out = ""
        pattern = _pattern_file[self.serialize_format]
        self.current_class = cls

        if cls.type == 'enum':
            for member in cls.members:
                if member.initial_value is not None and member.name == '_value':
                    member.initial_value = cls.members[0].initial_value

        declaration_list = ''
        initialization_list = ''
        for object in cls.members:
            declare, init = self.write_object(object)
            declaration_list += declare + '\n'
            if init:
                initialization_list += init + '\n'

        self.create_serialization_function(cls, SERIALIZATION)
        self.create_serialization_function(cls, DESERIALIZATION)
        functions = ''
        for function in cls.functions:
            f = self.write_function(cls, function)
            functions += f

        imports = ''
        name = cls.name
        extend = ''
        include_patter_std = '\nimport {};'
        include_patter = '\nimport org.mlc_tools.mg.{};'
        if cls.behaviors:
            extend = ' extends ' + cls.behaviors[0].name
            imports += include_patter.format(cls.behaviors[0].name)
        for obj in cls.members:
            if self.parser.find_class(obj.type):
                if obj.type != cls.name:
                    imports += include_patter.format(obj.type)
            elif obj.type == 'list' or obj.type == 'map':
                for arg in obj.template_args:
                    if isinstance(arg, Class) and arg.name != cls.name:
                        imports += include_patter.format(arg.name)
                    elif self.parser.find_class(arg.type) and arg.type != cls.name:
                        imports += include_patter.format(arg.type)
                if obj.type == 'list' and 'java.util.ArrayList' not in imports:
                    imports += include_patter_std.format('java.util.ArrayList')
                if obj.type == 'map' and 'java.util.HashMap' not in imports:
                    imports += include_patter_std.format('java.util.HashMap')

        # imports += include_patter.format('Factory')
        if 'DataStorage' in functions:
            imports += include_patter.format('DataStorage')

        out = pattern.format(name, extend, declaration_list, functions, imports, initialization_list)
        self.current_class = None
        return {flags: out}

    def write_function(self, cls, function):
        if cls.name not in self.functions_cache:
            self.functions_cache[cls.name] = []
        if function.name == 'visit' and \
                ((cls.behaviors and cls.behaviors[0].name.startswith('IVisitor')) or cls.name.startswith('IVisitor'))\
                and function.args and len(function.args[0]) > 1:
            ctx_name = function.args[0][1]
            ctx_name = ctx_name[0].lower() + ctx_name[1:]
            ctx_name = ctx_name.replace('*', '')
            function.name = 'visit_' + ctx_name

        if function.name in self.functions_cache[cls.name]:
            Error.warning(Error.DUBLICATE_METHODS, cls.name, function.name)
            return ''
        self.functions_cache[cls.name].append(function.name)
        convert = function.name not in generated_functions and self.current_class.name != 'DataStorage'

        out = '''{3} {0}({1})
        @(
        {2}
        @)\n'''

        if function.is_static:
            out = 'public static ' + out
        else:
            out = 'public ' + out

        name = function.name
        args = ', '.join([self.build_type(x[1]) + ' ' + x[0] for x in function.args])
        ops = '\n'.join(function.operations)
        if convert:
            ops = convert_function_to_php(ops, self.parser, args)
        type = self.build_type(function.return_type)
        out = out.format(name, args, ops, type)
        return out

    def write_object(self, object):
        out_declaration = ''
        out_init = ''
        value = object.initial_value
        if value is None and not object.is_pointer:
            type = object.type
            if type == "string":
                value = '""'
            elif type == "int":
                value = "0"
            elif type == "float":
                value = "0"
            elif type == "uint":
                value = "0"
            elif type == "bool":
                value = "False"
            elif type == "list":
                value = "new ArrayList<>()"
            elif type == "map":
                value = "new HashMap<>()"
            else:
                if self.parser.find_class(object.type):
                    value = 'null'
                    out_init = 'this.{} = new {}();'.format(object.name, object.type)

        accesses = {
            AccessSpecifier.public: 'public',
            AccessSpecifier.protected: 'protected',
            AccessSpecifier.private: 'private',
        }

        if object.is_static:
            out_declaration = accesses[object.access] + ' static {1} {0} = {2};'
        else:
            out_declaration = accesses[object.access] + ' {1} {0} = {2};'
        out_declaration = out_declaration.format(object.name, self.build_type(object), convertInitializeValue(value))
        return out_declaration, out_init

    def build_type(self, type_, as_object=False):
        if isinstance(type_, str):
            types = dict()
            types['int'] = 'Integer' if as_object else 'int'
            types['bool'] = 'Boolean' if as_object else 'boolean'
            types['float'] = 'Float' if as_object else 'float'
            types['list'] = 'ArrayList'
            types['map'] = 'HashMap'
            types['string'] = 'String'
            types['Observer'] = 'Observer'
            type_ = type_.replace('&', '')
            type_ = type_.replace('*', '')
            if type_ in types:
                return types[type_]
        elif isinstance(type_, Object):
            s = self.build_type(type_.type, as_object)
            if type_.template_args:
                s += '<'
                for i, arg in enumerate(type_.template_args):
                    s += self.build_type(arg, as_object=True)
                    if i < len(type_.template_args) - 1:
                        s += ', '
                s += '>'
            if type_.is_const:
                s = 'final ' + s
            return s
        else:
            # TODO: add error
            exit(1)
        return type_

    def _get_filename_of_class(self, cls):
        return (cls.name if isinstance(cls, Class) else cls) + ".java"

    def get_serialiation_function_args(self):
        return self.serialize_format, 'Node'

    def create_serialization_function(self, cls, serialize_type):
        function = Function()
        function.name = 'serialize' if serialize_type == SERIALIZATION else 'deserialize'
        function.return_type = 'void'
        for func in cls.functions:
            if func.name == function.name:
                return

        n, t = self.get_serialiation_function_args()
        function.args = [[n, t]]

        if len(cls.behaviors):
            function.operations.append('super.{}({});'.format(function.name, self.get_serialiation_function_args()[0]))
        for obj in cls.members:
            if obj.is_runtime:
                continue
            if obj.is_static:
                continue
            if obj.is_const and not obj.is_link:
                continue

            line = self.build_serialize_operation(obj.name, obj.type, obj.initial_value, serialize_type,
                                                  obj.template_args, obj.is_pointer, is_link=obj.is_link)
            function.operations.append(line)

        cls.functions.append(function)

    def build_map_serialization(self, obj_name, obj_type, obj_value, obj_is_pointer, obj_template_args, serialization_type):
        key = obj_template_args[0]
        value = obj_template_args[1]
        key_type = key.name if isinstance(key, Class) else key.type
        value_type = value.name if isinstance(value, Class) else value.type
        str = self.serialize_protocol[serialization_type]['map'][0]
        _value_is_pointer = value.is_pointer
        if value_type not in self.parser.simple_types:
            value_declararion = 'value = new {}();'.format(value_type)
        else:
            value_declararion = ''
        a0 = obj_name
        a1 = self.build_serialize_operation('key', key_type, None, serialization_type, key.template_args, False, 'this.', key.is_link)
        a2 = self.build_serialize_operation('value', value_type, None, serialization_type, value.template_args, _value_is_pointer, 'this.', False)
        a1 = a1.split('\n')
        for index, a in enumerate(a1):
            a1[index] = a
        a1 = '\n'.join(a1)
        a2 = a2.split('\n')
        for index, a in enumerate(a2):
            a2[index] = a
        a2 = '\n'.join(a2)
        return str.format(a0, a1, a2, '{}', 'this.', value_declararion) + '\n'

    def build_serialize_operation(self, obj_name, obj_type, obj_value, serialization_type, obj_template_args,
                                  obj_is_pointer, owner='this.', is_link=False):
        index = 0
        if obj_value is None:
            index = 1
        type = obj_type
        cls = self.parser.find_class(type)
        if cls and cls.type == 'enum':
            type = 'enum'
        elif obj_type not in self.simple_types and type != "list" and type != "map":
            if is_link:
                type = 'link'
            elif obj_is_pointer:
                type = "pointer"
            else:
                type = "serialized"
        elif obj_type in self.simple_types:
            type = obj_type
        else:
            if len(obj_template_args) > 0:
                if type == "map":
                    if len(obj_template_args) != 2:
                        Error.exit(Error.MAP_TWO_ARGS, self._current_class.name, obj_name)
                    return self.build_map_serialization(obj_name, obj_type, obj_value, obj_is_pointer,
                                                        obj_template_args, serialization_type)
                else:
                    arg = obj_template_args[0]
                    arg_type = arg.name if isinstance(arg, Class) else arg.type
                    if arg.is_link:
                        type = 'list<link>'
                    elif arg_type in self.simple_types:
                        type = "list<{}>".format(arg_type)
                        obj_type = arg_type
                    elif arg.is_pointer:
                        type = "list<pointer>"
                    elif arg.type == 'enum':
                        type = 'list<string>'
                    else:
                        type = "list<serialized>"
                        obj_type = arg_type
        fstr = self.serialize_protocol[serialization_type][type][index]
        return fstr.format(obj_name, obj_type, obj_value, '{}', owner,
                           self.build_type(obj_template_args[0].type, True) if len(obj_template_args) > 0 else 'unknown_arg')

    def save_config_file(self):
        content = '''package org.mlc_tools.mg;

        class Config
        @(
            public final int MG_XML = 1;
            public final int MG_JSON = 2;
            public final int MG_SERIALIZE_FORMAT = MG_{};
        @)

        '''.format(self.serialize_format.upper())
        self.save_file(self._get_filename_of_class('config'), content)

    def create_factory(self):
        pattern = ''

        factory_methods = {}
        factory_methods['xml'] = ''
        factory_methods['json'] = ''

        factory = pattern.format(factory_methods[self.serialize_format])
        self.save_file(self._get_filename_of_class('Factory'), factory)

    def create_visitor_acceptors(self):
        self.save_visitors = True
        pattern = _pattern_visitor
        line = 'else if(ctx.get_type() == {0}.TYPE)\n@(\nthis.visit_{1}(ctx);\n@)\n'
        # line_import = 'import org.mlc_tools.mg.{0};\n'
        line_visit = '''\nfunction void visit_{0}(ctx)\n@(\n@)\n'''
        base_visitors = {}
        for cls in self.parser.classes:
            if cls.is_visitor and (cls.behaviors and not cls.behaviors[0].is_visitor):
                base_visitors[cls] = []
        for cls in self.parser.classes:
            parent = cls.behaviors[0] if cls.behaviors else None
            while parent:
                if parent in base_visitors:
                    base_visitors[parent].append(cls)
                    break
                parent = parent.behaviors[0] if parent.behaviors else None
        for parent in base_visitors:
            lines = ''
            visits = ''
            # imports = ''
            for cls in base_visitors[parent]:
                if self.parser.is_visitor(cls):
                    func_name = cls.name
                    func_name = func_name[0].lower() + func_name[1:]

                    lines += line.format(cls.name, func_name)
                    # imports += line_import.format(cls.name)
                    visits += line_visit.format(func_name)
            name = 'IVisitor{}'.format(parent.name)
            body = pattern.format('', lines, visits, name)
            body = body.replace('@(', '{')
            body = body.replace('@)', '}')
            self.save_file(self._get_filename_of_class(name), body)

    def create_data_storage_class(self, name, classes):
        if self.serialize_format == 'xml':
            return DataStoragePhpXml(name, classes, self.parser)
        else:
            return DataStoragePhpJson(name, classes, self.parser)

    def prepare_file(self, body):
        body = body.replace('@(', '{')
        body = body.replace('@)', '}')
        body = body.replace('::TYPE', '.TYPE')
        body = body.replace('__begin__', '{')
        body = body.replace('__end__', '}')
        body = body.replace('nullptr', 'null')

        tabs = 0
        lines = body.split('\n')
        body = list()

        def get_tabs(count):
            out = ''
            for i in range(count):
                out += '\t'
            return out

        for line in lines:
            line = line.strip()

            if line and line[0] == '}':
                tabs -= 1
            line = get_tabs(tabs) + line
            if line.strip() and line.strip()[0] == '{':
                tabs += 1
            body.append(line)
        body = '\n'.join(body)
        for i in range(10):
            tabs = '\n'
            for k in range(i):
                tabs += '\t'
            tabs += '{'
            body = body.replace(tabs, ' {')
        body = body.replace('foreach(', 'foreach (')
        body = body.replace('for(', 'for (')
        body = body.replace('if(', 'if (')
        body = body.replace('  extends', ' extends')
        body = body.strip()
        return body

    def create_data_storage(self):
        storage = self.create_data_storage_class('DataStorage', self.parser.classes)
        content = self.write_class(storage, 0)[0]
        self.save_file(self._get_filename_of_class(storage.name), content)

    def convert_to_enum(self, cls, use_type='string'):
        Writer.convert_to_enum(self, cls, use_type)
        function = Function()
        function.name = '__toString'
        function.operations.append('return this._value;')
        cls.functions.append(function)

        function = Function()
        function.name = 'str'
        function.operations.append('return (string)this;')
        cls.functions.append(function)

        for i, member in enumerate(cls.members):
            if member.name == '_value':
                member.type = use_type

        function = Function()
        function.name = 'set'
        function.args.append(['value', ''])
        function.operations.append('this._value = value;')
        cls.functions.append(function)

        function = Function()
        function.name = 'serialize'
        cls.functions.append(function)

        function = Function()
        function.name = 'deserialize'
        cls.functions.append(function)

    def save_file(self, filename, string):
        if not self.save_visitors and filename.startswith('IVisitor'):
            return
        Writer.save_file(self, filename, string)


regs = [
    [re.compile(r'DataStorage::shared\(\).get<(\w+)>'), r'DataStorage.shared().get\1'],
    [re.compile(r'\.str\(\)'), r''],
    [re.compile(r'for\s*\(auto (.+?)\s*:\s*(.+?)\s*\)'), r'foreach(\2 as \1)'],
    [re.compile(r'for\s*\(auto& (.+?)\s*:\s*(.+?)\s*\)'), r'foreach(\2 as \1)'],
    [re.compile(r'for\s*\(auto&&\s*\[(\w+),\s*(\w+)\]\s*:\s*(.+)\)'), r'foreach (\3 as \1 => \2)'],
    [re.compile(r'auto (\w+)'), r'var \1'],
    [re.compile(r'auto& (\w+)'), r'var \1'],
    [re.compile(r'void (\w+)'), r'void \1'],
    [re.compile(r'int (\w+)'), r'int \1'],
    [re.compile(r'bool (\w+)'), r'boolean \1'],
    [re.compile(r'float (\w+)'), r'float \1'],
    [re.compile(r'std::string (\w+)'), r'String \1'],
    [re.compile(r'\((\w+) (\w+)\)'), r'(\1 \2)'],
    [re.compile(r'\(const (\w+)\& (\w+)\)'), r'(final \1 \2)'],
    [re.compile(r'\(const (\w+)\* (\w+)\)'), r'(final \1 \2)'],
    [re.compile(r'\((\w+)\* (\w+)\)'), r'(\1 \2)'],
    [re.compile(r'(\w+)\ (\w+),'), r'\1 \2,'],
    [re.compile(r'(\w+)\& (\w+),'), r'\1 \2,'],
    [re.compile(r'(\w+)\* (\w+),'), r'\1 \2,'],
    [re.compile(r'const (\w+)\* (\w+)'), r'final \1 \2'],
    [re.compile(r'const (\w+)\& (\w+)'), r'final \1 \2'],
    [re.compile(r':const'), r''],
    [re.compile(r'(\w+)::(\w+)'), r'\1.\2'],
    [re.compile(r'(\w+)::(\w+)\)'), r'\1.\2)'],
    [re.compile(r'(\w+)::(\w+)\.'), r'\1.\2.'],
    [re.compile(r'(\w+)::(\w+)\]'), r'\1.\2]'],
    [re.compile(r'(\w+)::(\w+)\((\w*)\)'), r'\1.\2(\3)'],
    [re.compile(r'function (\w+)'), r'function \1'],
    [re.compile(r'\.at\((.*?)\)'), r'[\1]'],
    [re.compile(r'(\w+)\.'), r'\1.'],
    [re.compile(r'(\w+)\(\)\.'), r'\1().'],
    [re.compile(r'(\w+)\]\.'), r'\1].'],
    [re.compile(r'&(\w+)'), r'\1'],
    [re.compile(r'delete (\w+);'), r''],
    [re.compile(r'assert\(.+\);'), r''],
    [re.compile(r'make_intrusive<(\w+)>\(\s*\)'), r'new \1()'],
    [re.compile(r'dynamic_pointer_cast_intrusive<(\w+)>\((.+?)\)'), r'(\1)\2'],
    [re.compile(r'new\s*(\w+)\s*\(\s*\)'), r'new \1()'],
    [re.compile(r'(.+?)\.push_back\((.+)\);'), r'\1.add(\2);'],
    [re.compile(r'list_push\(([\w\.\->]+),\s*([\w\.\->""]+)\);'), r'\1.add(\2);'],
    [re.compile(r'(".*?")\s*\+'), r'\1.'],
    [re.compile(r'\+\s*(".*?")'), r'.\1'],
    [re.compile(r'(\w+)\s+(\w+);'), r'\2 = new \1();'],
    [re.compile(r'(\w+) = new return\(\);'), r'return \1;'],
    [re.compile(r'std::vector<(\w+)>\s+(\w+);'), r'\1 = Array(\1);'],
]


def convert_function_to_php(func, parser, function_args):
    global regs

    repl = [
        ['->', '.'],
        ['time(nullptr)', 'time()'],
        ['std::max', 'max'],
        ['std::min', 'min'],
        ['std::round', 'round'],
        ['std::floor', 'floor'],
        ['in_list(', 'in_array('],
        ['in_map', 'array_key_exists'],
        ['list_size', 'count'],
        ['map_size', 'count'],
    ]

    for reg in regs:
        func = re.sub(reg[0], reg[1], func)

    for reg in repl:
        func = func.replace(reg[0], reg[1])

    # for cls in parser.classes:
    #     if cls.name in func:
    #         func = 'import org.mlc_tools.mg.{};\n'.format(cls.name) + func

    return func


generated_functions = [
    'serialize',
    'deserialize',
    'get_type',
    'shared',
    '__toString',
    'str',
    'int',
    'set',
    's_to_int',
]
# format(name, initialize_list, functions, imports)
_pattern_file = {}
_pattern_file['xml'] = '''
package org.mlc_tools.mg;

import org.w3c.dom.Node;
import org.w3c.dom.Element;
{4}

public class {0} {1}
@(
//members:
{2}
public {0}()
@(
{5}
@)
//functions
{3}
@);

'''
_pattern_file['json'] = _pattern_file['xml']

_pattern_visitor = '''

{0}\nclass {3}
@(
function visit(ctx)
@(
    if(0)
    @(
    @)
    {1}
@)
{2}
@);
'''
