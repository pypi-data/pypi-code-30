# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BillsBillHeaderChildDTO(Model):
    """BillsBillHeaderChildDTO.

    :param value:
    :type value: str
    :param required:
    :type required: bool
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': 'str'},
        'required': {'key': 'required', 'type': 'bool'},
    }

    def __init__(self, value=None, required=None):
        super(BillsBillHeaderChildDTO, self).__init__()
        self.value = value
        self.required = required
