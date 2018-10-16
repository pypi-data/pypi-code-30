# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineScaleSetOSDisk(Model):
    """Describes a virtual machine scale set operating system disk.

    All required parameters must be populated in order to send to Azure.

    :param name: The disk name.
    :type name: str
    :param caching: Specifies the caching requirements. <br><br> Possible
     values are: <br><br> **None** <br><br> **ReadOnly** <br><br> **ReadWrite**
     <br><br> Default: **None for Standard storage. ReadOnly for Premium
     storage**. Possible values include: 'None', 'ReadOnly', 'ReadWrite'
    :type caching: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.CachingTypes
    :param create_option: Required. Specifies how the virtual machines in the
     scale set should be created.<br><br> The only allowed value is:
     **FromImage** \\u2013 This value is used when you are using an image to
     create the virtual machine. If you are using a platform image, you also
     use the imageReference element described above. If you are using a
     marketplace image, you  also use the plan element previously described.
     Possible values include: 'FromImage', 'Empty', 'Attach'
    :type create_option: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.DiskCreateOptionTypes
    :param os_type: This property allows you to specify the type of the OS
     that is included in the disk if creating a VM from user-image or a
     specialized VHD. <br><br> Possible values are: <br><br> **Windows**
     <br><br> **Linux**. Possible values include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2016_04_30_preview.models.OperatingSystemTypes
    :param image: The Source User Image VirtualHardDisk. This VirtualHardDisk
     will be copied before using it to attach to the Virtual Machine. If
     SourceImage is provided, the destination VirtualHardDisk should not exist.
    :type image:
     ~azure.mgmt.compute.v2016_04_30_preview.models.VirtualHardDisk
    :param vhd_containers: The list of virtual hard disk container uris.
    :type vhd_containers: list[str]
    :param managed_disk: The managed disk parameters.
    :type managed_disk:
     ~azure.mgmt.compute.v2016_04_30_preview.models.VirtualMachineScaleSetManagedDiskParameters
    """

    _validation = {
        'create_option': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'create_option': {'key': 'createOption', 'type': 'DiskCreateOptionTypes'},
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'image': {'key': 'image', 'type': 'VirtualHardDisk'},
        'vhd_containers': {'key': 'vhdContainers', 'type': '[str]'},
        'managed_disk': {'key': 'managedDisk', 'type': 'VirtualMachineScaleSetManagedDiskParameters'},
    }

    def __init__(self, **kwargs):
        super(VirtualMachineScaleSetOSDisk, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.caching = kwargs.get('caching', None)
        self.create_option = kwargs.get('create_option', None)
        self.os_type = kwargs.get('os_type', None)
        self.image = kwargs.get('image', None)
        self.vhd_containers = kwargs.get('vhd_containers', None)
        self.managed_disk = kwargs.get('managed_disk', None)
