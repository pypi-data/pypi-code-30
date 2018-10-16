# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Policy(pulumi.CustomResource):
    """
    Provides an IoT policy.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, policy=None):
        """Create a Policy resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the policy.
        """
        __props__['name'] = name

        if not policy:
            raise TypeError('Missing required property policy')
        elif not isinstance(policy, basestring):
            raise TypeError('Expected property policy to be a basestring')
        __self__.policy = policy
        """
        The policy document. This is a JSON formatted string.
        The heredoc syntax or `file` function is helpful here. Use the [IoT Developer Guide]
        (http://docs.aws.amazon.com/iot/latest/developerguide/iot-policies.html) for more information on IoT Policies
        """
        __props__['policy'] = policy

        __self__.arn = pulumi.runtime.UNKNOWN
        """
        The ARN assigned by AWS to this policy.
        """
        __self__.default_version_id = pulumi.runtime.UNKNOWN
        """
        The default version of this policy.
        """

        super(Policy, __self__).__init__(
            'aws:iot/policy:Policy',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'arn' in outs:
            self.arn = outs['arn']
        if 'defaultVersionId' in outs:
            self.default_version_id = outs['defaultVersionId']
        if 'name' in outs:
            self.name = outs['name']
        if 'policy' in outs:
            self.policy = outs['policy']
