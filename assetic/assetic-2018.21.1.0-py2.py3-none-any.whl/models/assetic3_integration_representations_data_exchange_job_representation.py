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


class Assetic3IntegrationRepresentationsDataExchangeJobRepresentation(object):
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
        'profile_id': 'str',
        'document_id': 'str',
        'links': 'list[WebApiHalLink]',
        'embedded': 'list[WebApiHalEmbeddedResource]'
    }

    attribute_map = {
        'profile_id': 'ProfileId',
        'document_id': 'DocumentId',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, profile_id=None, document_id=None, links=None, embedded=None):  # noqa: E501
        """Assetic3IntegrationRepresentationsDataExchangeJobRepresentation - a model defined in Swagger"""  # noqa: E501

        self._profile_id = None
        self._document_id = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if profile_id is not None:
            self.profile_id = profile_id
        if document_id is not None:
            self.document_id = document_id
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def profile_id(self):
        """Gets the profile_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501


        :return: The profile_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.


        :param profile_id: The profile_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def document_id(self):
        """Gets the document_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501


        :return: The document_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :rtype: str
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.


        :param document_id: The document_id of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :type: str
        """

        self._document_id = document_id

    @property
    def links(self):
        """Gets the links of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501


        :return: The links of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :rtype: list[WebApiHalLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.


        :param links: The links of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :type: list[WebApiHalLink]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501


        :return: The embedded of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
        :rtype: list[WebApiHalEmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.


        :param embedded: The embedded of this Assetic3IntegrationRepresentationsDataExchangeJobRepresentation.  # noqa: E501
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
        if not isinstance(other, Assetic3IntegrationRepresentationsDataExchangeJobRepresentation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
