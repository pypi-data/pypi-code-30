# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock_day.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock_day.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0fstock_day.proto\"\xb2\x01\n\tstock_day\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x02\x12\x0c\n\x04high\x18\x03 \x01(\x02\x12\x0b\n\x03low\x18\x04 \x01(\x02\x12\r\n\x05\x63lose\x18\x05 \x01(\x02\x12\x0e\n\x06volume\x18\x06 \x01(\x02\x12\x0c\n\x04\x64\x61te\x18\x07 \x01(\t\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x02\x12\x12\n\ndate_stamp\x18\t \x01(\t\x12\x10\n\x08preclose\x18\n \x01(\x02\x12\x0b\n\x03\x61\x64j\x18\x0b \x01(\x02\x32\x31\n\rSearchService\x12 \n\x06Search\x12\n.stock_day\x1a\n.stock_dayb\x06proto3')
)




_STOCK_DAY = _descriptor.Descriptor(
  name='stock_day',
  full_name='stock_day',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='stock_day.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='stock_day.open', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='stock_day.high', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='stock_day.low', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='stock_day.close', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='stock_day.volume', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='stock_day.date', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='stock_day.amount', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_stamp', full_name='stock_day.date_stamp', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='preclose', full_name='stock_day.preclose', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='adj', full_name='stock_day.adj', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=198,
)

DESCRIPTOR.message_types_by_name['stock_day'] = _STOCK_DAY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

stock_day = _reflection.GeneratedProtocolMessageType('stock_day', (_message.Message,), dict(
  DESCRIPTOR = _STOCK_DAY,
  __module__ = 'stock_day_pb2'
  # @@protoc_insertion_point(class_scope:stock_day)
  ))
_sym_db.RegisterMessage(stock_day)



_SEARCHSERVICE = _descriptor.ServiceDescriptor(
  name='SearchService',
  full_name='SearchService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=200,
  serialized_end=249,
  methods=[
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='SearchService.Search',
    index=0,
    containing_service=None,
    input_type=_STOCK_DAY,
    output_type=_STOCK_DAY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SEARCHSERVICE)

DESCRIPTOR.services_by_name['SearchService'] = _SEARCHSERVICE

# @@protoc_insertion_point(module_scope)
