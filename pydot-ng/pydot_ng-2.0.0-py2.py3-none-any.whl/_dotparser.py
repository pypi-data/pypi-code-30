# Graphviz's dot language parser.

# The dotparser parses graphviz files in dot and dot files and transforms them
# into a class representation defined by pydot.

# The module needs pyparsing (tested with version 1.2.2) and pydot

# Author: Michael Krause <michael@krause-software.de>
# Fixes by: Ero Carrera <ero@dkbza.org>

from __future__ import division
from __future__ import print_function

import codecs
import pydot_ng as pydot
import pyparsing
import sys


__author__ = ['Michael Krause', 'Ero Carrera']
__license__ = 'MIT'


PY3 = not sys.version_info < (3, 0, 0)

if PY3:
    basestring = str


class P_AttrList(object):

    def __init__(self, toks):
        self.attrs = {}
        i = 0

        while i < len(toks):
            attrname = toks[i]
            if i + 2 < len(toks) and toks[i + 1] == '=':
                attrvalue = toks[i + 2]
                i += 3
            else:
                attrvalue = None
                i += 1

            self.attrs[attrname] = attrvalue

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.attrs)


class DefaultStatement(P_AttrList):

    def __init__(self, default_type, attrs):
        self.default_type = default_type
        self.attrs = attrs

    def __repr__(self):
        return "%s(%s, %r)" % (
            self.__class__.__name__,
            self.default_type, self.attrs)


top_graphs = list()


def push_top_graph_stmt(str, loc, toks):
    attrs = {}
    g = None

    for element in toks:
        if (isinstance(element, (pyparsing.ParseResults, tuple, list)) and
                len(element) == 1 and isinstance(element[0], basestring)):
            element = element[0]

        if element == 'strict':
            attrs['strict'] = True

        elif element in ['graph', 'digraph']:
            attrs = {}

            g = pydot.Dot(graph_type=element, **attrs)
            attrs['type'] = element

            top_graphs.append(g)

        elif isinstance(element, basestring):
            g.set_name(element)

        elif isinstance(element, pydot.Subgraph):
            g.obj_dict['attributes'].update(element.obj_dict['attributes'])
            g.obj_dict['edges'].update(element.obj_dict['edges'])
            g.obj_dict['nodes'].update(element.obj_dict['nodes'])
            g.obj_dict['subgraphs'].update(element.obj_dict['subgraphs'])
            g.set_parent_graph(g)

        elif isinstance(element, P_AttrList):
            attrs.update(element.attrs)

        elif isinstance(element, (pyparsing.ParseResults, list)):
            add_elements(g, element)

        else:
            raise ValueError("Unknown element statement: %r " % element)

    for g in top_graphs:
        update_parent_graph_hierarchy(g)

    if len(top_graphs) == 1:
        return top_graphs[0]

    return top_graphs


def update_parent_graph_hierarchy(g, parent_graph=None, level=0):
    if parent_graph is None:
        parent_graph = g

    for key_name in ('edges',):
        if isinstance(g, pydot.frozendict):
            item_dict = g
        else:
            item_dict = g.obj_dict

        if key_name not in item_dict:
            continue

        for key, objs in item_dict[key_name].items():
            for obj in objs:
                if ('parent_graph' in obj and
                        obj['parent_graph'].get_parent_graph() == g):
                    if obj['parent_graph'] is g:
                        pass
                    else:
                        obj['parent_graph'].set_parent_graph(parent_graph)

                if key_name == 'edges' and len(key) == 2:
                    for vertex in obj['points']:
                        if isinstance(vertex, (pydot.Graph, pydot.Subgraph,
                                               pydot.Cluster)):
                            vertex.set_parent_graph(parent_graph)
                        if isinstance(vertex, pydot.frozendict):
                            if vertex['parent_graph'] is g:
                                pass
                            else:
                                vertex['parent_graph'].\
                                    set_parent_graph(parent_graph)


