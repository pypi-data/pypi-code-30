# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class TxtRecord(pulumi.CustomResource):
    """
    Enables you to manage DNS TXT Records within Azure DNS.
    """
    def __init__(__self__, __name__, __opts__=None, name=None, records=None, resource_group_name=None, tags=None, ttl=None, zone_name=None):
        """Create a TxtRecord resource with the given unique name, props, and options."""
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
        The name of the DNS TXT Record.
        """
        __props__['name'] = name

        if not records:
            raise TypeError('Missing required property records')
        elif not isinstance(records, list):
            raise TypeError('Expected property records to be a list')
        __self__.records = records
        """
        A list of values that make up the txt record. Each `record` block supports fields documented below.
        """
        __props__['records'] = records

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        Specifies the resource group where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if not ttl:
            raise TypeError('Missing required property ttl')
        elif not isinstance(ttl, int):
            raise TypeError('Expected property ttl to be a int')
        __self__.ttl = ttl
        """
        The Time To Live (TTL) of the DNS record.
        """
        __props__['ttl'] = ttl

        if not zone_name:
            raise TypeError('Missing required property zone_name')
        elif not isinstance(zone_name, basestring):
            raise TypeError('Expected property zone_name to be a basestring')
        __self__.zone_name = zone_name
        """
        Specifies the DNS Zone where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['zoneName'] = zone_name

        super(TxtRecord, __self__).__init__(
            'azure:dns/txtRecord:TxtRecord',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'name' in outs:
            self.name = outs['name']
        if 'records' in outs:
            self.records = outs['records']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'ttl' in outs:
            self.ttl = outs['ttl']
        if 'zoneName' in outs:
            self.zone_name = outs['zoneName']
