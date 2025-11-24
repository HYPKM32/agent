# Google ADK Tools Google API Tool API Reference

`google.adk.tools.google_api_tool` 모듈의 API 레퍼런스 문서입니다.

Google API용 자동 생성 도구 및 툴셋입니다.

이러한 도구와 툴셋은 Google API Discovery API에서 제공하는 API 사양을 기반으로 자동 생성됩니다.

## 클래스

### GoogleApiTool

```python
class google.adk.tools.google_api_tool.GoogleApiTool(rest_api_tool, client_id=None, client_secret=None, service_account=None)
```

**상속**: `BaseTool`

#### 필드

- **description**: `str` - 도구의 설명
- **name**: `str` - 도구의 이름

#### 메소드

##### `configure_auth(client_id, client_secret)`

인증을 구성합니다.

##### `configure_sa_auth(service_account)`

서비스 계정 인증을 구성합니다.

##### `async run_async(*, args, tool_context)`

주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Dict[str, Any]`

> **참고**
> - 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다.
> - 그렇지 않으면 생략할 수 있습니다. 예: Gemini용 내장 GoogleSearch 도구의 경우.

**매개변수:**
- **args** – LLM이 채운 인자들
- **tool_context** – 도구의 컨텍스트

**반환값:** 도구 실행 결과

---

### GoogleApiToolset

```python
class google.adk.tools.google_api_tool.GoogleApiToolset(api_name, api_version, client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `BaseToolset`

Google API Toolset은 Google API와 상호 작용하기 위한 도구를 포함합니다.

일반적으로 하나의 툴셋은 하나의 Google API와만 관련된 도구를 포함합니다. 예를 들어, Google BigQuery API 툴셋은 데이터셋 나열 도구, 테이블 나열 도구 등과 같이 Google BigQuery API와만 관련된 도구를 포함합니다.

#### 메소드

##### `async close()`

툴셋이 보유한 리소스를 정리하고 해제합니다.

> **참고**
> 이 메소드는 예를 들어 에이전트 서버의 생명주기 끝이나 툴셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 모든 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되어 누수를 방지하도록 해야 합니다.

##### `configure_auth(client_id, client_secret)`

인증을 구성합니다.

##### `configure_sa_auth(service_account)`

서비스 계정 인증을 구성합니다.

##### `async get_tools(readonly_context=None)`

툴셋의 모든 도구를 가져옵니다.

- **반환 타입**: `List[GoogleApiTool]`

##### `set_tool_filter(tool_filter)`

도구 필터를 설정합니다.

---

### BigQueryToolset

```python
class google.adk.tools.google_api_tool.BigQueryToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 Google BigQuery API v2 사양을 기반으로 자동 생성된 BigQuery 툴셋입니다.

---

### CalendarToolset

```python
class google.adk.tools.google_api_tool.CalendarToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 Google Calendar API v3 사양을 기반으로 자동 생성된 Calendar 툴셋입니다.

---

### DocsToolset

```python
class google.adk.tools.google_api_tool.DocsToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 Google Docs API v1 사양을 기반으로 자동 생성된 Docs 툴셋입니다.

---

### GmailToolset

```python
class google.adk.tools.google_api_tool.GmailToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 Google Gmail API v1 사양을 기반으로 자동 생성된 Gmail 툴셋입니다.

---

### SheetsToolset

```python
class google.adk.tools.google_api_tool.SheetsToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 Google Sheets API v4 사양을 기반으로 자동 생성된 Sheets 툴셋입니다.

---

### SlidesToolset

```python
class google.adk.tools.google_api_tool.SlidesToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 Google Slides API v1 사양을 기반으로 자동 생성된 Slides 툴셋입니다.

---

### YoutubeToolset

```python
class google.adk.tools.google_api_tool.YoutubeToolset(client_id=None, client_secret=None, tool_filter=None, service_account=None)
```

**상속**: `GoogleApiToolset`

Google API Discovery API에서 노출하는 YouTube API v3 사양을 기반으로 자동 생성된 YouTube 툴셋입니다.