def add_defaults(element, defaults):
    d = element.__dict__
    for key, value in defaults.items():
        if not d.get(key):
            d[key] = value


def add_elements(g, toks, defaults_graph=None, defaults_node=None,
                 defaults_edge=None):
    if defaults_graph is None:
        defaults_graph = {}
    if defaults_node is None:
        defaults_node = {}
    if defaults_edge is None:
        defaults_edge = {}

    for element in toks:
        if isinstance(element, (pydot.Subgraph, pydot.Cluster)):
            add_defaults(element, defaults_graph)
            g.add_subgraph(element)

        elif isinstance(element, pydot.Node):
            add_defaults(element, defaults_node)
            g.add_node(element)

        elif isinstance(element, pydot.Edge):
            add_defaults(element, defaults_edge)
            g.add_edge(element)

        elif isinstance(element, pyparsing.ParseResults):
            for e in element:
                add_elements(g, [e], defaults_graph, defaults_node,
                             defaults_edge)

        elif isinstance(element, DefaultStatement):
            if element.default_type == 'graph':
                default_graph_attrs = pydot.Node('graph', **element.attrs)
                g.add_node(default_graph_attrs)

            elif element.default_type == 'node':
                default_node_attrs = pydot.Node('node', **element.attrs)
                g.add_node(default_node_attrs)

            elif element.default_type == 'edge':
                default_edge_attrs = pydot.Node('edge', **element.attrs)
                g.add_node(default_edge_attrs)
                defaults_edge.update(element.attrs)

            else:
                raise ValueError("Unknown DefaultStatement: {0} ".
                                 format(element.default_type))

        elif isinstance(element, P_AttrList):
            g.obj_dict['attributes'].update(element.attrs)

        else:
            raise ValueError("Unknown element statement: %r" % element)


def push_graph_stmt(str, loc, toks):
    g = pydot.Subgraph('')
    add_elements(g, toks)
    return g


def push_subgraph_stmt(str, loc, toks):
    g = pydot.Subgraph('')

    for e in toks:
        if len(e) == 3:
            e[2].set_name(e[1])
            if e[0] == 'subgraph':
                e[2].obj_dict['show_keypyparsing.Word'] = True
            return e[2]
        else:
            if e[0] == 'subgraph':
                e[1].obj_dict['show_keypyparsing.Word'] = True
            return e[1]

    return g


def push_default_stmt(str, loc, toks):
    # The pydot class instances should be marked as
    # default statements to be inherited by actual
    # graphs, nodes and edges.
    default_type = toks[0][0]
    if len(toks) > 1:
        attrs = toks[1].attrs
    else:
        attrs = {}

    if default_type in ['graph', 'node', 'edge']:
        return DefaultStatement(default_type, attrs)
    else:
        raise ValueError("Unknown default statement: %r " % toks)


def push_attr_list(str, loc, toks):
    p = P_AttrList(toks)
    return p


def get_port(node):
    if len(node) > 1:
        if isinstance(node[1], pyparsing.ParseResults):
            if len(node[1][0]) == 2:
                if node[1][0][0] == ':':
                    return node[1][0][1]
    return None


def do_node_ports(node):
    node_port = ''

    if len(node) > 1:
        node_port = ''.join([str(a) + str(b) for a, b in node[1]])

    return node_port


