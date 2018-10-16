# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class QueueAuthorizationRule(pulumi.CustomResource):
    """
    Manages an Authorization Rule for a ServiceBus Queue.
    """
    def __init__(__self__, __name__, __opts__=None, listen=None, manage=None, name=None, namespace_name=None, queue_name=None, resource_group_name=None, send=None):
        """Create a QueueAuthorizationRule resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if listen and not isinstance(listen, bool):
            raise TypeError('Expected property listen to be a bool')
        __self__.listen = listen
        """
        Does this Authorization Rule have Listen permissions to the ServiceBus Queue? Defaults to `false`.
        """
        __props__['listen'] = listen

        if manage and not isinstance(manage, bool):
            raise TypeError('Expected property manage to be a bool')
        __self__.manage = manage
        """
        Does this Authorization Rule have Manage permissions to the ServiceBus Queue? When this property is `true` - both `listen` and `send` must be too. Defaults to `false`.
        """
        __props__['manage'] = manage

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the Authorization Rule. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not namespace_name:
            raise TypeError('Missing required property namespace_name')
        elif not isinstance(namespace_name, basestring):
            raise TypeError('Expected property namespace_name to be a basestring')
        __self__.namespace_name = namespace_name
        """
        Specifies the name of the ServiceBus Namespace in which the Queue exists. Changing this forces a new resource to be created.
        """
        __props__['namespaceName'] = namespace_name

        if not queue_name:
            raise TypeError('Missing required property queue_name')
        elif not isinstance(queue_name, basestring):
            raise TypeError('Expected property queue_name to be a basestring')
        __self__.queue_name = queue_name
        """
        Specifies the name of the ServiceBus Queue. Changing this forces a new resource to be created.
        """
        __props__['queueName'] = queue_name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the Resource Group in which the ServiceBus Namespace exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if send and not isinstance(send, bool):
            raise TypeError('Expected property send to be a bool')
        __self__.send = send
        """
        Does this Authorization Rule have Send permissions to the ServiceBus Queue? Defaults to `false`.
        """
        __props__['send'] = send

        __self__.primary_connection_string = pulumi.runtime.UNKNOWN
        """
        The Primary Connection String for the Authorization Rule.
        """
        __self__.primary_key = pulumi.runtime.UNKNOWN
        """
        The Primary Key for the Authorization Rule.
        """
        __self__.secondary_connection_string = pulumi.runtime.UNKNOWN
        """
        The Secondary Connection String for the Authorization Rule.
        """
        __self__.secondary_key = pulumi.runtime.UNKNOWN
        """
        The Secondary Key for the Authorization Rule.
        """

        super(QueueAuthorizationRule, __self__).__init__(
            'azure:servicebus/queueAuthorizationRule:QueueAuthorizationRule',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'listen' in outs:
            self.listen = outs['listen']
        if 'manage' in outs:
            self.manage = outs['manage']
        if 'name' in outs:
            self.name = outs['name']
        if 'namespaceName' in outs:
            self.namespace_name = outs['namespaceName']
        if 'primaryConnectionString' in outs:
            self.primary_connection_string = outs['primaryConnectionString']
        if 'primaryKey' in outs:
            self.primary_key = outs['primaryKey']
        if 'queueName' in outs:
            self.queue_name = outs['queueName']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'secondaryConnectionString' in outs:
            self.secondary_connection_string = outs['secondaryConnectionString']
        if 'secondaryKey' in outs:
            self.secondary_key = outs['secondaryKey']
        if 'send' in outs:
            self.send = outs['send']
