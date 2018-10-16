# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EmbedOptions(object):
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
        'enable_dev_features': 'bool',
        'enable_newsletters_index': 'bool',
        'enable_subscription_management': 'bool',
        'locale': 'str',
        'media_url': 'str'
    }

    attribute_map = {
        'enable_dev_features': 'enable_dev_features',
        'enable_newsletters_index': 'enable_newsletters_index',
        'enable_subscription_management': 'enable_subscription_management',
        'locale': 'locale',
        'media_url': 'media_url'
    }

    def __init__(self, enable_dev_features=None, enable_newsletters_index=None, enable_subscription_management=None, locale=None, media_url=None):  # noqa: E501
        """EmbedOptions - a model defined in Swagger"""  # noqa: E501

        self._enable_dev_features = None
        self._enable_newsletters_index = None
        self._enable_subscription_management = None
        self._locale = None
        self._media_url = None
        self.discriminator = None

        if enable_dev_features is not None:
            self.enable_dev_features = enable_dev_features
        if enable_newsletters_index is not None:
            self.enable_newsletters_index = enable_newsletters_index
        if enable_subscription_management is not None:
            self.enable_subscription_management = enable_subscription_management
        if locale is not None:
            self.locale = locale
        if media_url is not None:
            self.media_url = media_url

    @property
    def enable_dev_features(self):
        """Gets the enable_dev_features of this EmbedOptions.  # noqa: E501


        :return: The enable_dev_features of this EmbedOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dev_features

    @enable_dev_features.setter
    def enable_dev_features(self, enable_dev_features):
        """Sets the enable_dev_features of this EmbedOptions.


        :param enable_dev_features: The enable_dev_features of this EmbedOptions.  # noqa: E501
        :type: bool
        """

        self._enable_dev_features = enable_dev_features

    @property
    def enable_newsletters_index(self):
        """Gets the enable_newsletters_index of this EmbedOptions.  # noqa: E501


        :return: The enable_newsletters_index of this EmbedOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enable_newsletters_index

    @enable_newsletters_index.setter
    def enable_newsletters_index(self, enable_newsletters_index):
        """Sets the enable_newsletters_index of this EmbedOptions.


        :param enable_newsletters_index: The enable_newsletters_index of this EmbedOptions.  # noqa: E501
        :type: bool
        """

        self._enable_newsletters_index = enable_newsletters_index

    @property
    def enable_subscription_management(self):
        """Gets the enable_subscription_management of this EmbedOptions.  # noqa: E501


        :return: The enable_subscription_management of this EmbedOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enable_subscription_management

    @enable_subscription_management.setter
    def enable_subscription_management(self, enable_subscription_management):
        """Sets the enable_subscription_management of this EmbedOptions.


        :param enable_subscription_management: The enable_subscription_management of this EmbedOptions.  # noqa: E501
        :type: bool
        """

        self._enable_subscription_management = enable_subscription_management

    @property
    def locale(self):
        """Gets the locale of this EmbedOptions.  # noqa: E501


        :return: The locale of this EmbedOptions.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this EmbedOptions.


        :param locale: The locale of this EmbedOptions.  # noqa: E501
        :type: str
        """
        allowed_values = ["en_US", "nb_NO", "sv_SE"]  # noqa: E501
        if locale not in allowed_values:
            raise ValueError(
                "Invalid value for `locale` ({0}), must be one of {1}"  # noqa: E501
                .format(locale, allowed_values)
            )

        self._locale = locale

    @property
    def media_url(self):
        """Gets the media_url of this EmbedOptions.  # noqa: E501


        :return: The media_url of this EmbedOptions.  # noqa: E501
        :rtype: str
        """
        return self._media_url

    @media_url.setter
    def media_url(self, media_url):
        """Sets the media_url of this EmbedOptions.


        :param media_url: The media_url of this EmbedOptions.  # noqa: E501
        :type: str
        """

        self._media_url = media_url

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
        if not isinstance(other, EmbedOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
