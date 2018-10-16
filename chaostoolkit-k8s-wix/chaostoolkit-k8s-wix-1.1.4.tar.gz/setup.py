#!/usr/bin/env python
"""chaostoolkit builder and installer"""
import os
import sys
import io

import setuptools


def get_version_from_package() -> str:
    """
    Read the package version from the source without importing it.
    Will accept version information from TRAVIS_TAG env var
    """
    version = "UNKNOWN"
    val = os.getenv("TRAVIS_TAG")
    if val is not None:
        version = val
    else:
        path = os.path.join(os.path.dirname(__file__), "chaosk8s_wix/__init__.py")
        path = os.path.normpath(os.path.abspath(path))
        with open(path) as f:
            for line in f:
                if line.startswith("__version__"):
                    token, version = line.split(" = ", 1)
                    version = version.replace("'", "").strip()
                    break
    return version


name = 'chaostoolkit-k8s-wix'
desc = 'Extended version of Chaos Toolkit Kubernetes support'

with io.open('README.md', encoding='utf-8') as strm:
    long_desc = strm.read()

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Developers',
    'License :: Freely Distributable',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation',
    'Programming Language :: Python :: Implementation :: CPython'
]
author = 'chaostoolkit Team'
author_email = 'contact@chaostoolkit.org'
url = 'http://chaostoolkit.org'
license = 'Apache License Version 2'
packages = [
    'chaosk8s_wix',
    'chaosk8s_wix.node',
    'chaosk8s_wix.pod',
    'chaosk8s_wix.slack'
]

needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
test_require = []
with io.open('requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]

setup_params = dict(
    name=name,
    version=get_version_from_package(),
    description=desc,
    long_description=long_desc,
    classifiers=classifiers,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=packages,
    include_package_data=True,
    install_requires=install_require,
    tests_require=test_require,
    setup_requires=pytest_runner,
    python_requires='>=3.5.*'
)


def main():
    """Package installation entry point."""
    setuptools.setup(**setup_params)


if __name__ == '__main__':
    main()
