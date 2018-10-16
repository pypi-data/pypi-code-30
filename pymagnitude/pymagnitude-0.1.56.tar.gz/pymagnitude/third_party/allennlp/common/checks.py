u"""
Functions and exceptions for checking that
AllenNLP and its models are configured correctly.
"""


from __future__ import absolute_import
import logging

from torch import cuda

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name


class ConfigurationError(Exception):
    u"""
    The exception raised by any AllenNLP object when it's misconfigured
    (e.g. missing properties, invalid properties, unknown properties).
    """

    def __init__(self, message):
        super(ConfigurationError, self).__init__()
        self.message = message

    def __str__(self):
        return repr(self.message)


def log_pytorch_version_info():
    import torch
    logger.info(u"Pytorch version: %s", torch.__version__)


def check_dimensions_match(dimension_1     ,
                           dimension_2     ,
                           dim_1_name     ,
                           dim_2_name     )        :
    if dimension_1 != dimension_2:
        raise ConfigurationError("{dim_1_name} must match {dim_2_name}, but got {dimension_1} "
                                 "and {dimension_2} instead")


def check_for_gpu(device_id     ):
    if device_id is not None and device_id >= cuda.device_count():
        raise ConfigurationError(u"Experiment specified a GPU but none is available;"
                                 u" if you want to run on CPU use the override"
                                 u" 'trainer.cuda_device=-1' in the json config file.")
