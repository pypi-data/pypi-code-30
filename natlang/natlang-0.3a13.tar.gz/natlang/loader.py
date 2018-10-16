# -*- coding: utf-8 -*-
# Python version: 2/3
#
# Dataset loader for NLP experiments.
# Simon Fraser University
# Jetic Gu
#
#
from __future__ import absolute_import
import os
import sys
import inspect
import unittest
import importlib

from natlang.format import *

__version__ = "0.3a"

supportedList = {
    'tree': tree,
    'txtFiles': txtFiles,
    'txt': txt,
    'AMR': AMR,
    'txtOrTree': txtOrTree,
    'pyCode': pyCode
}


class ParallelDataLoader():
    def __init__(self, srcFormat='txtOrTree', tgtFormat='txtOrTree'):
        self.srcLoader = supportedList[srcFormat].load
        #    importlib.import_module(srcFormat, format).load
        self.tgtLoader = supportedList[tgtFormat].load
        return

    def load(self, fFile, eFile, linesToLoad=sys.maxsize):
        data = zip(self.srcLoader(fFile, linesToLoad),
                   self.tgtLoader(eFile, linesToLoad))
        # Remove incomplete or invalid entries
        data = [(f, e) for f, e in data if f is not None and e is not None]
        data = [(f, e) for f, e in data if len(f) > 0 and len(e) > 0]
        return data
