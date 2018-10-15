# coding: utf-8

"""
    Assetic Integration API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

##from assetic.models.web_api_hal_embedded_resource import WebApiHalEmbeddedResource  # noqa: F401,E501
##from assetic.models.web_api_hal_link import WebApiHalLink  # noqa: F401,E501


class Assetic3IntegrationRepresentationsRequestorTypeRepresentation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'type': 'str',
        'links': 'list[WebApiHalLink]',
        'embedded': 'list[WebApiHalEmbeddedResource]'
    }

    attribute_map = {
        'id': 'Id',
        'type': 'Type',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, id=None, type=None, links=None, embedded=None):  # noqa: E501
        """Assetic3IntegrationRepresentationsRequestorTypeRepresentation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._type = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def id(self):
        """Gets the id of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501


        :return: The id of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.


        :param id: The id of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501


        :return: The type of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.


        :param type: The type of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def links(self):
        """Gets the links of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501


        :return: The links of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :rtype: list[WebApiHalLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.


        :param links: The links of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :type: list[WebApiHalLink]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501


        :return: The embedded of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :rtype: list[WebApiHalEmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.


        :param embedded: The embedded of this Assetic3IntegrationRepresentationsRequestorTypeRepresentation.  # noqa: E501
        :type: list[WebApiHalEmbeddedResource]
        """

        self._embedded = embedded

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Assetic3IntegrationRepresentationsRequestorTypeRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
