# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arista/workspace.v1/workspace.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from fmp import extensions_pb2 as fmp_dot_extensions__pb2
from fmp import wrappers_pb2 as fmp_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from arista.configstatus.v1 import configstatus_pb2 as arista_dot_configstatus_dot_v1_dot_configstatus__pb2
from arista.imagestatus.v1 import imagestatus_pb2 as arista_dot_imagestatus_dot_v1_dot_imagestatus__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#arista/workspace.v1/workspace.proto\x12\x13\x61rista.workspace.v1\x1a\x14\x66mp/extensions.proto\x1a\x12\x66mp/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a)arista/configstatus.v1/configstatus.proto\x1a\'arista/imagestatus.v1/imagestatus.proto\"A\n\rRequestParams\x12\x30\n\nrequest_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x9f\x01\n\x08Response\x12\x33\n\x06status\x18\x01 \x01(\x0e\x32#.arista.workspace.v1.ResponseStatus\x12-\n\x07message\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\x04\x63ode\x18\x03 \x01(\x0e\x32!.arista.workspace.v1.ResponseCode\"\x95\x01\n\tResponses\x12:\n\x06values\x18\x01 \x03(\x0b\x32*.arista.workspace.v1.Responses.ValuesEntry\x1aL\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12,\n\x05value\x18\x02 \x01(\x0b\x32\x1d.arista.workspace.v1.Response:\x02\x38\x01\"H\n\x0cWorkspaceKey\x12\x32\n\x0cworkspace_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\x9b\x02\n\x0fWorkspaceConfig\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.workspace.v1.WorkspaceKey\x12\x32\n\x0c\x64isplay_name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07request\x18\x04 \x01(\x0e\x32\x1c.arista.workspace.v1.Request\x12:\n\x0erequest_params\x18\x05 \x01(\x0b\x32\".arista.workspace.v1.RequestParams:\x06\xfa\x8d\x19\x02rw\"\xd3\x05\n\tWorkspace\x12.\n\x03key\x18\x01 \x01(\x0b\x32!.arista.workspace.v1.WorkspaceKey\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\ncreated_by\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x10last_modified_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x36\n\x10last_modified_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x05state\x18\x06 \x01(\x0e\x32#.arista.workspace.v1.WorkspaceState\x12\x33\n\rlast_build_id\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\tresponses\x18\x08 \x01(\x0b\x32\x1e.arista.workspace.v1.Responses\x12#\n\x06\x63\x63_ids\x18\t \x01(\x0b\x32\x13.fmp.RepeatedString\x12/\n\x0bneeds_build\x18\n \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x33\n\x0flast_rebased_at\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0cneeds_rebase\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x32\n\x0c\x64isplay_name\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0b\x64\x65scription\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x06\xfa\x8d\x19\x02ro\"\xb4\x01\n\nInputError\x12.\n\x08\x66ield_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12!\n\x04path\x18\x02 \x01(\x0b\x32\x13.fmp.RepeatedString\x12$\n\x07members\x18\x03 \x01(\x0b\x32\x13.fmp.RepeatedString\x12-\n\x07message\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\">\n\x0bInputErrors\x12/\n\x06values\x18\x01 \x03(\x0b\x32\x1f.arista.workspace.v1.InputError\"\xbf\x01\n\x15InputValidationResult\x12=\n\x13input_schema_errors\x18\x01 \x01(\x0b\x32 .arista.workspace.v1.InputErrors\x12<\n\x12input_value_errors\x18\x02 \x01(\x0b\x32 .arista.workspace.v1.InputErrors\x12)\n\x0cother_errors\x18\x03 \x01(\x0b\x32\x13.fmp.RepeatedString\"\xbc\x01\n\x16InputValidationResults\x12G\n\x06values\x18\x01 \x03(\x0b\x32\x37.arista.workspace.v1.InputValidationResults.ValuesEntry\x1aY\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.arista.workspace.v1.InputValidationResult:\x02\x38\x01\"\xd3\x01\n\rTemplateError\x12.\n\x08line_num\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32Value\x12/\n\texception\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12,\n\x06\x64\x65tail\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rexception_msg\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"D\n\x0eTemplateErrors\x12\x32\n\x06values\x18\x01 \x03(\x0b\x32\".arista.workspace.v1.TemplateError\"\xab\x02\n\x14\x43onfigletBuildResult\x12<\n\x0ftemplate_errors\x18\x01 \x01(\x0b\x32#.arista.workspace.v1.TemplateErrors\x12\x36\n\x10generated_config\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bother_error\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x32\n\x0c\x65xecution_id\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x0cinput_errors\x18\x05 \x01(\x0b\x32 .arista.workspace.v1.InputErrors\"\xb9\x01\n\x15\x43onfigletBuildResults\x12\x46\n\x06values\x18\x01 \x03(\x0b\x32\x36.arista.workspace.v1.ConfigletBuildResults.ValuesEntry\x1aX\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x38\n\x05value\x18\x02 \x01(\x0b\x32).arista.workspace.v1.ConfigletBuildResult:\x02\x38\x01\"\xfd\x01\n\x16\x43onfigValidationResult\x12\x36\n\x07summary\x18\x01 \x01(\x0b\x32%.arista.configstatus.v1.ConfigSummary\x12\x34\n\x06\x65rrors\x18\x02 \x01(\x0b\x32$.arista.configstatus.v1.ConfigErrors\x12\x36\n\x08warnings\x18\x03 \x01(\x0b\x32$.arista.configstatus.v1.ConfigErrors\x12=\n\x0e\x63onfig_sources\x18\x04 \x01(\x0b\x32%.arista.configstatus.v1.ConfigSources\"\xa4\x02\n\x15ImageValidationResult\x12\x34\n\x07summary\x18\x01 \x01(\x0b\x32#.arista.imagestatus.v1.ImageSummary\x12\x32\n\x06\x65rrors\x18\x02 \x01(\x0b\x32\".arista.imagestatus.v1.ImageErrors\x12\x36\n\x08warnings\x18\x03 \x01(\x0b\x32$.arista.imagestatus.v1.ImageWarnings\x12\x37\n\x11image_input_error\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\x05infos\x18\x05 \x01(\x0b\x32!.arista.imagestatus.v1.ImageInfos\"\xbf\x01\n\x10\x43onfigSyncResult\x12\x36\n\x07summary\x18\x01 \x01(\x0b\x32%.arista.configstatus.v1.ConfigSummary\x12\x34\n\x06\x65rrors\x18\x02 \x01(\x0b\x32$.arista.configstatus.v1.ConfigErrors\x12=\n\x0e\x63onfig_sources\x18\x03 \x01(\x0b\x32%.arista.configstatus.v1.ConfigSources\"\xa3\x01\n\x0f\x42uildStageState\x12@\n\x06values\x18\x01 \x03(\x0b\x32\x30.arista.workspace.v1.BuildStageState.ValuesEntry\x1aN\n\x0bValuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0e\x32\x1f.arista.workspace.v1.BuildState:\x02\x38\x01\"\xbf\x01\n\x0b\x41uthzResult\x12?\n\x1bhas_unauthorized_tag_change\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x42\n\x1ehas_unauthorized_device_change\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12+\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"}\n\x11WorkspaceBuildKey\x12\x32\n\x0cworkspace_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x62uild_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\x98\x02\n\x0eWorkspaceBuild\x12\x33\n\x03key\x18\x01 \x01(\x0b\x32&.arista.workspace.v1.WorkspaceBuildKey\x12.\n\x05state\x18\x02 \x01(\x0e\x32\x1f.arista.workspace.v1.BuildState\x12+\n\x05\x65rror\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x62uilt_by\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x0c\x61uthz_result\x18\x06 \x01(\x0b\x32 .arista.workspace.v1.AuthzResult:\x06\xfa\x8d\x19\x02roJ\x04\x08\x03\x10\x04\"\xb5\x01\n\x18WorkspaceBuildDetailsKey\x12\x32\n\x0cworkspace_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x62uild_id\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\tdevice_id\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue:\x04\x80\x8e\x19\x01\"\xa9\x07\n\x15WorkspaceBuildDetails\x12:\n\x03key\x18\x01 \x01(\x0b\x32-.arista.workspace.v1.WorkspaceBuildDetailsKey\x12.\n\x05state\x18\x02 \x01(\x0e\x32\x1f.arista.workspace.v1.BuildState\x12.\n\x05stage\x18\x03 \x01(\x0e\x32\x1f.arista.workspace.v1.BuildStage\x12M\n\x18input_validation_results\x18\x04 \x01(\x0b\x32+.arista.workspace.v1.InputValidationResults\x12K\n\x17\x63onfiglet_build_results\x18\x05 \x01(\x0b\x32*.arista.workspace.v1.ConfigletBuildResults\x12M\n\x18\x63onfig_validation_result\x18\x06 \x01(\x0b\x32+.arista.workspace.v1.ConfigValidationResult\x12K\n\x17image_validation_result\x18\x07 \x01(\x0b\x32*.arista.workspace.v1.ImageValidationResult\x12T\n\x1c\x63onfig_validation_skip_cause\x18\x08 \x01(\x0e\x32..arista.workspace.v1.ConfigValidationSkipCause\x12R\n\x1bimage_validation_skip_cause\x18\t \x01(\x0e\x32-.arista.workspace.v1.ImageValidationSkipCause\x12?\n\x11\x62uild_stage_state\x18\n \x01(\x0b\x32$.arista.workspace.v1.BuildStageState\x12<\n\x0c\x61uthz_status\x18\x0b \x01(\x0e\x32&.arista.workspace.v1.DeviceAuthzStatus\x12\x41\n\x12\x63onfig_sync_result\x18\x0c \x01(\x0b\x32%.arista.workspace.v1.ConfigSyncResult\x12H\n\x16\x63onfig_sync_skip_cause\x18\r \x01(\x0e\x32(.arista.workspace.v1.ConfigSyncSkipCause:\x06\xfa\x8d\x19\x02ro\"\x88\x01\n\x10WorkspaceSyncKey\x12\x32\n\x0cworkspace_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x0esync_operation\x18\x02 \x01(\x0e\x32\".arista.workspace.v1.SyncOperation:\x04\x80\x8e\x19\x01\"z\n\x13WorkspaceSyncConfig\x12\x32\n\x03key\x18\x01 \x01(\x0b\x32%.arista.workspace.v1.WorkspaceSyncKey\x12\'\n\ndevice_ids\x18\x02 \x01(\x0b\x32\x13.fmp.RepeatedString:\x06\xfa\x8d\x19\x02rw*\xcc\x01\n\x0eWorkspaceState\x12\x1f\n\x1bWORKSPACE_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x17WORKSPACE_STATE_PENDING\x10\x01\x12\x1d\n\x19WORKSPACE_STATE_SUBMITTED\x10\x02\x12\x1d\n\x19WORKSPACE_STATE_ABANDONED\x10\x03\x12\x1d\n\x19WORKSPACE_STATE_CONFLICTS\x10\x04\x12\x1f\n\x1bWORKSPACE_STATE_ROLLED_BACK\x10\x05*\xc2\x01\n\x07Request\x12\x17\n\x13REQUEST_UNSPECIFIED\x10\x00\x12\x17\n\x13REQUEST_START_BUILD\x10\x01\x12\x18\n\x14REQUEST_CANCEL_BUILD\x10\x02\x12\x12\n\x0eREQUEST_SUBMIT\x10\x03\x12\x13\n\x0fREQUEST_ABANDON\x10\x04\x12\x14\n\x10REQUEST_ROLLBACK\x10\x05\x12\x18\n\x14REQUEST_SUBMIT_FORCE\x10\x06\x12\x12\n\x0eREQUEST_REBASE\x10\x07*h\n\x0eResponseStatus\x12\x1f\n\x1bRESPONSE_STATUS_UNSPECIFIED\x10\x00\x12\x1b\n\x17RESPONSE_STATUS_SUCCESS\x10\x01\x12\x18\n\x14RESPONSE_STATUS_FAIL\x10\x02*W\n\x0cResponseCode\x12\x1d\n\x19RESPONSE_CODE_UNSPECIFIED\x10\x00\x12(\n$RESPONSE_CODE_INACTIVE_DEVICES_EXIST\x10\x01*\xa8\x01\n\nBuildState\x12\x1b\n\x17\x42UILD_STATE_UNSPECIFIED\x10\x00\x12\x1b\n\x17\x42UILD_STATE_IN_PROGRESS\x10\x01\x12\x18\n\x14\x42UILD_STATE_CANCELED\x10\x02\x12\x17\n\x13\x42UILD_STATE_SUCCESS\x10\x03\x12\x14\n\x10\x42UILD_STATE_FAIL\x10\x04\x12\x17\n\x13\x42UILD_STATE_SKIPPED\x10\x05*\xb1\x01\n\nBuildStage\x12\x1b\n\x17\x42UILD_STAGE_UNSPECIFIED\x10\x00\x12 \n\x1c\x42UILD_STAGE_INPUT_VALIDATION\x10\x01\x12\x1f\n\x1b\x42UILD_STAGE_CONFIGLET_BUILD\x10\x02\x12!\n\x1d\x42UILD_STAGE_CONFIG_VALIDATION\x10\x03\x12 \n\x1c\x42UILD_STAGE_IMAGE_VALIDATION\x10\x04*\x82\x01\n\x11\x44\x65viceAuthzStatus\x12#\n\x1f\x44\x45VICE_AUTHZ_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1e\x44\x45VICE_AUTHZ_STATUS_AUTHORIZED\x10\x01\x12$\n DEVICE_AUTHZ_STATUS_UNAUTHORIZED\x10\x02*\xc5\x02\n\x19\x43onfigValidationSkipCause\x12,\n(CONFIG_VALIDATION_SKIP_CAUSE_UNSPECIFIED\x10\x00\x12)\n%CONFIG_VALIDATION_SKIP_CAUSE_INACTIVE\x10\x01\x12\x30\n,CONFIG_VALIDATION_SKIP_CAUSE_PRE_PROVISIONED\x10\x02\x12\x31\n-CONFIG_VALIDATION_SKIP_CAUSE_CONFIG_UNCHANGED\x10\x03\x12\x32\n.CONFIG_VALIDATION_SKIP_CAUSE_NO_CONFIG_SOURCES\x10\x04\x12\x36\n2CONFIG_VALIDATION_SKIP_CAUSE_DEVICE_DECOMMISSIONED\x10\x05*\x89\x02\n\x18ImageValidationSkipCause\x12+\n\'IMAGE_VALIDATION_SKIP_CAUSE_UNSPECIFIED\x10\x00\x12(\n$IMAGE_VALIDATION_SKIP_CAUSE_INACTIVE\x10\x01\x12/\n+IMAGE_VALIDATION_SKIP_CAUSE_PRE_PROVISIONED\x10\x02\x12/\n+IMAGE_VALIDATION_SKIP_CAUSE_IMAGE_UNCHANGED\x10\x03\x12\x34\n0IMAGE_VALIDATION_SKIP_CAUSE_NO_PROPOSED_SOFTWARE\x10\x04*\xb8\x01\n\x13\x43onfigSyncSkipCause\x12&\n\"CONFIG_SYNC_SKIP_CAUSE_UNSPECIFIED\x10\x00\x12#\n\x1f\x43ONFIG_SYNC_SKIP_CAUSE_INACTIVE\x10\x01\x12*\n&CONFIG_SYNC_SKIP_CAUSE_PRE_PROVISIONED\x10\x02\x12(\n$CONFIG_SYNC_SKIP_CAUSE_IN_COMPLIANCE\x10\x03*J\n\rSyncOperation\x12\x1e\n\x1aSYNC_OPERATION_UNSPECIFIED\x10\x00\x12\x19\n\x15SYNC_OPERATION_CONFIG\x10\x01\x42LZJgithub.com/aristanetworks/cloudvision-go/api/arista/workspace.v1;workspaceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'arista.workspace.v1.workspace_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'ZJgithub.com/aristanetworks/cloudvision-go/api/arista/workspace.v1;workspace'
  _globals['_RESPONSES_VALUESENTRY']._options = None
  _globals['_RESPONSES_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_WORKSPACEKEY']._options = None
  _globals['_WORKSPACEKEY']._serialized_options = b'\200\216\031\001'
  _globals['_WORKSPACECONFIG']._options = None
  _globals['_WORKSPACECONFIG']._serialized_options = b'\372\215\031\002rw'
  _globals['_WORKSPACE']._options = None
  _globals['_WORKSPACE']._serialized_options = b'\372\215\031\002ro'
  _globals['_INPUTVALIDATIONRESULTS_VALUESENTRY']._options = None
  _globals['_INPUTVALIDATIONRESULTS_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_CONFIGLETBUILDRESULTS_VALUESENTRY']._options = None
  _globals['_CONFIGLETBUILDRESULTS_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_BUILDSTAGESTATE_VALUESENTRY']._options = None
  _globals['_BUILDSTAGESTATE_VALUESENTRY']._serialized_options = b'8\001'
  _globals['_WORKSPACEBUILDKEY']._options = None
  _globals['_WORKSPACEBUILDKEY']._serialized_options = b'\200\216\031\001'
  _globals['_WORKSPACEBUILD']._options = None
  _globals['_WORKSPACEBUILD']._serialized_options = b'\372\215\031\002ro'
  _globals['_WORKSPACEBUILDDETAILSKEY']._options = None
  _globals['_WORKSPACEBUILDDETAILSKEY']._serialized_options = b'\200\216\031\001'
  _globals['_WORKSPACEBUILDDETAILS']._options = None
  _globals['_WORKSPACEBUILDDETAILS']._serialized_options = b'\372\215\031\002ro'
  _globals['_WORKSPACESYNCKEY']._options = None
  _globals['_WORKSPACESYNCKEY']._serialized_options = b'\200\216\031\001'
  _globals['_WORKSPACESYNCCONFIG']._options = None
  _globals['_WORKSPACESYNCCONFIG']._serialized_options = b'\372\215\031\002rw'
  _globals['_WORKSPACESTATE']._serialized_start=6027
  _globals['_WORKSPACESTATE']._serialized_end=6231
  _globals['_REQUEST']._serialized_start=6234
  _globals['_REQUEST']._serialized_end=6428
  _globals['_RESPONSESTATUS']._serialized_start=6430
  _globals['_RESPONSESTATUS']._serialized_end=6534
  _globals['_RESPONSECODE']._serialized_start=6536
  _globals['_RESPONSECODE']._serialized_end=6623
  _globals['_BUILDSTATE']._serialized_start=6626
  _globals['_BUILDSTATE']._serialized_end=6794
  _globals['_BUILDSTAGE']._serialized_start=6797
  _globals['_BUILDSTAGE']._serialized_end=6974
  _globals['_DEVICEAUTHZSTATUS']._serialized_start=6977
  _globals['_DEVICEAUTHZSTATUS']._serialized_end=7107
  _globals['_CONFIGVALIDATIONSKIPCAUSE']._serialized_start=7110
  _globals['_CONFIGVALIDATIONSKIPCAUSE']._serialized_end=7435
  _globals['_IMAGEVALIDATIONSKIPCAUSE']._serialized_start=7438
  _globals['_IMAGEVALIDATIONSKIPCAUSE']._serialized_end=7703
  _globals['_CONFIGSYNCSKIPCAUSE']._serialized_start=7706
  _globals['_CONFIGSYNCSKIPCAUSE']._serialized_end=7890
  _globals['_SYNCOPERATION']._serialized_start=7892
  _globals['_SYNCOPERATION']._serialized_end=7966
  _globals['_REQUESTPARAMS']._serialized_start=251
  _globals['_REQUESTPARAMS']._serialized_end=316
  _globals['_RESPONSE']._serialized_start=319
  _globals['_RESPONSE']._serialized_end=478
  _globals['_RESPONSES']._serialized_start=481
  _globals['_RESPONSES']._serialized_end=630
  _globals['_RESPONSES_VALUESENTRY']._serialized_start=554
  _globals['_RESPONSES_VALUESENTRY']._serialized_end=630
  _globals['_WORKSPACEKEY']._serialized_start=632
  _globals['_WORKSPACEKEY']._serialized_end=704
  _globals['_WORKSPACECONFIG']._serialized_start=707
  _globals['_WORKSPACECONFIG']._serialized_end=990
  _globals['_WORKSPACE']._serialized_start=993
  _globals['_WORKSPACE']._serialized_end=1716
  _globals['_INPUTERROR']._serialized_start=1719
  _globals['_INPUTERROR']._serialized_end=1899
  _globals['_INPUTERRORS']._serialized_start=1901
  _globals['_INPUTERRORS']._serialized_end=1963
  _globals['_INPUTVALIDATIONRESULT']._serialized_start=1966
  _globals['_INPUTVALIDATIONRESULT']._serialized_end=2157
  _globals['_INPUTVALIDATIONRESULTS']._serialized_start=2160
  _globals['_INPUTVALIDATIONRESULTS']._serialized_end=2348
  _globals['_INPUTVALIDATIONRESULTS_VALUESENTRY']._serialized_start=2259
  _globals['_INPUTVALIDATIONRESULTS_VALUESENTRY']._serialized_end=2348
  _globals['_TEMPLATEERROR']._serialized_start=2351
  _globals['_TEMPLATEERROR']._serialized_end=2562
  _globals['_TEMPLATEERRORS']._serialized_start=2564
  _globals['_TEMPLATEERRORS']._serialized_end=2632
  _globals['_CONFIGLETBUILDRESULT']._serialized_start=2635
  _globals['_CONFIGLETBUILDRESULT']._serialized_end=2934
  _globals['_CONFIGLETBUILDRESULTS']._serialized_start=2937
  _globals['_CONFIGLETBUILDRESULTS']._serialized_end=3122
  _globals['_CONFIGLETBUILDRESULTS_VALUESENTRY']._serialized_start=3034
  _globals['_CONFIGLETBUILDRESULTS_VALUESENTRY']._serialized_end=3122
  _globals['_CONFIGVALIDATIONRESULT']._serialized_start=3125
  _globals['_CONFIGVALIDATIONRESULT']._serialized_end=3378
  _globals['_IMAGEVALIDATIONRESULT']._serialized_start=3381
  _globals['_IMAGEVALIDATIONRESULT']._serialized_end=3673
  _globals['_CONFIGSYNCRESULT']._serialized_start=3676
  _globals['_CONFIGSYNCRESULT']._serialized_end=3867
  _globals['_BUILDSTAGESTATE']._serialized_start=3870
  _globals['_BUILDSTAGESTATE']._serialized_end=4033
  _globals['_BUILDSTAGESTATE_VALUESENTRY']._serialized_start=3955
  _globals['_BUILDSTAGESTATE_VALUESENTRY']._serialized_end=4033
  _globals['_AUTHZRESULT']._serialized_start=4036
  _globals['_AUTHZRESULT']._serialized_end=4227
  _globals['_WORKSPACEBUILDKEY']._serialized_start=4229
  _globals['_WORKSPACEBUILDKEY']._serialized_end=4354
  _globals['_WORKSPACEBUILD']._serialized_start=4357
  _globals['_WORKSPACEBUILD']._serialized_end=4637
  _globals['_WORKSPACEBUILDDETAILSKEY']._serialized_start=4640
  _globals['_WORKSPACEBUILDDETAILSKEY']._serialized_end=4821
  _globals['_WORKSPACEBUILDDETAILS']._serialized_start=4824
  _globals['_WORKSPACEBUILDDETAILS']._serialized_end=5761
  _globals['_WORKSPACESYNCKEY']._serialized_start=5764
  _globals['_WORKSPACESYNCKEY']._serialized_end=5900
  _globals['_WORKSPACESYNCCONFIG']._serialized_start=5902
  _globals['_WORKSPACESYNCCONFIG']._serialized_end=6024
# @@protoc_insertion_point(module_scope)
