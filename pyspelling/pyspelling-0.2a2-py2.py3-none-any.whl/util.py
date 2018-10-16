"""Utilities."""
from __future__ import unicode_literals
import subprocess
import sys
import string
import random
import re
from collections import namedtuple

RE_LAST_SPACE_IN_CHUNK = re.compile(rb'(\s+)(?=\S+\Z)')


def get_process(cmd):
    """Get a command process."""

    if sys.platform.startswith('win'):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        process = subprocess.Popen(
            cmd,
            startupinfo=startupinfo,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=False
        )
    else:
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.PIPE,
            shell=False
        )
    return process


def get_process_output(process):
    """Get the output from the process."""

    output = process.communicate()
    returncode = process.returncode

    if returncode != 0:
        raise RuntimeError("Runtime Error: %s" % (output[0].rstrip().decode('utf-8')))

    return output[0].decode('utf-8')


def call(cmd, input_file=None, input_text=None):
    """Call with arguments."""

    process = get_process(cmd)

    if input_file is not None:
        with open(input_file, 'rb') as f:
            process.stdin.write(f.read())
    if input_text is not None:
        process.stdin.write(input_text)

    return get_process_output(process)


def call_spellchecker(cmd, input_text):
    """Call spell checker with arguments."""

    process = get_process(cmd)

    if input_text is not None:
        for line in input_text.splitlines():
            # Hunspell truncates lines at 0x1fff (at least on Windows this has been observed)
            # Avoid trunctation by chunking the line on white space and inserting a new line to break it.
            offset = 0
            end = len(line)
            while True:
                chunk_end = offset + 0x1fff
                m = None if chunk_end >= end else RE_LAST_SPACE_IN_CHUNK.search(line, offset, chunk_end)
                if m:
                    chunk_end = m.start(1)
                    chunk = line[offset:m.start(1)]
                    offset = m.end(1)
                else:
                    chunk = line[offset:chunk_end]
                    offset = chunk_end
                process.stdin.write(chunk + b'\n')
                if offset >= end:
                    break

    return get_process_output(process)


def random_name_gen(size=6):
    """Generate a random python attribute name."""

    return ''.join(
        [random.choice(string.ascii_uppercase)] +
        [random.choice(string.ascii_uppercase + string.digits) for i in range(size - 1)]
    ) if size > 0 else ''


class Results(namedtuple('Results', ['words', 'context', 'category', 'error'])):
    """Results."""

    def __new__(cls, words, context, category, error=None):
        """Allow defaults."""

        return super(Results, cls).__new__(cls, words, context, category, error)
