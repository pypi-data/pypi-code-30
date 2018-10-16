# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CustomersCustomerResponseDTO(Model):
    """CustomersCustomerResponseDTO.

    :param customer_id: The customer identifier
    :type customer_id: int
    :param customer_code: The customer code
    :type customer_code: str
    :param customer_info: The customer info
    :type customer_info: str
    :param address: The address of the customer
    :type address: ~energycap.sdk.models.AccountsAddressChildDTO
    """

    _attribute_map = {
        'customer_id': {'key': 'customerId', 'type': 'int'},
        'customer_code': {'key': 'customerCode', 'type': 'str'},
        'customer_info': {'key': 'customerInfo', 'type': 'str'},
        'address': {'key': 'address', 'type': 'AccountsAddressChildDTO'},
    }

    def __init__(self, customer_id=None, customer_code=None, customer_info=None, address=None):
        super(CustomersCustomerResponseDTO, self).__init__()
        self.customer_id = customer_id
        self.customer_code = customer_code
        self.customer_info = customer_info
        self.address = address
