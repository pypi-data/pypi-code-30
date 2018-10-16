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

from .server_properties_for_create_py3 import ServerPropertiesForCreate


class ServerPropertiesForGeoRestore(ServerPropertiesForCreate):
    """The properties used to create a new server by restoring to a different
    region from a geo replicated backup.

    All required parameters must be populated in order to send to Azure.

    :param version: Server version. Possible values include: '5.6', '5.7'
    :type version: str or ~azure.mgmt.rdbms.mariadb.models.ServerVersion
    :param ssl_enforcement: Enable ssl enforcement or not when connect to
     server. Possible values include: 'Enabled', 'Disabled'
    :type ssl_enforcement: str or
     ~azure.mgmt.rdbms.mariadb.models.SslEnforcementEnum
    :param storage_profile: Storage profile of a server.
    :type storage_profile: ~azure.mgmt.rdbms.mariadb.models.StorageProfile
    :param create_mode: Required. Constant filled by server.
    :type create_mode: str
    :param source_server_id: Required. The source server id to restore from.
    :type source_server_id: str
    """

    _validation = {
        'create_mode': {'required': True},
        'source_server_id': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'ssl_enforcement': {'key': 'sslEnforcement', 'type': 'SslEnforcementEnum'},
        'storage_profile': {'key': 'storageProfile', 'type': 'StorageProfile'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
        'source_server_id': {'key': 'sourceServerId', 'type': 'str'},
    }

    def __init__(self, *, source_server_id: str, version=None, ssl_enforcement=None, storage_profile=None, **kwargs) -> None:
        super(ServerPropertiesForGeoRestore, self).__init__(version=version, ssl_enforcement=ssl_enforcement, storage_profile=storage_profile, **kwargs)
        self.source_server_id = source_server_id
        self.create_mode = 'GeoRestore'
