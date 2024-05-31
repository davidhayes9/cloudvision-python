# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/redirector.v1/services.gen.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from arista.redirector.v1 import redirector_pb2 as arista_dot_redirector_dot_v1_dot_redirector__pb2
from arista.time import time_pb2 as arista_dot_time_dot_time__pb2
from arista.subscriptions import subscriptions_pb2 as arista_dot_subscriptions_dot_subscriptions__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'arista/redirector.v1/services.gen.proto\x12\x14\x61rista.redirector.v1\x1a%arista/redirector.v1/redirector.proto\x1a\x16\x61rista/time/time.proto\x1a(arista/subscriptions/subscriptions.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"\x94\x01\n\x0cMetaResponse\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x02 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\x12+\n\x05\x63ount\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"o\n\x11\x41ssignmentRequest\x12\x30\n\x03key\x18\x01 \x01(\x0b\x32#.arista.redirector.v1.AssignmentKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"o\n\x12\x41ssignmentResponse\x12/\n\x05value\x18\x01 \x01(\x0b\x32 .arista.redirector.v1.Assignment\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"t\n\x15\x41ssignmentSomeRequest\x12\x31\n\x04keys\x18\x01 \x03(\x0b\x32#.arista.redirector.v1.AssignmentKey\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xa0\x01\n\x16\x41ssignmentSomeResponse\x12/\n\x05value\x18\x01 \x01(\x0b\x32 .arista.redirector.v1.Assignment\x12+\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12(\n\x04time\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"}\n\x17\x41ssignmentStreamRequest\x12;\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32 .arista.redirector.v1.Assignment\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\"\xa4\x01\n\x18\x41ssignmentStreamResponse\x12/\n\x05value\x18\x01 \x01(\x0b\x32 .arista.redirector.v1.Assignment\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\x04type\x18\x03 \x01(\x0e\x32\x1f.arista.subscriptions.Operation\"\xb8\x01\n\x1e\x41ssignmentBatchedStreamRequest\x12;\n\x11partial_eq_filter\x18\x01 \x03(\x0b\x32 .arista.redirector.v1.Assignment\x12%\n\x04time\x18\x03 \x01(\x0b\x32\x17.arista.time.TimeBounds\x12\x32\n\x0cmax_messages\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\"d\n\x1f\x41ssignmentBatchedStreamResponse\x12\x41\n\tresponses\x18\x01 \x03(\x0b\x32..arista.redirector.v1.AssignmentStreamResponse2\xf9\x06\n\x11\x41ssignmentService\x12[\n\x06GetOne\x12\'.arista.redirector.v1.AssignmentRequest\x1a(.arista.redirector.v1.AssignmentResponse\x12\x66\n\x07GetSome\x12+.arista.redirector.v1.AssignmentSomeRequest\x1a,.arista.redirector.v1.AssignmentSomeResponse0\x01\x12i\n\x06GetAll\x12-.arista.redirector.v1.AssignmentStreamRequest\x1a..arista.redirector.v1.AssignmentStreamResponse0\x01\x12l\n\tSubscribe\x12-.arista.redirector.v1.AssignmentStreamRequest\x1a..arista.redirector.v1.AssignmentStreamResponse0\x01\x12\\\n\x07GetMeta\x12-.arista.redirector.v1.AssignmentStreamRequest\x1a\".arista.redirector.v1.MetaResponse\x12\x64\n\rSubscribeMeta\x12-.arista.redirector.v1.AssignmentStreamRequest\x1a\".arista.redirector.v1.MetaResponse0\x01\x12~\n\rGetAllBatched\x12\x34.arista.redirector.v1.AssignmentBatchedStreamRequest\x1a\x35.arista.redirector.v1.AssignmentBatchedStreamResponse0\x01\x12\x81\x01\n\x10SubscribeBatched\x12\x34.arista.redirector.v1.AssignmentBatchedStreamRequest\x1a\x35.arista.redirector.v1.AssignmentBatchedStreamResponse0\x01\x42NZLgithub.com/aristanetworks/cloudvision-go/api/arista/redirector.v1;redirectorb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.redirector.v1.services.gen_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZLgithub.com/aristanetworks/cloudvision-go/api/arista/redirector.v1;redirector'
  _globals['_METARESPONSE']._serialized_start=236
  _globals['_METARESPONSE']._serialized_end=384
  _globals['_ASSIGNMENTREQUEST']._serialized_start=386
  _globals['_ASSIGNMENTREQUEST']._serialized_end=497
  _globals['_ASSIGNMENTRESPONSE']._serialized_start=499
  _globals['_ASSIGNMENTRESPONSE']._serialized_end=610
  _globals['_ASSIGNMENTSOMEREQUEST']._serialized_start=612
  _globals['_ASSIGNMENTSOMEREQUEST']._serialized_end=728
  _globals['_ASSIGNMENTSOMERESPONSE']._serialized_start=731
  _globals['_ASSIGNMENTSOMERESPONSE']._serialized_end=891
  _globals['_ASSIGNMENTSTREAMREQUEST']._serialized_start=893
  _globals['_ASSIGNMENTSTREAMREQUEST']._serialized_end=1018
  _globals['_ASSIGNMENTSTREAMRESPONSE']._serialized_start=1021
  _globals['_ASSIGNMENTSTREAMRESPONSE']._serialized_end=1185
  _globals['_ASSIGNMENTBATCHEDSTREAMREQUEST']._serialized_start=1188
  _globals['_ASSIGNMENTBATCHEDSTREAMREQUEST']._serialized_end=1372
  _globals['_ASSIGNMENTBATCHEDSTREAMRESPONSE']._serialized_start=1374
  _globals['_ASSIGNMENTBATCHEDSTREAMRESPONSE']._serialized_end=1474
  _globals['_ASSIGNMENTSERVICE']._serialized_start=1477
  _globals['_ASSIGNMENTSERVICE']._serialized_end=2366
# @@protoc_insertion_point(module_scope)
