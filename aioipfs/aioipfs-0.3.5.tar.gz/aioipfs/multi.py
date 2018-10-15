
import os, os.path
import io
import re

import asyncio
import aiohttp
from aiohttp import payload

class FormDataWriter(aiohttp.MultipartWriter):
    def __init__(self):
        super().__init__(subtype="form-data")

def multiform_bytes(bytes):
    with FormDataWriter() as mpwriter:
        part = payload.BytesPayload(bytes)
        part.set_content_disposition('form-data', filename='')
        mpwriter.append_payload(part)
        return mpwriter

def multiform_json(json):
    with FormDataWriter() as mpwriter:
        part = payload.JsonPayload(json)
        part.set_content_disposition('form-data', name='',
            filename='')
        mpwriter.append_payload(part)
        return mpwriter

def bytes_payload_from_file(filepath):
    basename = os.path.basename(filepath)
    file_payload = payload.BytesIOPayload(open(filepath, 'rb'))
    file_payload.set_content_disposition('form-data',
            filename=basename)
    return file_payload

def glob_compile(pat):
    """ From ipfsapi.multipart

       Translate a shell glob PATTERN to a regular expression.

    This is almost entirely based on `fnmatch.translate` source-code from the
    python 3.5 standard-library.
    """

    i, n = 0, len(pat)
    res = ''
    while i < n:
        c = pat[i]
        i = i + 1
        if c == '/' and len(pat) > (i + 2) and pat[i:(i + 3)] == '**/':
            # Special-case for "any number of sub-directories" operator since
            # may also expand to no entries:
            #  Otherwise `a/**/b` would expand to `a[/].*[/]b` which wouldn't
            #  match the immediate sub-directories of `a`, like `a/b`.
            i = i + 3
            res = res + '[/]([^/]*[/])*'
        elif c == '*':
            if len(pat) > i and pat[i] == '*':
                i = i + 1
                res = res + '.*'
            else:
                res = res + '[^/]*'
        elif c == '?':
            res = res + '[^/]'
        elif c == '[':
            j = i
            if j < n and pat[j] == '!':
                j = j + 1
            if j < n and pat[j] == ']':
                j = j + 1
            while j < n and pat[j] != ']':
                j = j + 1
            if j >= n:
                res = res + '\\['
            else:
                stuff = pat[i:j].replace('\\', '\\\\')
                i = j + 1
                if stuff[0] == '!':
                    stuff = '^' + stuff[1:]
                elif stuff[0] == '^':
                    stuff = '\\' + stuff
                res = '%s[%s]' % (res, stuff)
        else:
            res = res + re.escape(c)
    return re.compile('^' + res + '\Z(?ms)' + '$')

class DirectoryListing:
    """ This class is from ipfsapi.multipart.DirectoryStream, reused it
        just to generate the file paths. It's not a generator """

    def __init__(self,
                 directory,
                 recursive=False,
                 patterns='**',
                 chunk_size=4096):

        self.patterns = []
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            if isinstance(pattern, str):
                self.patterns.append(glob_compile(pattern))
            else:
                self.patterns.append(pattern)

        self.directory = os.path.normpath(directory)
        self.recursive = recursive

    def genNames(self):
        """ Returns the file paths inside self.directory
            with associated opened file descriptors """
        names = []

        added_directories = set()

        def add_directory(short_path):
            # Do not continue if this directory has already been added
            if short_path in added_directories:
                return

            # Scan for first super-directory that has already been added
            dir_base  = short_path
            dir_parts = []
            while dir_base:
                dir_base, dir_name = os.path.split(dir_base)
                dir_parts.append(dir_name)
                if dir_base in added_directories:
                    break

            # Add missing intermediate directory nodes in the right order
            while dir_parts:
                dir_base = os.path.join(dir_base, dir_parts.pop())

                # Create an empty, fake file to represent the directory
                mock_file = io.StringIO()
                mock_file.write(u'')
                # Add this directory to those that will be sent
                names.append(('files',
                             (dir_base, mock_file, 'application/x-directory')))
                # Remember that this directory has already been sent
                added_directories.add(dir_base)

        def add_file(short_path, full_path):
            try:
                # Always add files in wildcard directories
                names.append(('files', (short_name,
                                        open(full_path, 'rb'),
                                        'application/octet-stream')))
            except OSError:
                # File might have disappeared between `os.walk()` and `open()`
                pass

        def match_short_path(short_path):
            # Remove initial path component so that all files are based in
            # the target directory itself (not one level above)
            if os.sep in short_path:
                path = short_path.split(os.sep, 1)[1]
            else:
                return False

            # Convert all path seperators to POSIX style
            path = path.replace(os.sep, '/')

            # Do the matching and the simplified path
            for pattern in self.patterns:
                if pattern.match(path):
                    return True
            return False

        # Identify the unecessary portion of the relative path
        truncate = os.path.dirname(self.directory)
        # Traverse the filesystem downward from the target directory's uri
        # Errors: `os.walk()` will simply return an empty generator if the
        #         target directory does not exist.
        wildcard_directories = set()
        for curr_dir, _, files in os.walk(self.directory):
            # find the path relative to the directory being added
            if len(truncate) > 0:
                _, _, short_path = curr_dir.partition(truncate)
            else:
                short_path = curr_dir
            # remove leading / or \ if it is present
            if short_path.startswith(os.sep):
                short_path = short_path[1:]

            wildcard_directory = False
            if os.path.split(short_path)[0] in wildcard_directories:
                # Parent directory has matched a pattern, all sub-nodes should
                # be added too
                wildcard_directories.add(short_path)
                wildcard_directory = True
            else:
                # Check if directory path matches one of the patterns
                if match_short_path(short_path):
                    # Directory matched pattern and it should therefor
                    # be added along with all of its contents
                    wildcard_directories.add(short_path)
                    wildcard_directory = True

            # Always add directories within wildcard directories - even if they
            # are empty
            if wildcard_directory:
                add_directory(short_path)

            # Iterate across the files in the current directory
            for filename in files:
                # Find the filename relative to the directory being added
                short_name = os.path.join(short_path, filename)
                filepath = os.path.join(curr_dir, filename)

                if wildcard_directory:
                    # Always add files in wildcard directories
                    add_file(short_name, filepath)
                else:
                    # Add file (and all missing intermediary directories)
                    # if it matches one of the patterns
                    if match_short_path(short_name):
                        add_directory(short_path)
                        add_file(short_name, filepath)

        return names
