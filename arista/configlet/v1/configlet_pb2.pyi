"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import fmp.wrappers_pb2
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _MatchPolicy:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType
class _MatchPolicyEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_MatchPolicy.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    MATCH_POLICY_UNSPECIFIED: _MatchPolicy.ValueType  # 0
    MATCH_POLICY_MATCH_FIRST: _MatchPolicy.ValueType  # 1
    """MATCH_POLICY_MATCH_FIRST dictates that matching devices are used only for the first match amongst its children"""

    MATCH_POLICY_MATCH_ALL: _MatchPolicy.ValueType  # 2
    """MATCH_POLICY_MATCH_ALL dictates that matching devices are used across all children"""

class MatchPolicy(_MatchPolicy, metaclass=_MatchPolicyEnumTypeWrapper):
    """MatchPolicy specifies how the tag query of a configlet assignment
    should be used to resolve devices for its children
    """
    pass

MATCH_POLICY_UNSPECIFIED: MatchPolicy.ValueType  # 0
MATCH_POLICY_MATCH_FIRST: MatchPolicy.ValueType  # 1
"""MATCH_POLICY_MATCH_FIRST dictates that matching devices are used only for the first match amongst its children"""

MATCH_POLICY_MATCH_ALL: MatchPolicy.ValueType  # 2
"""MATCH_POLICY_MATCH_ALL dictates that matching devices are used across all children"""

global___MatchPolicy = MatchPolicy


