#!/usr/bin/env
# Copyright (c) 2012-2013 Mitch Garnaat http://garnaat.org/
# Copyright 2012-2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
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
from tests import unittest, BaseEnvVar
import os
import ibm_botocore.exceptions
from ibm_botocore.configloader import raw_config_parse, load_config, \
    multi_file_load_config


def path(filename):
    return os.path.join(os.path.dirname(__file__), 'cfg', filename)


class TestConfigLoader(BaseEnvVar):

    def test_config_not_found(self):
        with self.assertRaises(ibm_botocore.exceptions.ConfigNotFound):
            loaded_config = raw_config_parse(path('aws_config_notfound'))

    def test_config_parse_error(self):
        filename = path('aws_config_bad')
        with self.assertRaises(ibm_botocore.exceptions.ConfigParseError):
            raw_config_parse(filename)

    def test_config(self):
        loaded_config = raw_config_parse(path('aws_config'))
        self.assertIn('default', loaded_config)
        self.assertIn('profile "personal"', loaded_config)

    def test_profile_map_conversion(self):
        loaded_config = load_config(path('aws_config'))
        self.assertIn('profiles', loaded_config)
        self.assertEqual(sorted(loaded_config['profiles'].keys()),
                         ['default', 'personal'])

    def test_bad_profiles_are_ignored(self):
        filename = path('aws_bad_profile')
        loaded_config = load_config(filename)
        self.assertEqual(len(loaded_config['profiles']), 3)
        profiles = loaded_config['profiles']
        self.assertIn('my profile', profiles)
        self.assertIn('personal1', profiles)
        self.assertIn('default', profiles)

    def test_nested_hierarchy_parsing(self):
        filename = path('aws_config_nested')
        loaded_config = load_config(filename)
        config = loaded_config['profiles']['default']
        self.assertEqual(config['aws_access_key_id'], 'foo')
        self.assertEqual(config['region'], 'us-west-2')
        self.assertEqual(config['s3']['signature_version'], 's3v4')
        self.assertEqual(config['cloudwatch']['signature_version'], 'v4')

    def test_nested_hierarchy_with_no_subsection_parsing(self):
        filename = path('aws_config_nested')
        raw_config = raw_config_parse(filename, False)['default']
        self.assertEqual(raw_config['aws_access_key_id'], 'foo')
        self.assertEqual(raw_config['region'], 'us-west-2')
        # Specifying False for pase_subsections in raw_config_parse
        # will make sure that indented sections such as singature_version
        # will not be treated as another subsection but rather
        # its literal value.
        self.assertEqual(
            raw_config['cloudwatch'], '\nsignature_version = v4')
        self.assertEqual(
            raw_config['s3'],
            '\nsignature_version = s3v4'
            '\naddressing_style = path'
        )

    def test_nested_bad_config(self):
        filename = path('aws_config_nested_bad')
        with self.assertRaises(ibm_botocore.exceptions.ConfigParseError):
            loaded_config = load_config(filename)

    def test_multi_file_load(self):
        filenames = [path('aws_config_other'),
                     path('aws_config'),
                     path('aws_third_config'),
                     path('aws_config_notfound')]
        loaded_config = multi_file_load_config(*filenames)
        config = loaded_config['profiles']['default']
        self.assertEqual(config['aws_access_key_id'], 'other_foo')
        self.assertEqual(config['aws_secret_access_key'], 'other_bar')
        second_config = loaded_config['profiles']['personal']
        self.assertEqual(second_config['aws_access_key_id'], 'fie')
        self.assertEqual(second_config['aws_secret_access_key'], 'baz')
        self.assertEqual(second_config['aws_security_token'], 'fiebaz')
        third_config = loaded_config['profiles']['third']
        self.assertEqual(third_config['aws_access_key_id'], 'third_fie')
        self.assertEqual(third_config['aws_secret_access_key'], 'third_baz')
        self.assertEqual(third_config['aws_security_token'], 'third_fiebaz')


if __name__ == "__main__":
    unittest.main()
