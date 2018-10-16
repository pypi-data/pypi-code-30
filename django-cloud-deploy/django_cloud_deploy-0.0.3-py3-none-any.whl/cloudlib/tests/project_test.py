# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the cloudlib.project module."""

from unittest import mock

from absl.testing import absltest
from googleapiclient import errors

from django_cloud_deploy.cloudlib import project
from django_cloud_deploy.cloudlib.tests.lib import http_fake


class ProjectsFake:
    """A fake object returned by ...projects()."""

    def __init__(self):
        self.projects = []

    def create(self, body):
        self.projects.append(body)
        return http_fake.HttpRequestFake({
            'name':
            'operations/cp.7730969938063130608'
        })

    def get(self, projectId):
        for p in self.projects:
            if p['projectId'] == projectId:
                return http_fake.HttpRequestFake(p)
        return http_fake.HttpRequestFake(
            errors.HttpError(
                http_fake.HttpResponseFake(403), b'permission denied'))


class ServiceFake:
    """A fake Resource returned by discovery.build('cloudresourcemanager', .."""

    def __init__(self):
        self.projects_fake = ProjectsFake()

    def projects(self):
        return self.projects_fake


class ProjectClientTestCase(absltest.TestCase):
    """Test case for project.ProjectClient."""

    def setUp(self):
        self._service_fake = ServiceFake()
        self._project_client = project.ProjectClient(self._service_fake)

    def test_create_project(self):
        self._project_client.create_project('fn123', 'Friendly Name')
        self.assertEqual(self._service_fake.projects_fake.projects,
                         [{
                             'name': 'Friendly Name',
                             'projectId': 'fn123',
                         }])

    @mock.patch('subprocess.check_call')
    def test_create_and_set_project(self, check_call):
        self._project_client.create_and_set_project('fn123', 'Friendly Name')
        self.assertEqual(self._service_fake.projects_fake.projects,
                         [{
                             'name': 'Friendly Name',
                             'projectId': 'fn123',
                         }])

        check_call.assert_called_once_with(
            ['gcloud', 'config', 'set', 'project', 'fn123'])

    def test_project_exists_does(self):
        self._project_client.create_and_set_project('p123', 'Friendly Name')
        self.assertTrue(self._project_client.project_exists('p123'))

    def test_project_exists_doesnot(self):
        self.assertFalse(self._project_client.project_exists('p123'))

    @mock.patch('subprocess.check_call')
    def test_set_existing_project(self, check_call):
        self._project_client.create_project('fn123', 'Friendly Name')
        self._project_client.set_existing_project('fn123')
        check_call.assert_called_once_with(
            ['gcloud', 'config', 'set', 'project', 'fn123'])

    def test_set_existing_project_non_existant(self):
        with self.assertRaises(project.ProjectError):
            self._project_client.set_existing_project('fn123')
