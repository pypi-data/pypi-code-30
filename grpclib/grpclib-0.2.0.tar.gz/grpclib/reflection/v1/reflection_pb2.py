# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: grpclib/reflection/v1/reflection.proto

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
  name='grpclib/reflection/v1/reflection.proto',
  package='grpc.reflection.v1',
  syntax='proto3',
  serialized_pb=_b('\n&grpclib/reflection/v1/reflection.proto\x12\x12grpc.reflection.v1\"\x85\x02\n\x17ServerReflectionRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x1a\n\x10\x66ile_by_filename\x18\x03 \x01(\tH\x00\x12 \n\x16\x66ile_containing_symbol\x18\x04 \x01(\tH\x00\x12I\n\x19\x66ile_containing_extension\x18\x05 \x01(\x0b\x32$.grpc.reflection.v1.ExtensionRequestH\x00\x12\'\n\x1d\x61ll_extension_numbers_of_type\x18\x06 \x01(\tH\x00\x12\x17\n\rlist_services\x18\x07 \x01(\tH\x00\x42\x11\n\x0fmessage_request\"E\n\x10\x45xtensionRequest\x12\x17\n\x0f\x63ontaining_type\x18\x01 \x01(\t\x12\x18\n\x10\x65xtension_number\x18\x02 \x01(\x05\"\xb8\x03\n\x18ServerReflectionResponse\x12\x12\n\nvalid_host\x18\x01 \x01(\t\x12\x45\n\x10original_request\x18\x02 \x01(\x0b\x32+.grpc.reflection.v1.ServerReflectionRequest\x12N\n\x18\x66ile_descriptor_response\x18\x04 \x01(\x0b\x32*.grpc.reflection.v1.FileDescriptorResponseH\x00\x12U\n\x1e\x61ll_extension_numbers_response\x18\x05 \x01(\x0b\x32+.grpc.reflection.v1.ExtensionNumberResponseH\x00\x12I\n\x16list_services_response\x18\x06 \x01(\x0b\x32\'.grpc.reflection.v1.ListServiceResponseH\x00\x12;\n\x0e\x65rror_response\x18\x07 \x01(\x0b\x32!.grpc.reflection.v1.ErrorResponseH\x00\x42\x12\n\x10message_response\"7\n\x16\x46ileDescriptorResponse\x12\x1d\n\x15\x66ile_descriptor_proto\x18\x01 \x03(\x0c\"K\n\x17\x45xtensionNumberResponse\x12\x16\n\x0e\x62\x61se_type_name\x18\x01 \x01(\t\x12\x18\n\x10\x65xtension_number\x18\x02 \x03(\x05\"K\n\x13ListServiceResponse\x12\x34\n\x07service\x18\x01 \x03(\x0b\x32#.grpc.reflection.v1.ServiceResponse\"\x1f\n\x0fServiceResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\":\n\rErrorResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t2\x89\x01\n\x10ServerReflection\x12u\n\x14ServerReflectionInfo\x12+.grpc.reflection.v1.ServerReflectionRequest\x1a,.grpc.reflection.v1.ServerReflectionResponse(\x01\x30\x01\x42\x66\n\x15io.grpc.reflection.v1B\x15ServerReflectionProtoP\x01Z4google.golang.org/grpc/reflection/grpc_reflection_v1b\x06proto3')
)




_SERVERREFLECTIONREQUEST = _descriptor.Descriptor(
  name='ServerReflectionRequest',
  full_name='grpc.reflection.v1.ServerReflectionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='host', full_name='grpc.reflection.v1.ServerReflectionRequest.host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_by_filename', full_name='grpc.reflection.v1.ServerReflectionRequest.file_by_filename', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_containing_symbol', full_name='grpc.reflection.v1.ServerReflectionRequest.file_containing_symbol', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_containing_extension', full_name='grpc.reflection.v1.ServerReflectionRequest.file_containing_extension', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_extension_numbers_of_type', full_name='grpc.reflection.v1.ServerReflectionRequest.all_extension_numbers_of_type', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_services', full_name='grpc.reflection.v1.ServerReflectionRequest.list_services', index=5,
      number=7, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='message_request', full_name='grpc.reflection.v1.ServerReflectionRequest.message_request',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=63,
  serialized_end=324,
)


_EXTENSIONREQUEST = _descriptor.Descriptor(
  name='ExtensionRequest',
  full_name='grpc.reflection.v1.ExtensionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='containing_type', full_name='grpc.reflection.v1.ExtensionRequest.containing_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_number', full_name='grpc.reflection.v1.ExtensionRequest.extension_number', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=326,
  serialized_end=395,
)