def push_edge_stmt(str, loc, toks):
    tok_attrs = [a for a in toks if isinstance(a, P_AttrList)]
    attrs = {}

    for a in tok_attrs:
        attrs.update(a.attrs)

    e = []

    if isinstance(toks[0][0], pydot.Graph):
        n_prev = pydot.frozendict(toks[0][0].obj_dict)
    else:
        n_prev = toks[0][0] + do_node_ports(toks[0])

    if isinstance(toks[2][0], pyparsing.ParseResults):
        n_next_list = [[n.get_name()] for n in toks[2][0]]
        for n_next in [n for n in n_next_list]:
            n_next_port = do_node_ports(n_next)
            e.append(pydot.Edge(n_prev, n_next[0] + n_next_port, **attrs))

    elif isinstance(toks[2][0], pydot.Graph):
        e.append(pydot.Edge(n_prev, pydot.frozendict(toks[2][0].obj_dict),
                            **attrs))

    elif isinstance(toks[2][0], pydot.Node):
        node = toks[2][0]

        if node.get_port() is not None:
            name_port = node.get_name() + ":" + node.get_port()
        else:
            name_port = node.get_name()

        e.append(pydot.Edge(n_prev, name_port, **attrs))

    elif isinstance(toks[2][0], type('')):
        for n_next in [n for n in tuple(toks)[2::2]]:
            if isinstance(n_next, P_AttrList) or not isinstance(n_next[0],
                                                                type('')):
                continue

            n_next_port = do_node_ports(n_next)
            e.append(pydot.Edge(n_prev, n_next[0] + n_next_port, **attrs))

            n_prev = n_next[0] + n_next_port

    else:
        # UNEXPECTED EDGE TYPE
        pass

    return e


def push_node_stmt(s, loc, toks):

    if len(toks) == 2:
        attrs = toks[1].attrs
    else:
        attrs = {}

    node_name = toks[0]
    if isinstance(node_name, list) or isinstance(node_name, tuple):
        if len(node_name) > 0:
            node_name = node_name[0]

    n = pydot.Node(str(node_name), **attrs)
    return n


graphparser = None


