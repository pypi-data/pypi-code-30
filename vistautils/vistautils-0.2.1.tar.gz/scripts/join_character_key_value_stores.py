#!/usr/bin/env python

"""
Joins multiple character key-value stores into one.

This is useful when recombining the results of a corpus which has been split for parallel
processing.

Currently the input stores are always assumed to be standard zip file stores. This might become
configurable in the future.

The "input_store_list_file" parameter points to a file containing the paths of the stores to join.
The "output" namespace describes the key-value store to output to. See
char_key_value_sink_from_params for details.
"""
import sys
from typing import Set

from vistautils.parameters import Parameters, YAMLParametersLoader
from vistautils.key_value import KeyValueSource, char_key_value_sink_from_params


def main(params: Parameters):
    input_paths = params.path_list_from_file('input_store_list_file',
                                             log_name="input key-value stores")
    keys_written: Set[str] = set()
    with char_key_value_sink_from_params('output', params,
                                         eval_context=locals()) as out:
        for input_path in input_paths:
            with KeyValueSource.zip_character_source(input_path) as inp:
                for key in inp.keys():
                    if key in keys_written:
                        raise RuntimeError("Duplicate key: {}".format(key))
                    keys_written.add(key)
                    out[key] = inp[key]


if __name__ == '__main__':
    main(YAMLParametersLoader().load(sys.argv[1]))
