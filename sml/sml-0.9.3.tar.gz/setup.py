"""Setup module for sml."""

# Copyright 2016-2018 ASI Data Science
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path

from setuptools import find_packages, setup


def source_root_dir():
    """Return the path to the root of the source distribution."""
    return os.path.abspath(os.path.dirname(__file__))


def read_version():
    """Read the version from the ``sml.version`` module."""
    filename = os.path.join(source_root_dir(), "sml/version.py")
    with open(filename) as fin:
        namespace = {}
        exec(fin.read(), namespace)  # pylint: disable=exec-used
        return namespace["__version__"]


def read_long_description():
    """Read from the README file in root of source directory."""
    readme = os.path.join(source_root_dir(), "README.rst")
    with open(readme) as fin:
        return fin.read()


setup(
    name="sml",
    version=read_version(),
    description="The command line interface to SherlockML",
    long_description=read_long_description(),
    url="https://sherlockml.com",
    author="ASI Data Science",
    author_email="engineering@asidatascience.com",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Operating System :: POSIX",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords="data science platform",
    packages=find_packages(),
    install_requires=[
        "click",
        "python-dateutil",
        "requests",
        "six",
        "tabulate",
    ],
    entry_points={"console_scripts": ["sml=sml.cli:cli"]},
)
