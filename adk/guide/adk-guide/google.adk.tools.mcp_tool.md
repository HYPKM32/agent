# Google ADK Tools MCP Tool API Reference

`google.adk.tools.mcp_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### MCPTool

```python
class google.adk.tools.mcp_tool.MCPTool(*, mcp_tool, mcp_session_manager, auth_scheme=None, auth_credential=None)
```

**상속**: `BaseAuthenticatedTool`

MCP Tool을 ADK Tool로 변환합니다.

내부적으로 이 도구는 MCP Tool에서 초기화되고 MCP Session을 사용하여 도구를 호출합니다.

> **참고**: API 키 인증의 경우, 헤더 기반 API 키만 지원됩니다. 쿼리 및 쿠키 기반 API 키는 인증 오류를 발생시킵니다.

#### 생성자

MCPTool을 초기화합니다.

이 도구는 MCP Tool 인터페이스를 래핑하고 세션 관리자를 사용하여 MCP 서버와 통신합니다.

**매개변수:**
- **mcp_tool** – 래핑할 MCP 도구
- **mcp_session_manager** – 통신에 사용할 MCP 세션 관리자
- **auth_scheme** – 사용할 인증 스키마
- **auth_credential** – 사용할 인증 자격 증명

**예외:**
- **ValueError** – mcp_tool 또는 mcp_session_manager가 None인 경우

---

### MCPToolset

```python
class google.adk.tools.mcp_tool.MCPToolset(*, connection_params, tool_filter=None, errlog=<crewai.llm.FilteredStream object>, auth_scheme=None, auth_credential=None)
```

**상속**: `BaseToolset`

MCP 서버에 연결하고 MCP Tools를 ADK Tools로 검색합니다.

이 툴셋은 MCP 서버에 대한 연결을 관리하고 에이전트가 사용할 수 있는 도구를 제공합니다. 에이전트 프레임워크와의 쉬운 통합을 위해 BaseToolset 인터페이스를 적절히 구현합니다.

#### 사용법

```python
toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command='npx',
        args=["-y", "@modelcontextprotocol/server-filesystem"],
    ),
    tool_filter=['read_file', 'list_directory']  # 선택사항: 특정 도구 필터링
)

# 에이전트에서 사용
agent = LlmAgent(
    model='gemini-2.0-flash',
    name='enterprise_assistant',
    instruction='Help user accessing their file systems',
    tools=[toolset],
)

