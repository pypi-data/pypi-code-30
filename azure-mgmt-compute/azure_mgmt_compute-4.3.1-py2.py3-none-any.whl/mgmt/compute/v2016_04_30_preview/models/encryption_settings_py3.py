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


class EncryptionSettings(Model):
    """Encryption settings for disk or snapshot.

    :param enabled: Set this flag to true and provide DiskEncryptionKey and
     optional KeyEncryptionKey to enable encryption. Set this flag to false and
     remove DiskEncryptionKey and KeyEncryptionKey to disable encryption. If
     EncryptionSettings is null in the request object, the existing settings
     remain unchanged.
    :type enabled: bool
    :param disk_encryption_key: Key Vault Secret Url and vault id of the disk
     encryption key
    :type disk_encryption_key:
     ~azure.mgmt.compute.v2016_04_30_preview.models.KeyVaultAndSecretReference
    :param key_encryption_key: Key Vault Key Url and vault id of the key
     encryption key
    :type key_encryption_key:
     ~azure.mgmt.compute.v2016_04_30_preview.models.KeyVaultAndKeyReference
    """

    _attribute_map = {
        'enabled': {'key': 'enabled', 'type': 'bool'},
        'disk_encryption_key': {'key': 'diskEncryptionKey', 'type': 'KeyVaultAndSecretReference'},
        'key_encryption_key': {'key': 'keyEncryptionKey', 'type': 'KeyVaultAndKeyReference'},
    }

    def __init__(self, *, enabled: bool=None, disk_encryption_key=None, key_encryption_key=None, **kwargs) -> None:
        super(EncryptionSettings, self).__init__(**kwargs)
        self.enabled = enabled
        self.disk_encryption_key = disk_encryption_key
        self.key_encryption_key = key_encryption_key
