# Google ADK Tools Preload Memory Tool API Reference

`google.adk.tools.preload_memory_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### PreloadMemoryTool

```python
class google.adk.tools.preload_memory_tool.PreloadMemoryTool
```

**상속**: `BaseTool`

현재 사용자의 메모리를 미리 로드하는 도구입니다.

> **참고**: 현재 이 도구는 메모리에서 텍스트 부분만 사용합니다.

#### 필드

- **description**: `str` - 도구의 설명
- **name**: `str` - 도구의 이름

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