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


class ContainerExec(Model):
    """The container execution command, for liveness or readiness probe.

    :param command: The commands to execute within the container.
    :type command: list[str]
    """

    _attribute_map = {
        'command': {'key': 'command', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(ContainerExec, self).__init__(**kwargs)
        self.command = kwargs.get('command', None)
