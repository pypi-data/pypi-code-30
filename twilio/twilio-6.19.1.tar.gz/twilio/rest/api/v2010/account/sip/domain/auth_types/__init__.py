# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping import AuthTypeCallsList
from twilio.rest.api.v2010.account.sip.domain.auth_types.auth_registrations_mapping import AuthTypeRegistrationsList


class AuthTypesList(ListResource):
    """  """

    def __init__(self, version, account_sid, domain_sid):
        """
        Initialize the AuthTypesList

        :param Version version: Version that contains the resource
        :param account_sid: The unique id of the account that sent the call
        :param domain_sid: A string that uniquely identifies the SIP Domain

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesList
        """
        super(AuthTypesList, self).__init__(version)

        # Path Solution
        self._solution = {'account_sid': account_sid, 'domain_sid': domain_sid, }

        # Components
        self._calls = None
        self._registrations = None

    @property
    def calls(self):
        """
        Access the calls

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_calls_mapping.AuthTypeCallsList
        """
        if self._calls is None:
            self._calls = AuthTypeCallsList(
                self._version,
                account_sid=self._solution['account_sid'],
                domain_sid=self._solution['domain_sid'],
            )
        return self._calls

    @property
    def registrations(self):
        """
        Access the registrations

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_registrations_mapping.AuthTypeRegistrationsList
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.auth_registrations_mapping.AuthTypeRegistrationsList
        """
        if self._registrations is None:
            self._registrations = AuthTypeRegistrationsList(
                self._version,
                account_sid=self._solution['account_sid'],
                domain_sid=self._solution['domain_sid'],
            )
        return self._registrations

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypesList>'


class AuthTypesPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the AuthTypesPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param account_sid: The unique id of the account that sent the call
        :param domain_sid: A string that uniquely identifies the SIP Domain

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesPage
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesPage
        """
        super(AuthTypesPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of AuthTypesInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesInstance
        """
        return AuthTypesInstance(
            self._version,
            payload,
            account_sid=self._solution['account_sid'],
            domain_sid=self._solution['domain_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypesPage>'


class AuthTypesInstance(InstanceResource):
    """  """

    def __init__(self, version, payload, account_sid, domain_sid):
        """
        Initialize the AuthTypesInstance

        :returns: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesInstance
        :rtype: twilio.rest.api.v2010.account.sip.domain.auth_types.AuthTypesInstance
        """
        super(AuthTypesInstance, self).__init__(version)

        # Context
        self._context = None
        self._solution = {'account_sid': account_sid, 'domain_sid': domain_sid, }

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.AuthTypesInstance>'
