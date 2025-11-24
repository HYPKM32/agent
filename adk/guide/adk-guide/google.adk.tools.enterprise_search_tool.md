# Google ADK Tools Enterprise Search Tool API Reference

`google.adk.tools.enterprise_search_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### EnterpriseWebSearchTool

```python
class google.adk.tools.enterprise_search_tool.EnterpriseWebSearchTool
```

**상속**: `BaseTool`

기업 규정 준수를 위한 웹 그라운딩을 사용하는 Gemini 2+ 내장 도구입니다.

자세한 내용은 문서를 참조하세요: https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/web-grounding-enterprise

#### 생성자

Vertex AI Search 도구를 초기화합니다.

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