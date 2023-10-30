from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageDestroyRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MessageListRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class MessageListResponse(_message.Message):
    __slots__ = ["results"]
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MessageResponse]
    def __init__(self, results: _Optional[_Iterable[_Union[MessageResponse, _Mapping]]] = ...) -> None: ...

class MessagePartialUpdateRequest(_message.Message):
    __slots__ = ["id", "chat", "user", "message", "_partial_update_fields"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    _PARTIAL_UPDATE_FIELDS_FIELD_NUMBER: _ClassVar[int]
    id: int
    chat: int
    user: int
    message: str
    _partial_update_fields: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., chat: _Optional[int] = ..., user: _Optional[int] = ..., message: _Optional[str] = ..., _partial_update_fields: _Optional[_Iterable[str]] = ...) -> None: ...

class MessageRequest(_message.Message):
    __slots__ = ["id", "chat", "user", "message"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: int
    chat: int
    user: int
    message: str
    def __init__(self, id: _Optional[int] = ..., chat: _Optional[int] = ..., user: _Optional[int] = ..., message: _Optional[str] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ["id", "chat", "user", "message", "date"]
    ID_FIELD_NUMBER: _ClassVar[int]
    CHAT_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    chat: int
    user: int
    message: str
    date: str
    def __init__(self, id: _Optional[int] = ..., chat: _Optional[int] = ..., user: _Optional[int] = ..., message: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class MessageRetrieveRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...