# 정리는 에이전트 프레임워크에서 자동으로 처리됩니다
# 하지만 필요한 경우 수동으로 닫을 수도 있습니다:
# await toolset.close()
```

#### 생성자

MCPToolset을 초기화합니다.

**매개변수:**
- **connection_params** – MCP 서버에 대한 연결 매개변수. 다음 중 하나일 수 있습니다:
  - 로컬 MCP 서버 사용을 위한 `StdioConnectionParams` (예: npx 또는 python3 사용)
  - 로컬/원격 SSE 서버를 위한 `SseConnectionParams`
  - 로컬/원격 Streamable HTTP 서버를 위한 `StreamableHTTPConnectionParams`
  - `StdioServerParameters`도 로컬 MCP 서버 사용을 위해 지원되지만, 타임아웃을 지원하지 않으므로 타임아웃이 필요한 경우 `StdioConnectionParams` 사용을 권장합니다.
- **tool_filter** – 특정 도구를 선택하는 선택적 필터. 다음 중 하나일 수 있습니다:
  - 포함할 도구 이름 목록
  - 사용자 정의 필터링 로직을 위한 ToolPredicate 함수
- **errlog** – 오류 로깅을 위한 TextIO 스트림
- **auth_scheme** – 도구 호출을 위한 도구의 인증 스키마
- **auth_credential** – 도구 호출을 위한 도구의 인증 자격 증명

#### 메소드

##### `async close()`

툴셋이 보유한 리소스를 정리하고 해제합니다.

이 메소드는 MCP 세션을 닫고 관련된 모든 리소스를 정리합니다. 여러 번 호출하는 것이 안전하도록 설계되었으며 애플리케이션 종료를 차단하지 않도록 정리 오류를 우아하게 처리합니다.

- **반환 타입**: `None`

##### `async get_tools(readonly_context=None)`

제공된 컨텍스트를 기반으로 툴셋의 모든 도구를 반환합니다.

- **반환 타입**: `List[BaseTool]`
- **매개변수**:
  - **readonly_context** – 에이전트가 사용할 수 있는 도구를 필터링하는 데 사용되는 컨텍스트. None인 경우 툴셋의 모든 도구가 반환됩니다.
- **반환값**: 지정된 컨텍스트에서 사용 가능한 도구 목록

---

### SseConnectionParams

```python
pydantic model google.adk.tools.mcp_tool.SseConnectionParams
```

**상속**: `BaseModel`

MCP SSE 연결을 위한 매개변수입니다.

자세한 내용은 MCP SSE Client 문서를 참조하세요: https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/client/sse.py

#### 필드

- **url**: MCP SSE 서버의 URL
- **headers**: MCP SSE 연결의 헤더
- **timeout**: MCP SSE 서버에 연결을 설정하는 타임아웃(초)
- **sse_read_timeout**: MCP SSE 서버에서 데이터를 읽는 타임아웃(초)

##### `field headers: dict[str, Any] | None = None`
##### `field sse_read_timeout: float = 300.0`
##### `field timeout: float = 5.0`
##### `field url: str [Required]`

---

### StdioConnectionParams

```python
pydantic model google.adk.tools.mcp_tool.StdioConnectionParams
```

**상속**: `BaseModel`

MCP Stdio 연결을 위한 매개변수입니다.

#### 필드

- **server_params**: MCP Stdio 서버를 위한 매개변수
- **timeout**: MCP stdio 서버에 연결을 설정하는 타임아웃(초)

##### `field server_params: StdioServerParameters [Required]`
##### `field timeout: float = 5.0`

---

### StreamableHTTPConnectionParams

```python
pydantic model google.adk.tools.mcp_tool.StreamableHTTPConnectionParams
```

**상속**: `BaseModel`

MCP SSE 연결을 위한 매개변수입니다.

자세한 내용은 MCP SSE Client 문서를 참조하세요: https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/client/streamable_http.py

#### 필드

- **url**: MCP Streamable HTTP 서버의 URL
- **headers**: MCP Streamable HTTP 연결의 헤더
- **timeout**: MCP Streamable HTTP 서버에 연결을 설정하는 타임아웃(초)
- **sse_read_timeout**: MCP Streamable HTTP 서버에서 데이터를 읽는 타임아웃(초)
- **terminate_on_close**: 연결이 닫힐 때 MCP Streamable HTTP 서버를 종료할지 여부

##### `field headers: dict[str, Any] | None = None`
##### `field sse_read_timeout: float = 300.0`
##### `field terminate_on_close: bool = True`
##### `field timeout: float = 5.0`
##### `field url: str [Required]`

## 함수

### adk_to_mcp_tool_type

```python
google.adk.tools.mcp_tool.adk_to_mcp_tool_type(tool)
```

ADK의 Tool을 MCP 도구 타입으로 변환합니다.

이 함수는 ADK 도구 정의를 MCP(Model Context Protocol) 시스템의 동등한 표현으로 변환합니다.

- **반환 타입**: `Tool`
- **매개변수**:
  - **tool** – 변환할 ADK 도구. BaseTool에서 파생된 클래스의 인스턴스여야 합니다.
- **반환값**: 변환된 도구를 나타내는 MCP Tool 타입의 객체

#### 예시

```python
# 'my_tool'이 BaseTool 파생 클래스의 인스턴스라고 가정
mcp_tool = adk_to_mcp_tool_type(my_tool)
print(mcp_tool)
```

### gemini_to_json_schema

```python
google.adk.tools.mcp_tool.gemini_to_json_schema(gemini_schema)
```

Gemini Schema 객체를 JSON Schema 딕셔너리로 변환합니다.

- **반환 타입**: `Dict[str, Any]`
- **매개변수**:
  - **gemini_schema** – Gemini Schema 클래스의 인스턴스
- **반환값**: 동등한 JSON Schema를 나타내는 딕셔너리

**예외:**
- **TypeError** – 입력이 예상되는 Schema 클래스의 인스턴스가 아닌 경우
- **ValueError** – 잘못된 Gemini Type enum 값이 발견된 경우