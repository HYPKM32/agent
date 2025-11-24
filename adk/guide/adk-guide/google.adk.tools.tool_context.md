# Google ADK Tools Tool Context API Reference

`google.adk.tools.tool_context` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### ToolContext

```python
class google.adk.tools.tool_context.ToolContext(invocation_context, *, function_call_id=None, event_actions=None)
```

**상속**: `CallbackContext`

도구의 컨텍스트입니다.

이 클래스는 도구 호출에 대한 컨텍스트를 제공하며, 호출 컨텍스트, 함수 호출 ID, 이벤트 액션 및 인증 응답에 대한 액세스를 포함합니다. 또한 자격 증명 요청, 인증 응답 검색, 아티팩트 나열 및 메모리 검색을 위한 메소드를 제공합니다.

#### 필드

- **invocation_context** - 도구의 호출 컨텍스트
- **function_call_id** - 현재 도구 호출의 함수 호출 ID. 이 ID는 LLM에서 함수 호출을 식별하기 위해 함수 호출 이벤트에서 반환되었습니다. LLM이 이 ID를 반환하지 않으면, ADK가 하나를 할당합니다. 이 ID는 함수 호출 응답을 원래 함수 호출에 매핑하는 데 사용됩니다.
- **event_actions** - 현재 도구 호출의 이벤트 액션

#### 속성

##### `property actions: EventActions`

#### 메소드

##### `get_auth_response(auth_config)`

- **반환 타입**: `AuthCredential`

##### `request_credential(auth_config)`

- **반환 타입**: `None`

##### `async search_memory(query)`

현재 사용자의 메모리를 검색합니다.

- **반환 타입**: `SearchMemoryResponse`