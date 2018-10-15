__author__ = 'aarongary'

import json
import sys
import os
import errno
import pandas as pd
import networkx as nx
import io
import decimal
import numpy as np
import math
import json
import ijson
import requests
import base64
from ndex2cx import known_aspects_min
from ndex2.niceCxInterface import NiceCx
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client

if sys.version_info.major == 3:
    from urllib.request import urlopen, Request, HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, \
        build_opener, install_opener, HTTPError, URLError
else:
    from urllib2 import urlopen, Request, HTTPBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, \
        build_opener, install_opener, HTTPError, URLError

userAgent = 'NDEx-NiceCX/2.0'

class NiceCXNetwork():
    def __init__(self, **attr):

        self.metadata = {}
        self.context = []
        self.nodes = {}
        self.node_int_id_generator = 0
        self.edge_int_id_generator = 0
        self.node_id_lookup = []
        self.edges = {}
        self.citations = {}
        self.nodeCitations = {}
        self.edgeCitations = {}
        self.edgeSupports = {}
        self.nodeSupports = {}
        self.supports = {}
        self.nodeAttributes = {}
        self.edgeAttributes = {}
        self.edgeAttributeHeader = set([])
        self.nodeAttributeHeader = set([])
        self.networkAttributes = []
        self.nodeAssociatedAspects = {}
        self.edgeAssociatedAspects = {}
        self.opaqueAspects = {}
        self.provenance = []
        self.missingNodes = {}
        self.s = None
        self.node_name_to_id_map_cache = {}
        self.user_agent = 'ndex2-client:v2.0'

        #if cx:
        #    self.create_from_cx(cx)
        #elif networkx_G:
        #    self.create_from_networkx(networkx_G)
        #elif pandas_df is not None:
        #    self.create_from_pandas(pandas_df)
        #elif filename is not None:
        #    if os.path.isfile(filename):
        #        with open(filename, 'rU') as file_cx:
                    #====================================
                    # BUILD NICECX FROM FILE
                    #====================================
        #            self.create_from_cx(json.load(file_cx))
        #    else:
        #        raise Exception('Input provided is not a valid file')
        #else:
        #    if server and uuid:
        #        self.create_from_server(server, username, password, uuid)

    def __create_edge(self, id=None, edge_source=None, edge_target=None, edge_interaction=None):
        """
        Create a new edge in the network by specifying source-interaction-target

        :param id:
        :type id:
        :param edge_source: The source node this edge, either its id or the node object itself.
        :type edge_source: int
        :param edge_target: The target node this edge, either its id or the node object itself.
        :type edge_target: int
        :param edge_interaction: The interaction that describes the relationship between the source and target nodes
        :type edge_interaction: string
        :param cx_fragment: CX Fragment
        :type cx_fragment: json
        :return: Edge ID
        :rtype: int
        """

        self.edges[id] = {'@id': id, 's': edge_source, 't': edge_target}

        if edge_interaction is not None:
            self.edges[id]['i'] = edge_interaction

        return id

    def create_edge(self, edge_source=None, edge_target=None, edge_interaction=None):
        """
        Create a new edge in the network by specifying source-interaction-target

        Example:

            ``my_edge = create_edge(edge_source=my_node, edge_target=my_node2, edge_interaction='up-regulates')``

        :param edge_source: The source node of this edge, either its id or the node object itself.
        :type edge_source: int, dict (with @id property)
        :param edge_target: The target node of this edge, either its id or the node object itself.
        :type edge_target: int, dict (with @id property)
        :param edge_interaction: The interaction that describes the relationship between the source and target nodes
        :type edge_interaction: string
        :return: Edge ID
        :rtype: int
        """
        edge_id = self.edge_int_id_generator

        #if not edge_interaction:
        #    edge_interaction = ''

        self.__create_edge(id=edge_id, edge_source=edge_source, edge_target=edge_target, edge_interaction=edge_interaction)
        self.edge_int_id_generator += 1

        return edge_id

    def add_edge(self, id=None, source=None, target=None, interaction=None):
        """
        .. warning::

           This method has been deprecated.  Please use **create_edge()**

        ..

        """
        raise Warning('add_edge() is deprecated.  Please use create_edge().')
        #if id is None:
        #    raise Exception('No ID provided')

        #if source is None or target is None or interaction is None:
        #    print('source: %s, target: %s or target: %s was None.  Skipping edge' % (source, target, interaction))
        #    return None
            #raise Exception('Source, Target and Interaction are required to create an edge')

        #self.edges[id] = {'@id': id, 's': source, 't': target, 'i': interaction}

        #return id

    #==================
    # NODE OPERATIONS
    #==================
    def __create_node(self, id=None, node_name=None, node_represents=None):
        if id is None:
            id=self.get_next_node_id()

        if node_represents is not None:
            self.nodes[id] = {'@id': id, 'n': node_name, 'r': node_represents}
        else:
            self.nodes[id] = {'@id': id, 'n': node_name, 'r': node_name}

        return id

    def create_node(self, node_name=None, node_represents=None):
        """
        Creates a new node with the corresponding name and represents (external id)

        Example:

            ``my_node = create_node(node_name='MAPK1, node_represents='1114208')``

        :param node_name: Name of the node
        :type node_name: str
        :param node_represents: Representation of the node (alternate identifier)
        :type node_represents: str
        :return: Node ID
        :rtype: int
        """

        id = self.node_int_id_generator
        self.__create_node(id=id, node_name=node_name, node_represents=node_represents)
        self.node_int_id_generator += 1

        return id

    def add_node(self, id=None, name=None, represents=None):
        """
        .. warning::

           This method has been deprecated.  Please use **create_node()**

        ..

        """
        raise Warning('add_node() is deprecated.  Please use create_node().')

        #if represents is not None:
        #    self.nodes[id] = {'@id': id, 'n': name, 'r': represents}
        #else:
        #    self.nodes[id] = {'@id': id, 'n': name, 'r': name}

        #if data_type is not None:
        #    self.nodes[id]['d'] = data_type

        #return id

    def add_network_attribute(self, name=None, values=None, type=None, subnetwork=None):
        """
        Add an attribute to the network

        :param name: Name of the attribute
        :type name: str
        :param values:  The value(s) of the attribute
        :type values: One of the allowable CX types.  See `Supported data types`_
        :param type: They type of data supplied in values. Default is string.  See `Supported data types`_
        :type type: str
        :return: None
        :rtype: None
        """
        found_attr = False
        for n_a in self.networkAttributes:
            if n_a.get('n') == name:
                n_a['v'] = values

                if type is not None:
                    n_a['d'] = type

                found_attr = True

                break

        if not found_attr:
            if type is not None:
                network_attribute = {'n': name, 'v': values, 'd': type}
            else:
                network_attribute = {'n': name, 'v': values}

            self.networkAttributes.append(network_attribute)

    def add_citation(self, id, title=None, contributor=None, identifier=None, type=None, description=None, attributes=None):
        add_this_citation = {'@id': id}

        if contributor is not None:
            add_this_citation['dc:contributor'] = contributor

        if identifier is not None:
            add_this_citation['dc:identifier'] = identifier

        if type is not None:
            add_this_citation['dc:type'] = type

        if title is not None:
            add_this_citation['dc:title'] = title

        if description is not None:
            add_this_citation['dc:description'] = description

        if attributes is not None:
            add_this_citation[attributes] = attributes

        self.citations[id] = add_this_citation

        return add_this_citation

    def add_edge_citations(self, edge_id, citation):
        if isinstance(citation, dict):
            edge_citation_element = {'po': [edge_id], 'citations': [citation.get('@id')]}
        else:
            edge_citation_element = {'po': [edge_id], 'citations': [citation]}

        self.build_many_to_many_relation('edgeCitations', edge_citation_element, 'citations')

    def add_support(self, id=None, text=None, citation_id=None, attributes=None, props=None):
        add_this_supports = {'@id': id}

        if text is not None:
            add_this_supports['text'] = text

        if citation_id is not None:
            add_this_supports['citation'] = citation_id

        if attributes is not None and len(attributes) > 0:
            add_this_supports['attributes'] = attributes

        if props is not None and len(props) > 0:
            add_this_supports['properties'] = props


        self.supports[id] = add_this_supports

        return add_this_supports

    def add_edge_supports(self, edge_id, support):
        if isinstance(support, dict):
            edge_support_element = {'po': [edge_id], 'supports': [support.get('@id')]}
        else:
            edge_support_element = {'po': [edge_id], 'supports': [support]}

        self.build_many_to_many_relation('edgeSupports', edge_support_element, 'supports')

    def build_many_to_many_relation(self, aspect_name, element, relation_name):
        if aspect_name == 'nodeCitations':
            aspect = self.nodeCitations
        elif aspect_name == 'edgeCitations':
            aspect = self.edgeCitations
        elif aspect_name == 'edgeSupports':
            aspect = self.edgeSupports
        else:
            raise Exception('Only nodeCitations, edgeCitations and edgeSupports are supported. ' + aspect_name + ' was supplied')

        for po in element.get('po'):
            po_id = aspect.get(po)
            if po_id is None:
                aspect[po] = element.get(relation_name)
            else:
                aspect[po] += element.get(relation_name)
    # TODO
    # make opaque aspect into a one shot method to set the whole aspect.
    # i.e. not one element at a time
    def add_opaque_aspect(self, aspect_name, aspect):
        if isinstance(aspect, list):
            self.opaqueAspects[aspect_name] = aspect
        elif isinstance(aspect, dict):
            if 'error' in aspect:
                pass
            else:
                self.opaqueAspects[aspect_name] = [aspect]
        else:
            raise Exception('Provided input was not of type list.')

    def add_opaque_aspect_element(self, opaque_element):
        raise Exception('add_opaque_aspect_element() is deprecated.  Please use add_opaque_aspect()')

    def set_name(self, network_name):
        """
        Set the network name

        Example:

            ``set_name('P38 Signaling')``

        :param network_name: Network name
        :type network_name: string
        :return: None
        :rtype: None

        """
        #add_this_network_attribute = NetworkAttributesElement(name='name', values=network_name, type=ATTRIBUTE_DATA_TYPE.STRING)

        self.add_network_attribute(name='name', values=network_name, type='string')

    def get_name(self):
        """
        Get the network name

        :return: Network name
        :rtype: string
        """
        for net_a in self.networkAttributes:
            if net_a.get('n') == 'name':
                return net_a.get('v')

        return None

    def add_name_space(self, prefix, uri):
        found_context = False
        for n_a in self.networkAttributes:
            if n_a.get('n') == '@context':
                found_context = True
                add_to_this_context = json.loads(n_a['v'])
                add_to_this_context[prefix] = uri
                n_a['v'] = json.dumps(add_to_this_context)
                break

        if not found_context:
            self.add_network_attribute(name='@context', values=json.dumps({prefix: uri}), type='string')


    def set_namespaces(self, ns):
        self.set_context(ns)

        # TODO - uncomment the following when the web app supports context located in the network attributes
        #if isinstance(ns, list):
        #    add_this_context = {}
        #    for c in ns:
        #        for k, v in c.items():
        #            add_this_context[k] = v
        #    self.add_network_attribute(name='@context', values=json.dumps(add_this_context), type='string')
        #elif isinstance(ns, dict):
        #    self.add_network_attribute(name='@context', values=json.dumps(ns), type='string')
        #else:
        #    raise Exception('Namespace must be of type dict or list')

    def get_namespaces(self,):
        for n_a in self.networkAttributes:
            if n_a.get('n') == '@context':
                return json.loads(n_a['v'])

        return None

    def get_edges (self):
        """
        Returns an iterator over edge ids as keys and edge objects as values.

        Example:

            ``for edge_id, edge_obj in nice_cx.get_edges():``

            ``print(edge_obj.get('i')) # print interaction``

            ``print(edge_obj.get('s')) # print source node id``

        :return: Edge iterator
        :rtype: iterator
        """
        return self.edges.items()

    def get_edge(self, edge):
        return self.edges.get(edge)

    def get_edge_attribute_object(self, edge, attribute_name):
        """
        .. warning::

           This method has been deprecated.  Please use **get_edge_attribute()**

        ..

        """
        raise Warning('get_edge_attribute_object() is deprecated.  Please use get_edge_attribute().')

        #edge_attrs = self.edgeAttributes.get(edge)

        #if edge_attrs:
        #    for e_a in edge_attrs:
        #        if e_a.get('n') == attribute_name:
        #            return e_a

        #return None

    #==============================
    # NETWORK PROPERTY OPERATIONS
    #==============================
    def get_network_attribute(self, attribute_name):
        """
        Get the value of a network attribute

        :param attribute_name: Attribute name
        :type attribute_name: string
        :return: Network attribute object
        :rtype: dict
        """
        for n_a in self.networkAttributes:
            if n_a.get('n') == attribute_name:
                return n_a

        return None

    def get_next_node_id(self):
        return_id = self.node_int_id_generator
        self.node_int_id_generator += 1
        return return_id

    def add_node_attribute(self, property_of=None, name=None, values=None, type=None, subnetwork=None):
        if property_of is None:
            raise Exception('Node attribute requires property_of')

        if name is None or values is None:
            raise Exception('Node attribute requires the name and values property')

        if self.nodeAttributes.get(property_of) is None :
            self.nodeAttributes[property_of] = []

        if type is None:
            attr_type = None
            if isinstance(values, float):
                attr_type = 'double'
            elif isinstance(values, int):
                attr_type = 'integer'
            elif isinstance(values, list):
                attr_type = 'list_of_string'

            if attr_type:
                self.nodeAttributes[property_of].append({'po': property_of, 'n': name, 'v': values, 'd': attr_type})
            else:
                self.nodeAttributes[property_of].append({'po': property_of, 'n': name, 'v': values})
        else:
            self.nodeAttributes[property_of].append({'po': property_of, 'n': name, 'v': values, 'd': type})
            #TODO add support for subnetwork

    def add_edge_attribute(self, property_of, name, values, type=None, subnetwork=None):
        if isinstance(property_of, dict):
            property_of = property_of.get('@id')

        #if property_of is None:
        #    raise Exception('Edge attribute requires the property_of property')

        #if name is None or values is None:
        #    raise Exception('Edge attribute requires the name and values property')

        if self.edgeAttributes.get(property_of) is None :
            self.edgeAttributes[property_of] = []

        if type is None:
            self.edgeAttributes[property_of].append({'po': property_of, 'n': name, 'v': values})
        else:
            #TODO check for float --> double and numpy types
            if type == 'float' or type == 'list_of_float':
                type = 'float'
            self.edgeAttributes[property_of].append({'po': property_of, 'n': name, 'v': values, 'd': type})

    def get_nodes(self):
        """
        Returns an iterator over node ids as keys and node objects as values.

        Example:

            ``for id, node in nice_cx.get_nodes():``

            ``node_name = node.get('n')``

            ``node_represents = node.get('r')``



        :return: iterator over nodes
        :rtype: iterator
        """
        return self.nodes.items()

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def _generate_node_name_to_id_map(self):
        self.node_name_to_id_map_cache = {node.get('n'): node_id for node_id, node in self.get_nodes()}

    def get_node_by_name(self, node_name):
        if(len(self.node_name_to_id_map_cache) < 1):
            self._generate_node_name_to_id_map()

        node_id_lookup = self.node_name_to_id_map_cache.get(node_name)
        if node_id_lookup is not None:
            return self.nodes.get(node_id_lookup)
        else:
            return None

    # TODO - Check edges for orphans.  Check node attributes for orphans
    #def remove_node(self, node_id):
    #    raise Warning()
    #    return self.nodes.pop(node_id, None)

    #=============================
    # NODE ATTRIBUTES OPERATIONS
    #=============================
    def set_node_attribute(self, node, attribute_name, values, type=None):
        """
        Set an attribute of a node, where the node may be specified by its id or passed in as a node dict.

        Example:

            ``set_node_attribute(my_node, 'Pathway', 'Signal Transduction / Growth Regulation')``

            or

            ``set_node_attribute(my_node, 'Mutation Frequency', 0.007, type='double')``

        :param node: Node to add the attribute to
        :type node: int or node dict with @id attribute
        :param attribute_name: attribute name
        :type attribute_name: string
        :param values: A value or list of values of the attribute
        :type values: list, string, int or double
        :param type: The datatype of the attribute values, defaults is string.  See `Supported data types`_
        :type type: str
        :param cx_fragment: CX fragment
        :type cx_fragment: json
        :return: None
        :rtype: None
        """

        self.add_node_attribute(property_of=node, name=attribute_name, values=values, type=type)

    def get_node_attribute_objects(self, node, attribute_name):
        """
        .. warning::

           This method has been deprecated.  Please use **get_node_attribute()**

        ..

        """

        raise Warning('get_node_attribute_objects() is deprecated.  Please use get_node_attribute() instead')

        #node_attrs = self.get_node_attributes(node)

        #if node_attrs:
        #    for n_a in node_attrs:
        #        if n_a.get('n') == attribute_name:
        #            return n_a

        #return None

    def get_node_attribute(self, node, attribute_name):
        """
        Get the node attribute of a node, where the node may be specified by its id or passed in as an object.

        Example:

             ``get_node_attribute(my_node, 'Pathway')``
             ``# returns: {'@id': 0, 'n': 'diffusion-heat', 'v': 0.832, 'd': 'double'}``


        :param node: node object or node id
        :type node: int or node dict with @id attribute
        :param attribute_name: attribute name
        :type attribute_name:
        :return: the node attibute object or None if the attribute doesn't exist
        :rtype: dict
        """
        #n_a = self.get_node_attribute_objects(node, attribute_name)

        node_attrs = self.get_node_attributes(node)

        if node_attrs:
            for n_a in node_attrs:
                if n_a.get('n') == attribute_name:
                    return n_a

        return None


    def get_node_attribute_value(self, node, attribute_name):
        """
        Get the value(s) of an attribute of a node, where the node may be specified by its id or passed in as an object.

        Example:

             ``get_node_attribute_value(my_node, 'Pathway')``
             ``# returns: 'Signal Transduction / Growth Regulation'``


        :param node: node object or node id
        :type node: int or node dict with @id attribute
        :param attribute_name: attribute name
        :type attribute_name:
        :return: the value of the attibute or None if the attribute doesn't exist
        :rtype: string
        """
        #n_a = self.get_node_attribute_objects(node, attribute_name)

        node_attrs = self.get_node_attributes(node)

        if node_attrs:
            for n_a in node_attrs:
                if n_a.get('n') == attribute_name:
                    return n_a.get('v')

        return None



    def get_node_attributes(self, node):
        """
        Get the attribute objects of a node, where the node may be specified by its id or passed in as an object.

        Example:

             ``get_node_attributes(my_node)``
             ``# returns: [{'po': 0, 'n': 'Pathway', 'v': 'Signal Transduction / Growth Regulation'}]``

        :param node: node object or node id
        :type node: int or node dict with @id attribute
        :return: node attributes
        :rtype: list
        """
        if isinstance(node, dict):
            return self.nodeAttributes.get(node.get('@id'))
        else:
            return self.nodeAttributes.get(node)


    def set_network_attribute(self, name, values=None, type=None):
        """
        Set an attribute of the network

        Example:

            ``set_network_attribute(name='networkType', values='Genetic interactions')``

        :param name: Attribute name
        :type name: string
        :param values: The values of the attribute
        :type values: list, string, double or int
        :param type: The datatype of the attribute values.  See `Supported data types`_
        :type type: str
        :return: None
        :rtype: none
        """
        subnetwork = None
        #TODO add support for subnetworks
        found_attr = False
        for n_a in self.networkAttributes:
            if n_a.get('n') == name:
                n_a['v'] = values
                if type is not None:
                    if type == 'float':
                        type = 'double'
                    elif type == 'list_of_float':
                        type = 'list_of_double'
                    n_a['d'] = type

                if subnetwork:
                    n_a['s'] = subnetwork

                found_attr = True

                break

        if not found_attr:
            if type is not None:
                if type == 'float':
                    type = 'double'
                elif type == 'list_of_float':
                    type = 'list_of_double'

                net_attr = {
                    'n': name,
                    'v': values,
                    'd': type
                }
            else:
                net_attr = {
                    'n': name,
                    'v': values
                }

            self.networkAttributes.append(net_attr)


    def set_edge_attribute(self, edge, attribute_name, values, type=None):
        """
        Set the value(s) of attribute of an edge, where the edge may be specified by its id or passed in an object.

        Example:

            ``set_edge_attribute(0, 'weight', 0.5, type='double')``

            or

            ``set_edge_attribute(my_edge, 'Disease', 'Atherosclerosis')``


        :param edge: Edge to add the attribute to
        :type edge: int or edge dict with @id attribute
        :param attribute_name: Attribute name
        :type attribute_name: str
        :param values: A value or list of values of the attribute
        :type values: list
        :param type: The datatype of the attribute values, defaults to the python datatype of the values.  See `Supported data types`_
        :type type: str
        :return: None
        :rtype: None
        """

        self.add_edge_attribute(property_of=edge, name=attribute_name, values=values, type=type)
        #TODO add support for subnetworks

    def get_edge_attributes(self, edge):
        """
        Get the attribute objects of an edge, where the edge may be specified by its id or passed in as an object.

        Example:

             ``get_edge_attributes(my_edge)``

             ``# returns: [{'@id': 0, 'n': 'weight', 'v': 0.849, 'd': 'double'}, {'@id': 0, 'n': 'Type', 'v': 'E1'}]``

        :param edge: Edge object or edge id
        :type edge: int or edge dict with @id attribute
        :return: Edge attribute objects
        :rtype: list of edge dict
        """
        if isinstance(edge, dict):
            return self.edgeAttributes.get(edge.get('@id'))

        return self.edgeAttributes.get(edge)

    def get_edge_attribute_objects(self, edge, attribute_name):
        """
        .. warning::

           This method has been deprecated.  Please use **get_edge_attributes()**

        ..

        """

        raise Warning('get_edge_attribute_objects() is deprecated')
        #edge_attrs = self.get_edge_attributes(edge)

        #if edge_attrs:
        #    for e_a in edge_attrs:
        #        if e_a.get('n') == attribute_name:
        #            return e_a

        #return None


    def get_edge_attribute(self, edge, attribute_name):
        """
        Get the edge attributes of an edge, where the edge may be specified by its id or passed in as an object.


        Example:

             ``get_edge_attribute(my_edge, 'weight')``

             ``# returns: {'@id': 0, 'n': 'weight', 'v': 0.849, 'd': 'double'}``


        :param edge: Edge object or edge id
        :type edge: int or edge dict with @id attribute
        :param attribute_name: Attribute name
        :type attribute_name:
        :return: Edge attribute object
        :rtype: list, string, int or double
        """

        edge_attrs = self.get_edge_attributes(edge)
        if edge_attrs:
            edge_attr_found = False
            for e_a in edge_attrs:
                if e_a.get('n') == attribute_name:
                    return e_a

        return None, None

    def get_edge_attribute_value(self, edge, attribute_name):
        """
        Get the value(s) of an attribute of an edge, where the edge may be specified by its id or passed in as an object.

        Example:

             ``get_edge_attribute_value(my_edge, 'weight')``

             ``# returns: 0.849``

        :param edge: Edge object or edge id
        :type edge: int or edge dict with @id attribute
        :param attribute_name: Attribute name
        :type attribute_name:
        :return: Edge attribute value(s)
        :rtype: list, string, int or double
        """

        edge_attrs = self.get_edge_attributes(edge)
        if edge_attrs:
            edge_attr_found = False
            for e_a in edge_attrs:
                if e_a.get('n') == attribute_name:
                    return e_a.get('v')

        return None, None

    def get_node_attributesx(self):
        return self.nodeAttributes.items()

    def remove_node(self, node):
        return self.nodes.pop(node, None)

    def remove_node_attribute(self, node, attribute_name):
        node_attrs = self.get_node_attributes(node)

        if node_attrs:
            for n_a in node_attrs:
                if n_a.get('n') == attribute_name:
                    node_attrs.remove(n_a)
                    break

    def remove_edge(self, edge):
        return self.edges.pop(edge, None)

    def remove_edge_attribute(self, edge, attribute_name):
        edge_attrs = self.get_edge_attributes(edge)

        if edge_attrs:
            for e_a in edge_attrs:
                if e_a.get('n') == attribute_name:
                    edge_attrs.remove(e_a)
                    break

    #==================
    # OTHER OPERATIONS
    #==================

    def get_context(self):
        """
        Get the @context information of the network.  This information maps namespace prefixes to their defining URIs

        Example:

            ``{'pmid': 'https://www.ncbi.nlm.nih.gov/pubmed/'}``

        :return: context object
        :rtype: dict
        """

        return self.context

        # TODO uncomment when context is fixed on web app ---
        #for n_a in self.networkAttributes:
        #    if n_a.get('n') == '@context':
        #        return json.loads(n_a['v'])

        #return None

    def set_context(self, context):
        """
        Set the @context information of the network.  This information maps namespace prefixes to their defining URIs

        Example:

            ``set_context({'pmid': 'https://www.ncbi.nlm.nih.gov/pubmed/'})``


        :param context: dict of name, URI pairs
        :type context: dict
        :return: None
        :rtype: none
        """
        if isinstance(context, list):
            self.context = context

            add_this_context = {}
            for c in context:
                for k, v in c.items():
                    add_this_context[k] = v
            # TODO uncomment when context is fixed on web app --- self.add_network_attribute(name='@context', values=json.dumps(add_this_context), type='string')
        elif isinstance(context, dict):
            self.context = [context]

            # TODO uncomment when context is fixed on web app --- self.add_network_attribute(name='@context', values=json.dumps(context), type='string')
        else:
            raise Exception('Context provided is not of type list or dict')


    def get_metadata(self):
        """
        Get the network metadata

        :return: Network metadata
        :rtype: Iterator of metadata dict
        """
        return self.metadata.items()

    def set_metadata(self, metadata_obj):
        """
        Set the network metadata

        :param metadata_obj: Dict of metadata objects
        :type metadata_obj: dict
        :return: None
        :rtype: none
        """
        if isinstance(metadata_obj, dict):
            self.metadata = metadata_obj
        else:
            raise Exception('Set metadata input was not of type <dict>')

    def add_metadata(self, md):
        raise Exception('add_metadata() is deprecated')

    def get_provenance(self):
        """
        .. warning::

           This method has been deprecated.

        ..

        """
        raise Warning('getProvenance() is deprecated')
        #return self.provenance

    def get_opaque_aspect_table(self):
        return self.opaqueAspects

    def get_opaque_aspect(self, aspect_name):
        """
        Get the elements of the aspect specified by aspect_name

        :param aspect_name: the name of the aspect to retrieve.
        :type aspect_name: string
        :return: Opaque aspect
        :rtype: list of aspect elements
        """
        return self.opaqueAspects.get(aspect_name)

    def set_opaque_aspect(self, aspect_name, aspect_elements):
        """
        Set the aspect specified by aspect_name to the list of aspect elements. If aspect_elements is None, the
        aspect is removed.

        :param aspect_name: Name of the aspect
        :type aspect_name: string
        :param aspect_elements: Aspect element
        :type aspect_elements: list of dict
        :return: None
        :rtype: none
        """

        if isinstance(aspect_elements, list):
            self.opaqueAspects[aspect_name] = aspect_elements
        elif isinstance(aspect_elements, dict):
            self.opaqueAspects[aspect_name] = [aspect_elements]
        else:
            #if aspect_name is None:
            #    aspect_name = 'unknown'
            raise Exception('Provided aspect for ' + aspect_name + ' is not of type <list>')

    # TODO move removal code to remove_opaque_aspect() - Done
    def remove_opaque_aspect(self, aspect_name):
        '''
        Removes the given aspect from the opaque aspects collection

        :param aspect_name: The opaque aspect name
        :type aspect_name: str
        :return: None
        :rtype: None
        '''
        self.opaqueAspects.pop(aspect_name, None)

    def get_opaque_aspect_names(self):
        """
        Get the names of all opaque aspects

        :return: List of opaque aspect names
        :rtype: list of strings
        """
        return self.opaqueAspects.keys()

    # TODO - determine if this is useful
    def get_edge_attribute_element(self, edge, attr_name):
        attrs =  self.edgeAttributes.get(edge.get_id())
        for attr in attrs:
            if attr.get_name() == attr_name:
                return attr

        return None

    def get_edge_attributes_by_id(self, id):
        return self.edgeAttributes.get(id)

    def get_node_associated_aspects(self):
        return self.nodeAssociatedAspects

    def get_edge_associated_aspects(self):
        return self.edgeAssociatedAspects

    def get_node_associated_aspect(self, aspectName):
        return self.nodeAssociatedAspects.get(aspectName)

    def get_edge_associated_aspect(self, aspectName):
        return self.edgeAssociatedAspects.get(aspectName)

    def get_provenance(self):
        return self.provenance

    def get_missing_nodes(self):
        return self.missingNodes

    def set_provenance(self, provenance):
        """
        .. warning::

           This method has been deprecated.

        ..

        """
        raise Warning('set_provenance() is deprecated.')
        #if isinstance(provenance, list):
        #    self.provenance = provenance
        #else:
        #    raise Exception('Provided provenance was not of type <list>')

    def get_edge_citations(self):
        return self.edgeCitations

    def get_node_citations(self):
        return self.nodeCitations

    def apply_template(self, server, uuid, username=None, password=None):
        """
        Applies the Cytoscape visual properties of a network from the provided uuid to this network.

        This allows the use of networks formatted in Cytoscape as templates to apply visual styles to other networks.

        Example:

            ``nice_cx.apply_template('public.ndexbio.org', '51247435-1e5f-11e8-b939-0ac135e8bacf')``

        :param server: server host name (i.e. public.ndexbio.org)
        :type server: string
        :param username: username (optional - used when accessing private networks)
        :type username: string
        :param password: password (optional - used when accessing private networks)
        :type password:  string
        :param uuid: uuid of the styled network
        :type uuid: string
        :return: None
        :rtype: None
        """
        error_message = []
        if not server:
            error_message.append('server')
        if not uuid:
            error_message.append('uuid')

        if server and uuid:
            #===================
            # METADATA
            #===================
            available_aspects = []
            metadata_return = self.get_aspect(uuid, 'metaData', server, username, password)
            if metadata_return is None:
                raise Exception('Template not found %s.' % uuid)

            for ae in (o for o in self.get_aspect(uuid, 'metaData', server, username, password)):
                available_aspects.append(ae.get('name'))

            #=======================
            # ADD VISUAL PROPERTIES
            #=======================
            for oa in available_aspects:
                if 'visualProperties' in oa:
                    objects = self.get_aspect(uuid, 'visualProperties', server, username, password)
                    obj_items = (o for o in objects)
                    for oa_item in obj_items:
                        aspectElmts = self.opaqueAspects.get(oa)
                        if aspectElmts is None:
                            aspectElmts = []
                            self.opaqueAspects['cyVisualProperties'] = aspectElmts # ALWAYS USE cyVisualProperties

                        aspectElmts.append(oa_item)

                    mde = {
                        'name': 'cyVisualProperties',
                        'elementCount': len(aspectElmts),
                        'version': "1.0",
                        'consistencyGroup': 1,
                        'properties': []
                    }
                    self.metadata['visualProperties'] = mde

                if 'cyVisualProperties' in oa:
                    objects = self.get_aspect(uuid, 'cyVisualProperties', server, username, password)
                    obj_items = (o for o in objects)
                    for oa_item in obj_items:
                        aspectElmts = self.opaqueAspects.get(oa)
                        if aspectElmts is None:
                            aspectElmts = []
                            self.opaqueAspects[oa] = aspectElmts

                        aspectElmts.append(oa_item)

                    mde = {
                              'name': 'cyVisualProperties',
                              'elementCount': len(aspectElmts),
                              'version': "1.0",
                              'consistencyGroup': 1,
                              'properties': []
                          }
                    self.metadata['cyVisualProperties'] = mde

        else:
            raise Exception(', '.join(error_message) + 'not specified in apply_template')

    def __merge_node_attributes(self, source_attribute1, source_attribute2, target_attribute):
        """
        Checks 2 attribute fields for values and merges them into one attribute.  The best use is when one attribute
        is empty which occurs when loading from an edge file.  Use with caution

        :param source_attribute1: The name of the first attribute
        :type source_attribute1: basestring
        :param source_attribute2: The name of the second attribute
        :type source_attribute2: basestring
        :param target_attribute: The desired name for the merged data
        :type target_attribute: basestring
        :return:
        :rtype:
        """
        raise Warning('merge_node_attributes() is deprecated')

        #for node_id, node in self.nodes.items():
        #    value1 = self.get_node_attribute(node, source_attribute1)
        #    value2 = self.get_node_attribute(node, source_attribute2)
        #    merged_value = value1 or value2
        #    if merged_value:
        #        self.set_node_attribute(node, target_attribute, merged_value)
        #        self.remove_node_attribute(node, source_attribute1)
        #        self.remove_node_attribute(node, source_attribute2)

    def create_from_pandas(self, df, source_field=None, target_field=None, source_node_attr=[], target_node_attr=[], edge_attr=[], edge_interaction=None):
        raise Exception('create_from_pandas() is no longer supported in NiceCXNetwork.  Please use ndex2.create_nice_cx_from_pandas()')

    def create_from_networkx(self, G):
        raise Exception('create_from_networkx() is no longer supported in NiceCXNetwork.  Please use ndex2.create_nice_cx_from_networkx()')

    def create_from_server(self, server, username, password, uuid):
        raise Exception('create_from_server() is no longer supported in NiceCXNetwork.  Please use ndex2.create_nice_cx_from_server()')

    def create_from_cx(self, cx):
        raise Exception('create_from_cx() is no longer supported in NiceCXNetwork.  Please use ndex2.create_nice_cx_from_raw_cx()')

    def get_frag_from_list_by_key(self, cx, key):
        for aspect in cx:
            if key in aspect:
                return aspect[key]

        return []

    def to_pandas_dataframe(self):
        """
        Export the network as a Pandas DataFrame.

         Example:

            ``df = nice_cx.to_pandas_dataframe() # df is now a pandas dataframe``

        Note: This method only processes nodes, edges, node attributes and edge attributes, but not network attributes
        or other aspects

        :return: Pandas dataframe
        :rtype: Pandas dataframe
        """
        #TODO expand documentation
        rows = []
        edge_items = None
        if sys.version_info.major == 3:
            edge_items = self.edges.items()
        else:
            edge_items = self.edges.iteritems()

        for k, v in edge_items:
            e_a = self.edgeAttributes.get(k)
            #==========================
            # PROCESS EDGE ATTRIBUTES
            #==========================
            add_this_dict = {}
            if e_a is not None:
                for e_a_item in e_a:
                    if isinstance(e_a_item.get('v'), list):
                        add_this_dict[e_a_item.get('n')] = ','.join(str(e) for e in e_a_item.get('v'))
                        add_this_dict[e_a_item.get('n')] = '"' + add_this_dict[e_a_item.get('n')] + '"'
                    else:
                        add_this_dict[e_a_item.get('n')] = e_a_item.get('v')
            #================================
            # PROCESS SOURCE NODE ATTRIBUTES
            #================================
            s_a = self.nodeAttributes.get(v.get('s'))
            if s_a is not None:
                for s_a_item in s_a:
                    if isinstance(s_a_item.get('v'), list):
                        add_this_dict['source_' + s_a_item.get('n')] = ','.join(str(e) for e in s_a_item.get('v'))
                        add_this_dict['source_' + s_a_item.get('n')] = '"' + add_this_dict['source_' + s_a_item.get('n')] + '"'
                    else:
                        add_this_dict['source_' + s_a_item.get('n')] = s_a_item.get('v')

            #================================
            # PROCESS TARGET NODE ATTRIBUTES
            #================================
            t_a = self.nodeAttributes.get(v.get('t'))
            if t_a is not None:
                for t_a_item in t_a:
                    if isinstance(t_a_item.get('v'), list):
                        add_this_dict['target_' + t_a_item.get('n')] = ','.join(str(e) for e in t_a_item.get('v'))
                        add_this_dict['target_' + t_a_item.get('n')] = '"' + add_this_dict['target_' + t_a_item.get('n')] + '"'
                    else:
                        add_this_dict['target_' + t_a_item.get('n')] = t_a_item.get('v')

            if add_this_dict:
                rows.append(dict(add_this_dict, source=self.nodes.get(v.get('s')).get('n'), target=self.nodes.get(v.get('t')).get('n'), interaction=v.get('i')))
            else:
                rows.append(dict(source=self.nodes.get(v.get('s')).get('n'), target=self.nodes.get(v.get('t')).get('n'), interaction=v.get('i')))

        nodeAttributeSourceTarget = []
        for n_a in self.nodeAttributeHeader:
            nodeAttributeSourceTarget.append('source_' + n_a)
            nodeAttributeSourceTarget.append('target_' + n_a)

        df_columns = ['source', 'interaction', 'target'] + list(self.edgeAttributeHeader) + nodeAttributeSourceTarget

        return_df = pd.DataFrame(rows, columns=df_columns)

        return return_df

    def to_neo4j(self):
    
        #niceCx = ndex2.create_nice_cx_from_server(server='public.ndexbio.org',
                                                  #uuid='d3c5ca09-bb42-11e7-94d3-0ac135e8bacf')
    
        neo4j_node_lookup = {}
        db = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")
    
        # CREATE NODES
        gene = db.labels.create("Gene")
        for k, v in self.get_nodes():
            neo4j_node_lookup[v.get('@id')] = db.nodes.create(name=v.get('n'))
            gene.add(neo4j_node_lookup[v.get('@id')])
    
        # CREATE EDGES
        for k, v in self.get_edges():
            g1 = neo4j_node_lookup.get(v.get('s'))
            g2 = neo4j_node_lookup.get(v.get('t'))
            g1.relationships.create(v.get('i'), g2)
    
        #q = 'MATCH (n)-[r]-p RETURN n,r,p'
    
        #results = db.query(q, returns=(client.Node, str, client.Node))
    
        #for r in results:
        #    print("(%s)-[%s]->(%s)" % (r[0]["name"], r[1], r[2]["name"]))
        print('neo4j data created')
    
    def add_metadata_stub(self, aspect_name):
        md = self.metadata.get(aspect_name)
        #if md is None:
        #    mde = MetaDataElement(elementCount=0, properties=[], version='1.0', consistencyGroup=1, name=aspect_name)
        #    self.add_metadata(mde)

    def to_cx_stream(self):
        """
        Returns a stream of the CX corresponding to the network. Can be used to post to endpoints that can accept
        streaming inputs

        :return: The CX stream representation of this network.
        :rtype: io.BytesIO
        """
        cx = self.to_cx()

        if sys.version_info.major == 3:
            return io.BytesIO(json.dumps(cx).encode('utf-8'))
        else:
            return_bytes = None
            try:
                return_bytes = io.BytesIO(json.dumps(cx))
            except UnicodeDecodeError as err1:
                print("Detected invalid encoding. Trying latin-1 encoding.")
                return_bytes = io.BytesIO(json.dumps(cx, encoding="latin-1"))
                print("Success")
            except Exception as err2:
                print(err2.message)

            return return_bytes

    def upload_to(self, server, username, password):
        """
        Upload this network to the specified server to the account specified by username and password.

        Example:

            ``nice_cx.upload_to('http://public.ndexbio.org', username, password)``

        :param server: The NDEx server to upload the network to.
        :type server: string
        :param username: The username of the account to store the network.
        :type username: string
        :param password: The password for the account.
        :type password: string
        :return: The UUID of the network on NDEx.
        :rtype: string
        """
        if server and 'http' not in server:
            server = 'http://' + server

        ndex = nc.Ndex2(server,username,password, user_agent=self.user_agent)

        return ndex.save_new_network(self.to_cx())

    def upload_new_network_stream(self, server, username, password):
        raise Exception('upload_new_network_stream() is no longer supported.  Please use upload_to()')

    def update_to(self, uuid, server, username, password):
        """ Upload this network to the specified server to the account specified by username and password.

        Example:

            ``nice_cx.update_to('2ec87c51-c349-11e8-90ac-525400c25d22', 'public.ndexbio.org, username, password)``

        :param server: The NDEx server to upload the network to.
        :type server: str
        :param username: The username of the account to store the network.
        :type username: str
        :param password: The password for the account.
        :type password: str
        :return: The UUID of the network on NDEx.
        :rtype: str

        """
        cx = self.to_cx()
        ndex = nc.Ndex2(server,username,password, user_agent=self.user_agent)

        if(len(cx) > 0):
            if(cx[len(cx) - 1] is not None):
                if(cx[len(cx) - 1].get('status') is None):
                    # No STATUS element in the array.  Append a new status
                    cx.append({"status" : [ {"error" : "","success" : True} ]})
                else:
                    if(len(cx[len(cx) - 1].get('status')) < 1):
                        # STATUS element found, but the status was empty
                        cx[len(cx) - 1].get('status').append({"error" : "","success" : True})

            if sys.version_info.major == 3:
                stream = io.BytesIO(json.dumps(cx).encode('utf-8'))
            else:
                stream = io.BytesIO(json.dumps(cx))

            return ndex.update_cx_network(stream, uuid)
        else:
            raise IndexError("Cannot save empty CX.  Please provide a non-empty CX document.")

    def to_networkx(self):
        """
        Returns a NetworkX graph based on the network. Elements in the CartesianCoordinates aspect
        of the network are transformed to the NetworkX pos attribute. Node name is stored in the networkx
        node id. Node 'represents' is stored in the networkx node attribute 'represents'

        Example:

            ``G = nice_cx.to_networkx() # G is now a networkx object``

        :return: Networkx graph
        :rtype: networkx Graph()
        """
        G = nx.Graph()

        if sys.version_info.major == 3:
            node_items = self.nodes.items()
            edge_items = self.edges.items()
        else:
            node_items = self.nodes.iteritems()
            edge_items = self.edges.iteritems()

        #============================
        # PROCESS NETWORK ATTRIBUTES
        #============================
        for net_a in self.networkAttributes:
            G.graph[net_a.get('n')] = net_a.get('v')


        if float(nx.__version__) >= 2.0:
            # ================================
            # PROCESS NODE & NODE ATTRIBUTES
            # ================================
            for k, v in node_items:
                node_name = v.get('n')
                G.add_node(v.get('n'))
                n_a = self.nodeAttributes.get(k)
                if n_a:
                    for na_item in n_a:
                        G.nodes[node_name][na_item.get('n')] = na_item.get('v')

                if v.get('r'):
                    G.nodes[node_name]['represents'] = v.get('r')

            #================================
            # PROCESS EDGE & EDGE ATTRIBUTES
            #================================
            for k, v in edge_items:
                source_node = self.nodes.get(v.get('s')).get('n')
                target_node = self.nodes.get(v.get('t')).get('n')

                G.add_edge(source_node, target_node)

                e_a = self.edgeAttributes.get(k)
                add_this_dict = {}
                add_this_dict['interaction'] = v.get('i')
                G[source_node][target_node]['interaction'] = v.get('i')
                if e_a is not None:
                    for e_a_item in e_a:
                        if isinstance(e_a_item.get('v'), list):
                            G[source_node][target_node][e_a_item.get('n')] =  '"%s"' % ','.join(str(e) for e in e_a_item.get('v'))
                        else:
                            G[source_node][target_node][e_a_item.get('n')] =  e_a_item.get('v')
        else:
            print('networkx version 1.11')
            # ================================
            # PROCESS NODE & NODE ATTRIBUTES
            # ================================
            for k, v in node_items:
                node_attrs = {}
                n_a = self.nodeAttributes.get(k)
                if n_a:
                    for na_item in n_a:
                        node_attrs[na_item.get('n')] = na_item.get('v')

                G.add_node(k, node_attrs, name=v.get('n'))

            # ================================
            # PROCESS EDGE & EDGE ATTRIBUTES
            # ================================
            for k, v in edge_items:
                e_a = self.edgeAttributes.get(k)
                add_this_dict = {}
                add_this_dict['interaction'] = v.get('i')
                if e_a is not None:
                    for e_a_item in e_a:
                        if isinstance(e_a_item.get('v'), list):
                            add_this_dict[e_a_item.get('n')] = ','.join(str(e) for e in e_a_item.get('v'))
                            add_this_dict[e_a_item.get('n')] = '"' + add_this_dict[e_a_item.get('n')] + '"'
                        else:
                            add_this_dict[e_a_item.get('n')] = e_a_item.get('v')

                G.add_edge(v.get('s'), v.get('t'), add_this_dict)

        #================
        # PROCESS LAYOUT
        #================
        cartesian_layout = self.opaqueAspects.get('cartesianLayout')
        if cartesian_layout:
            G.pos = {}
            for x_y_pos in cartesian_layout:
                G.pos[x_y_pos.get('node')] = (x_y_pos.get('x'), x_y_pos.get('y'))

        return G

    def get_summary(self):
        """
        .. warning::

           This method has been deprecated.  Please use **print_summary()**

        ..

        """

        raise Warning('get_summary() is deprecated.  Please use print_summary() instead')

        n_a_count = 0
        for k, v in self.nodeAttributes.items():
            n_a_count += len(v)

        e_a_count = 0
        for k, v in self.edgeAttributes.items():
            e_a_count += len(v)

        network_name = self.get_name()
        if not network_name:
            network_name = 'Untitled'

        summary_json = {
            'Name': network_name,
            'Nodes': len(self.nodes),
            'Edges': + len(self.edges),
            'Node Attributes': n_a_count,
            'Edge Attributes': e_a_count
        }

        return summary_json

    def print_summary(self):
        """
        Print a network summary

        :return: Network summary
        :rtype: string
        """
        n_a_count = 0
        for k, v in self.nodeAttributes.items():
            n_a_count += len(v)

        e_a_count = 0
        for k, v in self.edgeAttributes.items():
            e_a_count += len(v)

        network_name = self.get_name()
        if not network_name:
            network_name = 'Untitled'

        summary_string = \
            'Name: ' + network_name + '\n'\
            'Nodes: ' + str(len(self.nodes)) + '\n'\
            + 'Edges: ' + str(len(self.edges)) + '\n'\
            + 'Node Attributes: ' + str(n_a_count) + '\n'\
            + 'Edge Attributes: ' + str(e_a_count) + '\n'

        print(summary_string)

    def __str__(self):
        return 'nodes: %d \n edges: %d' % (len(self.nodes), len(self.edges)) #f'nodes: {len(self.nodes)} edges: {len(self.edges)}'

    def to_cx(self):
        """
        Return the CX corresponding to the network.

        :return: CX representation of the network
        :rtype: CX (list of dict aspects)
        """

        if len(self.nodes.keys()) < 1:
            raise Exception('No nodes detected.  Please ensure that at least one node is present.')

        #TODO - when server is compatible remove numberVerification and alter metadata insert() to position 0
        output_cx = [{"numberVerification": [{"longNumber": 281474976710655}]}]

        #print('Generating CX')

        #=====================================================
        # IF THE @ID IS NOT NUMERIC WE NEED TO CONVERT IT TO
        # INT BY USING THE INDEX OF THE NON-NUMERIC VALUE
        #=====================================================
        if self.context:
            output_cx.append(self.generate_aspect('@context'))
        if self.nodes:
            output_cx.append(self.generate_aspect('nodes'))
        if self.edges:
            output_cx.append(self.generate_aspect('edges'))
        if self.networkAttributes:
            output_cx.append(self.generate_aspect('networkAttributes'))
        if self.nodeAttributes:
            output_cx.append(self.generate_aspect('nodeAttributes'))
        if self.edgeAttributes:
            output_cx.append(self.generate_aspect('edgeAttributes'))
        if self.citations:
            output_cx.append(self.generate_aspect('citations'))
        if self.nodeCitations:
            output_cx.append(self.generate_aspect('nodeCitations'))
        if self.edgeCitations:
            output_cx.append(self.generate_aspect('edgeCitations'))
        if self.supports:
            output_cx.append(self.generate_aspect('supports'))
        if self.edgeSupports:
            output_cx.append(self.generate_aspect('edgeSupports'))
        if self.opaqueAspects:
            for oa in self.opaqueAspects:
                if isinstance(self.opaqueAspects[oa], bytes):
                    bytes_string = self.opaqueAspects[oa].decode('ascii')
                    output_cx.append({oa: [bytes_string]})
                else:
                    output_cx.append({oa: self.opaqueAspects[oa]})
                oa_md = self.metadata.get(oa)
                if oa_md:
                    oa_md['elementCount'] = len(self.opaqueAspects[oa])
                else:
                    self.metadata[oa] = {
                        'name': oa,
                        'elementCount': len(self.opaqueAspects[oa]),
                        'idCounter': len(self.opaqueAspects[oa]) + 1,
                        'properties': []
                    }

        if self.metadata:
            #===========================
            # UPDATE CONSISTENCY GROUP
            #===========================
            metadata_list = []
            for k, mdata in self.metadata.items():
                metadata_list.append(mdata)

            output_cx.insert(1, {'metaData': metadata_list})

            if output_cx[-1].get('status') is None:
                output_cx.append({'status': [{'error': '', 'success': True}]})

        return output_cx

    def generate_aspect(self, aspect_name):
        core_aspect = ['nodes', 'edges','networkAttributes', 'nodeAttributes', 'edgeAttributes', 'metaData', '@context', 'citations', 'supports']
        aspect_element_array = []
        element_count = 0
        element_id_max = 0

        use_this_aspect = None
        #=============================
        # PROCESS CORE ASPECTS FIRST
        #=============================
        if aspect_name in core_aspect:
            use_this_aspect = self.string_to_aspect_object(aspect_name)

        if use_this_aspect is not None:



            if isinstance(use_this_aspect, dict):
                if aspect_name in ['nodes', 'edges']:
                    for k, asp in use_this_aspect.items():
                        element_count += 1
                        if asp.get('@id') > element_id_max:
                            element_id_max = asp.get('@id')
                        aspect_element_array.append(asp)
                else:
                    for k, asp in use_this_aspect.items():
                        if isinstance(asp, list):
                            for asp_item in asp:
                                element_count += 1
                                aspect_element_array.append(asp_item)
                        else:
                            element_count += 1
                            aspect_element_array.append(asp)
            elif isinstance(use_this_aspect, list):
                aspect_element_array = use_this_aspect
                element_count = len(use_this_aspect)

        else:
            #===========================
            # PROCESS NON-CORE ASPECTS
            #===========================
            use_this_aspect = self.string_to_aspect_object(aspect_name)

            if use_this_aspect is not None:
                if isinstance(use_this_aspect, dict):
                    items = None
                    if sys.version_info.major == 3:
                        items = use_this_aspect.items()
                    else:
                        items = use_this_aspect.iteritems()

                    for k, v in items:
                        if aspect_name == 'edgeSupports':
                            if isinstance(v, list):
                                aspect_element_array.append({'po': [k], 'supports': v})
                            else:
                                aspect_element_array.append({'po': [k], 'supports': [v]})
                        else:
                            if isinstance(v, list):
                                aspect_element_array.append({'po': [k], 'citations': v})
                            else:
                                aspect_element_array.append({'po': [k], 'citations': [v]})
                        element_count +=1
                else:
                    raise Exception('Citation was not in json format')
            else:
                return None

        md = {
            'name': aspect_name,
            'elementCount': element_count,
            'idCounter': element_count,
            'version': "1.0",
            'consistencyGroup': 1,
            'properties': []
        }

        self.metadata[aspect_name] = md

        aspect = {aspect_name: aspect_element_array}

        return aspect

    def generate_metadata_aspect(self):
        aspect_element_array = []
        element_count = 0
        element_id_max = 0

        use_this_aspect = self.string_to_aspect_object('metaData')

        if use_this_aspect is not None:
            if sys.version_info.major == 3:
                items = use_this_aspect.items()
            else:
                items = use_this_aspect.iteritems()

            for k, v in items:
                add_this_element = v.to_cx()
                id = add_this_element.get('@id')

                if id is not None and id > element_id_max:
                    element_id_max = id
                aspect_element_array.append(add_this_element)
                element_count +=1

        aspect = {'metaData': aspect_element_array}

        return aspect

    def handle_metadata_update(self, aspect_name):
        aspect = self.string_to_aspect_object(aspect_name)

    def update_consistency_group(self):
        consistency_group = 1
        if self.metadata:
            for mi_k, mi_v in self.metadata.items():
                cg = mi_v.get_consistency_group()
                if cg > consistency_group:
                    consistency_group = cg

            consistency_group += 1 # bump the consistency group up by one

            for mi_k, mi_v in self.metadata.items():
                #print mi_k
                #print mi_v
                mi_v.set_consistency_group(consistency_group)

    def generate_metadata(self, G, unclassified_cx):
        #if self.metadata:
        #    for k, v in self.metadata.iteritems():


        return_metadata = []
        consistency_group = 1
        if(self.metadata_original is not None):
            for mi in self.metadata_original:
                if(mi.get("consistencyGroup") is not None):
                    if(mi.get("consistencyGroup") > consistency_group):
                        consistency_group = mi.get("consistencyGroup")
                else:
                    mi['consistencyGroup'] = 0

            consistency_group += 1 # bump the consistency group up by one

            #print("consistency group max: " + str(consistency_group))

        # ========================
        # @context metadata
        # ========================
        #if self.context: # REPLACED BY NETWORK ATTRIBUTE: @context
        #    return_metadata.append(
        #        {
        #            "consistencyGroup": consistency_group,
        #            "elementCount": 1,
        #            "name": "@context",
        #            "properties": [],
        #            "version": "1.0"
        #        }
        #    )

        #========================
        # Nodes metadata
        #========================
        node_ids = [n[0] for n in G.nodes_iter(data=True)]
        if(len(node_ids) < 1):
            node_ids = [0]
        return_metadata.append(
            {
                "consistencyGroup" : consistency_group,
                "elementCount" : len(node_ids),
                "idCounter": max(node_ids),
                "name" : "nodes",
                "properties" : [ ],
                "version" : "1.0"
            }
        )

        #========================
        # Edges metadata
        #========================
        edge_ids = [e[2]for e in G.edges_iter(data=True, keys=True)]
        if(len(edge_ids) < 1):
            edge_ids = [0]
        return_metadata.append(
            {
                "consistencyGroup" : consistency_group,
                "elementCount" : len(edge_ids),
                "idCounter": max(edge_ids),
                "name" : "edges",
                "properties" : [ ],
                "version" : "1.0"
            }
        )

        #=============================
        # Network Attributes metadata
        #=============================
        if(len(G.graph) > 0):
            return_metadata.append(
                {
                    "consistencyGroup" : consistency_group,
                    "elementCount" : len(G.graph),
                    "name" : "networkAttributes",
                    "properties" : [ ],
                    "version" : "1.0"
                }
            )

        #===========================
        # Node Attributes metadata
        #===========================
        #id_max = 0
        attr_count = 0
        for node_id , attributes in G.nodes_iter(data=True):
            for attribute_name in attributes:
                if attribute_name != "name" and attribute_name != "represents":
                    attr_count += 1

        if(attr_count > 0):
            return_metadata.append(
                {
                    "consistencyGroup" : consistency_group,
                    "elementCount" : attr_count,
                    #"idCounter": id_max,
                    "name" : "nodeAttributes",
                    "properties" : [ ],
                    "version" : "1.0"
                }
            )

        #===========================
        # Edge Attributes metadata
        #===========================
        #id_max = 0
        attr_count = 0
        for s, t, id, a in G.edges(data=True, keys=True):
            if(bool(a)):
                for attribute_name in a:
                    if attribute_name != "interaction":
                        attr_count += 1

        if(attr_count > 0):
            return_metadata.append(
                {
                    "consistencyGroup" : consistency_group,
                    "elementCount" : attr_count,
                    #"idCounter": id_max,
                    "name" : "edgeAttributes",
                    "properties" : [ ],
                    "version" : "1.0"
                }
            )

        #===========================
        # cyViews metadata
        #===========================
        if self.view_id != None:
            return_metadata.append(
                {
                    "elementCount": 1,
                    "name": "cyViews",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        #===========================
        # subNetworks metadata
        #===========================
        if self.subnetwork_id != None:
            return_metadata.append(
                {
                    "elementCount": 1,
                    "name": "subNetworks",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        #===========================
        # networkRelations metadata
        #===========================
        if self.subnetwork_id != None and self.view_id != None:
            return_metadata.append(
                {
                    "elementCount": 2,
                    "name": "networkRelations",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        #===========================
        # citations and supports metadata
        #===========================
        if len(self.support_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.support_map),
                    "name": "supports",
                    "properties": [],
                    "idCounter": max(self.support_map.keys()),
                    "consistencyGroup" : consistency_group
                }
            )

        if len(self.node_support_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.node_support_map),
                    "name": "nodeSupports",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )
        if len(self.edge_support_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.edge_support_map),
                    "name": "edgeSupports",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        if len(self.citation_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.citation_map),
                    "name": "citations",
                    "properties": [],
                    "idCounter": max(self.citation_map.keys()),
                    "consistencyGroup" : consistency_group
                }
            )

        if len(self.node_citation_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.node_citation_map),
                    "name": "nodeCitations",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        if len(self.edge_citation_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.edge_citation_map),
                    "name": "edgeCitations",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        if len(self.function_term_map) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.function_term_map),
                    "name": "functionTerms",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        if len(self.reified_edges) > 0:
            return_metadata.append(
                {
                    "elementCount": len(self.reified_edges),
                    "name": "reifiedEdges",
                    "properties": [],
                    "consistencyGroup" : consistency_group
                }
            )

        #===========================
        # ndexStatus metadata
        #===========================
        return_metadata.append(
            {
                "consistencyGroup": consistency_group,
                "elementCount": 1,
                "name": "ndexStatus",
                "properties": [],
                "version": "1.0"
            }
        )

        #===========================
        # cartesianLayout metadata
        #===========================
        if self.pos and len(self.pos) > 0:
            return_metadata.append(
                {
                    "consistencyGroup": consistency_group,
                    "elementCount": len(self.pos),
                    "name": "cartesianLayout",
                    "properties": [],
                    "version": "1.0"
                }
            )

        #===========================
        # OTHER metadata
        #===========================
        for asp in self.unclassified_cx:
            try:
                aspect_type = asp.iterkeys().next()
                if(aspect_type == "visualProperties"
                   or aspect_type == "cyVisualProperties"
                   or aspect_type == "@context"):
                    return_metadata.append(
                        {
                            "consistencyGroup" : consistency_group,
                            "elementCount":len(asp[aspect_type]),
                            "name":aspect_type,
                            "properties":[]
                         }
                    )
            except Exception as e:
                print(e.message)

        return [{'metaData': return_metadata}]

    def string_to_aspect_object(self, aspect_name):
        if aspect_name == 'metaData':
            return self.metadata
        elif aspect_name == '@context':
            return self.context
        elif aspect_name == 'nodes':
            return self.nodes
        elif aspect_name == 'edges':
            return self.edges
        elif aspect_name == 'networkAttributes':
            return self.networkAttributes
        elif aspect_name == 'nodeAttributes':
            return self.nodeAttributes
        elif aspect_name == 'edgeAttributes':
            return self.edgeAttributes
        elif aspect_name == 'citations':
            return self.citations
        elif aspect_name == 'nodeCitations':
            return self.nodeCitations
        elif aspect_name == 'edgeCitations':
            return self.edgeCitations
        elif aspect_name == 'edgeSupports':
            return self.edgeSupports
        elif aspect_name == 'supports':
            return self.supports

    def get_aspect(self, uuid, aspect_name, server, username, password, stream=False):
        if stream:
            return self.stream_aspect(uuid, aspect_name, server, username, password)
        else:
            return self.get_stream(uuid, aspect_name, server, username, password)

    # The stream refers to the Response, not the Request
    def get_stream(self, uuid, aspect_name, server, username, password):
        if 'http' not in server:
            server = 'http://' + server

        s = requests.session()
        if username and password:
            # add credentials to the session, if available
            s.auth = (username, password)

        if aspect_name == 'metaData':
            md_response = s.get(server + '/v2/network/' + uuid + '/aspect')
            json_response = md_response.json()
            s.close()
            return json_response.get('metaData')
        else:
            aspect_response = s.get(server + '/v2/network/' + uuid + '/aspect/' + aspect_name)
            json_response = aspect_response.json()
            s.close()
            return json_response

    def stream_aspect(self, uuid, aspect_name, server, username, password):
        if 'http' not in server:
            server = 'http://' + server
        if aspect_name == 'metaData':
            print(server + '/v2/network/' + uuid + '/aspect')

            s = requests.session()
            if username and password:
                # add credentials to the session, if available
                s.auth = (username, password)
            md_response = s.get(server + '/v2/network/' + uuid + '/aspect')
            json_response = md_response.json()
            s.close()
            return json_response.get('metaData')
        else:
            if username and password:
                #base64string = base64.b64encode('%s:%s' % (username, password))
                request = Request(server + '/v2/network/' + uuid + '/aspect/' + aspect_name, headers={"Authorization": "Basic " + base64.encodestring(username + ':' + password).replace('\n', '')})
            else:
                request = Request(server + '/v2/network/' + uuid + '/aspect/' + aspect_name)
            try:
                urlopen_result = urlopen(request) #'http://dev2.ndexbio.org/v2/network/' + uuid + '/aspect/' + aspect_name)
            except HTTPError as e:
                print(e.code)
                return []
            except URLError as e:
                print('Other error')
                print('URL Error %s' % e.message())
                return []

            return_items = ijson.items(urlopen_result, 'item')
            return return_items

    def _stringify_node_attributes(self):
        for node_id, node in self.get_nodes():
            if self.get_node_attributes(node) is not None:
                for attr in self.get_node_attributes(node):
                    if isinstance(attr['v'], dict) or isinstance(attr['v'], list):
                        attr['v'] = json.dumps(attr['v'])
                    elif not isinstance(attr['v'], str):
                        attr['v'] = str(attr['v'])




class DecimalEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        if sys.version_info.major == 3:
            if isinstance(o, np.int64):
                return int(o)
        return super(DecimalEncoder, self).default(o)

import ndex2.client as nc