_SERVERREFLECTIONRESPONSE = _descriptor.Descriptor(
  name='ServerReflectionResponse',
  full_name='grpc.reflection.v1.ServerReflectionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid_host', full_name='grpc.reflection.v1.ServerReflectionResponse.valid_host', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='original_request', full_name='grpc.reflection.v1.ServerReflectionResponse.original_request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_descriptor_response', full_name='grpc.reflection.v1.ServerReflectionResponse.file_descriptor_response', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_extension_numbers_response', full_name='grpc.reflection.v1.ServerReflectionResponse.all_extension_numbers_response', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_services_response', full_name='grpc.reflection.v1.ServerReflectionResponse.list_services_response', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_response', full_name='grpc.reflection.v1.ServerReflectionResponse.error_response', index=5,
      number=7, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='message_response', full_name='grpc.reflection.v1.ServerReflectionResponse.message_response',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=398,
  serialized_end=838,
)


_FILEDESCRIPTORRESPONSE = _descriptor.Descriptor(
  name='FileDescriptorResponse',
  full_name='grpc.reflection.v1.FileDescriptorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_descriptor_proto', full_name='grpc.reflection.v1.FileDescriptorResponse.file_descriptor_proto', index=0,
      number=1, type=12, cpp_type=9, label=3,
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
  serialized_start=840,
  serialized_end=895,
)


_EXTENSIONNUMBERRESPONSE = _descriptor.Descriptor(
  name='ExtensionNumberResponse',
  full_name='grpc.reflection.v1.ExtensionNumberResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_type_name', full_name='grpc.reflection.v1.ExtensionNumberResponse.base_type_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extension_number', full_name='grpc.reflection.v1.ExtensionNumberResponse.extension_number', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=897,
  serialized_end=972,
)


_LISTSERVICERESPONSE = _descriptor.Descriptor(
  name='ListServiceResponse',
  full_name='grpc.reflection.v1.ListServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='grpc.reflection.v1.ListServiceResponse.service', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=974,
  serialized_end=1049,
)


_SERVICERESPONSE = _descriptor.Descriptor(
  name='ServiceResponse',
  full_name='grpc.reflection.v1.ServiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.reflection.v1.ServiceResponse.name', index=0,
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
  serialized_start=1051,
  serialized_end=1082,
)


_ERRORRESPONSE = _descriptor.Descriptor(
  name='ErrorResponse',
  full_name='grpc.reflection.v1.ErrorResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='grpc.reflection.v1.ErrorResponse.error_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_message', full_name='grpc.reflection.v1.ErrorResponse.error_message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1084,
  serialized_end=1142,
)

_SERVERREFLECTIONREQUEST.fields_by_name['file_containing_extension'].message_type = _EXTENSIONREQUEST
_SERVERREFLECTIONREQUEST.oneofs_by_name['message_request'].fields.append(
  _SERVERREFLECTIONREQUEST.fields_by_name['file_by_filename'])
_SERVERREFLECTIONREQUEST.fields_by_name['file_by_filename'].containing_oneof = _SERVERREFLECTIONREQUEST.oneofs_by_name['message_request']
_SERVERREFLECTIONREQUEST.oneofs_by_name['message_request'].fields.append(
  _SERVERREFLECTIONREQUEST.fields_by_name['file_containing_symbol'])
_SERVERREFLECTIONREQUEST.fields_by_name['file_containing_symbol'].containing_oneof = _SERVERREFLECTIONREQUEST.oneofs_by_name['message_request']
_SERVERREFLECTIONREQUEST.oneofs_by_name['message_request'].fields.append(
  _SERVERREFLECTIONREQUEST.fields_by_name['file_containing_extension'])
_SERVERREFLECTIONREQUEST.fields_by_name['file_containing_extension'].containing_oneof = _SERVERREFLECTIONREQUEST.oneofs_by_name['message_request']
_SERVERREFLECTIONREQUEST.oneofs_by_name['message_request'].fields.append(
  _SERVERREFLECTIONREQUEST.fields_by_name['all_extension_numbers_of_type'])
_SERVERREFLECTIONREQUEST.fields_by_name['all_extension_numbers_of_type'].containing_oneof = _SERVERREFLECTIONREQUEST.oneofs_by_name['message_request']
_SERVERREFLECTIONREQUEST.oneofs_by_name['message_request'].fields.append(
  _SERVERREFLECTIONREQUEST.fields_by_name['list_services'])
_SERVERREFLECTIONREQUEST.fields_by_name['list_services'].containing_oneof = _SERVERREFLECTIONREQUEST.oneofs_by_name['message_request']
_SERVERREFLECTIONRESPONSE.fields_by_name['original_request'].message_type = _SERVERREFLECTIONREQUEST
_SERVERREFLECTIONRESPONSE.fields_by_name['file_descriptor_response'].message_type = _FILEDESCRIPTORRESPONSE
_SERVERREFLECTIONRESPONSE.fields_by_name['all_extension_numbers_response'].message_type = _EXTENSIONNUMBERRESPONSE
_SERVERREFLECTIONRESPONSE.fields_by_name['list_services_response'].message_type = _LISTSERVICERESPONSE
_SERVERREFLECTIONRESPONSE.fields_by_name['error_response'].message_type = _ERRORRESPONSE
_SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response'].fields.append(
  _SERVERREFLECTIONRESPONSE.fields_by_name['file_descriptor_response'])
