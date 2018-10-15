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


class Assetic3IntegrationRepresentationsResourceGroupCraft(object):
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
        'unit_craft_id': 'str',
        'group_craft_id': 'str',
        'work_group_id': 'int',
        'work_group_name': 'str',
        'craft_type_id': 'int',
        'craft_type': 'str',
        'unit_type_id': 'str',
        'unit_type': 'str',
        'unit_rate': 'float',
        'links': 'list[WebApiHalLink]',
        'embedded': 'list[WebApiHalEmbeddedResource]'
    }

    attribute_map = {
        'unit_craft_id': 'UnitCraftId',
        'group_craft_id': 'GroupCraftId',
        'work_group_id': 'WorkGroupId',
        'work_group_name': 'WorkGroupName',
        'craft_type_id': 'CraftTypeId',
        'craft_type': 'CraftType',
        'unit_type_id': 'UnitTypeId',
        'unit_type': 'UnitType',
        'unit_rate': 'UnitRate',
        'links': '_links',
        'embedded': '_embedded'
    }

    def __init__(self, unit_craft_id=None, group_craft_id=None, work_group_id=None, work_group_name=None, craft_type_id=None, craft_type=None, unit_type_id=None, unit_type=None, unit_rate=None, links=None, embedded=None):  # noqa: E501
        """Assetic3IntegrationRepresentationsResourceGroupCraft - a model defined in Swagger"""  # noqa: E501

        self._unit_craft_id = None
        self._group_craft_id = None
        self._work_group_id = None
        self._work_group_name = None
        self._craft_type_id = None
        self._craft_type = None
        self._unit_type_id = None
        self._unit_type = None
        self._unit_rate = None
        self._links = None
        self._embedded = None
        self.discriminator = None

        if unit_craft_id is not None:
            self.unit_craft_id = unit_craft_id
        if group_craft_id is not None:
            self.group_craft_id = group_craft_id
        if work_group_id is not None:
            self.work_group_id = work_group_id
        if work_group_name is not None:
            self.work_group_name = work_group_name
        if craft_type_id is not None:
            self.craft_type_id = craft_type_id
        if craft_type is not None:
            self.craft_type = craft_type
        if unit_type_id is not None:
            self.unit_type_id = unit_type_id
        if unit_type is not None:
            self.unit_type = unit_type
        if unit_rate is not None:
            self.unit_rate = unit_rate
        if links is not None:
            self.links = links
        if embedded is not None:
            self.embedded = embedded

    @property
    def unit_craft_id(self):
        """Gets the unit_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The unit_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: str
        """
        return self._unit_craft_id

    @unit_craft_id.setter
    def unit_craft_id(self, unit_craft_id):
        """Sets the unit_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param unit_craft_id: The unit_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: str
        """

        self._unit_craft_id = unit_craft_id

    @property
    def group_craft_id(self):
        """Gets the group_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The group_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: str
        """
        return self._group_craft_id

    @group_craft_id.setter
    def group_craft_id(self, group_craft_id):
        """Sets the group_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param group_craft_id: The group_craft_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: str
        """

        self._group_craft_id = group_craft_id

    @property
    def work_group_id(self):
        """Gets the work_group_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The work_group_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: int
        """
        return self._work_group_id

    @work_group_id.setter
    def work_group_id(self, work_group_id):
        """Sets the work_group_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param work_group_id: The work_group_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: int
        """

        self._work_group_id = work_group_id

    @property
    def work_group_name(self):
        """Gets the work_group_name of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The work_group_name of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: str
        """
        return self._work_group_name

    @work_group_name.setter
    def work_group_name(self, work_group_name):
        """Sets the work_group_name of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param work_group_name: The work_group_name of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: str
        """

        self._work_group_name = work_group_name

    @property
    def craft_type_id(self):
        """Gets the craft_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The craft_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: int
        """
        return self._craft_type_id

    @craft_type_id.setter
    def craft_type_id(self, craft_type_id):
        """Sets the craft_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param craft_type_id: The craft_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: int
        """

        self._craft_type_id = craft_type_id

    @property
    def craft_type(self):
        """Gets the craft_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The craft_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: str
        """
        return self._craft_type

    @craft_type.setter
    def craft_type(self, craft_type):
        """Sets the craft_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param craft_type: The craft_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: str
        """

        self._craft_type = craft_type

    @property
    def unit_type_id(self):
        """Gets the unit_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The unit_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: str
        """
        return self._unit_type_id

    @unit_type_id.setter
    def unit_type_id(self, unit_type_id):
        """Sets the unit_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param unit_type_id: The unit_type_id of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: str
        """

        self._unit_type_id = unit_type_id

    @property
    def unit_type(self):
        """Gets the unit_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The unit_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: str
        """
        return self._unit_type

    @unit_type.setter
    def unit_type(self, unit_type):
        """Sets the unit_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param unit_type: The unit_type of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: str
        """

        self._unit_type = unit_type

    @property
    def unit_rate(self):
        """Gets the unit_rate of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The unit_rate of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: float
        """
        return self._unit_rate

    @unit_rate.setter
    def unit_rate(self, unit_rate):
        """Sets the unit_rate of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param unit_rate: The unit_rate of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: float
        """

        self._unit_rate = unit_rate

    @property
    def links(self):
        """Gets the links of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The links of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: list[WebApiHalLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param links: The links of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :type: list[WebApiHalLink]
        """

        self._links = links

    @property
    def embedded(self):
        """Gets the embedded of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501


        :return: The embedded of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
        :rtype: list[WebApiHalEmbeddedResource]
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this Assetic3IntegrationRepresentationsResourceGroupCraft.


        :param embedded: The embedded of this Assetic3IntegrationRepresentationsResourceGroupCraft.  # noqa: E501
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
        if not isinstance(other, Assetic3IntegrationRepresentationsResourceGroupCraft):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
