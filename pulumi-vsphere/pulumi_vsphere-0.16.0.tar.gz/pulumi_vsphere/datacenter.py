# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class Datacenter(pulumi.CustomResource):
    """
    Provides a VMware vSphere datacenter resource. This can be used as the primary
    container of inventory objects such as hosts and virtual machines.
    """
    def __init__(__self__, __name__, __opts__=None, custom_attributes=None, folder=None, name=None, tags=None):
        """Create a Datacenter resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if custom_attributes and not isinstance(custom_attributes, dict):
            raise TypeError('Expected property custom_attributes to be a dict')
        __self__.custom_attributes = custom_attributes
        """
        Map of custom attribute ids to value 
        strings to set for datacenter resource. See
        [here][docs-setting-custom-attributes] for a reference on how to set values
        for custom attributes.
        """
        __props__['customAttributes'] = custom_attributes

        if folder and not isinstance(folder, basestring):
            raise TypeError('Expected property folder to be a basestring')
        __self__.folder = folder
        """
        The folder where the datacenter should be created.
        Forces a new resource if changed.
        """
        __props__['folder'] = folder

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the datacenter. This name needs to be unique
        within the folder. Forces a new resource if changed.
        """
        __props__['name'] = name

        if tags and not isinstance(tags, list):
            raise TypeError('Expected property tags to be a list')
        __self__.tags = tags
        """
        The IDs of any tags to attach to this resource. See
        [here][docs-applying-tags] for a reference on how to apply tags.
        """
        __props__['tags'] = tags

        __self__.moid = pulumi.runtime.UNKNOWN
        """
        [Managed object ID][docs-about-morefs] of this datacenter.
        """

        super(Datacenter, __self__).__init__(
            'vsphere:index/datacenter:Datacenter',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'customAttributes' in outs:
            self.custom_attributes = outs['customAttributes']
        if 'folder' in outs:
            self.folder = outs['folder']
        if 'moid' in outs:
            self.moid = outs['moid']
        if 'name' in outs:
            self.name = outs['name']
        if 'tags' in outs:
            self.tags = outs['tags']
