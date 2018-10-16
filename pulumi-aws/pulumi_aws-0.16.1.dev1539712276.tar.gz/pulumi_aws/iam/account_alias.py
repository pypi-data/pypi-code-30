# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class AccountAlias(pulumi.CustomResource):
    """
    -> **Note:** There is only a single account alias per AWS account.
    
    Manages the account alias for the AWS Account.
    """
    def __init__(__self__, __name__, __opts__=None, account_alias=None):
        """Create a AccountAlias resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not account_alias:
            raise TypeError('Missing required property account_alias')
        elif not isinstance(account_alias, basestring):
            raise TypeError('Expected property account_alias to be a basestring')
        __self__.account_alias = account_alias
        """
        The account alias
        """
        __props__['accountAlias'] = account_alias

        super(AccountAlias, __self__).__init__(
            'aws:iam/accountAlias:AccountAlias',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'accountAlias' in outs:
            self.account_alias = outs['accountAlias']
