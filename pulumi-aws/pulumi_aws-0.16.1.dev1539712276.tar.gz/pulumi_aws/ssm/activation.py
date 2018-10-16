# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Activation(pulumi.CustomResource):
    """
    Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, expiration_date=None, iam_role=None, name=None, registration_limit=None):
        """Create a Activation resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        The description of the resource that you want to register.
        """
        __props__['description'] = description

        if expiration_date and not isinstance(expiration_date, basestring):
            raise TypeError('Expected property expiration_date to be a basestring')
        __self__.expiration_date = expiration_date
        """
        A timestamp in [RFC3339 format](https://tools.ietf.org/html/rfc3339#section-5.8) by which this activation request should expire. The default value is 24 hours from resource creation time.
        """
        __props__['expirationDate'] = expiration_date

        if not iam_role:
            raise TypeError('Missing required property iam_role')
        elif not isinstance(iam_role, basestring):
            raise TypeError('Expected property iam_role to be a basestring')
        __self__.iam_role = iam_role
        """
        The IAM Role to attach to the managed instance.
        """
        __props__['iamRole'] = iam_role

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The default name of the registered managed instance.
        """
        __props__['name'] = name

        if registration_limit and not isinstance(registration_limit, int):
            raise TypeError('Expected property registration_limit to be a int')
        __self__.registration_limit = registration_limit
        """
        The maximum number of managed instances you want to register. The default value is 1 instance.
        """
        __props__['registrationLimit'] = registration_limit

        __self__.activation_code = pulumi.runtime.UNKNOWN
        """
        The code the system generates when it processes the activation.
        """
        __self__.expired = pulumi.runtime.UNKNOWN
        """
        If the current activation has expired.
        """
        __self__.registration_count = pulumi.runtime.UNKNOWN
        """
        The number of managed instances that are currently registered using this activation.
        """

        super(Activation, __self__).__init__(
            'aws:ssm/activation:Activation',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'activationCode' in outs:
            self.activation_code = outs['activationCode']
        if 'description' in outs:
            self.description = outs['description']
        if 'expirationDate' in outs:
            self.expiration_date = outs['expirationDate']
        if 'expired' in outs:
            self.expired = outs['expired']
        if 'iamRole' in outs:
            self.iam_role = outs['iamRole']
        if 'name' in outs:
            self.name = outs['name']
        if 'registrationCount' in outs:
            self.registration_count = outs['registrationCount']
        if 'registrationLimit' in outs:
            self.registration_limit = outs['registrationLimit']
