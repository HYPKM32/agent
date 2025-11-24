# Google ADK Tools Retrieval API Reference

`google.adk.tools.retrieval` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseRetrievalTool

```python
class google.adk.tools.retrieval.BaseRetrievalTool(*, name, description, is_long_running=False)
```

**상속**: `BaseTool`

#### 필드

- **description**: `str` - 도구의 설명
- **name**: `str` - 도구의 이름

---

### LlamaIndexRetrieval

```python
class google.adk.tools.retrieval.LlamaIndexRetrieval(*, name, description, retriever)
```

**상속**: `BaseRetrievalTool`

#### 필드

- **description**: `str` - 도구의 설명
- **name**: `str` - 도구의 이름

#### 메소드

##### `async run_async(*, args, tool_context)`

주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`

> **참고**
> - 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다.
> - 그렇지 않으면 생략할 수 있습니다. 예: Gemini용 내장 GoogleSearch 도구의 경우.

**매개변수:**
- **args** – LLM이 채운 인자들
- **tool_context** – 도구의 컨텍스트

**반환값:** 도구 실행 결과

---

### FilesRetrieval

```python
class google.adk.tools.retrieval.FilesRetrieval(*, name, description, input_dir)
```

**상속**: `LlamaIndexRetrieval`

#### 필드

- **description**: `str` - 도구의 설명
- **name**: `str` - 도구의 이름

---

### VertexAiRagRetrieval

```python
class google.adk.tools.retrieval.VertexAiRagRetrieval(*, name, description, rag_corpora=None, rag_resources=None, similarity_top_k=None, vector_distance_threshold=None)
```

**상속**: `BaseRetrievalTool`

Vertex AI RAG(Retrieval-Augmented Generation)를 사용하여 데이터를 검색하는 검색 도구입니다.

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

##### `async run_async(*, args, tool_context)`

주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`

> **참고**
> - 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다.
> - 그렇지 않으면 생략할 수 있습니다. 예: Gemini용 내장 GoogleSearch 도구의 경우.

**매개변수:**
- **args** – LLM이 채운 인자들
- **tool_context** – 도구의 컨텍스트

**반환값:** 도구 실행 결과