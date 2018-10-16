# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/clarifai/api/video.proto

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
  name='proto/clarifai/api/video.proto',
  package='clarifai.api',
  syntax='proto3',
  serialized_pb=_b('\n\x1eproto/clarifai/api/video.proto\x12\x0c\x63larifai.api\"A\n\x05Video\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0e\n\x06\x62\x61se64\x18\x02 \x01(\x0c\x12\x1b\n\x13\x61llow_duplicate_url\x18\x04 \x01(\x08\x42$Z\x03\x61pi\xa2\x02\x04\x43\x41IP\xc2\x02\x01_\xca\x02\x11\x43larifai\\Internalb\x06proto3')
)




_VIDEO = _descriptor.Descriptor(
  name='Video',
  full_name='clarifai.api.Video',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='clarifai.api.Video.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base64', full_name='clarifai.api.Video.base64', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_duplicate_url', full_name='clarifai.api.Video.allow_duplicate_url', index=2,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=48,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['Video'] = _VIDEO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Video = _reflection.GeneratedProtocolMessageType('Video', (_message.Message,), dict(
  DESCRIPTOR = _VIDEO,
  __module__ = 'proto.clarifai.api.video_pb2'
  # @@protoc_insertion_point(class_scope:clarifai.api.Video)
  ))
_sym_db.RegisterMessage(Video)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\003api\242\002\004CAIP\302\002\001_\312\002\021Clarifai\\Internal'))
# @@protoc_insertion_point(module_scope)
