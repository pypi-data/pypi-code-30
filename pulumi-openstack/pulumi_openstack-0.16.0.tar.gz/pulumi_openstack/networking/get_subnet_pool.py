# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class GetSubnetPoolResult(object):
    """
    A collection of values returned by getSubnetPool.
    """
    def __init__(__self__, address_scope_id=None, created_at=None, default_prefixlen=None, default_quota=None, description=None, ip_version=None, is_default=None, max_prefixlen=None, min_prefixlen=None, name=None, prefixes=None, project_id=None, region=None, revision_number=None, shared=None, updated_at=None, id=None):
        if address_scope_id and not isinstance(address_scope_id, basestring):
            raise TypeError('Expected argument address_scope_id to be a basestring')
        __self__.address_scope_id = address_scope_id
        """
        See Argument Reference above.
        * `ip_version` -The IP protocol version.
        """
        if created_at and not isinstance(created_at, basestring):
            raise TypeError('Expected argument created_at to be a basestring')
        __self__.created_at = created_at
        """
        The time at which subnetpool was created.
        """
        if default_prefixlen and not isinstance(default_prefixlen, int):
            raise TypeError('Expected argument default_prefixlen to be a int')
        __self__.default_prefixlen = default_prefixlen
        """
        See Argument Reference above.
        """
        if default_quota and not isinstance(default_quota, int):
            raise TypeError('Expected argument default_quota to be a int')
        __self__.default_quota = default_quota
        """
        See Argument Reference above.
        """
        if description and not isinstance(description, basestring):
            raise TypeError('Expected argument description to be a basestring')
        __self__.description = description
        """
        See Argument Reference above.
        """
        if ip_version and not isinstance(ip_version, int):
            raise TypeError('Expected argument ip_version to be a int')
        __self__.ip_version = ip_version
        if is_default and not isinstance(is_default, bool):
            raise TypeError('Expected argument is_default to be a bool')
        __self__.is_default = is_default
        """
        See Argument Reference above.
        """
        if max_prefixlen and not isinstance(max_prefixlen, int):
            raise TypeError('Expected argument max_prefixlen to be a int')
        __self__.max_prefixlen = max_prefixlen
        """
        See Argument Reference above.
        """
        if min_prefixlen and not isinstance(min_prefixlen, int):
            raise TypeError('Expected argument min_prefixlen to be a int')
        __self__.min_prefixlen = min_prefixlen
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, basestring):
            raise TypeError('Expected argument name to be a basestring')
        __self__.name = name
        """
        See Argument Reference above.
        """
        if prefixes and not isinstance(prefixes, list):
            raise TypeError('Expected argument prefixes to be a list')
        __self__.prefixes = prefixes
        """
        See Argument Reference above.
        """
        if project_id and not isinstance(project_id, basestring):
            raise TypeError('Expected argument project_id to be a basestring')
        __self__.project_id = project_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, basestring):
            raise TypeError('Expected argument region to be a basestring')
        __self__.region = region
        """
        See Argument Reference above.
        """
        if revision_number and not isinstance(revision_number, int):
            raise TypeError('Expected argument revision_number to be a int')
        __self__.revision_number = revision_number
        """
        The revision number of the subnetpool.
        """
        if shared and not isinstance(shared, bool):
            raise TypeError('Expected argument shared to be a bool')
        __self__.shared = shared
        """
        See Argument Reference above.
        """
        if updated_at and not isinstance(updated_at, basestring):
            raise TypeError('Expected argument updated_at to be a basestring')
        __self__.updated_at = updated_at
        """
        The time at which subnetpool was created.
        """
        if id and not isinstance(id, basestring):
            raise TypeError('Expected argument id to be a basestring')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

def get_subnet_pool(address_scope_id=None, default_prefixlen=None, default_quota=None, description=None, ip_version=None, is_default=None, max_prefixlen=None, min_prefixlen=None, name=None, project_id=None, region=None, shared=None):
    """
    Use this data source to get the ID of an available OpenStack subnetpool.
    """
    __args__ = dict()

    __args__['addressScopeId'] = address_scope_id
    __args__['defaultPrefixlen'] = default_prefixlen
    __args__['defaultQuota'] = default_quota
    __args__['description'] = description
    __args__['ipVersion'] = ip_version
    __args__['isDefault'] = is_default
    __args__['maxPrefixlen'] = max_prefixlen
    __args__['minPrefixlen'] = min_prefixlen
    __args__['name'] = name
    __args__['projectId'] = project_id
    __args__['region'] = region
    __args__['shared'] = shared
    __ret__ = pulumi.runtime.invoke('openstack:networking/getSubnetPool:getSubnetPool', __args__)

    return GetSubnetPoolResult(
        address_scope_id=__ret__.get('addressScopeId'),
        created_at=__ret__.get('createdAt'),
        default_prefixlen=__ret__.get('defaultPrefixlen'),
        default_quota=__ret__.get('defaultQuota'),
        description=__ret__.get('description'),
        ip_version=__ret__.get('ipVersion'),
        is_default=__ret__.get('isDefault'),
        max_prefixlen=__ret__.get('maxPrefixlen'),
        min_prefixlen=__ret__.get('minPrefixlen'),
        name=__ret__.get('name'),
        prefixes=__ret__.get('prefixes'),
        project_id=__ret__.get('projectId'),
        region=__ret__.get('region'),
        revision_number=__ret__.get('revisionNumber'),
        shared=__ret__.get('shared'),
        updated_at=__ret__.get('updatedAt'),
        id=__ret__.get('id'))
