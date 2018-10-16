# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ApiError(Model):
    """Api error.

    :param details: The Api error details
    :type details: list[~azure.mgmt.compute.v2018_10_01.models.ApiErrorBase]
    :param innererror: The Api inner error
    :type innererror: ~azure.mgmt.compute.v2018_10_01.models.InnerError
    :param code: The error code.
    :type code: str
    :param target: The target of the particular error.
    :type target: str
    :param message: The error message.
    :type message: str
    """

    _attribute_map = {
        'details': {'key': 'details', 'type': '[ApiErrorBase]'},
        'innererror': {'key': 'innererror', 'type': 'InnerError'},
        'code': {'key': 'code', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, details=None, innererror=None, code: str=None, target: str=None, message: str=None, **kwargs) -> None:
        super(ApiError, self).__init__(**kwargs)
        self.details = details
        self.innererror = innererror
        self.code = code
        self.target = target
        self.message = message
