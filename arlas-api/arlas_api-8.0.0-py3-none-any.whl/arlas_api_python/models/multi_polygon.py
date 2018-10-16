# coding: utf-8

"""
    ARLAS Exploration API

    Explore the content of ARLAS collections

    OpenAPI spec version: 8.0.0
    Contact: contact@gisaia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MultiPolygon(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'crs': 'Crs',
        'bbox': 'list[float]',
        'coordinates': 'list[list[list[LngLatAlt]]]'
    }

    attribute_map = {
        'crs': 'crs',
        'bbox': 'bbox',
        'coordinates': 'coordinates'
    }

    def __init__(self, crs=None, bbox=None, coordinates=None):
        """
        MultiPolygon - a model defined in Swagger
        """

        self._crs = None
        self._bbox = None
        self._coordinates = None

        if crs is not None:
          self.crs = crs
        if bbox is not None:
          self.bbox = bbox
        if coordinates is not None:
          self.coordinates = coordinates

    @property
    def crs(self):
        """
        Gets the crs of this MultiPolygon.

        :return: The crs of this MultiPolygon.
        :rtype: Crs
        """
        return self._crs

    @crs.setter
    def crs(self, crs):
        """
        Sets the crs of this MultiPolygon.

        :param crs: The crs of this MultiPolygon.
        :type: Crs
        """

        self._crs = crs

    @property
    def bbox(self):
        """
        Gets the bbox of this MultiPolygon.

        :return: The bbox of this MultiPolygon.
        :rtype: list[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """
        Sets the bbox of this MultiPolygon.

        :param bbox: The bbox of this MultiPolygon.
        :type: list[float]
        """

        self._bbox = bbox

    @property
    def coordinates(self):
        """
        Gets the coordinates of this MultiPolygon.

        :return: The coordinates of this MultiPolygon.
        :rtype: list[list[list[LngLatAlt]]]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this MultiPolygon.

        :param coordinates: The coordinates of this MultiPolygon.
        :type: list[list[list[LngLatAlt]]]
        """

        self._coordinates = coordinates

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, MultiPolygon):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
