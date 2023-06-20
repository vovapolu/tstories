from google.api import annotations_pb2 as _annotations_pb2
from protoc_gen_openapiv2.options import annotations_pb2 as _annotations_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatCompletionChoice(_message.Message):
    __slots__ = ["finish_reason", "index", "message"]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    finish_reason: str
    index: int
    message: ChatCompletionMessage
    def __init__(self, index: _Optional[int] = ..., message: _Optional[_Union[ChatCompletionMessage, _Mapping]] = ..., finish_reason: _Optional[str] = ...) -> None: ...

class ChatCompletionMessage(_message.Message):
    __slots__ = ["content", "name", "role"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    content: str
    name: str
    role: str
    def __init__(self, role: _Optional[str] = ..., content: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class ChatCompletionStreamChoice(_message.Message):
    __slots__ = ["delta", "finish_reason", "index"]
    DELTA_FIELD_NUMBER: _ClassVar[int]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    delta: ChatCompletionStreamChoiceDelta
    finish_reason: str
    index: int
    def __init__(self, index: _Optional[int] = ..., delta: _Optional[_Union[ChatCompletionStreamChoiceDelta, _Mapping]] = ..., finish_reason: _Optional[str] = ...) -> None: ...

class ChatCompletionStreamChoiceDelta(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class ChatCompletionStreamV1Response(_message.Message):
    __slots__ = ["choices", "created", "id", "model", "object"]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    choices: _containers.RepeatedCompositeFieldContainer[ChatCompletionStreamChoice]
    created: int
    id: str
    model: str
    object: str
    def __init__(self, id: _Optional[str] = ..., object: _Optional[str] = ..., created: _Optional[int] = ..., model: _Optional[str] = ..., choices: _Optional[_Iterable[_Union[ChatCompletionStreamChoice, _Mapping]]] = ...) -> None: ...

class ChatCompletionV1Request(_message.Message):
    __slots__ = ["frequency_penalty", "logit_bias", "max_tokens", "messages", "model", "n", "presence_penalty", "stop", "temperature", "top_p", "user"]
    class LogitBiasEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    LOGIT_BIAS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    frequency_penalty: float
    logit_bias: _containers.ScalarMap[str, int]
    max_tokens: int
    messages: _containers.RepeatedCompositeFieldContainer[ChatCompletionMessage]
    model: str
    n: int
    presence_penalty: float
    stop: _containers.RepeatedScalarFieldContainer[str]
    temperature: float
    top_p: float
    user: str
    def __init__(self, model: _Optional[str] = ..., messages: _Optional[_Iterable[_Union[ChatCompletionMessage, _Mapping]]] = ..., max_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., n: _Optional[int] = ..., stop: _Optional[_Iterable[str]] = ..., presence_penalty: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., logit_bias: _Optional[_Mapping[str, int]] = ..., user: _Optional[str] = ...) -> None: ...

class ChatCompletionV1Response(_message.Message):
    __slots__ = ["choices", "created", "id", "model", "object", "usage"]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    choices: _containers.RepeatedCompositeFieldContainer[ChatCompletionChoice]
    created: int
    id: str
    model: str
    object: str
    usage: Usage
    def __init__(self, id: _Optional[str] = ..., object: _Optional[str] = ..., created: _Optional[int] = ..., model: _Optional[str] = ..., choices: _Optional[_Iterable[_Union[ChatCompletionChoice, _Mapping]]] = ..., usage: _Optional[_Union[Usage, _Mapping]] = ...) -> None: ...

class CompletionChoice(_message.Message):
    __slots__ = ["finish_reason", "index", "logprobs", "text"]
    FINISH_REASON_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    finish_reason: str
    index: int
    logprobs: LogprobResult
    text: str
    def __init__(self, text: _Optional[str] = ..., index: _Optional[int] = ..., finish_reason: _Optional[str] = ..., logprobs: _Optional[_Union[LogprobResult, _Mapping]] = ...) -> None: ...

class CompletionV1Request(_message.Message):
    __slots__ = ["best_of", "echo", "frequency_penalty", "logit_bias", "logprobs", "max_tokens", "model", "n", "presence_penalty", "prompt", "stop", "suffix", "temperature", "top_p", "user"]
    class LogitBiasEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int
        def __init__(self, key: _Optional[str] = ..., value: _Optional[int] = ...) -> None: ...
    BEST_OF_FIELD_NUMBER: _ClassVar[int]
    ECHO_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_PENALTY_FIELD_NUMBER: _ClassVar[int]
    LOGIT_BIAS_FIELD_NUMBER: _ClassVar[int]
    LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    N_FIELD_NUMBER: _ClassVar[int]
    PRESENCE_PENALTY_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    TOP_P_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    best_of: int
    echo: bool
    frequency_penalty: float
    logit_bias: _containers.ScalarMap[str, int]
    logprobs: int
    max_tokens: int
    model: str
    n: int
    presence_penalty: float
    prompt: _containers.RepeatedScalarFieldContainer[str]
    stop: _containers.RepeatedScalarFieldContainer[str]
    suffix: str
    temperature: float
    top_p: float
    user: str
    def __init__(self, model: _Optional[str] = ..., prompt: _Optional[_Iterable[str]] = ..., suffix: _Optional[str] = ..., max_tokens: _Optional[int] = ..., temperature: _Optional[float] = ..., top_p: _Optional[float] = ..., n: _Optional[int] = ..., logprobs: _Optional[int] = ..., echo: bool = ..., stop: _Optional[_Iterable[str]] = ..., presence_penalty: _Optional[float] = ..., frequency_penalty: _Optional[float] = ..., best_of: _Optional[int] = ..., logit_bias: _Optional[_Mapping[str, int]] = ..., user: _Optional[str] = ...) -> None: ...

class CompletionV1Response(_message.Message):
    __slots__ = ["choices", "created", "id", "model", "object", "usage"]
    CHOICES_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    OBJECT_FIELD_NUMBER: _ClassVar[int]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    choices: _containers.RepeatedCompositeFieldContainer[CompletionChoice]
    created: int
    id: str
    model: str
    object: str
    usage: Usage
    def __init__(self, id: _Optional[str] = ..., object: _Optional[str] = ..., created: _Optional[int] = ..., model: _Optional[str] = ..., choices: _Optional[_Iterable[_Union[CompletionChoice, _Mapping]]] = ..., usage: _Optional[_Union[Usage, _Mapping]] = ...) -> None: ...

class LogprobResult(_message.Message):
    __slots__ = ["text_offset", "token_logprobs", "tokens", "top_logprobs"]
    TEXT_OFFSET_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOKEN_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    TOP_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    text_offset: _containers.RepeatedScalarFieldContainer[int]
    token_logprobs: _containers.RepeatedScalarFieldContainer[float]
    tokens: _containers.RepeatedScalarFieldContainer[str]
    top_logprobs: _containers.RepeatedCompositeFieldContainer[TopLogprobs]
    def __init__(self, tokens: _Optional[_Iterable[str]] = ..., token_logprobs: _Optional[_Iterable[float]] = ..., top_logprobs: _Optional[_Iterable[_Union[TopLogprobs, _Mapping]]] = ..., text_offset: _Optional[_Iterable[int]] = ...) -> None: ...

class TopLogprobs(_message.Message):
    __slots__ = ["top_logprobs"]
    class TopLogprobsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: float
        def __init__(self, key: _Optional[str] = ..., value: _Optional[float] = ...) -> None: ...
    TOP_LOGPROBS_FIELD_NUMBER: _ClassVar[int]
    top_logprobs: _containers.ScalarMap[str, float]
    def __init__(self, top_logprobs: _Optional[_Mapping[str, float]] = ...) -> None: ...

class Usage(_message.Message):
    __slots__ = ["completion_tokens", "prompt_tokens", "total_tokens"]
    COMPLETION_TOKENS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    def __init__(self, prompt_tokens: _Optional[int] = ..., completion_tokens: _Optional[int] = ..., total_tokens: _Optional[int] = ...) -> None: ...
