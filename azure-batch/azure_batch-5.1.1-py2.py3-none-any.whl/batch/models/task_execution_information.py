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


class TaskExecutionInformation(Model):
    """Information about the execution of a task.

    All required parameters must be populated in order to send to Azure.

    :param start_time: The time at which the task started running. 'Running'
     corresponds to the running state, so if the task specifies resource files
     or application packages, then the start time reflects the time at which
     the task started downloading or deploying these. If the task has been
     restarted or retried, this is the most recent time at which the task
     started running. This property is present only for tasks that are in the
     running or completed state.
    :type start_time: datetime
    :param end_time: The time at which the task completed. This property is
     set only if the task is in the Completed state.
    :type end_time: datetime
    :param exit_code: The exit code of the program specified on the task
     command line. This property is set only if the task is in the completed
     state. In general, the exit code for a process reflects the specific
     convention implemented by the application developer for that process. If
     you use the exit code value to make decisions in your code, be sure that
     you know the exit code convention used by the application process.
     However, if the Batch service terminates the task (due to timeout, or user
     termination via the API) you may see an operating system-defined exit
     code.
    :type exit_code: int
    :param container_info: Information about the container under which the
     task is executing. This property is set only if the task runs in a
     container context.
    :type container_info:
     ~azure.batch.models.TaskContainerExecutionInformation
    :param failure_info: Information describing the task failure, if any. This
     property is set only if the task is in the completed state and encountered
     a failure.
    :type failure_info: ~azure.batch.models.TaskFailureInformation
    :param retry_count: Required. The number of times the task has been
     retried by the Batch service. Task application failures (non-zero exit
     code) are retried, pre-processing errors (the task could not be run) and
     file upload errors are not retried. The Batch service will retry the task
     up to the limit specified by the constraints.
    :type retry_count: int
    :param last_retry_time: The most recent time at which a retry of the task
     started running. This element is present only if the task was retried
     (i.e. retryCount is nonzero). If present, this is typically the same as
     startTime, but may be different if the task has been restarted for reasons
     other than retry; for example, if the compute node was rebooted during a
     retry, then the startTime is updated but the lastRetryTime is not.
    :type last_retry_time: datetime
    :param requeue_count: Required. The number of times the task has been
     requeued by the Batch service as the result of a user request. When the
     user removes nodes from a pool (by resizing/shrinking the pool) or when
     the job is being disabled, the user can specify that running tasks on the
     nodes be requeued for execution. This count tracks how many times the task
     has been requeued for these reasons.
    :type requeue_count: int
    :param last_requeue_time: The most recent time at which the task has been
     requeued by the Batch service as the result of a user request. This
     property is set only if the requeueCount is nonzero.
    :type last_requeue_time: datetime
    :param result: The result of the task execution. If the value is 'failed',
     then the details of the failure can be found in the failureInfo property.
     Possible values include: 'success', 'failure'
    :type result: str or ~azure.batch.models.TaskExecutionResult
    """

    _validation = {
        'retry_count': {'required': True},
        'requeue_count': {'required': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'exit_code': {'key': 'exitCode', 'type': 'int'},
        'container_info': {'key': 'containerInfo', 'type': 'TaskContainerExecutionInformation'},
        'failure_info': {'key': 'failureInfo', 'type': 'TaskFailureInformation'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'last_retry_time': {'key': 'lastRetryTime', 'type': 'iso-8601'},
        'requeue_count': {'key': 'requeueCount', 'type': 'int'},
        'last_requeue_time': {'key': 'lastRequeueTime', 'type': 'iso-8601'},
        'result': {'key': 'result', 'type': 'TaskExecutionResult'},
    }

    def __init__(self, **kwargs):
        super(TaskExecutionInformation, self).__init__(**kwargs)
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.exit_code = kwargs.get('exit_code', None)
        self.container_info = kwargs.get('container_info', None)
        self.failure_info = kwargs.get('failure_info', None)
        self.retry_count = kwargs.get('retry_count', None)
        self.last_retry_time = kwargs.get('last_retry_time', None)
        self.requeue_count = kwargs.get('requeue_count', None)
        self.last_requeue_time = kwargs.get('last_requeue_time', None)
        self.result = kwargs.get('result', None)
