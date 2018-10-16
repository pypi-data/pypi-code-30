# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AccountMeterAccountMeterRequestDTO(Model):
    """AccountMeterAccountMeterRequestDTO.

    :param account_id: The account identifier for this account meter <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Topmost (Account)</span>
    :type account_id: int
    :param meter_id: The meter identifier for this account meter <span
     class='property-internal'>Required</span> <span
     class='property-internal'>Topmost (Meter)</span>
    :type meter_id: int
    :param begin_date: The beginning date and time for this account meter
     relationship
     Defaults to 1899-01-01
    :type begin_date: datetime
    :param end_date: The ending date and time for this account meter
     relationship
     Defaults to 3000-01-01
    :type end_date: datetime
    :param general_ledger_id: The identifier for the general ledger assigned
     to this account meter
    :type general_ledger_id: int
    :param vendor_type_id: The identifier for the vendor type. Vendors may
     assume different types on different account meters
    :type vendor_type_id: int
    :param deregulated: Indicates if the account meter is deregulated
    :type deregulated: bool
    :param template_id: Indicates if the account meter template <span
     class='property-internal'>Required</span>
    :type template_id: int
    :param rate_id: Indicates if the account meter rate <span
     class='property-internal'>Required</span>
    :type rate_id: int
    """

    _validation = {
        'account_id': {'required': True},
        'meter_id': {'required': True},
        'template_id': {'required': True},
        'rate_id': {'required': True},
    }

    _attribute_map = {
        'account_id': {'key': 'accountId', 'type': 'int'},
        'meter_id': {'key': 'meterId', 'type': 'int'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
        'general_ledger_id': {'key': 'generalLedgerId', 'type': 'int'},
        'vendor_type_id': {'key': 'vendorTypeId', 'type': 'int'},
        'deregulated': {'key': 'deregulated', 'type': 'bool'},
        'template_id': {'key': 'templateId', 'type': 'int'},
        'rate_id': {'key': 'rateId', 'type': 'int'},
    }

    def __init__(self, account_id, meter_id, template_id, rate_id, begin_date=None, end_date=None, general_ledger_id=None, vendor_type_id=None, deregulated=None):
        super(AccountMeterAccountMeterRequestDTO, self).__init__()
        self.account_id = account_id
        self.meter_id = meter_id
        self.begin_date = begin_date
        self.end_date = end_date
        self.general_ledger_id = general_ledger_id
        self.vendor_type_id = vendor_type_id
        self.deregulated = deregulated
        self.template_id = template_id
        self.rate_id = rate_id
