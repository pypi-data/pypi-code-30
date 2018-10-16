# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class TaskQueueCumulativeStatisticsList(ListResource):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueCumulativeStatisticsList

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsList
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsList
        """
        super(TaskQueueCumulativeStatisticsList, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }

    def get(self):
        """
        Constructs a TaskQueueCumulativeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        """
        return TaskQueueCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __call__(self):
        """
        Constructs a TaskQueueCumulativeStatisticsContext

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        """
        return TaskQueueCumulativeStatisticsContext(
            self._version,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsList>'


class TaskQueueCumulativeStatisticsPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the TaskQueueCumulativeStatisticsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsPage
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsPage
        """
        super(TaskQueueCumulativeStatisticsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of TaskQueueCumulativeStatisticsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsInstance
        """
        return TaskQueueCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsPage>'


class TaskQueueCumulativeStatisticsContext(InstanceContext):
    """  """

    def __init__(self, version, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueCumulativeStatisticsContext

        :param Version version: Version that contains the resource
        :param workspace_sid: The workspace_sid
        :param task_queue_sid: The task_queue_sid

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        """
        super(TaskQueueCumulativeStatisticsContext, self).__init__(version)

        # Path Solution
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }
        self._uri = '/Workspaces/{workspace_sid}/TaskQueues/{task_queue_sid}/CumulativeStatistics'.format(**self._solution)

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset,
              split_by_wait_time=values.unset):
        """
        Fetch a TaskQueueCumulativeStatisticsInstance

        :param datetime end_date: Filter cumulative statistics by an end date.
        :param unicode minutes: Filter cumulative statistics by up to 'x' minutes in the past.
        :param datetime start_date: Filter cumulative statistics by a start date.
        :param unicode task_channel: Filter real-time and cumulative statistics by TaskChannel.
        :param unicode split_by_wait_time: A comma separated values for viewing splits of tasks canceled and accepted above the given threshold in seconds.

        :returns: Fetched TaskQueueCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsInstance
        """
        params = values.of({
            'EndDate': serialize.iso8601_datetime(end_date),
            'Minutes': minutes,
            'StartDate': serialize.iso8601_datetime(start_date),
            'TaskChannel': task_channel,
            'SplitByWaitTime': split_by_wait_time,
        })

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return TaskQueueCumulativeStatisticsInstance(
            self._version,
            payload,
            workspace_sid=self._solution['workspace_sid'],
            task_queue_sid=self._solution['task_queue_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsContext {}>'.format(context)


class TaskQueueCumulativeStatisticsInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, workspace_sid, task_queue_sid):
        """
        Initialize the TaskQueueCumulativeStatisticsInstance

        :returns: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsInstance
        """
        super(TaskQueueCumulativeStatisticsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'avg_task_acceptance_time': deserialize.integer(payload['avg_task_acceptance_time']),
            'start_time': deserialize.iso8601_datetime(payload['start_time']),
            'end_time': deserialize.iso8601_datetime(payload['end_time']),
            'reservations_created': deserialize.integer(payload['reservations_created']),
            'reservations_accepted': deserialize.integer(payload['reservations_accepted']),
            'reservations_rejected': deserialize.integer(payload['reservations_rejected']),
            'reservations_timed_out': deserialize.integer(payload['reservations_timed_out']),
            'reservations_canceled': deserialize.integer(payload['reservations_canceled']),
            'reservations_rescinded': deserialize.integer(payload['reservations_rescinded']),
            'split_by_wait_time': payload['split_by_wait_time'],
            'task_queue_sid': payload['task_queue_sid'],
            'wait_duration_until_accepted': payload['wait_duration_until_accepted'],
            'wait_duration_until_canceled': payload['wait_duration_until_canceled'],
            'tasks_canceled': deserialize.integer(payload['tasks_canceled']),
            'tasks_completed': deserialize.integer(payload['tasks_completed']),
            'tasks_deleted': deserialize.integer(payload['tasks_deleted']),
            'tasks_entered': deserialize.integer(payload['tasks_entered']),
            'tasks_moved': deserialize.integer(payload['tasks_moved']),
            'workspace_sid': payload['workspace_sid'],
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'workspace_sid': workspace_sid, 'task_queue_sid': task_queue_sid, }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: TaskQueueCumulativeStatisticsContext for this TaskQueueCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsContext
        """
        if self._context is None:
            self._context = TaskQueueCumulativeStatisticsContext(
                self._version,
                workspace_sid=self._solution['workspace_sid'],
                task_queue_sid=self._solution['task_queue_sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def avg_task_acceptance_time(self):
        """
        :returns: The average time from Task creation to reservation acceptance while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['avg_task_acceptance_time']

    @property
    def start_time(self):
        """
        :returns: The start_time
        :rtype: datetime
        """
        return self._properties['start_time']

    @property
    def end_time(self):
        """
        :returns: The end_time
        :rtype: datetime
        """
        return self._properties['end_time']

    @property
    def reservations_created(self):
        """
        :returns: The total number of Reservations that were created for Tasks while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['reservations_created']

    @property
    def reservations_accepted(self):
        """
        :returns: The total number of Reservations that were accepted for Tasks while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['reservations_accepted']

    @property
    def reservations_rejected(self):
        """
        :returns: The total number of Reservations that were rejected for Tasks while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['reservations_rejected']

    @property
    def reservations_timed_out(self):
        """
        :returns: The total number of Reservations that were timed out for Tasks while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['reservations_timed_out']

    @property
    def reservations_canceled(self):
        """
        :returns: The total number of Reservations that were canceled for Tasks while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['reservations_canceled']

    @property
    def reservations_rescinded(self):
        """
        :returns: The total number of Reservations that were rescinded
        :rtype: unicode
        """
        return self._properties['reservations_rescinded']

    @property
    def split_by_wait_time(self):
        """
        :returns: The splits of the tasks canceled and accepted based on the provided SplitByWaitTime parameter
        :rtype: dict
        """
        return self._properties['split_by_wait_time']

    @property
    def task_queue_sid(self):
        """
        :returns: The task_queue_sid
        :rtype: unicode
        """
        return self._properties['task_queue_sid']

    @property
    def wait_duration_until_accepted(self):
        """
        :returns: The wait duration stats for tasks that were accepted while in this TaskQueue
        :rtype: dict
        """
        return self._properties['wait_duration_until_accepted']

    @property
    def wait_duration_until_canceled(self):
        """
        :returns: The wait duration stats for tasks that were canceled while in this TaskQueue
        :rtype: dict
        """
        return self._properties['wait_duration_until_canceled']

    @property
    def tasks_canceled(self):
        """
        :returns: The total number of Tasks canceled while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['tasks_canceled']

    @property
    def tasks_completed(self):
        """
        :returns: The total number of Tasks completed while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['tasks_completed']

    @property
    def tasks_deleted(self):
        """
        :returns: The total number of Tasks that were deleted while in this TaskQueue
        :rtype: unicode
        """
        return self._properties['tasks_deleted']

    @property
    def tasks_entered(self):
        """
        :returns: The total number of Tasks entered into this TaskQueue
        :rtype: unicode
        """
        return self._properties['tasks_entered']

    @property
    def tasks_moved(self):
        """
        :returns: The total number of Tasks moved to another TaskQueue from this TaskQueue
        :rtype: unicode
        """
        return self._properties['tasks_moved']

    @property
    def workspace_sid(self):
        """
        :returns: The workspace_sid
        :rtype: unicode
        """
        return self._properties['workspace_sid']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self, end_date=values.unset, minutes=values.unset,
              start_date=values.unset, task_channel=values.unset,
              split_by_wait_time=values.unset):
        """
        Fetch a TaskQueueCumulativeStatisticsInstance

        :param datetime end_date: Filter cumulative statistics by an end date.
        :param unicode minutes: Filter cumulative statistics by up to 'x' minutes in the past.
        :param datetime start_date: Filter cumulative statistics by a start date.
        :param unicode task_channel: Filter real-time and cumulative statistics by TaskChannel.
        :param unicode split_by_wait_time: A comma separated values for viewing splits of tasks canceled and accepted above the given threshold in seconds.

        :returns: Fetched TaskQueueCumulativeStatisticsInstance
        :rtype: twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics.TaskQueueCumulativeStatisticsInstance
        """
        return self._proxy.fetch(
            end_date=end_date,
            minutes=minutes,
            start_date=start_date,
            task_channel=task_channel,
            split_by_wait_time=split_by_wait_time,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Taskrouter.V1.TaskQueueCumulativeStatisticsInstance {}>'.format(context)
