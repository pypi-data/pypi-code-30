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


class StreamingPath(Model):
    """Class of paths for streaming.

    All required parameters must be populated in order to send to Azure.

    :param streaming_protocol: Required. Streaming protocol. Possible values
     include: 'Hls', 'Dash', 'SmoothStreaming', 'Download'
    :type streaming_protocol: str or
     ~azure.mgmt.media.models.StreamingPolicyStreamingProtocol
    :param encryption_scheme: Required. Encryption scheme. Possible values
     include: 'NoEncryption', 'EnvelopeEncryption', 'CommonEncryptionCenc',
     'CommonEncryptionCbcs'
    :type encryption_scheme: str or ~azure.mgmt.media.models.EncryptionScheme
    :param paths: Streaming paths for each protocol and encryptionScheme pair
    :type paths: list[str]
    """

    _validation = {
        'streaming_protocol': {'required': True},
        'encryption_scheme': {'required': True},
    }

    _attribute_map = {
        'streaming_protocol': {'key': 'streamingProtocol', 'type': 'StreamingPolicyStreamingProtocol'},
        'encryption_scheme': {'key': 'encryptionScheme', 'type': 'EncryptionScheme'},
        'paths': {'key': 'paths', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(StreamingPath, self).__init__(**kwargs)
        self.streaming_protocol = kwargs.get('streaming_protocol', None)
        self.encryption_scheme = kwargs.get('encryption_scheme', None)
        self.paths = kwargs.get('paths', None)
