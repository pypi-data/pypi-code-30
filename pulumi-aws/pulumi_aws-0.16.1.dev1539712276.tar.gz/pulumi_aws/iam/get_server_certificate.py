# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetServerCertificateResult(object):
    """
    A collection of values returned by getServerCertificate.
    """
    def __init__(__self__, arn=None, certificate_body=None, certificate_chain=None, expiration_date=None, name=None, path=None, upload_date=None, id=None):
        if arn and not isinstance(arn, basestring):
            raise TypeError('Expected argument arn to be a basestring')
        __self__.arn = arn
        if certificate_body and not isinstance(certificate_body, basestring):
            raise TypeError('Expected argument certificate_body to be a basestring')
        __self__.certificate_body = certificate_body
        if certificate_chain and not isinstance(certificate_chain, basestring):
            raise TypeError('Expected argument certificate_chain to be a basestring')
        __self__.certificate_chain = certificate_chain
        if expiration_date and not isinstance(expiration_date, basestring):
            raise TypeError('Expected argument expiration_date to be a basestring')
        __self__.expiration_date = expiration_date
        if name and not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        if path and not isinstance(path, basestring):
            raise TypeError('Expected argument path to be a basestring')
        __self__.path = path
        if upload_date and not isinstance(upload_date, basestring):
            raise TypeError('Expected argument upload_date to be a basestring')
        __self__.upload_date = upload_date
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_server_certificate(latest=None, name=None, name_prefix=None, path_prefix=None):
    """
    Use this data source to lookup information about IAM Server Certificates.
    """
    __args__ = dict()

    __args__['latest'] = latest
    __args__['name'] = name
    __args__['namePrefix'] = name_prefix
    __args__['pathPrefix'] = path_prefix
    __ret__ = pulumi.runtime.invoke('aws:iam/getServerCertificate:getServerCertificate', __args__)

    return GetServerCertificateResult(
        arn=__ret__.get('arn'),
        certificate_body=__ret__.get('certificateBody'),
        certificate_chain=__ret__.get('certificateChain'),
        expiration_date=__ret__.get('expirationDate'),
        name=__ret__.get('name'),
        path=__ret__.get('path'),
        upload_date=__ret__.get('uploadDate'),
        id=__ret__.get('id'))
