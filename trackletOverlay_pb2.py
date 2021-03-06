# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trackletOverlay.proto

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
  name='trackletOverlay.proto',
  package='trackletOverlay',
  serialized_pb=_b('\n\x15trackletOverlay.proto\x12\x0ftrackletOverlay\"\x1d\n\x05Pixel\x12\t\n\x01x\x18\x01 \x02(\r\x12\t\n\x01y\x18\x02 \x02(\r\"@\n\x08Tracklet\x12\x0c\n\x04name\x18\x01 \x02(\t\x12&\n\x06pixels\x18\x03 \x03(\x0b\x32\x16.trackletOverlay.Pixel\"7\n\x07Overlay\x12,\n\ttracklets\x18\x01 \x03(\x0b\x32\x19.trackletOverlay.Tracklet')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PIXEL = _descriptor.Descriptor(
  name='Pixel',
  full_name='trackletOverlay.Pixel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='trackletOverlay.Pixel.x', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='trackletOverlay.Pixel.y', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=71,
)


_TRACKLET = _descriptor.Descriptor(
  name='Tracklet',
  full_name='trackletOverlay.Tracklet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='trackletOverlay.Tracklet.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pixels', full_name='trackletOverlay.Tracklet.pixels', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=73,
  serialized_end=137,
)


_OVERLAY = _descriptor.Descriptor(
  name='Overlay',
  full_name='trackletOverlay.Overlay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tracklets', full_name='trackletOverlay.Overlay.tracklets', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=194,
)

_TRACKLET.fields_by_name['pixels'].message_type = _PIXEL
_OVERLAY.fields_by_name['tracklets'].message_type = _TRACKLET
DESCRIPTOR.message_types_by_name['Pixel'] = _PIXEL
DESCRIPTOR.message_types_by_name['Tracklet'] = _TRACKLET
DESCRIPTOR.message_types_by_name['Overlay'] = _OVERLAY

Pixel = _reflection.GeneratedProtocolMessageType('Pixel', (_message.Message,), dict(
  DESCRIPTOR = _PIXEL,
  __module__ = 'trackletOverlay_pb2'
  # @@protoc_insertion_point(class_scope:trackletOverlay.Pixel)
  ))
_sym_db.RegisterMessage(Pixel)

Tracklet = _reflection.GeneratedProtocolMessageType('Tracklet', (_message.Message,), dict(
  DESCRIPTOR = _TRACKLET,
  __module__ = 'trackletOverlay_pb2'
  # @@protoc_insertion_point(class_scope:trackletOverlay.Tracklet)
  ))
_sym_db.RegisterMessage(Tracklet)

Overlay = _reflection.GeneratedProtocolMessageType('Overlay', (_message.Message,), dict(
  DESCRIPTOR = _OVERLAY,
  __module__ = 'trackletOverlay_pb2'
  # @@protoc_insertion_point(class_scope:trackletOverlay.Overlay)
  ))
_sym_db.RegisterMessage(Overlay)


# @@protoc_insertion_point(module_scope)
