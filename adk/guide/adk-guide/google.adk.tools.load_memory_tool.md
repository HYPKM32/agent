# Google ADK Tools Load Memory Tool API Reference

`google.adk.tools.load_memory_tool` 모듈의 API 레퍼런스 문서입니다.

## 모델

### LoadMemoryResponse

```python
pydantic model google.adk.tools.load_memory_tool.LoadMemoryResponse
```

**상속**: `BaseModel`

#### 필드

- **memories**: `list[MemoryEntry]` [선택사항]

##### `field memories: list[MemoryEntry] [Optional]`

## 클래스

### LoadMemoryTool

```python
class google.adk.tools.load_memory_tool.LoadMemoryTool
```

**상속**: `FunctionTool`

현재 사용자의 메모리를 로드하는 도구입니다.

> **참고**: 현재 이 도구는 메모리에서 텍스트 부분만 사용합니다.

#### 생성자

호출 가능한 객체에서 메타데이터를 추출합니다.

#### 메소드

##### `async process_llm_request(*, tool_context, llm_request)`

이 도구에 대한 나가는 LLM 요청을 처리합니다.

**사용 사례:**
- 가장 일반적인 사용 사례는 LLM 요청에 이 도구를 추가하는 것입니다.
- 일부 도구는 LLM 요청이 전송되기 전에 전처리만 할 수 있습니다.

- **반환 타입**: `None`
- **매개변수**:
  - **tool_context** – 도구의 컨텍스트
  - **llm_request** – 나가는 LLM 요청, 이 메소드에서 변경 가능

## 함수

### load_memory

```python
async google.adk.tools.load_memory_tool.load_memory(query, tool_context)
```

현재 사용자의 메모리를 로드합니다.

- **반환 타입**: `LoadMemoryResponse`
- **매개변수**:
  - **query** – 메모리를 로드할 쿼리
- **반환값**: 메모리 결과 목록