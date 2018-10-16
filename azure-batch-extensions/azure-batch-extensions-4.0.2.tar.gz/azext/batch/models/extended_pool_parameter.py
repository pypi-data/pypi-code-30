# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=redefined-builtin

from azure.batch.models import PoolAddParameter


class ExtendedPoolParameter(PoolAddParameter):
    """A pool in the Azure Batch service to add.

    :param id: A string that uniquely identifies the pool within the account.
     The ID can contain any combination of alphanumeric characters including
     hyphens and underscores, and cannot contain more than 64 characters. The
     ID is case-preserving and case-insensitive (that is, you may not have two
     pool IDs within an account that differ only by case).
    :type id: str
    :param display_name: The display name for the pool. The display name need
     not be unique and can contain any Unicode characters up to a maximum
     length of 1024.
    :type display_name: str
    :param vm_size: The size of virtual machines in the pool. All virtual
     machines in a pool are the same size. For information about available
     sizes of virtual machines for Cloud Services pools (pools created with
     cloudServiceConfiguration), see Sizes for Cloud Services
     (http://azure.microsoft.com/documentation/articles/cloud-services-sizes-specs/).
     Batch supports all Cloud Services VM sizes except ExtraSmall, A1V2 and
     A2V2. For information about available VM sizes for pools using images from
     the Virtual Machines Marketplace (pools created with
     virtualMachineConfiguration) see Sizes for Virtual Machines (Linux)
     (https://azure.microsoft.com/documentation/articles/virtual-machines-linux-sizes/)
     or Sizes for Virtual Machines (Windows)
     (https://azure.microsoft.com/documentation/articles/virtual-machines-windows-sizes/).
     Batch supports all Azure VM sizes except STANDARD_A0 and those with
     premium storage (STANDARD_GS, STANDARD_DS, and STANDARD_DSV2 series).
    :type vm_size: str
    :param cloud_service_configuration: The cloud service configuration for
     the pool. This property and virtualMachineConfiguration are mutually
     exclusive and one of the properties must be specified. This property
     cannot be specified if the Batch account was created with its
     poolAllocationMode property set to 'UserSubscription'.
    :type cloud_service_configuration: :class:`CloudServiceConfiguration
     <azure.batch.models.CloudServiceConfiguration>`
    :param virtual_machine_configuration: The virtual machine configuration
     for the pool. This property and cloudServiceConfiguration are mutually
     exclusive and one of the properties must be specified.
    :type virtual_machine_configuration: :class:`VirtualMachineConfiguration
     <azure.batch.models.VirtualMachineConfiguration>`
    :param resize_timeout: The timeout for allocation of compute nodes to the
     pool. This timeout applies only to manual scaling; it has no effect when
     enableAutoScale is set to true. The default value is 15 minutes. The
     minimum value is 5 minutes. If you specify a value less than 5 minutes,
     the Batch service returns an error; if you are calling the REST API
     directly, the HTTP status code is 400 (Bad Request).
    :type resize_timeout: timedelta
    :param target_dedicated_nodes: The desired number of dedicated compute
     nodes in the pool. This property must not be specified if enableAutoScale
     is set to true. If enableAutoScale is set to false, then you must set
     either targetDedicatedNodes, targetLowPriorityNodes, or both.
    :type target_dedicated_nodes: int
    :param target_low_priority_nodes: The desired number of low-priority
     compute nodes in the pool. This property must not be specified if
     enableAutoScale is set to true. If enableAutoScale is set to false, then
     you must set either targetDedicatedNodes, targetLowPriorityNodes, or both.
    :type target_low_priority_nodes: int
    :param enable_auto_scale: Whether the pool size should automatically
     adjust over time. If false, at least one of targetDedicateNodes and
     targetLowPriorityNodes must be specified. If true, the autoScaleFormula
     property is required and the pool automatically resizes according to the
     formula. The default value is false.
    :type enable_auto_scale: bool
    :param auto_scale_formula: A formula for the desired number of compute
     nodes in the pool. This property must not be specified if enableAutoScale
     is set to false. It is required if enableAutoScale is set to true. The
     formula is checked for validity before the pool is created. If the formula
     is not valid, the Batch service rejects the request with detailed error
     information. For more information about specifying this formula, see
     'Automatically scale compute nodes in an Azure Batch pool'
     (https://azure.microsoft.com/documentation/articles/batch-automatic-scaling/).
    :type auto_scale_formula: str
    :param auto_scale_evaluation_interval: The time interval at which to
     automatically adjust the pool size according to the autoscale formula. The
     default value is 15 minutes. The minimum and maximum value are 5 minutes
     and 168 hours respectively. If you specify a value less than 5 minutes or
     greater than 168 hours, the Batch service returns an error; if you are
     calling the REST API directly, the HTTP status code is 400 (Bad Request).
    :type auto_scale_evaluation_interval: timedelta
    :param enable_inter_node_communication: Whether the pool permits direct
     communication between nodes. Enabling inter-node communication limits the
     maximum size of the pool due to deployment restrictions on the nodes of
     the pool. This may result in the pool not reaching its desired size. The
     default value is false.
    :type enable_inter_node_communication: bool
    :param network_configuration: The network configuration for the pool.
    :type network_configuration: :class:`NetworkConfiguration
     <azure.batch.models.NetworkConfiguration>`
    :param start_task: A task specified to run on each compute node as it
     joins the pool. The task runs when the node is added to the pool or when
     the node is restarted.
    :type start_task: :class:`StartTask <azure.batch.models.StartTask>`
    :param certificate_references: The list of certificates to be installed on
     each compute node in the pool. For Windows compute nodes, the Batch
     service installs the certificates to the specified certificate store and
     location. For Linux compute nodes, the certificates are stored in a
     directory inside the task working directory and an environment variable
     AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this
     location. For certificates with visibility of 'remoteUser', a 'certs'
     directory is created in the user's home directory (e.g.,
     /home/{user-name}/certs) and certificates are placed in that directory.
    :type certificate_references: list of :class:`CertificateReference
     <azure.batch.models.CertificateReference>`
    :param application_package_references: The list of application packages to
     be installed on each compute node in the pool.
    :type application_package_references: list of
     :class:`ApplicationPackageReference
     <azure.batch.models.ApplicationPackageReference>`
    :param application_licenses: The list of application licenses the Batch
     service will make available on each compute node in the pool. The list of
     application licenses must be a subset of available Batch service
     application licenses. If a license is requested which is not supported,
     pool creation will fail.
    :type application_licenses: list of str
    :param max_tasks_per_node: The maximum number of tasks that can run
     concurrently on a single compute node in the pool. The default value is 1.
     The maximum value of this setting depends on the size of the compute nodes
     in the pool (the vmSize setting).
    :type max_tasks_per_node: int
    :param task_scheduling_policy: How tasks are distributed across compute
     nodes in a pool.
    :type task_scheduling_policy: :class:`TaskSchedulingPolicy
     <azure.batch.models.TaskSchedulingPolicy>`
    :param user_accounts: The list of user accounts to be created on each node
     in the pool.
    :type user_accounts: list of :class:`UserAccount
     <azure.batch.models.UserAccount>`
    :param metadata: A list of name-value pairs associated with the pool as
     metadata. The Batch service does not assign any meaning to metadata; it is
     solely for the use of user code.
    :type metadata: list of :class:`MetadataItem
     <azure.batch.models.MetadataItem>`
    :param package_references: A list of packages to be installed on the compute
     nodes. Must be of a Package Manager type in accordance with the selected
     operating system.
    :type package_references: list of :class:`PackageReferenceBase
     <azext.batch.models.PackageReferenceBase>`
    """

    _validation = {
        'id': {'required': True},
        'vm_size': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'vm_size': {'key': 'vmSize', 'type': 'str'},
        'cloud_service_configuration': {'key': 'cloudServiceConfiguration',
                                        'type': 'CloudServiceConfiguration'},
        'virtual_machine_configuration': {'key': 'virtualMachineConfiguration',
                                          'type': 'VirtualMachineConfiguration'},
        'resize_timeout': {'key': 'resizeTimeout', 'type': 'duration'},
        'target_dedicated_nodes': {'key': 'targetDedicatedNodes', 'type': 'int'},
        'target_low_priority_nodes': {'key': 'targetLowPriorityNodes', 'type': 'int'},
        'enable_auto_scale': {'key': 'enableAutoScale', 'type': 'bool'},
        'auto_scale_formula': {'key': 'autoScaleFormula', 'type': 'str'},
        'auto_scale_evaluation_interval': {'key': 'autoScaleEvaluationInterval', 'type': 'duration'},
        'enable_inter_node_communication': {'key': 'enableInterNodeCommunication', 'type': 'bool'},
        'network_configuration': {'key': 'networkConfiguration', 'type': 'NetworkConfiguration'},
        'start_task': {'key': 'startTask', 'type': 'StartTask'},
        'certificate_references': {'key': 'certificateReferences', 'type': '[CertificateReference]'},
        'application_package_references': {'key': 'applicationPackageReferences',
                                           'type': '[ApplicationPackageReference]'},
        'application_licenses': {'key': 'applicationLicenses', 'type': '[str]'},
        'max_tasks_per_node': {'key': 'maxTasksPerNode', 'type': 'int'},
        'task_scheduling_policy': {'key': 'taskSchedulingPolicy', 'type': 'TaskSchedulingPolicy'},
        'user_accounts': {'key': 'userAccounts', 'type': '[UserAccount]'},
        'metadata': {'key': 'metadata', 'type': '[MetadataItem]'},
        'package_references': {'key': 'packageReferences', 'type': '[PackageReferenceBase]'}
    }

    def __init__(self, **kwargs):
        super(ExtendedPoolParameter, self).__init__(**kwargs)
        self.package_references = kwargs.get('package_references', None)