_SERVERREFLECTIONRESPONSE.fields_by_name['file_descriptor_response'].containing_oneof = _SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response']
_SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response'].fields.append(
  _SERVERREFLECTIONRESPONSE.fields_by_name['all_extension_numbers_response'])
_SERVERREFLECTIONRESPONSE.fields_by_name['all_extension_numbers_response'].containing_oneof = _SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response']
_SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response'].fields.append(
  _SERVERREFLECTIONRESPONSE.fields_by_name['list_services_response'])
_SERVERREFLECTIONRESPONSE.fields_by_name['list_services_response'].containing_oneof = _SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response']
_SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response'].fields.append(
  _SERVERREFLECTIONRESPONSE.fields_by_name['error_response'])
_SERVERREFLECTIONRESPONSE.fields_by_name['error_response'].containing_oneof = _SERVERREFLECTIONRESPONSE.oneofs_by_name['message_response']
_LISTSERVICERESPONSE.fields_by_name['service'].message_type = _SERVICERESPONSE
DESCRIPTOR.message_types_by_name['ServerReflectionRequest'] = _SERVERREFLECTIONREQUEST
DESCRIPTOR.message_types_by_name['ExtensionRequest'] = _EXTENSIONREQUEST
DESCRIPTOR.message_types_by_name['ServerReflectionResponse'] = _SERVERREFLECTIONRESPONSE
DESCRIPTOR.message_types_by_name['FileDescriptorResponse'] = _FILEDESCRIPTORRESPONSE
DESCRIPTOR.message_types_by_name['ExtensionNumberResponse'] = _EXTENSIONNUMBERRESPONSE
DESCRIPTOR.message_types_by_name['ListServiceResponse'] = _LISTSERVICERESPONSE
DESCRIPTOR.message_types_by_name['ServiceResponse'] = _SERVICERESPONSE
DESCRIPTOR.message_types_by_name['ErrorResponse'] = _ERRORRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerReflectionRequest = _reflection.GeneratedProtocolMessageType('ServerReflectionRequest', (_message.Message,), dict(
  DESCRIPTOR = _SERVERREFLECTIONREQUEST,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ServerReflectionRequest)
  ))
_sym_db.RegisterMessage(ServerReflectionRequest)

ExtensionRequest = _reflection.GeneratedProtocolMessageType('ExtensionRequest', (_message.Message,), dict(
  DESCRIPTOR = _EXTENSIONREQUEST,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ExtensionRequest)
  ))
_sym_db.RegisterMessage(ExtensionRequest)

ServerReflectionResponse = _reflection.GeneratedProtocolMessageType('ServerReflectionResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERREFLECTIONRESPONSE,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ServerReflectionResponse)
  ))
_sym_db.RegisterMessage(ServerReflectionResponse)

FileDescriptorResponse = _reflection.GeneratedProtocolMessageType('FileDescriptorResponse', (_message.Message,), dict(
  DESCRIPTOR = _FILEDESCRIPTORRESPONSE,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.FileDescriptorResponse)
  ))
_sym_db.RegisterMessage(FileDescriptorResponse)

ExtensionNumberResponse = _reflection.GeneratedProtocolMessageType('ExtensionNumberResponse', (_message.Message,), dict(
  DESCRIPTOR = _EXTENSIONNUMBERRESPONSE,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ExtensionNumberResponse)
  ))
_sym_db.RegisterMessage(ExtensionNumberResponse)

ListServiceResponse = _reflection.GeneratedProtocolMessageType('ListServiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTSERVICERESPONSE,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ListServiceResponse)
  ))
_sym_db.RegisterMessage(ListServiceResponse)

ServiceResponse = _reflection.GeneratedProtocolMessageType('ServiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVICERESPONSE,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ServiceResponse)
  ))
_sym_db.RegisterMessage(ServiceResponse)

ErrorResponse = _reflection.GeneratedProtocolMessageType('ErrorResponse', (_message.Message,), dict(
  DESCRIPTOR = _ERRORRESPONSE,
  __module__ = 'grpclib.reflection.v1.reflection_pb2'
  # @@protoc_insertion_point(class_scope:grpc.reflection.v1.ErrorResponse)
  ))
_sym_db.RegisterMessage(ErrorResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025io.grpc.reflection.v1B\025ServerReflectionProtoP\001Z4google.golang.org/grpc/reflection/grpc_reflection_v1'))

_SERVERREFLECTION = _descriptor.ServiceDescriptor(
  name='ServerReflection',
  full_name='grpc.reflection.v1.ServerReflection',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1145,
  serialized_end=1282,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServerReflectionInfo',
    full_name='grpc.reflection.v1.ServerReflection.ServerReflectionInfo',
    index=0,
    containing_service=None,
    input_type=_SERVERREFLECTIONREQUEST,
    output_type=_SERVERREFLECTIONRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVERREFLECTION)

DESCRIPTOR.services_by_name['ServerReflection'] = _SERVERREFLECTION

# @@protoc_insertion_point(module_scope)
