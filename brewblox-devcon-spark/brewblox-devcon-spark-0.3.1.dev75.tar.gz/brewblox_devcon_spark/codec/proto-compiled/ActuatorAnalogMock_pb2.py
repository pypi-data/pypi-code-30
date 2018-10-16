# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorAnalogMock.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActuatorAnalogMock.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x18\x41\x63tuatorAnalogMock.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"\xf9\x01\n\x12\x41\x63tuatorAnalogMock\x12\x1d\n\x07setting\x18\x01 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12!\n\x05value\x18\x02 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12\x15\n\x05valid\x18\x03 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12 \n\nminSetting\x18\x04 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12 \n\nmaxSetting\x18\x05 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x1e\n\x08minValue\x18\x06 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x12\x1e\n\x08maxValue\x18\x07 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 :\x06\x92?\x03H\xb1\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_ACTUATORANALOGMOCK = _descriptor.Descriptor(
  name='ActuatorAnalogMock',
  full_name='blox.ActuatorAnalogMock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.ActuatorAnalogMock.setting', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.ActuatorAnalogMock.value', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid', full_name='blox.ActuatorAnalogMock.valid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minSetting', full_name='blox.ActuatorAnalogMock.minSetting', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxSetting', full_name='blox.ActuatorAnalogMock.maxSetting', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minValue', full_name='blox.ActuatorAnalogMock.minValue', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maxValue', full_name='blox.ActuatorAnalogMock.maxValue', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\222?\003H\261\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=314,
)

DESCRIPTOR.message_types_by_name['ActuatorAnalogMock'] = _ACTUATORANALOGMOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActuatorAnalogMock = _reflection.GeneratedProtocolMessageType('ActuatorAnalogMock', (_message.Message,), dict(
  DESCRIPTOR = _ACTUATORANALOGMOCK,
  __module__ = 'ActuatorAnalogMock_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorAnalogMock)
  ))
_sym_db.RegisterMessage(ActuatorAnalogMock)


_ACTUATORANALOGMOCK.fields_by_name['setting']._options = None
_ACTUATORANALOGMOCK.fields_by_name['value']._options = None
_ACTUATORANALOGMOCK.fields_by_name['valid']._options = None
_ACTUATORANALOGMOCK.fields_by_name['minSetting']._options = None
_ACTUATORANALOGMOCK.fields_by_name['maxSetting']._options = None
_ACTUATORANALOGMOCK.fields_by_name['minValue']._options = None
_ACTUATORANALOGMOCK.fields_by_name['maxValue']._options = None
_ACTUATORANALOGMOCK._options = None
# @@protoc_insertion_point(module_scope)
