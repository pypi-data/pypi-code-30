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


class SshConfiguration(Model):
    """SSH configuration for Linux based VMs running on Azure.

    :param public_keys: The list of SSH public keys used to authenticate with
     linux based VMs.
    :type public_keys:
     list[~azure.mgmt.compute.v2017_12_01.models.SshPublicKey]
    """

    _attribute_map = {
        'public_keys': {'key': 'publicKeys', 'type': '[SshPublicKey]'},
    }

    def __init__(self, **kwargs):
        super(SshConfiguration, self).__init__(**kwargs)
        self.public_keys = kwargs.get('public_keys', None)
