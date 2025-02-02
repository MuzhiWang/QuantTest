# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TdxReader.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TdxReader.proto',
  package='tdxreader',
  syntax='proto3',
  serialized_options=b'\n\022muzwang.tdx_readerB\016TdxReaderProtoP\001\242\002\003TDX',
  serialized_pb=b'\n\x0fTdxReader.proto\x12\ttdxreader\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"M\n\x12ReadTdxFileRequest\x12\x10\n\x08\x66ilePath\x18\x01 \x01(\t\x12%\n\x06metric\x18\x02 \x01(\x0e\x32\x15.tdxreader.DateMetric\"u\n\tStockData\x12\x10\n\x08\x64\x61teTime\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x01\x12\x0e\n\x06volume\x18\x07 \x01(\x01\"1\n\x0bTdxFileData\x12\"\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x14.tdxreader.StockData*C\n\nDateMetric\x12\r\n\tUNDEFINED\x10\x00\x12\x0b\n\x07ONE_MIN\x10\x01\x12\x0c\n\x08\x46IVE_MIN\x10\x02\x12\x0b\n\x07ONE_DAY\x10\x03\x32\x8e\x01\n\tTdxReader\x12\x39\n\x05Hello\x12\x17.tdxreader.HelloRequest\x1a\x15.tdxreader.HelloReply\"\x00\x12\x46\n\x0bReadTdxFile\x12\x1d.tdxreader.ReadTdxFileRequest\x1a\x16.tdxreader.TdxFileData\"\x00\x42,\n\x12muzwang.tdx_readerB\x0eTdxReaderProtoP\x01\xa2\x02\x03TDXb\x06proto3'
)

_DATEMETRIC = _descriptor.EnumDescriptor(
  name='DateMetric',
  full_name='tdxreader.DateMetric',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_MIN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIVE_MIN', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ONE_DAY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=340,
  serialized_end=407,
)
_sym_db.RegisterEnumDescriptor(_DATEMETRIC)

DateMetric = enum_type_wrapper.EnumTypeWrapper(_DATEMETRIC)
UNDEFINED = 0
ONE_MIN = 1
FIVE_MIN = 2
ONE_DAY = 3



_HELLOREQUEST = _descriptor.Descriptor(
  name='HelloRequest',
  full_name='tdxreader.HelloRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tdxreader.HelloRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=58,
)


_HELLOREPLY = _descriptor.Descriptor(
  name='HelloReply',
  full_name='tdxreader.HelloReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tdxreader.HelloReply.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=89,
)


_READTDXFILEREQUEST = _descriptor.Descriptor(
  name='ReadTdxFileRequest',
  full_name='tdxreader.ReadTdxFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='filePath', full_name='tdxreader.ReadTdxFileRequest.filePath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric', full_name='tdxreader.ReadTdxFileRequest.metric', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=168,
)


_STOCKDATA = _descriptor.Descriptor(
  name='StockData',
  full_name='tdxreader.StockData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dateTime', full_name='tdxreader.StockData.dateTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='tdxreader.StockData.open', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='tdxreader.StockData.high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='tdxreader.StockData.low', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='tdxreader.StockData.close', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='tdxreader.StockData.amount', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='tdxreader.StockData.volume', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=287,
)


_TDXFILEDATA = _descriptor.Descriptor(
  name='TdxFileData',
  full_name='tdxreader.TdxFileData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='tdxreader.TdxFileData.data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=338,
)

_READTDXFILEREQUEST.fields_by_name['metric'].enum_type = _DATEMETRIC
_TDXFILEDATA.fields_by_name['data'].message_type = _STOCKDATA
DESCRIPTOR.message_types_by_name['HelloRequest'] = _HELLOREQUEST
DESCRIPTOR.message_types_by_name['HelloReply'] = _HELLOREPLY
DESCRIPTOR.message_types_by_name['ReadTdxFileRequest'] = _READTDXFILEREQUEST
DESCRIPTOR.message_types_by_name['StockData'] = _STOCKDATA
DESCRIPTOR.message_types_by_name['TdxFileData'] = _TDXFILEDATA
DESCRIPTOR.enum_types_by_name['DateMetric'] = _DATEMETRIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'TdxReader_pb2'
  # @@protoc_insertion_point(class_scope:tdxreader.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'TdxReader_pb2'
  # @@protoc_insertion_point(class_scope:tdxreader.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

ReadTdxFileRequest = _reflection.GeneratedProtocolMessageType('ReadTdxFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _READTDXFILEREQUEST,
  '__module__' : 'TdxReader_pb2'
  # @@protoc_insertion_point(class_scope:tdxreader.ReadTdxFileRequest)
  })
_sym_db.RegisterMessage(ReadTdxFileRequest)

StockData = _reflection.GeneratedProtocolMessageType('StockData', (_message.Message,), {
  'DESCRIPTOR' : _STOCKDATA,
  '__module__' : 'TdxReader_pb2'
  # @@protoc_insertion_point(class_scope:tdxreader.StockData)
  })
_sym_db.RegisterMessage(StockData)

TdxFileData = _reflection.GeneratedProtocolMessageType('TdxFileData', (_message.Message,), {
  'DESCRIPTOR' : _TDXFILEDATA,
  '__module__' : 'TdxReader_pb2'
  # @@protoc_insertion_point(class_scope:tdxreader.TdxFileData)
  })
_sym_db.RegisterMessage(TdxFileData)


DESCRIPTOR._options = None

_TDXREADER = _descriptor.ServiceDescriptor(
  name='TdxReader',
  full_name='tdxreader.TdxReader',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=410,
  serialized_end=552,
  methods=[
  _descriptor.MethodDescriptor(
    name='Hello',
    full_name='tdxreader.TdxReader.Hello',
    index=0,
    containing_service=None,
    input_type=_HELLOREQUEST,
    output_type=_HELLOREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ReadTdxFile',
    full_name='tdxreader.TdxReader.ReadTdxFile',
    index=1,
    containing_service=None,
    input_type=_READTDXFILEREQUEST,
    output_type=_TDXFILEDATA,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TDXREADER)

DESCRIPTOR.services_by_name['TdxReader'] = _TDXREADER

# @@protoc_insertion_point(module_scope)
