# Google ADK Tools Base Toolset API Reference

`google.adk.tools.base_toolset` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseToolset

```python
class google.adk.tools.base_toolset.BaseToolset(*, tool_filter=None)
```

**상속**: `ABC`

툴셋의 기본 클래스입니다.

툴셋은 에이전트가 사용할 수 있는 도구들의 컬렉션입니다.

#### 추상 메소드

##### `abstractmethod async close()`

툴셋이 보유한 리소스를 정리하고 해제합니다.

- **반환 타입**: `None`

> **참고**
> 이 메소드는 예를 들어 에이전트 서버의 생명주기 끝이나 툴셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 모든 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되어 누수를 방지하도록 해야 합니다.

##### `abstractmethod async get_tools(readonly_context=None)`

제공된 컨텍스트를 기반으로 툴셋의 모든 도구를 반환합니다.

- **반환 타입**: `list[BaseTool]`
- **매개변수**:
  - **readonly_context** (*ReadonlyContext, optional*) – 에이전트가 사용할 수 있는 도구를 필터링하는 데 사용되는 컨텍스트. None인 경우 툴셋의 모든 도구가 반환됩니다.
- **반환값**: 지정된 컨텍스트에서 사용 가능한 도구 목록

#### 메소드

##### `async process_llm_request(*, tool_context, llm_request)`

이 툴셋에 대한 나가는 LLM 요청을 처리합니다. 이 메소드는 각 도구가 LLM 요청을 처리하기 전에 호출됩니다.

- **반환 타입**: `None`

**사용 사례:**
- 각 도구가 LLM 요청을 처리하도록 하는 대신, 툴셋이 LLM 요청을 처리하도록 할 수 있습니다. 예: ComputerUseToolset은 LLM 요청에 컴퓨터 사용 도구를 추가할 수 있습니다.

**매개변수:**
- **tool_context** – 도구의 컨텍스트
- **llm_request** – 나가는 LLM 요청, 이 메소드에서 변경 가능

---

### ToolPredicate

```python
class google.adk.tools.base_toolset.ToolPredicate(*args, **kwargs)
```

**상속**: `Protocol`

도구가 LLM에 노출되어야 하는지 결정하는 인터페이스를 정의하는 술어의 기본 클래스입니다. 툴셋 구현자는 툴셋의 생성자에서 이러한 인스턴스를 받아들일지 고려하고 get_tools 메소드에서 술어를 적용할 수 있습니다.