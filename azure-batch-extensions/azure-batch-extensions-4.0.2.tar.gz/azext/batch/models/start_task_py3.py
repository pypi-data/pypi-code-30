# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class StartTask(Model):
    """A task which is run when a compute node joins a pool in the Azure Batch
    service, or when the compute node is rebooted or reimaged.

    :param command_line: The command line of the start task. The command line
     does not run under a shell, and therefore cannot take advantage of shell
     features such as environment variable expansion. If you want to take
     advantage of such features, you should invoke the shell in the command
     line, for example using "cmd /c MyCommand" in Windows or "/bin/sh -c
     MyCommand" in Linux.
    :type command_line: str
    :param container_settings: The settings for the container under which the
     start task runs. When this is specified, all directories recursively below
     the AZ_BATCH_NODE_ROOT_DIR (the root of Azure Batch directories on the
     node) are mapped into the container, all task environment variables are
     mapped into the container, and the task command line is executed in the
     container.
    :type container_settings: :class:`TaskContainerSettings
     <azure.batch.models.TaskContainerSettings>`
    :param resource_files: A list of files that the Batch service will
     download to the compute node before running the command line. Files listed
     under this element are located in the task's working directory.
    :type resource_files: list of :class:`ExtendedResourceFile
     <azext.batch.models.ExtendedResourceFile>`
    :param environment_settings: A list of environment variable settings for
     the start task.
    :type environment_settings: list of :class:`EnvironmentSetting
     <azure.batch.models.EnvironmentSetting>`
    :param user_identity: The user identity under which the start task runs.
     If omitted, the task runs as a non-administrative user unique to the task.
    :type user_identity: :class:`UserIdentity
     <azure.batch.models.UserIdentity>`
    :param max_task_retry_count: The maximum number of times the task may be
     retried. The Batch service retries a task if its exit code is nonzero.
     Note that this value specifically controls the number of retries. The
     Batch service will try the task once, and may then retry up to this limit.
     For example, if the maximum retry count is 3, Batch tries the task up to 4
     times (one initial try and 3 retries). If the maximum retry count is 0,
     the Batch service does not retry the task. If the maximum retry count is
     -1, the Batch service retries the task without limit.
    :type max_task_retry_count: int
    :param wait_for_success: Whether the Batch service should wait for the
     start task to complete successfully (that is, to exit with exit code 0)
     before scheduling any tasks on the compute node. If true and the start
     task fails on a compute node, the Batch service retries the start task up
     to its maximum retry count (maxTaskRetryCount). If the task has still not
     completed successfully after all retries, then the Batch service marks the
     compute node unusable, and will not schedule tasks to it. This condition
     can be detected via the node state and failure info details. If false, the
     Batch service will not wait for the start task to complete. In this case,
     other tasks can start executing on the compute node while the start task
     is still running; and even if the start task fails, new tasks will
     continue to be scheduled on the node. The default is false.
    :type wait_for_success: bool
    """

    _validation = {
        'command_line': {'required': True},
    }

    _attribute_map = {
        'command_line': {'key': 'commandLine', 'type': 'str'},
        'container_settings': {'key': 'containerSettings', 'type': 'TaskContainerSettings'},
        'resource_files': {'key': 'resourceFiles', 'type': '[ExtendedResourceFile]'},
        'environment_settings': {'key': 'environmentSettings', 'type': '[EnvironmentSetting]'},
        'user_identity': {'key': 'userIdentity', 'type': 'UserIdentity'},
        'max_task_retry_count': {'key': 'maxTaskRetryCount', 'type': 'int'},
        'wait_for_success': {'key': 'waitForSuccess', 'type': 'bool'},
    }

    def __init__(self, *, command_line: str, container_settings=None, resource_files=None, environment_settings=None,
                 user_identity=None, max_task_retry_count: int=None, wait_for_success: bool=None, **kwargs) -> None:
        super(StartTask, self).__init__(**kwargs)
        self.command_line = command_line
        self.container_settings = container_settings
        self.resource_files = resource_files
        self.environment_settings = environment_settings
        self.user_identity = user_identity
        self.max_task_retry_count = max_task_retry_count
        self.wait_for_success = wait_for_success
