# Google ADK Tools Vertex AI Search Tool API Reference

`google.adk.tools.vertex_ai_search_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### VertexAiSearchTool

```python
class google.adk.tools.vertex_ai_search_tool.VertexAiSearchTool(*, data_store_id=None, data_store_specs=None, search_engine_id=None, filter=None, max_results=None)
```

**상속**: `BaseTool`

Vertex AI Search를 사용하는 내장 도구입니다.

#### 필드

- **data_store_id** - Vertex AI 검색 데이터 스토어 리소스 ID
- **search_engine_id** - Vertex AI 검색 엔진 리소스 ID

#### 생성자

Vertex AI Search 도구를 초기화합니다.

**매개변수:**
- **data_store_id** – "projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}" 형식의 Vertex AI 검색 데이터 스토어 리소스 ID
- **data_store_specs** – 검색할 특정 DataStore를 정의하는 사양. 엔진이 사용되는 경우에만 설정해야 합니다.
- **search_engine_id** – "projects/{project}/locations/{location}/collections/{collection}/engines/{engine}" 형식의 Vertex AI 검색 엔진 리소스 ID

**예외:**
- **ValueError** – data_store_id와 search_engine_id가 모두 지정되지 않았거나 둘 다 지정된 경우

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