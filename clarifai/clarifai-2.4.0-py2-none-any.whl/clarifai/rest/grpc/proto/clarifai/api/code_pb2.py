# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/code.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clarifai.rest.grpc.proto.clarifai.api.status import status_pb2 as proto_dot_clarifai_dot_api_dot_status_dot_status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/code.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1dproto/clarifai/api/code.proto\x12\x0c\x63larifai.api\x1a&proto/clarifai/api/status/status.proto\".\n\x14GetStatusCodeRequest\x12\x16\n\x0estatus_code_id\x18\x01 \x01(\t\"\x18\n\x16ListStatusCodesRequest\"G\n\x18SingleStatusCodeResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\"u\n\x17MultiStatusCodeResponse\x12+\n\x06status\x18\x01 \x01(\x0b\x32\x1b.clarifai.api.status.Status\x12-\n\x08statuses\x18\x02 \x03(\x0b\x32\x1b.clarifai.api.status.StatusB$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_status_dot_status__pb2.DESCRIPTOR,])




_GETSTATUSCODEREQUEST = _descriptor.Descriptor(
  name='GetStatusCodeRequest',
  full_name='clarifai.api.GetStatusCodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code_id', full_name='clarifai.api.GetStatusCodeRequest.status_code_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=87,
  serialized_end=133,
)


_LISTSTATUSCODESREQUEST = _descriptor.Descriptor(
  name='ListStatusCodesRequest',
  full_name='clarifai.api.ListStatusCodesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=135,
  serialized_end=159,
)


_SINGLESTATUSCODERESPONSE = _descriptor.Descriptor(
  name='SingleStatusCodeResponse',
  full_name='clarifai.api.SingleStatusCodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.SingleStatusCodeResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=161,
  serialized_end=232,
)


_MULTISTATUSCODERESPONSE = _descriptor.Descriptor(
  name='MultiStatusCodeResponse',
  full_name='clarifai.api.MultiStatusCodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='clarifai.api.MultiStatusCodeResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='clarifai.api.MultiStatusCodeResponse.statuses', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=234,
  serialized_end=351,
)

_SINGLESTATUSCODERESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTISTATUSCODERESPONSE.fields_by_name['status'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
_MULTISTATUSCODERESPONSE.fields_by_name['statuses'].message_type = proto_dot_clarifai_dot_api_dot_status_dot_status__pb2._STATUS
DESCRIPTOR.message_types_by_name['GetStatusCodeRequest'] = _GETSTATUSCODEREQUEST
DESCRIPTOR.message_types_by_name['ListStatusCodesRequest'] = _LISTSTATUSCODESREQUEST
DESCRIPTOR.message_types_by_name['SingleStatusCodeResponse'] = _SINGLESTATUSCODERESPONSE
DESCRIPTOR.message_types_by_name['MultiStatusCodeResponse'] = _MULTISTATUSCODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStatusCodeRequest = _reflection.GeneratedProtocolMessageType('GetStatusCodeRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETSTATUSCODEREQUEST,
  __module__ = 'proto.clarifai.api.code_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.GetStatusCodeRequest)
  ))
_sym_db.RegisterMessage(GetStatusCodeRequest)

ListStatusCodesRequest = _reflection.GeneratedProtocolMessageType('ListStatusCodesRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTSTATUSCODESREQUEST,
  __module__ = 'proto.clarifai.api.code_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.ListStatusCodesRequest)
  ))
_sym_db.RegisterMessage(ListStatusCodesRequest)

SingleStatusCodeResponse = _reflection.GeneratedProtocolMessageType('SingleStatusCodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _SINGLESTATUSCODERESPONSE,
  __module__ = 'proto.clarifai.api.code_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.SingleStatusCodeResponse)
  ))
_sym_db.RegisterMessage(SingleStatusCodeResponse)

MultiStatusCodeResponse = _reflection.GeneratedProtocolMessageType('MultiStatusCodeResponse', (_message.Message,), dict(
  DESCRIPTOR = _MULTISTATUSCODERESPONSE,
  __module__ = 'proto.clarifai.api.code_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.MultiStatusCodeResponse)
  ))
_sym_db.RegisterMessage(MultiStatusCodeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
# @@protoc_insertion_point(module_scope)
