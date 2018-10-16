# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class AutoPoolSpecification(Model):
    """Specifies characteristics for a temporary 'auto pool'. The Batch service
    will create this auto pool when the job is submitted.

    :param auto_pool_id_prefix: A prefix to be added to the unique identifier
     when a pool is automatically created. The Batch service assigns each auto
     pool a unique identifier on creation. To distinguish between pools created
     for different purposes, you can specify this element to add a prefix to
     the ID that is assigned. The prefix can be up to 20 characters long.
    :type auto_pool_id_prefix: str
    :param pool_lifetime_option: The minimum lifetime of created auto pools,
     and how multiple jobs on a schedule are assigned to pools. When the pool
     lifetime is jobSchedule the pool exists for the lifetime of the job
     schedule. The Batch Service creates the pool when it creates the first job
     on the schedule. You may apply this option only to job schedules, not to
     jobs. When the pool lifetime is job the pool exists for the lifetime of
     the job to which it is dedicated. The Batch service creates the pool when
     it creates the job. If the 'job' option is applied to a job schedule, the
     Batch service creates a new auto pool for every job created on the
     schedule. Possible values include: 'jobSchedule', 'job'
    :type pool_lifetime_option: str or :class:`PoolLifetimeOption
     <azure.batch.models.PoolLifetimeOption>`
    :param keep_alive: Whether to keep an auto pool alive after its lifetime
     expires. If false, the Batch service deletes the pool once its lifetime
     (as determined by the poolLifetimeOption setting) expires; that is, when
     the job or job schedule completes. If true, the Batch service does not
     delete the pool automatically. It is up to the user to delete auto pools
     created with this option.
    :type keep_alive: bool
    :param pool: The pool specification for the auto pool.
    :type pool: :class:`PoolSpecification
     <azure.batch.models.PoolSpecification>`
    """

    _validation = {
        'pool_lifetime_option': {'required': True},
    }

    _attribute_map = {
        'auto_pool_id_prefix': {'key': 'autoPoolIdPrefix', 'type': 'str'},
        'pool_lifetime_option': {'key': 'poolLifetimeOption', 'type': 'PoolLifetimeOption'},
        'keep_alive': {'key': 'keepAlive', 'type': 'bool'},
        'pool': {'key': 'pool', 'type': 'ExtendedPoolSpecification'},
    }

    def __init__(self, **kwargs):
        super(AutoPoolSpecification, self).__init__(**kwargs)
        self.auto_pool_id_prefix = kwargs.get('auto_pool_id_prefix', None)
        self.pool_lifetime_option = kwargs.get('pool_lifetime_option', None)
        self.keep_alive = kwargs.get('keep_alive', None)
        self.pool = kwargs.get('pool', None)
