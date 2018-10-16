# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
from msrest.serialization import Model


class MultiInstanceSettings(Model):
    """Settings which specify how to run a multi-instance task.

    Multi-instance tasks are commonly used to support MPI tasks.

    :param number_of_instances: The number of compute nodes required by the
     task. If omitted, the default is 1.
    :type number_of_instances: int
    :param coordination_command_line: The command line to run on all the
     compute nodes to enable them to coordinate when the primary runs the main
     task command. A typical coordination command line launches a background
     service and verifies that the service is ready to process inter-node
     messages.
    :type coordination_command_line: str
    :param common_resource_files: A list of files that the Batch service will
     download before running the coordination command line. The difference
     between common resource files and task resource files is that common
     resource files are downloaded for all subtasks including the primary,
     whereas task resource files are downloaded only for the primary. Also note
     that these resource files are not downloaded to the task working
     directory, but instead are downloaded to the task root directory (one
     directory above the working directory).
    :type common_resource_files: list of :class:`ExtendedResourceFile
     <azext.batch.models.ExtendedResourceFile>`
    """

    _validation = {
        'coordination_command_line': {'required': True},
    }

    _attribute_map = {
        'number_of_instances': {'key': 'numberOfInstances', 'type': 'int'},
        'coordination_command_line': {'key': 'coordinationCommandLine', 'type': 'str'},
        'common_resource_files': {'key': 'commonResourceFiles', 'type': '[ExtendedResourceFile]'},
    }

    def __init__(self, *, coordination_command_line: int, number_of_instances: str=None,
                 common_resource_files=None, **kwargs) -> None:
        super(MultiInstanceSettings, self).__init__(**kwargs)
        self.number_of_instances = number_of_instances
        self.coordination_command_line = coordination_command_line
        self.common_resource_files = common_resource_files
