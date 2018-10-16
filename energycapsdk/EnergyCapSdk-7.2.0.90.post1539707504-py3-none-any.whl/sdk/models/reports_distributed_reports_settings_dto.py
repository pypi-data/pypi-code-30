# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReportsDistributedReportsSettingsDTO(Model):
    """ReportsDistributedReportsSettingsDTO.

    :param format:
    :type format: str
    :param use_copy:
    :type use_copy: bool
    :param filters:
    :type filters: list[~energycap.sdk.models.CommonFilterEditDTO]
    :param clear_filters:
    :type clear_filters: bool
    :param save_filters:
    :type save_filters: bool
    :param only_send_if_data:
    :type only_send_if_data: bool
    :param distribution:
    :type distribution: ~energycap.sdk.models.EmailEmailPropertiesDTO
    """

    _attribute_map = {
        'format': {'key': 'format', 'type': 'str'},
        'use_copy': {'key': 'useCopy', 'type': 'bool'},
        'filters': {'key': 'filters', 'type': '[CommonFilterEditDTO]'},
        'clear_filters': {'key': 'clearFilters', 'type': 'bool'},
        'save_filters': {'key': 'saveFilters', 'type': 'bool'},
        'only_send_if_data': {'key': 'onlySendIfData', 'type': 'bool'},
        'distribution': {'key': 'distribution', 'type': 'EmailEmailPropertiesDTO'},
    }

    def __init__(self, format=None, use_copy=None, filters=None, clear_filters=None, save_filters=None, only_send_if_data=None, distribution=None):
        super(ReportsDistributedReportsSettingsDTO, self).__init__()
        self.format = format
        self.use_copy = use_copy
        self.filters = filters
        self.clear_filters = clear_filters
        self.save_filters = save_filters
        self.only_send_if_data = only_send_if_data
        self.distribution = distribution
