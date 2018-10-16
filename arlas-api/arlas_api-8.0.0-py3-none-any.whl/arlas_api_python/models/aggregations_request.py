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


class AggregationsRequest(object):
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
        'filter': 'Filter',
        'form': 'Form',
        'aggregations': 'list[Aggregation]'
    }

    attribute_map = {
        'filter': 'filter',
        'form': 'form',
        'aggregations': 'aggregations'
    }

    def __init__(self, filter=None, form=None, aggregations=None):
        """
        AggregationsRequest - a model defined in Swagger
        """

        self._filter = None
        self._form = None
        self._aggregations = None

        if filter is not None:
          self.filter = filter
        if form is not None:
          self.form = form
        if aggregations is not None:
          self.aggregations = aggregations

    @property
    def filter(self):
        """
        Gets the filter of this AggregationsRequest.

        :return: The filter of this AggregationsRequest.
        :rtype: Filter
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """
        Sets the filter of this AggregationsRequest.

        :param filter: The filter of this AggregationsRequest.
        :type: Filter
        """

        self._filter = filter

    @property
    def form(self):
        """
        Gets the form of this AggregationsRequest.

        :return: The form of this AggregationsRequest.
        :rtype: Form
        """
        return self._form

    @form.setter
    def form(self, form):
        """
        Sets the form of this AggregationsRequest.

        :param form: The form of this AggregationsRequest.
        :type: Form
        """

        self._form = form

    @property
    def aggregations(self):
        """
        Gets the aggregations of this AggregationsRequest.

        :return: The aggregations of this AggregationsRequest.
        :rtype: list[Aggregation]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """
        Sets the aggregations of this AggregationsRequest.

        :param aggregations: The aggregations of this AggregationsRequest.
        :type: list[Aggregation]
        """

        self._aggregations = aggregations

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
        if not isinstance(other, AggregationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
