# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ImportReadingImportProfileDTO(Model):
    """ImportReadingImportProfileDTO.

    :param channel_interval_in_seconds: The interval of the readings in
     seconds
    :type channel_interval_in_seconds: int
    :param delimiter: The string that represents how the file contents are
     delimited.  Valid options are "\\t" for tab, " " for space and "," for
     comma. <span class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 1 and 2 characters</span> <span
     class='property-internal'>One of 	,  , , </span>
    :type delimiter: str
    :param number_of_header_rows: Number of header rows before the data begins
     <span class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 1 and 2147483647</span>
    :type number_of_header_rows: int
    :param timestamp_column_number: The number of the column that holds the
     timestamp <span class='property-internal'>Must be between 1 and
     2147483647</span>
    :type timestamp_column_number: int
    :param timestamp_format: The format for the timestamp of the readings. An
     example is MM/dd/yyyy mm:hh:ss:zzz
    :type timestamp_format: str
    :param date_column_number: The number of the column that holds the date
     <span class='property-internal'>Must be between 1 and 2147483647</span>
    :type date_column_number: int
    :param time_column_number: The number of the column that holds the time
     <span class='property-internal'>Must be between 1 and 2147483647</span>
    :type time_column_number: int
    :param date_format: The format for the date of the readings. An example is
     MM/dd/yyyy
    :type date_format: str
    :param time_format: The format for the time of the readings. An example is
     mm:hh:ss:zzz
    :type time_format: str
    :param time_zone_id: The time zone for the readings
    :type time_zone_id: int
    :param meter_import_id_column_number: The number of the column that holds
     the meter import identifier <span class='property-internal'>Must be
     between 1 and 2147483647</span>
    :type meter_import_id_column_number: int
    :param channel_import_id_column_number: The number of the column that
     holds the channel import identifier <span class='property-internal'>Must
     be between 1 and 2147483647</span>
    :type channel_import_id_column_number: int
    :param number_of_columns: The minimum number of columns in the import
     sheet <span class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 1 and 2147483647</span>
    :type number_of_columns: int
    :param data_mapping: A list of columns from the import sheet with their
     observation type and unit
    :type data_mapping:
     list[~energycap.sdk.models.ImportReadingImportProfileColumn]
    """

    _validation = {
        'delimiter': {'required': True, 'max_length': 2, 'min_length': 1},
        'number_of_header_rows': {'required': True, 'maximum': 2147483647, 'minimum': 1},
        'timestamp_column_number': {'maximum': 2147483647, 'minimum': 1},
        'date_column_number': {'maximum': 2147483647, 'minimum': 1},
        'time_column_number': {'maximum': 2147483647, 'minimum': 1},
        'meter_import_id_column_number': {'maximum': 2147483647, 'minimum': 1},
        'channel_import_id_column_number': {'maximum': 2147483647, 'minimum': 1},
        'number_of_columns': {'required': True, 'maximum': 2147483647, 'minimum': 1},
    }

    _attribute_map = {
        'channel_interval_in_seconds': {'key': 'channelIntervalInSeconds', 'type': 'int'},
        'delimiter': {'key': 'delimiter', 'type': 'str'},
        'number_of_header_rows': {'key': 'numberOfHeaderRows', 'type': 'int'},
        'timestamp_column_number': {'key': 'timestampColumnNumber', 'type': 'int'},
        'timestamp_format': {'key': 'timestampFormat', 'type': 'str'},
        'date_column_number': {'key': 'dateColumnNumber', 'type': 'int'},
        'time_column_number': {'key': 'timeColumnNumber', 'type': 'int'},
        'date_format': {'key': 'dateFormat', 'type': 'str'},
        'time_format': {'key': 'timeFormat', 'type': 'str'},
        'time_zone_id': {'key': 'timeZoneId', 'type': 'int'},
        'meter_import_id_column_number': {'key': 'meterImportIdColumnNumber', 'type': 'int'},
        'channel_import_id_column_number': {'key': 'channelImportIdColumnNumber', 'type': 'int'},
        'number_of_columns': {'key': 'numberOfColumns', 'type': 'int'},
        'data_mapping': {'key': 'dataMapping', 'type': '[ImportReadingImportProfileColumn]'},
    }

    def __init__(self, delimiter, number_of_header_rows, number_of_columns, channel_interval_in_seconds=None, timestamp_column_number=None, timestamp_format=None, date_column_number=None, time_column_number=None, date_format=None, time_format=None, time_zone_id=None, meter_import_id_column_number=None, channel_import_id_column_number=None, data_mapping=None):
        super(ImportReadingImportProfileDTO, self).__init__()
        self.channel_interval_in_seconds = channel_interval_in_seconds
        self.delimiter = delimiter
        self.number_of_header_rows = number_of_header_rows
        self.timestamp_column_number = timestamp_column_number
        self.timestamp_format = timestamp_format
        self.date_column_number = date_column_number
        self.time_column_number = time_column_number
        self.date_format = date_format
        self.time_format = time_format
        self.time_zone_id = time_zone_id
        self.meter_import_id_column_number = meter_import_id_column_number
        self.channel_import_id_column_number = channel_import_id_column_number
        self.number_of_columns = number_of_columns
        self.data_mapping = data_mapping