class ConfigletKey(google.protobuf.message.Message):
    """ConfigletKey uniquely identifies a static configlet."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WORKSPACE_ID_FIELD_NUMBER: builtins.int
    CONFIGLET_ID_FIELD_NUMBER: builtins.int
    @property
    def workspace_id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """workspace_id identifies the workspace within which the static configlet resides
        empty string ("") stands for the "mainline".
        """
        pass
    @property
    def configlet_id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """configlet_id is the static configlet ID."""
        pass
    def __init__(self,
        *,
        workspace_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        configlet_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["configlet_id",b"configlet_id","workspace_id",b"workspace_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["configlet_id",b"configlet_id","workspace_id",b"workspace_id"]) -> None: ...
global___ConfigletKey = ConfigletKey

class Filter(google.protobuf.message.Message):
    """Filter is used to filter static configlets."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    INCLUDE_BODY_FIELD_NUMBER: builtins.int
    @property
    def include_body(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """include_body specifies the static configlet body is to be included."""
        pass
    def __init__(self,
        *,
        include_body: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["include_body",b"include_body"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["include_body",b"include_body"]) -> None: ...
global___Filter = Filter

class Configlet(google.protobuf.message.Message):
    """Configlet is the state of a static configlet in a workspace or mainline.
    Subscribe and GetAll do not return the "body"
    Use GetOne to get the body of individual configlets
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MIGRATED_FROM_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_AT_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_BY_FIELD_NUMBER: builtins.int
    DIGEST_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___ConfigletKey: ...
    @property
    def display_name(self) -> google.protobuf.wrappers_pb2.StringValue:
        """display_name is the display name of the static configlet."""
        pass
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue:
        """description is the description of the static configlet."""
        pass
    @property
    def migrated_from(self) -> google.protobuf.wrappers_pb2.StringValue:
        """migrated_from is populated with the source configlet name when migrated
        from network provisioning to studio.
        """
        pass
    @property
    def body(self) -> google.protobuf.wrappers_pb2.StringValue:
        """body is the static configlet body."""
        pass
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """created_at is the time when the Configlet was created."""
        pass
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue:
        """created_by is the user who created the Configlet."""
        pass
    @property
    def last_modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """last_modified_at is the time when the Configlet was last modified."""
        pass
    @property
    def last_modified_by(self) -> google.protobuf.wrappers_pb2.StringValue:
        """last_modified_by is the user who last modified the Configlet."""
        pass
    @property
    def digest(self) -> google.protobuf.wrappers_pb2.StringValue:
        """digest is the sha256 hash of the configlet body encoded in hexadecimal."""
        pass
    @property
    def size(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """size of configlet body in bytes."""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___ConfigletKey] = ...,
        display_name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        migrated_from: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        body: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        created_by: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        last_modified_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_modified_by: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        digest: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        size: typing.Optional[google.protobuf.wrappers_pb2.Int64Value] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body",b"body","created_at",b"created_at","created_by",b"created_by","description",b"description","digest",b"digest","display_name",b"display_name","key",b"key","last_modified_at",b"last_modified_at","last_modified_by",b"last_modified_by","migrated_from",b"migrated_from","size",b"size"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","created_at",b"created_at","created_by",b"created_by","description",b"description","digest",b"digest","display_name",b"display_name","key",b"key","last_modified_at",b"last_modified_at","last_modified_by",b"last_modified_by","migrated_from",b"migrated_from","size",b"size"]) -> None: ...
global___Configlet = Configlet

class ConfigletConfig(google.protobuf.message.Message):
    """ConfigletConfig updates a static configlet in a workspace."""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    MIGRATED_FROM_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___ConfigletKey: ...
    @property
    def remove(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """remove specifies the static configlet is to be removed from the workspace.
        Other data fields are not allowed when this field is set to true.
        """
        pass
    @property
    def display_name(self) -> google.protobuf.wrappers_pb2.StringValue:
        """display_name is the display name of the static configlet."""
        pass
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue:
        """description is the description of the static configlet."""
        pass
    @property
    def migrated_from(self) -> google.protobuf.wrappers_pb2.StringValue:
        """migrated_from is populated with the source configlet name when migrated
        from network provisioning to studio.
        """
        pass
    @property
    def body(self) -> google.protobuf.wrappers_pb2.StringValue:
        """body is the static configlet body."""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___ConfigletKey] = ...,
        remove: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        display_name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        migrated_from: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        body: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["body",b"body","description",b"description","display_name",b"display_name","key",b"key","migrated_from",b"migrated_from","remove",b"remove"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["body",b"body","description",b"description","display_name",b"display_name","key",b"key","migrated_from",b"migrated_from","remove",b"remove"]) -> None: ...
global___ConfigletConfig = ConfigletConfig

class ConfigletAssignmentKey(google.protobuf.message.Message):
    """ConfigletAssignmentKey uniquely identifies a configlet assignment"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    WORKSPACE_ID_FIELD_NUMBER: builtins.int
    CONFIGLET_ASSIGNMENT_ID_FIELD_NUMBER: builtins.int
    @property
    def workspace_id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """workspace_id is the unique identifier of the workspace."""
        pass
    @property
    def configlet_assignment_id(self) -> google.protobuf.wrappers_pb2.StringValue:
        """configlet_assignment_id is the unique identifier of the configlet_assignment."""
        pass
    def __init__(self,
        *,
        workspace_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        configlet_assignment_id: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["configlet_assignment_id",b"configlet_assignment_id","workspace_id",b"workspace_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["configlet_assignment_id",b"configlet_assignment_id","workspace_id",b"workspace_id"]) -> None: ...
global___ConfigletAssignmentKey = ConfigletAssignmentKey

class ConfigletAssignmentConfig(google.protobuf.message.Message):
    """ConfigletAssignmentConfig are the the inputs to the static configlet studio.
    Each assignment assigns a list of configlets to the devices matching the tag query.
    Individual assignments can have a list of "child" assignments.
    The totality of these assignments form a list of tree hierarchies.
    Using the corresponding GUI workflow should help explain this structure.
    When traversing a tree and assigning static configlets to devices, the following rules
    are applied:
    1) Tag queries at each level need to resolve to a subset of its parent's queries.
    Devices resolved in child assignments but which do not resolve in that of its parent's
    are skipped.
    2) Match policy determines how the assignment's devices get divied up amongst its children.
    """
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CONFIGLET_IDS_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    MATCH_POLICY_FIELD_NUMBER: builtins.int
    CHILD_ASSIGNMENT_IDS_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___ConfigletAssignmentKey: ...
    @property
    def display_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def configlet_ids(self) -> fmp.wrappers_pb2.RepeatedString:
        """configlet_ids is the list of configlets to be assigned"""
        pass
    @property
    def query(self) -> google.protobuf.wrappers_pb2.StringValue:
        """query is a tag query string that conforms to the CloudVision
        tag query language. E.g., the query, `"datacenter:NYC,SFO AND
        sflow:enabled"`, matches all devices with sflow enabled in
        data centers NYC and SFO.
        malformed queries result in an error
        tags not matching devices are ignored
        """
        pass
    @property
    def remove(self) -> google.protobuf.wrappers_pb2.BoolValue:
        """remove indicates whether to remove (`true`) or add (`false`,
        unset) the tag assignments involving the studio identified
        by the key if the encompassing workspace merges. Other data
        fields are not allowed if this field is set to true.
        """
        pass
    match_policy: global___MatchPolicy.ValueType
    """match_policy is the discriminator for the query field"""

    @property
    def child_assignment_ids(self) -> fmp.wrappers_pb2.RepeatedString:
        """list of child assignments"""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___ConfigletAssignmentKey] = ...,
        display_name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        configlet_ids: typing.Optional[fmp.wrappers_pb2.RepeatedString] = ...,
        query: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        remove: typing.Optional[google.protobuf.wrappers_pb2.BoolValue] = ...,
        match_policy: global___MatchPolicy.ValueType = ...,
        child_assignment_ids: typing.Optional[fmp.wrappers_pb2.RepeatedString] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["child_assignment_ids",b"child_assignment_ids","configlet_ids",b"configlet_ids","description",b"description","display_name",b"display_name","key",b"key","query",b"query","remove",b"remove"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["child_assignment_ids",b"child_assignment_ids","configlet_ids",b"configlet_ids","description",b"description","display_name",b"display_name","key",b"key","match_policy",b"match_policy","query",b"query","remove",b"remove"]) -> None: ...
global___ConfigletAssignmentConfig = ConfigletAssignmentConfig

class ConfigletAssignment(google.protobuf.message.Message):
    """ConfigletAssignment is the state of this assignment in a workspace/mainline"""
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    CONFIGLET_IDS_FIELD_NUMBER: builtins.int
    QUERY_FIELD_NUMBER: builtins.int
    MATCH_POLICY_FIELD_NUMBER: builtins.int
    CHILD_ASSIGNMENT_IDS_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    CREATED_BY_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_AT_FIELD_NUMBER: builtins.int
    LAST_MODIFIED_BY_FIELD_NUMBER: builtins.int
    @property
    def key(self) -> global___ConfigletAssignmentKey: ...
    @property
    def display_name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def description(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def configlet_ids(self) -> fmp.wrappers_pb2.RepeatedString:
        """configlet_ids is the list of configlets which are assigned"""
        pass
    @property
    def query(self) -> google.protobuf.wrappers_pb2.StringValue:
        """query represents the tag query assigned"""
        pass
    match_policy: global___MatchPolicy.ValueType
    """match_policy is the discriminator for the query field"""

    @property
    def child_assignment_ids(self) -> fmp.wrappers_pb2.RepeatedString:
        """list of child assignments"""
        pass
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """created_at is the time when the ConfigletAssignment was created."""
        pass
    @property
    def created_by(self) -> google.protobuf.wrappers_pb2.StringValue:
        """created_by is the user who created the ConfigletAssignment."""
        pass
    @property
    def last_modified_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """last_modified_at is the time when the ConfigletAssignment
        was last modified.
        """
        pass
    @property
    def last_modified_by(self) -> google.protobuf.wrappers_pb2.StringValue:
        """last_modified_by is the user who last modified the ConfigletAssignment."""
        pass
    def __init__(self,
        *,
        key: typing.Optional[global___ConfigletAssignmentKey] = ...,
        display_name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        description: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        configlet_ids: typing.Optional[fmp.wrappers_pb2.RepeatedString] = ...,
        query: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        match_policy: global___MatchPolicy.ValueType = ...,
        child_assignment_ids: typing.Optional[fmp.wrappers_pb2.RepeatedString] = ...,
        created_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        created_by: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        last_modified_at: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = ...,
        last_modified_by: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["child_assignment_ids",b"child_assignment_ids","configlet_ids",b"configlet_ids","created_at",b"created_at","created_by",b"created_by","description",b"description","display_name",b"display_name","key",b"key","last_modified_at",b"last_modified_at","last_modified_by",b"last_modified_by","query",b"query"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["child_assignment_ids",b"child_assignment_ids","configlet_ids",b"configlet_ids","created_at",b"created_at","created_by",b"created_by","description",b"description","display_name",b"display_name","key",b"key","last_modified_at",b"last_modified_at","last_modified_by",b"last_modified_by","match_policy",b"match_policy","query",b"query"]) -> None: ...
global___ConfigletAssignment = ConfigletAssignment
