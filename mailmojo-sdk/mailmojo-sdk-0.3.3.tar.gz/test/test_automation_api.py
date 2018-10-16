# coding: utf-8

"""
    MailMojo API

    v1 of the MailMojo API  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: hjelp@mailmojo.no
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import mailmojo
from mailmojo.api.automation_api import AutomationApi  # noqa: E501
from mailmojo.rest import ApiException


class TestAutomationApi(unittest.TestCase):
    """AutomationApi unit test stubs"""

    def setUp(self):
        self.api = mailmojo.api.automation_api.AutomationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_campaign_by_id(self):
        """Test case for get_campaign_by_id

        Retrieve an automation campaign by id.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
