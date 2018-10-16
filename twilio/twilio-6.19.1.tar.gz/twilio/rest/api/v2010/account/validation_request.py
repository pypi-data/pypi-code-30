# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ValidationRequestList(ListResource):
    """  """

    def __init__(self, version, account_sid):
        """
        Initialize the ValidationRequestList

        :param Version version: Version that contains the resource
        :param account_sid: The unique ID of the Account responsible for this Caller Id.

        :returns: twilio.rest.api.v2010.account.validation_request.ValidationRequestList
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestList
        """
        super(ValidationRequestList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds.json'.format(**self._solution)

    def create(self, phone_number, friendly_name=values.unset,
               call_delay=values.unset, extension=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Create a new ValidationRequestInstance

        :param unicode phone_number: The phone number to verify.
        :param unicode friendly_name: A human readable description for the new caller ID with maximum length 64 characters.
        :param unicode call_delay: The number of seconds, between 0 and 60, to delay before initiating the verification call.
        :param unicode extension: Digits to dial after connecting the verification call.
        :param unicode status_callback: A URL that Twilio will request when the verification call ends to notify your app if the verification process was successful or not.
        :param unicode status_callback_method: The HTTP method Twilio should use when requesting the above URL.

        :returns: Newly created ValidationRequestInstance
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestInstance
        """
        data = values.of({
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'CallDelay': call_delay,
            'Extension': extension,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return ValidationRequestInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestList>'


class ValidationRequestPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the ValidationRequestPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique ID of the Account responsible for this Caller Id.

        :returns: twilio.rest.api.v2010.account.validation_request.ValidationRequestPage
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestPage
        """
        super(ValidationRequestPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ValidationRequestInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.validation_request.ValidationRequestInstance
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestInstance
        """
        return ValidationRequestInstance(self._version, payload, account_sid=self._solution['account_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestPage>'


class ValidationRequestInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid):
        """
        Initialize the ValidationRequestInstance

        :returns: twilio.rest.api.v2010.account.validation_request.ValidationRequestInstance
        :rtype: twilio.rest.api.v2010.account.validation_request.ValidationRequestInstance
        """
        super(ValidationRequestInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'phone_number': payload['phone_number'],
            'friendly_name': payload['friendly_name'],
            'validation_code': deserialize.integer(payload['validation_code']),
            'call_sid': payload['call_sid'],
        }

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, }

    @property
    def account_sid(self):
        """
        :returns: The unique ID of the Account responsible for this Caller Id.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def phone_number(self):
        """
        :returns: The incoming phone number.
        :rtype: unicode
        """
        return self._properties['phone_number']

    @property
    def friendly_name(self):
        """
        :returns: A human readable descriptive text for this resource, up to 64 characters long.
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def validation_code(self):
        """
        :returns: The 6 digit validation code that must be entered via the phone to validate this phone number for Caller ID.
        :rtype: unicode
        """
        return self._properties['validation_code']

    @property
    def call_sid(self):
        """
        :returns: The unique id of the Call created for this validation attempt.
        :rtype: unicode
        """
        return self._properties['call_sid']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.ValidationRequestInstance>'
