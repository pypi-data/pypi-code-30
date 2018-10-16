# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities

class Database(pulumi.CustomResource):
    """
    Allows you to manage an Azure SQL Database
    """
    def __init__(__self__, __name__, __opts__=None, collation=None, create_mode=None, edition=None, elastic_pool_name=None, import_=None, location=None, max_size_bytes=None, name=None, requested_service_objective_id=None, requested_service_objective_name=None, resource_group_name=None, restore_point_in_time=None, server_name=None, source_database_deletion_date=None, source_database_id=None, tags=None, threat_detection_policy=None):
        """Create a Database resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if collation and not isinstance(collation, basestring):
            raise TypeError('Expected property collation to be a basestring')
        __self__.collation = collation
        """
        The name of the collation. Applies only if `create_mode` is `Default`.  Azure default is `SQL_LATIN1_GENERAL_CP1_CI_AS`. Changing this forces a new resource to be created.
        """
        __props__['collation'] = collation

        if create_mode and not isinstance(create_mode, basestring):
            raise TypeError('Expected property create_mode to be a basestring')
        __self__.create_mode = create_mode
        """
        Specifies the type of database to create. Defaults to `Default`. See below for the accepted values/
        """
        __props__['createMode'] = create_mode

        if edition and not isinstance(edition, basestring):
            raise TypeError('Expected property edition to be a basestring')
        __self__.edition = edition
        """
        The edition of the database to be created. Applies only if `create_mode` is `Default`. Valid values are: `Basic`, `Standard`, `Premium`, or `DataWarehouse`. Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).
        """
        __props__['edition'] = edition

        if elastic_pool_name and not isinstance(elastic_pool_name, basestring):
            raise TypeError('Expected property elastic_pool_name to be a basestring')
        __self__.elastic_pool_name = elastic_pool_name
        """
        The name of the elastic database pool.
        """
        __props__['elasticPoolName'] = elastic_pool_name

        if import_ and not isinstance(import_, dict):
            raise TypeError('Expected property import_ to be a dict')
        __self__.import_ = import_
        """
        A Database Import block as documented below. `create_mode` must be set to `Default`.
        """
        __props__['import'] = import_

        if not location:
            raise TypeError('Missing required property location')
        elif not isinstance(location, basestring):
            raise TypeError('Expected property location to be a basestring')
        __self__.location = location
        """
        Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
        """
        __props__['location'] = location

        if max_size_bytes and not isinstance(max_size_bytes, basestring):
            raise TypeError('Expected property max_size_bytes to be a basestring')
        __self__.max_size_bytes = max_size_bytes
        """
        The maximum size that the database can grow to. Applies only if `create_mode` is `Default`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).
        """
        __props__['maxSizeBytes'] = max_size_bytes

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        The name of the database.
        """
        __props__['name'] = name

        if requested_service_objective_id and not isinstance(requested_service_objective_id, basestring):
            raise TypeError('Expected property requested_service_objective_id to be a basestring')
        __self__.requested_service_objective_id = requested_service_objective_id
        """
        Use `requested_service_objective_id` or `requested_service_objective_name` to set the performance level for the database.
        Valid values are: `S0`, `S1`, `S2`, `S3`, `P1`, `P2`, `P4`, `P6`, `P11` and `ElasticPool`.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).
        """
        __props__['requestedServiceObjectiveId'] = requested_service_objective_id

        if requested_service_objective_name and not isinstance(requested_service_objective_name, basestring):
            raise TypeError('Expected property requested_service_objective_name to be a basestring')
        __self__.requested_service_objective_name = requested_service_objective_name
        """
        Use `requested_service_objective_name` or `requested_service_objective_id` to set the performance level for the database.  Please see [Azure SQL Database Service Tiers](https://azure.microsoft.com/en-gb/documentation/articles/sql-database-service-tiers/).
        """
        __props__['requestedServiceObjectiveName'] = requested_service_objective_name

        if not resource_group_name:
            raise TypeError('Missing required property resource_group_name')
        elif not isinstance(resource_group_name, basestring):
            raise TypeError('Expected property resource_group_name to be a basestring')
        __self__.resource_group_name = resource_group_name
        """
        The name of the resource group in which to create the database.  This must be the same as Database Server resource group currently.
        """
        __props__['resourceGroupName'] = resource_group_name

        if restore_point_in_time and not isinstance(restore_point_in_time, basestring):
            raise TypeError('Expected property restore_point_in_time to be a basestring')
        __self__.restore_point_in_time = restore_point_in_time
        """
        The point in time for the restore. Only applies if `create_mode` is `PointInTimeRestore` e.g. 2013-11-08T22:00:40Z
        """
        __props__['restorePointInTime'] = restore_point_in_time

        if not server_name:
            raise TypeError('Missing required property server_name')
        elif not isinstance(server_name, basestring):
            raise TypeError('Expected property server_name to be a basestring')
        __self__.server_name = server_name
        """
        The name of the SQL Server on which to create the database.
        """
        __props__['serverName'] = server_name

        if source_database_deletion_date and not isinstance(source_database_deletion_date, basestring):
            raise TypeError('Expected property source_database_deletion_date to be a basestring')
        __self__.source_database_deletion_date = source_database_deletion_date
        """
        The deletion date time of the source database. Only applies to deleted databases where `create_mode` is `PointInTimeRestore`.
        """
        __props__['sourceDatabaseDeletionDate'] = source_database_deletion_date

        if source_database_id and not isinstance(source_database_id, basestring):
            raise TypeError('Expected property source_database_id to be a basestring')
        __self__.source_database_id = source_database_id
        """
        The URI of the source database if `create_mode` value is not `Default`.
        """
        __props__['sourceDatabaseId'] = source_database_id

        if tags and not isinstance(tags, dict):
            raise TypeError('Expected property tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags to assign to the resource.
        """
        __props__['tags'] = tags

        if threat_detection_policy and not isinstance(threat_detection_policy, dict):
            raise TypeError('Expected property threat_detection_policy to be a dict')
        __self__.threat_detection_policy = threat_detection_policy
        """
        Threat detection policy configuration. The `threat_detection_policy` block supports fields documented below.
        """
        __props__['threatDetectionPolicy'] = threat_detection_policy

        __self__.creation_date = pulumi.runtime.UNKNOWN
        """
        The creation date of the SQL Database.
        """
        __self__.default_secondary_location = pulumi.runtime.UNKNOWN
        """
        The default secondary location of the SQL Database.
        """
        __self__.encryption = pulumi.runtime.UNKNOWN

        super(Database, __self__).__init__(
            'azure:sql/database:Database',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'collation' in outs:
            self.collation = outs['collation']
        if 'createMode' in outs:
            self.create_mode = outs['createMode']
        if 'creationDate' in outs:
            self.creation_date = outs['creationDate']
        if 'defaultSecondaryLocation' in outs:
            self.default_secondary_location = outs['defaultSecondaryLocation']
        if 'edition' in outs:
            self.edition = outs['edition']
        if 'elasticPoolName' in outs:
            self.elastic_pool_name = outs['elasticPoolName']
        if 'encryption' in outs:
            self.encryption = outs['encryption']
        if 'import' in outs:
            self.import_ = outs['import']
        if 'location' in outs:
            self.location = outs['location']
        if 'maxSizeBytes' in outs:
            self.max_size_bytes = outs['maxSizeBytes']
        if 'name' in outs:
            self.name = outs['name']
        if 'requestedServiceObjectiveId' in outs:
            self.requested_service_objective_id = outs['requestedServiceObjectiveId']
        if 'requestedServiceObjectiveName' in outs:
            self.requested_service_objective_name = outs['requestedServiceObjectiveName']
        if 'resourceGroupName' in outs:
            self.resource_group_name = outs['resourceGroupName']
        if 'restorePointInTime' in outs:
            self.restore_point_in_time = outs['restorePointInTime']
        if 'serverName' in outs:
            self.server_name = outs['serverName']
        if 'sourceDatabaseDeletionDate' in outs:
            self.source_database_deletion_date = outs['sourceDatabaseDeletionDate']
        if 'sourceDatabaseId' in outs:
            self.source_database_id = outs['sourceDatabaseId']
        if 'tags' in outs:
            self.tags = outs['tags']
        if 'threatDetectionPolicy' in outs:
            self.threat_detection_policy = outs['threatDetectionPolicy']
