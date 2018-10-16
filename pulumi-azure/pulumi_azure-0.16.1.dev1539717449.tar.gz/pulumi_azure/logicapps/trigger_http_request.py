# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class TriggerHttpRequest(pulumi.CustomResource):
    """
    Manages a HTTP Request Trigger within a Logic App Workflow
    """
    def __init__(__self__, __name__, __opts__=None, logic_app_id=None, method=None, name=None, relative_path=None, schema=None):
        """Create a TriggerHttpRequest resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not logic_app_id:
            raise TypeError('Missing required property logic_app_id')
        elif not isinstance(logic_app_id, basestring):
            raise TypeError('Expected property logic_app_id to be a basestring')
        __self__.logic_app_id = logic_app_id
        """
        Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.
        """
        __props__['logicAppId'] = logic_app_id

        if method and not isinstance(method, basestring):
            raise TypeError('Expected property method to be a basestring')
        __self__.method = method
        """
        Specifies the HTTP Method which the request be using. Possible values include `DELETE`, `GET`, `PATCH`, `POST` or `PUT`.
        """
        __props__['method'] = method

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if relative_path and not isinstance(relative_path, basestring):
            raise TypeError('Expected property relative_path to be a basestring')
        __self__.relative_path = relative_path
        """
        Specifies the Relative Path used for this Request.
        """
        __props__['relativePath'] = relative_path

        if not schema:
            raise TypeError('Missing required property schema')
        elif not isinstance(schema, basestring):
            raise TypeError('Expected property schema to be a basestring')
        __self__.schema = schema
        """
        A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.
        """
        __props__['schema'] = schema

        super(TriggerHttpRequest, __self__).__init__(
            'azure:logicapps/triggerHttpRequest:TriggerHttpRequest',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'logicAppId' in outs:
            self.logic_app_id = outs['logicAppId']
        if 'method' in outs:
            self.method = outs['method']
        if 'name' in outs:
            self.name = outs['name']
        if 'relativePath' in outs:
            self.relative_path = outs['relativePath']
        if 'schema' in outs:
            self.schema = outs['schema']
