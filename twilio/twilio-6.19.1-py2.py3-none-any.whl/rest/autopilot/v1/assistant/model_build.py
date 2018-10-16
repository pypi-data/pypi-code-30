# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ModelBuildList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid):
        """
        Initialize the ModelBuildList

        :param Version version: Version that contains the resource
        :param assistant_sid: The unique ID of the parent Assistant.

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildList
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildList
        """
        super(ModelBuildList, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, }
        self._uri = '/Assistants/{assistant_sid}/ModelBuilds'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams ModelBuildInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ModelBuildInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return ModelBuildPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return ModelBuildPage(self._version, response, self._solution)

    def create(self, status_callback=values.unset, unique_name=values.unset):
        """
        Create a new ModelBuildInstance

        :param unicode status_callback: The status_callback
        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long. For example: v0.1

        :returns: Newly created ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        data = values.of({'StatusCallback': status_callback, 'UniqueName': unique_name, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ModelBuildInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def get(self, sid):
        """
        Constructs a ModelBuildContext

        :param sid: The sid

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        return ModelBuildContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a ModelBuildContext

        :param sid: The sid

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        return ModelBuildContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.ModelBuildList>'


class ModelBuildPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the ModelBuildPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param assistant_sid: The unique ID of the parent Assistant.

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        """
        super(ModelBuildPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ModelBuildInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        return ModelBuildInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.ModelBuildPage>'


class ModelBuildContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, assistant_sid, sid):
        """
        Initialize the ModelBuildContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The assistant_sid
        :param sid: The sid

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        super(ModelBuildContext, self).__init__(version)

        # Path Solution
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid, }
        self._uri = '/Assistants/{assistant_sid}/ModelBuilds/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a ModelBuildInstance

        :returns: Fetched ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def update(self, unique_name=values.unset):
        """
        Update the ModelBuildInstance

        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long. For example: v0.1

        :returns: Updated ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        data = values.of({'UniqueName': unique_name, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the ModelBuildInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.ModelBuildContext {}>'.format(context)


class ModelBuildInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Status(object):
        ENQUEUED = "enqueued"
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"
        CANCELED = "canceled"

    def __init__(self, version, payload, assistant_sid, sid=None):
        """
        Initialize the ModelBuildInstance

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        super(ModelBuildInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'assistant_sid': payload['assistant_sid'],
            'sid': payload['sid'],
            'status': payload['status'],
            'unique_name': payload['unique_name'],
            'url': payload['url'],
            'build_duration': deserialize.integer(payload['build_duration']),
            'error_code': deserialize.integer(payload['error_code']),
        }

        # Context
        self._context = None
        self._solution = {'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ModelBuildContext for this ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        if self._context is None:
            self._context = ModelBuildContext(
                self._version,
                assistant_sid=self._solution['assistant_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account that created this Model Build.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def assistant_sid(self):
        """
        :returns: The unique ID of the parent Assistant.
        :rtype: unicode
        """
        return self._properties['assistant_sid']

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def status(self):
        """
        :returns: A string that described the model build status. The values can be: `enqueued`, `building`, `completed`, `failed`
        :rtype: ModelBuildInstance.Status
        """
        return self._properties['status']

    @property
    def unique_name(self):
        """
        :returns: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long.
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def build_duration(self):
        """
        :returns: The time in seconds it took to build the model.
        :rtype: unicode
        """
        return self._properties['build_duration']

    @property
    def error_code(self):
        """
        :returns: The error_code
        :rtype: unicode
        """
        return self._properties['error_code']

    def fetch(self):
        """
        Fetch a ModelBuildInstance

        :returns: Fetched ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        return self._proxy.fetch()

    def update(self, unique_name=values.unset):
        """
        Update the ModelBuildInstance

        :param unicode unique_name: A user-provided string that uniquely identifies this resource as an alternative to the sid. Unique up to 64 characters long. For example: v0.1

        :returns: Updated ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        return self._proxy.update(unique_name=unique_name, )

    def delete(self):
        """
        Deletes the ModelBuildInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.ModelBuildInstance {}>'.format(context)
