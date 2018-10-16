# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ReadingReadingDTOObservationDTO(Model):
    """ReadingReadingDTOObservationDTO.

    :param time: The date and time of the reading
    :type time: datetime
    :param value: The value of the reading
    :type value: float
    :param estimated: Indicates if the reading is estimated
    :type estimated: bool
    :param note: A note pertaining to the reading
    :type note: str
    """

    _attribute_map = {
        'time': {'key': 'time', 'type': 'iso-8601'},
        'value': {'key': 'value', 'type': 'float'},
        'estimated': {'key': 'estimated', 'type': 'bool'},
        'note': {'key': 'note', 'type': 'str'},
    }

    def __init__(self, time=None, value=None, estimated=None, note=None):
        super(ReadingReadingDTOObservationDTO, self).__init__()
        self.time = time
        self.value = value
        self.estimated = estimated
        self.note = note