def graph_definition():
    global graphparser

    if not graphparser:
        # punctuation
        colon = pyparsing.Literal(":")
        lbrace = pyparsing.Literal("{")
        rbrace = pyparsing.Literal("}")
        lbrack = pyparsing.Literal("[")
        rbrack = pyparsing.Literal("]")
        lparen = pyparsing.Literal("(")
        rparen = pyparsing.Literal(")")
        equals = pyparsing.Literal("=")
        comma = pyparsing.Literal(",")
        semi = pyparsing.Literal(";")
        at = pyparsing.Literal("@")
        minus = pyparsing.Literal("-")

        # keypyparsing.Words
        strict_ = pyparsing.CaselessLiteral("strict")
        graph_ = pyparsing.CaselessLiteral("graph")
        digraph_ = pyparsing.CaselessLiteral("digraph")
        subgraph_ = pyparsing.CaselessLiteral("subgraph")
        node_ = pyparsing.CaselessLiteral("node")
        edge_ = pyparsing.CaselessLiteral("edge")

        # token definitions
        identifier = pyparsing.Word(pyparsing.alphanums + "_.").\
            setName("identifier")

        # dblpyparsing.QuotedString
        double_quoted_string = pyparsing.QuotedString('"', multiline=True,
                                                      unquoteResults=False)

        noncomma_ = "".join([c for c in pyparsing.printables if c != ","])
        alphastring_ = pyparsing.OneOrMore(pyparsing.CharsNotIn(noncomma_ +
                                                                ' '))

        def parse_html(s, loc, toks):
            return '<%s>' % ''.join(toks[0])

        opener = '<'
        closer = '>'
        html_text = pyparsing.nestedExpr(
            opener, closer,
            (pyparsing.CharsNotIn(opener + closer))).\
            setParseAction(parse_html).leaveWhitespace()

        ID = (
            identifier | html_text |
            double_quoted_string |
            alphastring_).setName("ID")

        float_number = pyparsing.Combine(
            pyparsing.Optional(minus) +
            pyparsing.OneOrMore(pyparsing.Word(pyparsing.nums + "."))).\
            setName("float_number")

        righthand_id = (float_number | ID).setName("righthand_id")

        port_angle = (at + ID).setName("port_angle")

        port_location = (
            pyparsing.OneOrMore(pyparsing.Group(colon + ID)) |
            pyparsing.Group(colon + lparen + ID + comma + ID + rparen)).\
            setName("port_location")

        port = (
            pyparsing.Group(port_location + pyparsing.Optional(port_angle)) |
            pyparsing.Group(port_angle + pyparsing.Optional(port_location))).\
            setName("port")

        node_id = (ID + pyparsing.Optional(port))
        a_list = pyparsing.OneOrMore(
            ID + pyparsing.Optional(equals + righthand_id) +
            pyparsing.Optional(comma.suppress())).\
            setName("a_list")

        attr_list = pyparsing.OneOrMore(
            lbrack.suppress() + pyparsing.Optional(a_list) +
            rbrack.suppress()).setName("attr_list")

        attr_stmt = (pyparsing.Group(graph_ | node_ | edge_) + attr_list).\
            setName("attr_stmt")

        edgeop = (pyparsing.Literal("--") | pyparsing.Literal("->")).\
            setName("edgeop")

        stmt_list = pyparsing.Forward()
        graph_stmt = pyparsing.Group(
            lbrace.suppress() + pyparsing.Optional(stmt_list) +
            rbrace.suppress() + pyparsing.Optional(semi.suppress())).\
            setName("graph_stmt")

        edge_point = pyparsing.Forward()

        edgeRHS = pyparsing.OneOrMore(edgeop + edge_point)
        edge_stmt = edge_point + edgeRHS + pyparsing.Optional(attr_list)

        subgraph = pyparsing.Group(subgraph_ +
                                   pyparsing.Optional(ID) + graph_stmt).\
            setName("subgraph")

        edge_point << pyparsing.Group(subgraph | graph_stmt | node_id).\
            setName('edge_point')

        node_stmt = (node_id + pyparsing.Optional(attr_list) +
                     pyparsing.Optional(semi.suppress())).setName("node_stmt")

        assignment = (ID + equals + righthand_id).setName("assignment")
        stmt = (
            assignment | edge_stmt | attr_stmt |
            subgraph | graph_stmt | node_stmt).\
            setName("stmt")
        stmt_list << pyparsing.OneOrMore(stmt + pyparsing.Optional(
            semi.suppress()))

        graphparser = pyparsing.OneOrMore((
            pyparsing.Optional(strict_) +
            pyparsing.Group((graph_ | digraph_)) +
            pyparsing.Optional(ID) + graph_stmt).
            setResultsName("graph"))

        singleLineComment = (pyparsing.Group("//" + pyparsing.restOfLine) |
                             pyparsing.Group("#" + pyparsing.restOfLine))

        # actions
        graphparser.ignore(singleLineComment)
        graphparser.ignore(pyparsing.cStyleComment)

        assignment.setParseAction(push_attr_list)
        a_list.setParseAction(push_attr_list)
        edge_stmt.setParseAction(push_edge_stmt)
        node_stmt.setParseAction(push_node_stmt)
        attr_stmt.setParseAction(push_default_stmt)

        subgraph.setParseAction(push_subgraph_stmt)
        graph_stmt.setParseAction(push_graph_stmt)
        graphparser.setParseAction(push_top_graph_stmt)

    return graphparser


def parse_dot_data(data):
    global top_graphs

    top_graphs = list()

    if PY3:
        if isinstance(data, bytes):
            # this is extremely hackish
            try:
                idx = data.index(b'charset') + 7
                while data[idx] in b' \t\n\r=':
                    idx += 1
                fst = idx
                while data[idx] not in b' \t\n\r];,':
                    idx += 1
                charset = data[fst:idx].strip(b'"\'').decode('ascii')
                data = data.decode(charset)
            except Exception:
                data = data.decode('utf-8')
    else:
        if data.startswith(codecs.BOM_UTF8):
            data = data.decode('utf-8')

    try:

        graphparser = graph_definition()

        if pyparsing.__version__ >= '1.2':
            graphparser.parseWithTabs()

        tokens = graphparser.parseString(data)

        if len(tokens) == 1:
            return tokens[0]
        else:
            return [g for g in tokens]

    except pyparsing.ParseException:
        err = sys.exc_info()[1]
        print(err.line)
        print(" " * (err.column - 1) + "^")
        print(err)
        return None
