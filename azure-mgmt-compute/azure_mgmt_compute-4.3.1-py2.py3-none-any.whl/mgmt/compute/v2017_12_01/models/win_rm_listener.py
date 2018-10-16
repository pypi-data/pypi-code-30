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


class WinRMListener(Model):
    """Describes Protocol and thumbprint of Windows Remote Management listener.

    :param protocol: Specifies the protocol of listener. <br><br> Possible
     values are: <br>**http** <br><br> **https**. Possible values include:
     'Http', 'Https'
    :type protocol: str or
     ~azure.mgmt.compute.v2017_12_01.models.ProtocolTypes
    :param certificate_url: This is the URL of a certificate that has been
     uploaded to Key Vault as a secret. For adding a secret to the Key Vault,
     see [Add a key or secret to the key
     vault](https://docs.microsoft.com/azure/key-vault/key-vault-get-started/#add).
     In this case, your certificate needs to be It is the Base64 encoding of
     the following JSON Object which is encoded in UTF-8: <br><br> {<br>
     "data":"<Base64-encoded-certificate>",<br>  "dataType":"pfx",<br>
     "password":"<pfx-file-password>"<br>}
    :type certificate_url: str
    """

    _attribute_map = {
        'protocol': {'key': 'protocol', 'type': 'ProtocolTypes'},
        'certificate_url': {'key': 'certificateUrl', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WinRMListener, self).__init__(**kwargs)
        self.protocol = kwargs.get('protocol', None)
        self.certificate_url = kwargs.get('certificate_url', None)
