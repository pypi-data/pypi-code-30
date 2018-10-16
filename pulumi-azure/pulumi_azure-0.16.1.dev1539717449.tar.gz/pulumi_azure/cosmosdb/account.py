# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Account(pulumi.CustomResource):
    """
    Manages a CosmosDB (formally DocumentDB) Account.
    """
    def __init__(__self__, __name__, __opts__=None, capabilities=None, consistency_policy=None, enable_automatic_failover=None, failover_policies=None, geo_locations=None, ip_range_filter=None, is_virtual_network_filter_enabled=None, kind=None, location=None, name=None, offer_type=None, resource_group_name=None, tags=None, virtual_network_rules=None):
        """Create a Account resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if capabilities and not isinstance(capabilities, list):
            raise TypeError('Expected property capabilities to be a list')
        __self__.capabilities = capabilities
        """
        Enable capabilities for this Cosmos DB account. Possible values are `EnableTable` and `EnableGremlin`.
        """
        __props__['capabilities'] = capabilities

        if not consistency_policy:
            raise TypeError('Missing required property consistency_policy')
        elif not isinstance(consistency_policy, dict):
            raise TypeError('Expected property consistency_policy to be a dict')
        __self__.consistency_policy = consistency_policy
        """
        Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.
        """
        __props__['consistencyPolicy'] = consistency_policy

        if enable_automatic_failover and not isinstance(enable_automatic_failover, bool):
            raise TypeError('Expected property enable_automatic_failover to be a bool')
        __self__.enable_automatic_failover = enable_automatic_failover
        """
        Enable automatic fail over for this Cosmos DB account.
        """
        __props__['enableAutomaticFailover'] = enable_automatic_failover

        if failover_policies and not isinstance(failover_policies, list):
            raise TypeError('Expected property failover_policies to be a list')
        __self__.failover_policies = failover_policies
        __props__['failoverPolicies'] = failover_policies

        if geo_locations and not isinstance(geo_locations, list):
            raise TypeError('Expected property geo_locations to be a list')
        __self__.geo_locations = geo_locations
        """
        Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.
        """
        __props__['geoLocations'] = geo_locations

        if ip_range_filter and not isinstance(ip_range_filter, basestring):
            raise TypeError('Expected property ip_range_filter to be a basestring')
        __self__.ip_range_filter = ip_range_filter
        """
        CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.
        """
        __props__['ipRangeFilter'] = ip_range_filter

        if is_virtual_network_filter_enabled and not isinstance(is_virtual_network_filter_enabled, bool):
            raise TypeError('Expected property is_virtual_network_filter_enabled to be a bool')
        __self__.is_virtual_network_filter_enabled = is_virtual_network_filter_enabled
        __props__['isVirtualNetworkFilterEnabled'] = is_virtual_network_filter_enabled

        if kind and not isinstance(kind, basestring):
            raise TypeError('Expected property kind to be a basestring')
        __self__.kind = kind
        """
        Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.
        """
        __props__['kind'] = kind

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        The name of the Azure region to host replicated data.
        """
        __props__['location'] = location

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.
        """
        __props__['name'] = name

        if not offer_type:
            raise TypeError('Missing required property offer_type')
        elif not isinstance(offer_type, basestring):
            raise TypeError('Expected property offer_type to be a basestring')
        __self__.offer_type = offer_type
        """
        Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.
        """
        __props__['offerType'] = offer_type

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.
        """
        __props__['resourceGroupName'] = resource_group_name

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if virtual_network_rules and not isinstance(virtual_network_rules, list):
            raise TypeError('Expected property virtual_network_rules to be a list')
        __self__.virtual_network_rules = virtual_network_rules
        __props__['virtualNetworkRules'] = virtual_network_rules

        __self__.connection_strings = pulumi.runtime.UNKNOWN
        """
        A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.
        """
        __self__.endpoint = pulumi.runtime.UNKNOWN
        """
        The endpoint used to connect to the CosmosDB account.
        """
        __self__.primary_master_key = pulumi.runtime.UNKNOWN
        """
        The Primary master key for the CosmosDB Account.
        """
        __self__.primary_readonly_master_key = pulumi.runtime.UNKNOWN
        """
        The Primary read-only master Key for the CosmosDB Account.
        """
        __self__.read_endpoints = pulumi.runtime.UNKNOWN
        """
        A list of read endpoints available for this CosmosDB account.
        """
        __self__.secondary_master_key = pulumi.runtime.UNKNOWN
        """
        The Secondary master key for the CosmosDB Account.
        """
        __self__.secondary_readonly_master_key = pulumi.runtime.UNKNOWN
        """
        The Secondary read-only master key for the CosmosDB Account.
        """
        __self__.write_endpoints = pulumi.runtime.UNKNOWN
        """
        A list of write endpoints available for this CosmosDB account.
        """

        super(Account, __self__).__init__(
            'azure:cosmosdb/account:Account',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'capabilities' in outs:
            self.capabilities = outs['capabilities']
        if 'connectionStrings' in outs:
            self.connection_strings = outs['connectionStrings']
        if 'consistencyPolicy' in outs:
            self.consistency_policy = outs['consistencyPolicy']
        if 'enableAutomaticFailover' in outs:
            self.enable_automatic_failover = outs['enableAutomaticFailover']
        if 'endpoint' in outs:
            self.endpoint = outs['endpoint']
        if 'failoverPolicies' in outs:
            self.failover_policies = outs['failoverPolicies']
        if 'geoLocations' in outs:
            self.geo_locations = outs['geoLocations']
        if 'ipRangeFilter' in outs:
            self.ip_range_filter = outs['ipRangeFilter']
        if 'isVirtualNetworkFilterEnabled' in outs:
            self.is_virtual_network_filter_enabled = outs['isVirtualNetworkFilterEnabled']
        if 'kind' in outs:
            self.kind = outs['kind']
        if 'location' in outs:
            self.location = outs['location']
        if 'name' in outs:
            self.name = outs['name']
        if 'offerType' in outs:
            self.offer_type = outs['offerType']
        if 'primaryMasterKey' in outs:
            self.primary_master_key = outs['primaryMasterKey']
        if 'primaryReadonlyMasterKey' in outs:
            self.primary_readonly_master_key = outs['primaryReadonlyMasterKey']
        if 'readEndpoints' in outs:
            self.read_endpoints = outs['readEndpoints']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'secondaryMasterKey' in outs:
            self.secondary_master_key = outs['secondaryMasterKey']
        if 'secondaryReadonlyMasterKey' in outs:
            self.secondary_readonly_master_key = outs['secondaryReadonlyMasterKey']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'virtualNetworkRules' in outs:
            self.virtual_network_rules = outs['virtualNetworkRules']
        if 'writeEndpoints' in outs:
            self.write_endpoints = outs['writeEndpoints']
