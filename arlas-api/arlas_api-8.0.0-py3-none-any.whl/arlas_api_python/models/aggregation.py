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


class Aggregation(object):
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
        'type': 'str',
        'field': 'str',
        'interval': 'Interval',
        'format': 'str',
        'metrics': 'list[Metric]',
        'order': 'str',
        'on': 'str',
        'size': 'str',
        'include': 'str',
        'fetch_geometry': 'AggregatedGeometry'
    }

    attribute_map = {
        'type': 'type',
        'field': 'field',
        'interval': 'interval',
        'format': 'format',
        'metrics': 'metrics',
        'order': 'order',
        'on': 'on',
        'size': 'size',
        'include': 'include',
        'fetch_geometry': 'fetchGeometry'
    }

    def __init__(self, type=None, field=None, interval=None, format=None, metrics=None, order=None, on=None, size=None, include=None, fetch_geometry=None):
        """
        Aggregation - a model defined in Swagger
        """

        self._type = None
        self._field = None
        self._interval = None
        self._format = None
        self._metrics = None
        self._order = None
        self._on = None
        self._size = None
        self._include = None
        self._fetch_geometry = None

        if type is not None:
          self.type = type
        if field is not None:
          self.field = field
        if interval is not None:
          self.interval = interval
        if format is not None:
          self.format = format
        if metrics is not None:
          self.metrics = metrics
        if order is not None:
          self.order = order
        if on is not None:
          self.on = on
        if size is not None:
          self.size = size
        if include is not None:
          self.include = include
        if fetch_geometry is not None:
          self.fetch_geometry = fetch_geometry

    @property
    def type(self):
        """
        Gets the type of this Aggregation.

        :return: The type of this Aggregation.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Aggregation.

        :param type: The type of this Aggregation.
        :type: str
        """
        allowed_values = ["datehistogram", "geohash", "histogram", "term"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def field(self):
        """
        Gets the field of this Aggregation.

        :return: The field of this Aggregation.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        """
        Sets the field of this Aggregation.

        :param field: The field of this Aggregation.
        :type: str
        """

        self._field = field

    @property
    def interval(self):
        """
        Gets the interval of this Aggregation.

        :return: The interval of this Aggregation.
        :rtype: Interval
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """
        Sets the interval of this Aggregation.

        :param interval: The interval of this Aggregation.
        :type: Interval
        """

        self._interval = interval

    @property
    def format(self):
        """
        Gets the format of this Aggregation.

        :return: The format of this Aggregation.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this Aggregation.

        :param format: The format of this Aggregation.
        :type: str
        """

        self._format = format

    @property
    def metrics(self):
        """
        Gets the metrics of this Aggregation.

        :return: The metrics of this Aggregation.
        :rtype: list[Metric]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """
        Sets the metrics of this Aggregation.

        :param metrics: The metrics of this Aggregation.
        :type: list[Metric]
        """

        self._metrics = metrics

    @property
    def order(self):
        """
        Gets the order of this Aggregation.

        :return: The order of this Aggregation.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this Aggregation.

        :param order: The order of this Aggregation.
        :type: str
        """
        allowed_values = ["asc", "desc"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

    @property
    def on(self):
        """
        Gets the on of this Aggregation.

        :return: The on of this Aggregation.
        :rtype: str
        """
        return self._on

    @on.setter
    def on(self, on):
        """
        Sets the on of this Aggregation.

        :param on: The on of this Aggregation.
        :type: str
        """
        allowed_values = ["field", "count", "result"]
        if on not in allowed_values:
            raise ValueError(
                "Invalid value for `on` ({0}), must be one of {1}"
                .format(on, allowed_values)
            )

        self._on = on

    @property
    def size(self):
        """
        Gets the size of this Aggregation.

        :return: The size of this Aggregation.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Aggregation.

        :param size: The size of this Aggregation.
        :type: str
        """

        self._size = size

    @property
    def include(self):
        """
        Gets the include of this Aggregation.

        :return: The include of this Aggregation.
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        """
        Sets the include of this Aggregation.

        :param include: The include of this Aggregation.
        :type: str
        """

        self._include = include

    @property
    def fetch_geometry(self):
        """
        Gets the fetch_geometry of this Aggregation.

        :return: The fetch_geometry of this Aggregation.
        :rtype: AggregatedGeometry
        """
        return self._fetch_geometry

    @fetch_geometry.setter
    def fetch_geometry(self, fetch_geometry):
        """
        Sets the fetch_geometry of this Aggregation.

        :param fetch_geometry: The fetch_geometry of this Aggregation.
        :type: AggregatedGeometry
        """

        self._fetch_geometry = fetch_geometry

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
        if not isinstance(other, Aggregation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
