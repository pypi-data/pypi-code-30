# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class TagCategory(pulumi.CustomResource):
    """
    The `vsphere_tag_category` resource can be used to create and manage tag
    categories, which determine how tags are grouped together and applied to
    specific objects.
    
    For more information about tags, click [here][ext-tags-general]. For more
    information about tag categories specifically, click
    [here][ext-tag-categories].
    
    [ext-tags-general]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html
    [ext-tag-categories]: https://docs.vmware.com/en/VMware-vSphere/6.5/com.vmware.vsphere.vcenterhost.doc/GUID-BA3D1794-28F2-43F3-BCE9-3964CB207FB6.html
    
    ~> **NOTE:** Tagging support is unsupported on direct ESXi connections and
    requires vCenter 6.0 or higher.
    """
    def __init__(__self__, __name__, __opts__=None, associable_types=None, cardinality=None, description=None, name=None):
        """Create a TagCategory resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not associable_types:
            raise TypeError('Missing required property associable_types')
        elif not isinstance(associable_types, list):
            raise TypeError('Expected property associable_types to be a list')
        __self__.associable_types = associable_types
        """
        A list object types that this category is
        valid to be assigned to. For a full list, click
        here.
        """
        __props__['associableTypes'] = associable_types

        if not cardinality:
            raise TypeError('Missing required property cardinality')
        elif not isinstance(cardinality, basestring):
            raise TypeError('Expected property cardinality to be a basestring')
        __self__.cardinality = cardinality
        """
        The number of tags that can be assigned from this
        category to a single object at once. Can be one of `SINGLE` (object can only
        be assigned one tag in this category), to `MULTIPLE` (object can be assigned
        multiple tags in this category). Forces a new resource if changed.
        """
        __props__['cardinality'] = cardinality

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        A description for the category.
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the category.
        """
        __props__['name'] = name

        super(TagCategory, __self__).__init__(
            'vsphere:index/tagCategory:TagCategory',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'associableTypes' in outs:
            self.associable_types = outs['associableTypes']
        if 'cardinality' in outs:
            self.cardinality = outs['cardinality']
        if 'description' in outs:
            self.description = outs['description']
        if 'name' in outs:
            self.name = outs['name']
