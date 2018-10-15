# Copyright (C) 2017, 2018 rerobots, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import setup


with open('README.rst') as fp:
    long_description = fp.read()


# Version of this package
MAJOR=0
MINOR=5
PATCH=1
devel=False

version = '{}.{}.{}'.format(MAJOR, MINOR, PATCH)
if devel:
    version += '.dev0'
with open('rerobots/_version.py', 'w') as fp:
    fp.write('''# This file was automatically generated by setup.py. Do not edit.
__version__ = '{}'
'''.format(version))


setup(name='rerobots',
      version=version,
      author='Scott C. Livingston',
      author_email='q@rerobots.net',
      url='https://github.com/rerobots/py',
      description='client library for the rerobots API',
      long_description=long_description,
      classifiers=['License :: OSI Approved :: Apache Software License',
                   'Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
      packages=['rerobots'],
      install_requires=['requests'],
      entry_points={'console_scripts': ['rerobots = rerobots.cli:main']}
      )
