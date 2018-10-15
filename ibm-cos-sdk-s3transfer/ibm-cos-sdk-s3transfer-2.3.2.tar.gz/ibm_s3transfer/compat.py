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
import inspect
import sys
import os
import errno
import socket

from ibm_botocore.compat import six


if sys.platform.startswith('win'):
    def rename_file(current_filename, new_filename):
        try:
            os.remove(new_filename)
        except OSError as e:
            if not e.errno == errno.ENOENT:
                # We only want to a ignore trying to remove
                # a file that does not exist.  If it fails
                # for any other reason we should be propagating
                # that exception.
                raise
        os.rename(current_filename, new_filename)
else:
    rename_file = os.rename

if six.PY3:
    def accepts_kwargs(func):
        # In python3.4.1, there's backwards incompatible
        # changes when using getargspec with functools.partials.
        return inspect.getfullargspec(func)[2]

    # In python3, socket.error is OSError, which is too general
    # for what we want (i.e FileNotFoundError is a subclass of OSError).
    # In py3 all the socket related errors are in a newly created
    # ConnectionError
    SOCKET_ERROR = ConnectionError
    MAXINT = None
else:
    def accepts_kwargs(func):
        return inspect.getargspec(func)[2]

    SOCKET_ERROR = socket.error
    MAXINT = sys.maxint


def seekable(fileobj):
    """Backwards compat function to determine if a fileobj is seekable

    :param fileobj: The file-like object to determine if seekable

    :returns: True, if seekable. False, otherwise.
    """
    # If the fileobj has a seekable attr, try calling the seekable()
    # method on it.
    if hasattr(fileobj, 'seekable'):
        return fileobj.seekable()
    # If there is no seekable attr, check if the object can be seeked
    # or telled. If it can, try to seek to the current position.
    elif hasattr(fileobj, 'seek') and hasattr(fileobj, 'tell'):
        try:
            fileobj.seek(0, 1)
            return True
        except (OSError, IOError):
            # If an io related error was thrown then it is not seekable.
            return False
    # Else, the fileobj is not seekable
    return False


def readable(fileobj):
    """Determines whether or not a file-like object is readable.

    :param fileobj: The file-like object to determine if readable

    :returns: True, if readable. False otherwise.
    """
    if hasattr(fileobj, 'readable'):
        return fileobj.readable()

    return hasattr(fileobj, 'read')
