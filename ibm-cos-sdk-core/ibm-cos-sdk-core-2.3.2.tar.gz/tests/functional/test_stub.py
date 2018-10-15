# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import ibm_botocore.config
from tests import unittest

import ibm_botocore
import ibm_botocore.session
import ibm_botocore.stub as stub
from ibm_botocore.stub import Stubber
from ibm_botocore.exceptions import StubResponseError, ClientError, \
    StubAssertionError
from ibm_botocore.exceptions import ParamValidationError
import ibm_botocore.client
import ibm_botocore.retryhandler
import ibm_botocore.translate


class TestStubber(unittest.TestCase):
    def setUp(self):
        session = ibm_botocore.session.get_session()
        config = ibm_botocore.config.Config(signature_version=ibm_botocore.UNSIGNED)
        self.client = session.create_client('s3', config=config)

        self.stubber = Stubber(self.client)

    def test_stubber_returns_response(self):
        service_response = {'ResponseMetadata': {'foo': 'bar'}}
        self.stubber.add_response('list_objects', service_response)
        self.stubber.activate()
        response = self.client.list_objects(Bucket='foo')
        self.assertEqual(response, service_response)

    def test_context_manager_returns_response(self):
        service_response = {'ResponseMetadata': {'foo': 'bar'}}
        self.stubber.add_response('list_objects', service_response)

        with self.stubber:
            response = self.client.list_objects(Bucket='foo')
        self.assertEqual(response, service_response)

    def test_activated_stubber_errors_with_no_registered_stubs(self):
        self.stubber.activate()
        # Params one per line for readability.
        with self.assertRaisesRegexp(StubResponseError,
                                     "'Bucket': 'asdfasdfasdfasdf',\n"):
            self.client.list_objects(
                Bucket='asdfasdfasdfasdf',
                Delimiter='asdfasdfasdfasdf',
                Prefix='asdfasdfasdfasdf',
                EncodingType='url')

    def test_stubber_errors_when_stubs_are_used_up(self):
        self.stubber.add_response('list_objects', {})
        self.stubber.activate()
        self.client.list_objects(Bucket='foo')

        with self.assertRaises(StubResponseError):
            self.client.list_objects(Bucket='foo')

    def test_client_error_response(self):
        error_code = "AccessDenied"
        error_message = "Access Denied"
        self.stubber.add_client_error(
            'list_objects', error_code, error_message)
        self.stubber.activate()

        with self.assertRaises(ClientError):
            self.client.list_objects(Bucket='foo')

    def test_can_add_expected_params_to_client_error(self):
        self.stubber.add_client_error(
            'list_objects', 'Error', 'error',
            expected_params={'Bucket': 'foo'}
        )
        self.stubber.activate()
        with self.assertRaises(ClientError):
            self.client.list_objects(Bucket='foo')

    def test_can_expected_param_fails_in_client_error(self):
        self.stubber.add_client_error(
            'list_objects', 'Error', 'error',
            expected_params={'Bucket': 'foo'}
        )
        self.stubber.activate()
        # We expect an AssertionError instead of a ClientError
        # because we're calling the operation with the wrong
        # param value.
        with self.assertRaises(AssertionError):
            self.client.list_objects(Bucket='wrong-argument-value')

    def test_expected_params_success(self):
        service_response = {}
        expected_params = {'Bucket': 'foo'}
        self.stubber.add_response(
            'list_objects', service_response, expected_params)
        self.stubber.activate()
        # This should be called successfully with no errors being thrown
        # for mismatching expected params.
        response = self.client.list_objects(Bucket='foo')
        self.assertEqual(response, service_response)

    def test_expected_params_fail(self):
        service_response = {}
        expected_params = {'Bucket': 'bar'}
        self.stubber.add_response(
            'list_objects', service_response, expected_params)
        self.stubber.activate()
        # This should call should raise an for mismatching expected params.
        with self.assertRaisesRegexp(StubResponseError,
                                     "{'Bucket': 'bar'},\n"):
            self.client.list_objects(Bucket='foo')

    def test_expected_params_mixed_with_errors_responses(self):
        # Add an error response
        error_code = "AccessDenied"
        error_message = "Access Denied"
        self.stubber.add_client_error(
            'list_objects', error_code, error_message)

        # Add a response with incorrect expected params
        service_response = {}
        expected_params = {'Bucket': 'bar'}
        self.stubber.add_response(
            'list_objects', service_response, expected_params)

        self.stubber.activate()

        # The first call should throw and error as expected.
        with self.assertRaises(ClientError):
            self.client.list_objects(Bucket='foo')

        # The second call should throw an error for unexpected parameters
        with self.assertRaisesRegexp(StubResponseError, 'Expected parameters'):
            self.client.list_objects(Bucket='foo')

    def test_can_continue_to_call_after_expected_params_fail(self):
        service_response = {}
        expected_params = {'Bucket': 'bar'}

        self.stubber.add_response(
            'list_objects', service_response, expected_params)

        self.stubber.activate()
        # Throw an error for unexpected parameters
        with self.assertRaises(StubResponseError):
            self.client.list_objects(Bucket='foo')

        # The stubber should still have the responses queued up
        # even though the original parameters did not match the expected ones.
        self.client.list_objects(Bucket='bar')
        self.stubber.assert_no_pending_responses()

    def test_still_relies_on_param_validation_with_expected_params(self):
        service_response = {}
        expected_params = {'Buck': 'bar'}

        self.stubber.add_response(
            'list_objects', service_response, expected_params)

        self.stubber.activate()
        # Throw an error for invalid parameters
        with self.assertRaises(ParamValidationError):
            self.client.list_objects(Buck='bar')

    def test_any_ignores_param_for_validation(self):
        service_response = {}
        expected_params = {'Bucket': stub.ANY}

        self.stubber.add_response(
            'list_objects', service_response, expected_params)
        self.stubber.add_response(
            'list_objects', service_response, expected_params)

        try:
            with self.stubber:
                self.client.list_objects(Bucket='foo')
                self.client.list_objects(Bucket='bar')
        except StubAssertionError:
            self.fail("stub.ANY failed to ignore parameter for validation.")

    def test_mixed_any_and_concrete_params(self):
        service_response = {}
        expected_params = {'Bucket': stub.ANY, 'Key': 'foo.txt'}

        self.stubber.add_response(
            'head_object', service_response, expected_params)
        self.stubber.add_response(
            'head_object', service_response, expected_params)

        try:
            with self.stubber:
                self.client.head_object(Bucket='foo', Key='foo.txt')
                self.client.head_object(Bucket='bar', Key='foo.txt')
        except StubAssertionError:
            self.fail("stub.ANY failed to ignore parameter for validation.")

    def test_nested_any_param(self):
        service_response = {}
        expected_params = {
            'Bucket': 'foo',
            'Key': 'bar.txt',
            'Metadata': {
                'MyMeta': stub.ANY,
            }
        }

        self.stubber.add_response(
            'put_object', service_response, expected_params)
        self.stubber.add_response(
            'put_object', service_response, expected_params)

        try:
            with self.stubber:
                self.client.put_object(
                    Bucket='foo',
                    Key='bar.txt',
                    Metadata={
                        'MyMeta': 'Foo',
                    }
                )
                self.client.put_object(
                    Bucket='foo',
                    Key='bar.txt',
                    Metadata={
                        'MyMeta': 'Bar',
                    }
                )
        except StubAssertionError:
            self.fail(
                "stub.ANY failed to ignore nested parameter for validation.")

    def test_ANY_repr(self):
        self.assertEqual(repr(stub.ANY), '<ANY>')

    def test_none_param(self):
        service_response = {}
        expected_params = {'Buck': None}

        self.stubber.add_response(
            'list_objects', service_response, expected_params)

        self.stubber.activate()
        # Throw an error for invalid parameters
        with self.assertRaises(StubAssertionError):
            self.client.list_objects(Buck='bar')

    def test_many_expected_params(self):
        service_response = {}
        expected_params = {
            'Bucket': 'mybucket',
            'Prefix': 'myprefix',
            'Delimiter': '/',
            'EncodingType': 'url'
        }
        self.stubber.add_response(
            'list_objects', service_response, expected_params)
        try:
            with self.stubber:
                self.client.list_objects(**expected_params)
        except StubAssertionError:
            self.fail(
                "Stubber inappropriately raised error for same parameters.")
