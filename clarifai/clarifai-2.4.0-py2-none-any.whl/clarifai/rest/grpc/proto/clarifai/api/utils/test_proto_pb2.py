# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/utils/test_proto.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from clarifai.rest.grpc.proto.clarifai.api.utils import extensions_pb2 as proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/clarifai/api/utils/test_proto.proto',
  package='clarifai.api.utils',
  syntax='proto3',
  serialized_pb=_b('\n)proto/clarifai/api/utils/test_proto.proto\x12\x12\x63larifai.api.utils\x1a)proto/clarifai/api/utils/extensions.proto\"n\n\tTestProto\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x07message\x18\x02 \x01(\tB\x17\x80\xb5\x18\x01\x8a\xb5\x18\x0fprotos are cool\x12\x16\n\x05value\x18\x03 \x01(\x01\x42\x07\xd5\xb5\x18\x00\x00\x80?\x12\x13\n\x0bimage_bytes\x18\x04 \x01(\x0c\x42,Z\x05utils\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x17\x43larifai\\Internal\\Utilsb\x06proto3')
  ,
  dependencies=[proto_dot_clarifai_dot_api_dot_utils_dot_extensions__pb2.DESCRIPTOR,])




_TESTPROTO = _descriptor.Descriptor(
  name='TestProto',
  full_name='clarifai.api.utils.TestProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='clarifai.api.utils.TestProto.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='clarifai.api.utils.TestProto.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001\212\265\030\017protos are cool')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='clarifai.api.utils.TestProto.value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\325\265\030\000\000\200?')), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_bytes', full_name='clarifai.api.utils.TestProto.image_bytes', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=108,
  serialized_end=218,
)

DESCRIPTOR.message_types_by_name['TestProto'] = _TESTPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestProto = _reflection.GeneratedProtocolMessageType('TestProto', (_message.Message,), dict(
  DESCRIPTOR = _TESTPROTO,
  __module__ = 'proto.clarifai.api.utils.test_proto_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.utils.TestProto)
  ))
_sym_db.RegisterMessage(TestProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\005utils\242\002\004CAIP\302\002\001_\312\002\027Clarifai\\Internal\\Utils'))
_TESTPROTO.fields_by_name['message'].has_options = True
_TESTPROTO.fields_by_name['message']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\200\265\030\001\212\265\030\017protos are cool'))
_TESTPROTO.fields_by_name['value'].has_options = True
_TESTPROTO.fields_by_name['value']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\325\265\030\000\000\200?'))
# @@protoc_insertion_point(module_scope)
