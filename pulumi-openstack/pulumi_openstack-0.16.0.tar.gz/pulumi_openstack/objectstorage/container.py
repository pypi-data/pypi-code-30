# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Container(pulumi.CustomResource):
    """
    Manages a V1 container resource within OpenStack.
    """
    def __init__(__self__, __name__, __opts__=None, container_read=None, container_sync_key=None, container_sync_to=None, container_write=None, content_type=None, force_destroy=None, metadata=None, name=None, region=None):
        """Create a Container resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if container_read and not isinstance(container_read, basestring):
            raise TypeError('Expected property container_read to be a basestring')
        __self__.container_read = container_read
        """
        Sets an access control list (ACL) that grants
        read access. This header can contain a comma-delimited list of users that
        can read the container (allows the GET method for all objects in the
        container). Changing this updates the access control list read access.
        """
        __props__['containerRead'] = container_read

        if container_sync_key and not isinstance(container_sync_key, basestring):
            raise TypeError('Expected property container_sync_key to be a basestring')
        __self__.container_sync_key = container_sync_key
        """
        The secret key for container synchronization.
        Changing this updates container synchronization.
        """
        __props__['containerSyncKey'] = container_sync_key

        if container_sync_to and not isinstance(container_sync_to, basestring):
            raise TypeError('Expected property container_sync_to to be a basestring')
        __self__.container_sync_to = container_sync_to
        """
        The destination for container synchronization.
        Changing this updates container synchronization.
        """
        __props__['containerSyncTo'] = container_sync_to

        if container_write and not isinstance(container_write, basestring):
            raise TypeError('Expected property container_write to be a basestring')
        __self__.container_write = container_write
        """
        Sets an ACL that grants write access.
        Changing this updates the access control list write access.
        """
        __props__['containerWrite'] = container_write

        if content_type and not isinstance(content_type, basestring):
            raise TypeError('Expected property content_type to be a basestring')
        __self__.content_type = content_type
        """
        The MIME type for the container. Changing this
        updates the MIME type.
        """
        __props__['contentType'] = content_type

        if force_destroy and not isinstance(force_destroy, bool):
            raise TypeError('Expected property force_destroy to be a bool')
        __self__.force_destroy = force_destroy
        """
        A boolean that indicates all objects should be deleted from the container so that the container can be destroyed without error. These objects are not recoverable.
        """
        __props__['forceDestroy'] = force_destroy

        if metadata and not isinstance(metadata, dict):
            raise TypeError('Expected property metadata to be a dict')
        __self__.metadata = metadata
        """
        Custom key/value pairs to associate with the container.
        Changing this updates the existing container metadata.
        """
        __props__['metadata'] = metadata

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        A unique name for the container. Changing this creates a
        new container.
        """
        __props__['name'] = name

        if region and not isinstance(region, basestring):
            raise TypeError('Expected property region to be a basestring')
        __self__.region = region
        """
        The region in which to create the container. If
        omitted, the `region` argument of the provider is used. Changing this
        creates a new container.
        """
        __props__['region'] = region

        super(Container, __self__).__init__(
            'openstack:objectstorage/container:Container',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'containerRead' in outs:
            self.container_read = outs['containerRead']
        if 'containerSyncKey' in outs:
            self.container_sync_key = outs['containerSyncKey']
        if 'containerSyncTo' in outs:
            self.container_sync_to = outs['containerSyncTo']
        if 'containerWrite' in outs:
            self.container_write = outs['containerWrite']
        if 'contentType' in outs:
            self.content_type = outs['contentType']
        if 'forceDestroy' in outs:
            self.force_destroy = outs['forceDestroy']
        if 'metadata' in outs:
            self.metadata = outs['metadata']
        if 'name' in outs:
            self.name = outs['name']
        if 'region' in outs:
            self.region = outs['region']
