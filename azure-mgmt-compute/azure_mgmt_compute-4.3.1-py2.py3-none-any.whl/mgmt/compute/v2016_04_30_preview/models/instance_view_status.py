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


class InstanceViewStatus(Model):
    """Instance view status.

    :param code: The status code.
    :type code: str
    :param level: The level code. Possible values include: 'Info', 'Warning',
     'Error'
    :type level: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.StatusLevelTypes
    :param display_status: The short localizable label for the status.
    :type display_status: str
    :param message: The detailed status message, including for alerts and
     error messages.
    :type message: str
    :param time: The time of the status.
    :type time: datetime
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'level': {'key': 'level', 'type': 'StatusLevelTypes'},
        'display_status': {'key': 'displayStatus', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'time': {'key': 'time', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs):
        super(InstanceViewStatus, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.level = kwargs.get('level', None)
        self.display_status = kwargs.get('display_status', None)
        self.message = kwargs.get('message', None)
        self.time = kwargs.get('time', None)
