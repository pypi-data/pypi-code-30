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


class ServerUpdateParameters(Model):
    """Parameters allowd to update for a server.

    :param sku: The SKU (pricing tier) of the server.
    :type sku: ~azure.mgmt.rdbms.postgresql.models.Sku
    :param storage_profile: Storage profile of a server.
    :type storage_profile: ~azure.mgmt.rdbms.postgresql.models.StorageProfile
    :param administrator_login_password: The password of the administrator
     login.
    :type administrator_login_password: str
    :param version: The version of a server. Possible values include: '9.5',
     '9.6', '10', '10.0', '10.2'
    :type version: str or ~azure.mgmt.rdbms.postgresql.models.ServerVersion
    :param ssl_enforcement: Enable ssl enforcement or not when connect to
     server. Possible values include: 'Enabled', 'Disabled'
    :type ssl_enforcement: str or
     ~azure.mgmt.rdbms.postgresql.models.SslEnforcementEnum
    :param tags: Application-specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'sku': {'key': 'sku', 'type': 'Sku'},
        'storage_profile': {'key': 'properties.storageProfile', 'type': 'StorageProfile'},
        'administrator_login_password': {'key': 'properties.administratorLoginPassword', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'ssl_enforcement': {'key': 'properties.sslEnforcement', 'type': 'SslEnforcementEnum'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, sku=None, storage_profile=None, administrator_login_password: str=None, version=None, ssl_enforcement=None, tags=None, **kwargs) -> None:
        super(ServerUpdateParameters, self).__init__(**kwargs)
        self.sku = sku
        self.storage_profile = storage_profile
        self.administrator_login_password = administrator_login_password
        self.version = version
        self.ssl_enforcement = ssl_enforcement
        self.tags = tags
