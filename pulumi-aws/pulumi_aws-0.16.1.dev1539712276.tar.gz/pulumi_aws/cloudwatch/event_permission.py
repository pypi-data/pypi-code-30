# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class EventPermission(pulumi.CustomResource):
    """
    Provides a resource to create a CloudWatch Events permission to support cross-account events in the current account default event bus.
    """
    def __init__(__self__, __name__, __opts__=None, action=None, principal=None, statement_id=None):
        """Create a EventPermission resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if action and not isinstance(action, basestring):
            raise TypeError('Expected property action to be a basestring')
        __self__.action = action
        """
        The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.
        """
        __props__['action'] = action

        if not principal:
            raise TypeError('Missing required property principal')
        elif not isinstance(principal, basestring):
            raise TypeError('Expected property principal to be a basestring')
        __self__.principal = principal
        """
        The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus.
        """
        __props__['principal'] = principal

        if not statement_id:
            raise TypeError('Missing required property statement_id')
        elif not isinstance(statement_id, basestring):
            raise TypeError('Expected property statement_id to be a basestring')
        __self__.statement_id = statement_id
        """
        An identifier string for the external account that you are granting permissions to.
        """
        __props__['statementId'] = statement_id

        super(EventPermission, __self__).__init__(
            'aws:cloudwatch/eventPermission:EventPermission',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'action' in outs:
            self.action = outs['action']
        if 'principal' in outs:
            self.principal = outs['principal']
        if 'statementId' in outs:
            self.statement_id = outs['statementId']
