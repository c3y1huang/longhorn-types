# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: imrpc/instance.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from imrpc import common_pb2 as imrpc_dot_common__pb2
from imrpc import imrpc_pb2 as imrpc_dot_imrpc__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14imrpc/instance.proto\x12\x05imrpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x12imrpc/common.proto\x1a\x11imrpc/imrpc.proto\"3\n\x13ProcessInstanceSpec\x12\x0e\n\x06\x62inary\x18\x01 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\"\xf8\x01\n\x10SpdkInstanceSpec\x12K\n\x13replica_address_map\x18\x01 \x03(\x0b\x32..imrpc.SpdkInstanceSpec.ReplicaAddressMapEntry\x12\x11\n\tdisk_name\x18\x02 \x01(\t\x12\x11\n\tdisk_uuid\x18\x03 \x01(\t\x12\x0c\n\x04size\x18\x04 \x01(\x04\x12\x17\n\x0f\x65xpose_required\x18\x05 \x01(\x08\x12\x10\n\x08\x66rontend\x18\x06 \x01(\t\x1a\x38\n\x16ReplicaAddressMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xbb\x02\n\x0cInstanceSpec\x12;\n\x14\x62\x61\x63kend_store_driver\x18\x01 \x01(\x0e\x32\x19.imrpc.BackendStoreDriverB\x02\x18\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x13\n\x0bvolume_name\x18\x04 \x01(\t\x12\x12\n\nport_count\x18\x05 \x01(\x05\x12\x11\n\tport_args\x18\x06 \x03(\t\x12\x39\n\x15process_instance_spec\x18\x07 \x01(\x0b\x32\x1a.imrpc.ProcessInstanceSpec\x12\x33\n\x12spdk_instance_spec\x18\x08 \x01(\x0b\x32\x17.imrpc.SpdkInstanceSpec\x12&\n\x0b\x64\x61ta_engine\x18\t \x01(\x0e\x32\x11.imrpc.DataEngine\"\xc6\x01\n\x0eInstanceStatus\x12\r\n\x05state\x18\x01 \x01(\t\x12\x11\n\terror_msg\x18\x02 \x01(\t\x12\x12\n\nport_start\x18\x03 \x01(\x05\x12\x10\n\x08port_end\x18\x04 \x01(\x05\x12\x39\n\nconditions\x18\x05 \x03(\x0b\x32%.imrpc.InstanceStatus.ConditionsEntry\x1a\x31\n\x0f\x43onditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\":\n\x15InstanceCreateRequest\x12!\n\x04spec\x18\x01 \x01(\x0b\x32\x13.imrpc.InstanceSpec\"\xc5\x01\n\x15InstanceDeleteRequest\x12;\n\x14\x62\x61\x63kend_store_driver\x18\x01 \x01(\x0e\x32\x19.imrpc.BackendStoreDriverB\x02\x18\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x11\n\tdisk_uuid\x18\x04 \x01(\t\x12\x18\n\x10\x63leanup_required\x18\x05 \x01(\x08\x12&\n\x0b\x64\x61ta_engine\x18\x06 \x01(\x0e\x32\x11.imrpc.DataEngine\"\x95\x01\n\x12InstanceGetRequest\x12;\n\x14\x62\x61\x63kend_store_driver\x18\x01 \x01(\x0e\x32\x19.imrpc.BackendStoreDriverB\x02\x18\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12&\n\x0b\x64\x61ta_engine\x18\x04 \x01(\x0e\x32\x11.imrpc.DataEngine\"m\n\x10InstanceResponse\x12!\n\x04spec\x18\x01 \x01(\x0b\x32\x13.imrpc.InstanceSpec\x12%\n\x06status\x18\x02 \x01(\x0b\x32\x15.imrpc.InstanceStatus\x12\x0f\n\x07\x64\x65leted\x18\x03 \x01(\x08\"\xa0\x01\n\x14InstanceListResponse\x12=\n\tinstances\x18\x01 \x03(\x0b\x32*.imrpc.InstanceListResponse.InstancesEntry\x1aI\n\x0eInstancesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.imrpc.InstanceResponse:\x02\x38\x01\"\x95\x01\n\x12InstanceLogRequest\x12;\n\x14\x62\x61\x63kend_store_driver\x18\x01 \x01(\x0e\x32\x19.imrpc.BackendStoreDriverB\x02\x18\x01\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12&\n\x0b\x64\x61ta_engine\x18\x04 \x01(\x0e\x32\x11.imrpc.DataEngine\"U\n\x16InstanceReplaceRequest\x12!\n\x04spec\x18\x01 \x01(\x0b\x32\x13.imrpc.InstanceSpec\x12\x18\n\x10terminate_signal\x18\x02 \x01(\t\"K\n\x12LogSetLevelRequest\x12&\n\x0b\x64\x61ta_engine\x18\x01 \x01(\x0e\x32\x11.imrpc.DataEngine\x12\r\n\x05level\x18\x02 \x01(\t\"K\n\x12LogSetFlagsRequest\x12&\n\x0b\x64\x61ta_engine\x18\x01 \x01(\x0e\x32\x11.imrpc.DataEngine\x12\r\n\x05\x66lags\x18\x02 \x01(\t\"<\n\x12LogGetLevelRequest\x12&\n\x0b\x64\x61ta_engine\x18\x01 \x01(\x0e\x32\x11.imrpc.DataEngine\"$\n\x13LogGetLevelResponse\x12\r\n\x05level\x18\x01 \x01(\t\"<\n\x12LogGetFlagsRequest\x12&\n\x0b\x64\x61ta_engine\x18\x01 \x01(\x0e\x32\x11.imrpc.DataEngine\"$\n\x13LogGetFlagsResponse\x12\r\n\x05\x66lags\x18\x01 \x01(\t2\xc9\x06\n\x0fInstanceService\x12I\n\x0eInstanceCreate\x12\x1c.imrpc.InstanceCreateRequest\x1a\x17.imrpc.InstanceResponse\"\x00\x12I\n\x0eInstanceDelete\x12\x1c.imrpc.InstanceDeleteRequest\x1a\x17.imrpc.InstanceResponse\"\x00\x12\x43\n\x0bInstanceGet\x12\x19.imrpc.InstanceGetRequest\x1a\x17.imrpc.InstanceResponse\"\x00\x12\x45\n\x0cInstanceList\x12\x16.google.protobuf.Empty\x1a\x1b.imrpc.InstanceListResponse\"\x00\x12:\n\x0bInstanceLog\x12\x19.imrpc.InstanceLogRequest\x1a\x0c.LogResponse\"\x00\x30\x01\x12\x43\n\rInstanceWatch\x12\x16.google.protobuf.Empty\x1a\x16.google.protobuf.Empty\"\x00\x30\x01\x12K\n\x0fInstanceReplace\x12\x1d.imrpc.InstanceReplaceRequest\x1a\x17.imrpc.InstanceResponse\"\x00\x12@\n\x0bLogSetLevel\x12\x19.imrpc.LogSetLevelRequest\x1a\x16.google.protobuf.Empty\x12@\n\x0bLogSetFlags\x12\x19.imrpc.LogSetFlagsRequest\x1a\x16.google.protobuf.Empty\x12\x44\n\x0bLogGetLevel\x12\x19.imrpc.LogGetLevelRequest\x1a\x1a.imrpc.LogGetLevelResponse\x12\x44\n\x0bLogGetFlags\x12\x19.imrpc.LogGetFlagsRequest\x1a\x1a.imrpc.LogGetFlagsResponse\x12\x36\n\nVersionGet\x12\x16.google.protobuf.Empty\x1a\x10.VersionResponseB/Z-github.com/longhorn/types/pkg/generated/imrpcb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'imrpc.instance_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z-github.com/longhorn/types/pkg/generated/imrpc'
  _SPDKINSTANCESPEC_REPLICAADDRESSMAPENTRY._options = None
  _SPDKINSTANCESPEC_REPLICAADDRESSMAPENTRY._serialized_options = b'8\001'
  _INSTANCESPEC.fields_by_name['backend_store_driver']._options = None
  _INSTANCESPEC.fields_by_name['backend_store_driver']._serialized_options = b'\030\001'
  _INSTANCESTATUS_CONDITIONSENTRY._options = None
  _INSTANCESTATUS_CONDITIONSENTRY._serialized_options = b'8\001'
  _INSTANCEDELETEREQUEST.fields_by_name['backend_store_driver']._options = None
  _INSTANCEDELETEREQUEST.fields_by_name['backend_store_driver']._serialized_options = b'\030\001'
  _INSTANCEGETREQUEST.fields_by_name['backend_store_driver']._options = None
  _INSTANCEGETREQUEST.fields_by_name['backend_store_driver']._serialized_options = b'\030\001'
  _INSTANCELISTRESPONSE_INSTANCESENTRY._options = None
  _INSTANCELISTRESPONSE_INSTANCESENTRY._serialized_options = b'8\001'
  _INSTANCELOGREQUEST.fields_by_name['backend_store_driver']._options = None
  _INSTANCELOGREQUEST.fields_by_name['backend_store_driver']._serialized_options = b'\030\001'
  _globals['_PROCESSINSTANCESPEC']._serialized_start=99
  _globals['_PROCESSINSTANCESPEC']._serialized_end=150
  _globals['_SPDKINSTANCESPEC']._serialized_start=153
  _globals['_SPDKINSTANCESPEC']._serialized_end=401
  _globals['_SPDKINSTANCESPEC_REPLICAADDRESSMAPENTRY']._serialized_start=345
  _globals['_SPDKINSTANCESPEC_REPLICAADDRESSMAPENTRY']._serialized_end=401
  _globals['_INSTANCESPEC']._serialized_start=404
  _globals['_INSTANCESPEC']._serialized_end=719
  _globals['_INSTANCESTATUS']._serialized_start=722
  _globals['_INSTANCESTATUS']._serialized_end=920
  _globals['_INSTANCESTATUS_CONDITIONSENTRY']._serialized_start=871
  _globals['_INSTANCESTATUS_CONDITIONSENTRY']._serialized_end=920
  _globals['_INSTANCECREATEREQUEST']._serialized_start=922
  _globals['_INSTANCECREATEREQUEST']._serialized_end=980
  _globals['_INSTANCEDELETEREQUEST']._serialized_start=983
  _globals['_INSTANCEDELETEREQUEST']._serialized_end=1180
  _globals['_INSTANCEGETREQUEST']._serialized_start=1183
  _globals['_INSTANCEGETREQUEST']._serialized_end=1332
  _globals['_INSTANCERESPONSE']._serialized_start=1334
  _globals['_INSTANCERESPONSE']._serialized_end=1443
  _globals['_INSTANCELISTRESPONSE']._serialized_start=1446
  _globals['_INSTANCELISTRESPONSE']._serialized_end=1606
  _globals['_INSTANCELISTRESPONSE_INSTANCESENTRY']._serialized_start=1533
  _globals['_INSTANCELISTRESPONSE_INSTANCESENTRY']._serialized_end=1606
  _globals['_INSTANCELOGREQUEST']._serialized_start=1609
  _globals['_INSTANCELOGREQUEST']._serialized_end=1758
  _globals['_INSTANCEREPLACEREQUEST']._serialized_start=1760
  _globals['_INSTANCEREPLACEREQUEST']._serialized_end=1845
  _globals['_LOGSETLEVELREQUEST']._serialized_start=1847
  _globals['_LOGSETLEVELREQUEST']._serialized_end=1922
  _globals['_LOGSETFLAGSREQUEST']._serialized_start=1924
  _globals['_LOGSETFLAGSREQUEST']._serialized_end=1999
  _globals['_LOGGETLEVELREQUEST']._serialized_start=2001
  _globals['_LOGGETLEVELREQUEST']._serialized_end=2061
  _globals['_LOGGETLEVELRESPONSE']._serialized_start=2063
  _globals['_LOGGETLEVELRESPONSE']._serialized_end=2099
  _globals['_LOGGETFLAGSREQUEST']._serialized_start=2101
  _globals['_LOGGETFLAGSREQUEST']._serialized_end=2161
  _globals['_LOGGETFLAGSRESPONSE']._serialized_start=2163
  _globals['_LOGGETFLAGSRESPONSE']._serialized_end=2199
  _globals['_INSTANCESERVICE']._serialized_start=2202
  _globals['_INSTANCESERVICE']._serialized_end=3043
# @@protoc_insertion_point(module_scope)
