# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Model(pulumi.CustomResource):
    """
    Provides a Model for a API Gateway.
    """
    def __init__(__self__, __name__, __opts__=None, content_type=None, description=None, name=None, rest_api=None, schema=None):
        """Create a Model resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not content_type:
            raise TypeError('Missing required property content_type')
        elif not isinstance(content_type, basestring):
            raise TypeError('Expected property content_type to be a basestring')
        __self__.content_type = content_type
        """
        The content type of the model
        """
        __props__['contentType'] = content_type

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the model
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the model
        """
        __props__['name'] = name

        if not rest_api:
            raise TypeError('Missing required property rest_api')
        elif not isinstance(rest_api, basestring):
            raise TypeError('Expected property rest_api to be a basestring')
        __self__.rest_api = rest_api
        """
        The ID of the associated REST API
        """
        __props__['restApi'] = rest_api

        if schema and not isinstance(schema, basestring):
            raise TypeError('Expected property schema to be a basestring')
        __self__.schema = schema
        """
        The schema of the model in a JSON form
        """
        __props__['schema'] = schema

        super(Model, __self__).__init__(
            'aws:apigateway/model:Model',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'contentType' in outs:
            self.content_type = outs['contentType']
        if 'description' in outs:
            self.description = outs['description']
        if 'name' in outs:
            self.name = outs['name']
        if 'restApi' in outs:
            self.rest_api = outs['restApi']
        if 'schema' in outs:
            self.schema = outs['schema']
