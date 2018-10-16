# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RateRateVersionCreateDTO(Model):
    """RateRateVersionCreateDTO.

    :param begin_date:  <span class='property-internal'>Required</span>
    :type begin_date: datetime
    :param note:  <span class='property-internal'>Must be between 0 and 255
     characters</span>
    :type note: str
    :param bill_calculations:
    :type bill_calculations: list[~energycap.sdk.models.RateInputRequestDTO]
    :param meter_details:
    :type meter_details: list[~energycap.sdk.models.RateInputRequestDTO]
    :param rate_properties:
    :type rate_properties: list[~energycap.sdk.models.RateInputRequestDTO]
    :param meter_properties:
    :type meter_properties: list[~energycap.sdk.models.RateInputRequestDTO]
    :param account_properties:
    :type account_properties: list[~energycap.sdk.models.RateInputRequestDTO]
    """

    _validation = {
        'begin_date': {'required': True},
        'note': {'max_length': 255, 'min_length': 0},
    }

    _attribute_map = {
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'note': {'key': 'note', 'type': 'str'},
        'bill_calculations': {'key': 'billCalculations', 'type': '[RateInputRequestDTO]'},
        'meter_details': {'key': 'meterDetails', 'type': '[RateInputRequestDTO]'},
        'rate_properties': {'key': 'rateProperties', 'type': '[RateInputRequestDTO]'},
        'meter_properties': {'key': 'meterProperties', 'type': '[RateInputRequestDTO]'},
        'account_properties': {'key': 'accountProperties', 'type': '[RateInputRequestDTO]'},
    }

    def __init__(self, begin_date, note=None, bill_calculations=None, meter_details=None, rate_properties=None, meter_properties=None, account_properties=None):
        super(RateRateVersionCreateDTO, self).__init__()
        self.begin_date = begin_date
        self.note = note
        self.bill_calculations = bill_calculations
        self.meter_details = meter_details
        self.rate_properties = rate_properties
        self.meter_properties = meter_properties
        self.account_properties = account_properties
