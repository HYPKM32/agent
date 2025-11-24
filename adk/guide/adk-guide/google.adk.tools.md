# Google ADK Tools Package API Reference

`google.adk.tools` 패키지의 API 레퍼런스 문서입니다.

## 클래스

### APIHubToolset

```python
class google.adk.tools.APIHubToolset(
    *, 
    apihub_resource_name, 
    access_token=None, 
    service_account_json=None, 
    name='', 
    description='', 
    lazy_load_spec=False, 
    auth_scheme=None, 
    auth_credential=None, 
    apihub_client=None, 
    tool_filter=None
)
```

**상속**: `BaseToolset`

API Hub 리소스로부터 도구들을 생성하는 APIHubTool입니다.

#### 매개변수

- **apihub_resource_name**: API Hub에서의 API 리소스 이름 (API 이름 필수, API 버전 및 스펙 이름 선택사항)
- **access_token**: Google Access Token (`gcloud auth print-access-token`으로 생성)
- **service_account_json**: JSON 문자열 형태의 서비스 계정 설정
- **apihub_client**: 선택적 커스텀 API Hub 클라이언트
- **name**: 도구셋의 이름 (선택사항)
- **description**: 도구셋의 설명 (선택사항)
- **auth_scheme**: 도구셋의 모든 도구에 적용되는 인증 스킴
- **auth_credential**: 도구셋의 모든 도구에 적용되는 인증 자격증명
- **lazy_load_spec**: True일 경우 필요할 때 스펙을 지연 로딩
- **tool_filter**: 도구를 필터링하는데 사용되는 필터 (도구 술어 또는 도구 이름 리스트)

#### 리소스 이름 형식

```
projects/xxx/locations/us-central1/apis/apiname/...
```

**콘솔 URL**: `https://console.cloud.google.com/apigee/api-hub/apis/apiname?project=xxx`

#### 스펙 로딩 규칙

- `apihub_resource_name`에 스펙 리소스 이름이 포함된 경우: 해당 스펙의 내용을 사용하여 도구 생성
- API 또는 버전 이름만 포함된 경우: 해당 API의 첫 번째 버전의 첫 번째 스펙을 사용

#### 사용 예시

```python
# 기본 사용법
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/test-project/locations/us-central1/apis/test-api",
    service_account_json="...",
    tool_filter=lambda tool, ctx=None: tool.name in ('my_tool', 'my_other_tool')
)

agent = LlmAgent(tools=apihub_toolset)

# 특정 도구만 사용
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/test-project/locations/us-central1/apis/test-api",
    service_account_json="...",
    tool_filter=['my_tool']
)

agent = LlmAgent(tools=[apihub_toolset])
```

#### 메소드

##### `async close()`
도구셋이 보유한 리소스를 정리하고 해제합니다.

> **참고**: 이 메소드는 에이전트 서버의 생명주기 끝에서 또는 도구셋이 더 이상 필요하지 않을 때 호출됩니다.

##### `async get_tools(readonly_context=None)`
사용 가능한 모든 도구를 검색합니다.

- **반환 타입**: `List[RestApiTool]`
- **반환값**: 사용 가능한 모든 RestApiTool 객체의 리스트

---

### AgentTool

```python
class google.adk.tools.AgentTool(agent, skip_summarization=False)
```

**상속**: `BaseTool`

에이전트를 래핑하는 도구입니다.

이 도구는 더 큰 애플리케이션 내에서 에이전트를 도구로 호출할 수 있게 해줍니다. 에이전트의 입력 스키마가 도구의 입력 매개변수를 정의하는데 사용되고, 에이전트의 출력이 도구의 결과로 반환됩니다.

#### 속성

- **agent**: 래핑할 에이전트
- **skip_summarization**: 에이전트 출력의 요약을 건너뛸지 여부

#### 메소드

##### `classmethod from_config(config, config_abs_path)`
설정으로부터 도구 인스턴스를 생성합니다.

- **반환 타입**: `AgentTool`
- **매개변수**:
  - **config**: 도구의 설정
  - **config_abs_path**: 도구 설정이 포함된 설정 파일의 절대 경로

##### `populate_name()`
- **반환 타입**: `Any`

##### `async run_async(*, args, tool_context)`
주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`
- **매개변수**:
  - **args**: LLM이 채운 인자들
  - **tool_context**: 도구의 컨텍스트

---

### AuthToolArguments

```python
pydantic model google.adk.tools.AuthToolArguments
```

**상속**: `BaseModelWithConfig`

최종 사용자 자격 증명을 요청하는데 사용되는 특별한 장기 실행 함수 도구의 인자입니다.

#### 필드

- **auth_config**: `AuthConfig` (별칭: 'authConfig', 필수)
- **function_call_id**: `str` (별칭: 'functionCallId', 필수)

---

### BaseTool

```python
class google.adk.tools.BaseTool(*, name, description, is_long_running=False)
```

**상속**: `ABC`

모든 도구의 기본 클래스입니다.

#### 속성

- **name**: `str` - 도구의 이름
- **description**: `str` - 도구의 설명
- **is_long_running**: `bool = False` - 장기 실행 작업인지 여부 (일반적으로 리소스 ID를 먼저 반환하고 나중에 작업을 완료)

#### 메소드

##### `classmethod from_config(config, config_abs_path)`
설정으로부터 도구 인스턴스를 생성합니다.

- **반환 타입**: `TypeVar(SelfTool, bound=BaseTool)`
- **매개변수**:
  - **config**: 도구의 설정
  - **config_abs_path**: 도구 설정이 포함된 설정 파일의 절대 경로

##### `async process_llm_request(*, tool_context, llm_request)`
이 도구에 대한 나가는 LLM 요청을 처리합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **tool_context**: 도구의 컨텍스트
  - **llm_request**: 나가는 LLM 요청 (이 메소드에서 변경 가능)

**사용 사례**:
- 가장 일반적인 사용 사례는 LLM 요청에 이 도구를 추가하는 것
- 일부 도구는 LLM 요청이 전송되기 전에 전처리만 수행

##### `async run_async(*, args, tool_context)`
주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`
- **매개변수**:
  - **args**: LLM이 채운 인자들
  - **tool_context**: 도구의 컨텍스트

> **참고**: 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다. 그렇지 않으면 건너뛸 수 있습니다 (예: Gemini용 내장 GoogleSearch 도구).

---

### ExampleTool

```python
class google.adk.tools.ExampleTool(examples)
```

**상속**: `BaseTool`

LLM 요청에 (few-shot) 예시를 추가하는 도구입니다.

#### 속성

- **examples**: LLM 요청에 추가할 예시들

#### 메소드

##### `async process_llm_request(*, tool_context, llm_request)`
이 도구에 대한 나가는 LLM 요청을 처리합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **tool_context**: 도구의 컨텍스트
  - **llm_request**: 나가는 LLM 요청 (변경 가능)

---

### FunctionTool

```python
class google.adk.tools.FunctionTool(func)
```

**상속**: `BaseTool`

사용자 정의 Python 함수를 래핑하는 도구입니다.

#### 속성

- **func**: 래핑할 함수

호출 가능한 객체에서 메타데이터를 추출합니다.

#### 메소드

##### `async run_async(*, args, tool_context)`
주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`
- **매개변수**:
  - **args**: LLM이 채운 인자들
  - **tool_context**: 도구의 컨텍스트

---

### LongRunningFunctionTool

```python
class google.adk.tools.LongRunningFunctionTool(func)
```

**상속**: `FunctionTool`

결과를 비동기적으로 반환하는 함수 도구입니다.

이 도구는 완료하는데 상당한 시간이 걸릴 수 있는 장기 실행 작업에 사용됩니다. 프레임워크가 함수를 호출하고, 함수가 반환되면 응답이 function_call_id로 식별되는 프레임워크에 비동기적으로 반환됩니다.

#### 속성

- **is_long_running**: 장기 실행 작업인지 여부

#### 사용 예시

```python
tool = LongRunningFunctionTool(a_long_running_function)
```

호출 가능한 객체에서 메타데이터를 추출합니다.

---

### ToolContext

```python
class google.adk.tools.ToolContext(
    invocation_context, 
    *, 
    function_call_id=None, 
    event_actions=None
)
```

**상속**: `CallbackContext`

도구의 컨텍스트입니다.

이 클래스는 호출 컨텍스트, 함수 호출 ID, 이벤트 액션, 인증 응답에 대한 접근을 포함하여 도구 호출에 대한 컨텍스트를 제공합니다. 또한 자격 증명 요청, 인증 응답 검색, 아티팩트 나열, 메모리 검색을 위한 메소드도 제공합니다.

#### 속성

- **invocation_context**: 도구의 호출 컨텍스트
- **function_call_id**: 현재 도구 호출의 함수 호출 ID (LLM에서 함수 호출을 식별하기 위해 반환된 ID)
- **event_actions**: 현재 도구 호출의 이벤트 액션

#### 속성

##### `property actions: EventActions`
이벤트 액션에 대한 속성입니다.

#### 메소드

##### `get_auth_response(auth_config)`
- **반환 타입**: `AuthCredential`

##### `request_credential(auth_config)`
- **반환 타입**: `None`

##### `async search_memory(query)`
현재 사용자의 메모리를 검색합니다.

- **반환 타입**: `SearchMemoryResponse`

---

### VertexAiSearchTool

```python
class google.adk.tools.VertexAiSearchTool(
    *, 
    data_store_id=None, 
    data_store_specs=None, 
    search_engine_id=None, 
    filter=None, 
    max_results=None
)
```

**상속**: `BaseTool`

Vertex AI Search를 사용하는 내장 도구입니다.

#### 속성

- **data_store_id**: Vertex AI 검색 데이터 스토어 리소스 ID
- **search_engine_id**: Vertex AI 검색 엔진 리소스 ID

#### 생성자

Vertex AI Search 도구를 초기화합니다.

- **매개변수**:
  - **data_store_id**: `"projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}"` 형식의 Vertex AI 검색 데이터 스토어 리소스 ID
  - **data_store_specs**: 검색할 특정 DataStore를 정의하는 사양 (엔진 사용시에만 설정)
  - **search_engine_id**: `"projects/{project}/locations/{location}/collections/{collection}/engines/{engine}"` 형식의 Vertex AI 검색 엔진 리소스 ID
  - **filter**: 검색 필터
  - **max_results**: 최대 결과 수

- **예외**: **ValueError** - `data_store_id`와 `search_engine_id`가 모두 지정되지 않았거나 둘 다 지정된 경우

#### 메소드

##### `async process_llm_request(*, tool_context, llm_request)`
이 도구에 대한 나가는 LLM 요청을 처리합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **tool_context**: 도구의 컨텍스트
  - **llm_request**: 나가는 LLM 요청 (변경 가능)

---

## 유틸리티 함수

### exit_loop

```python
google.adk.tools.exit_loop(tool_context)
```

루프를 종료합니다.

지시받았을 때만 이 함수를 호출하세요.

### transfer_to_agent

```python
google.adk.tools.transfer_to_agent(agent_name, tool_context)
```

다른 에이전트로 질문을 전달합니다.

이 도구는 에이전트의 설명에 따라 사용자의 질문에 답변하기에 더 적합한 다른 에이전트로 제어권을 넘깁니다.

#### 매개변수

- **agent_name**: 전달할 에이전트의 이름
- **tool_context**: 도구 컨텍스트

---

## 사용 예시

### APIHubToolset 사용

```python
from google.adk.tools import APIHubToolset
from google.adk.agents import LlmAgent

# API Hub에서 도구셋 생성
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/my-api",
    service_account_json=service_account_config,
    tool_filter=['search_api', 'analytics_api']
)

# 에이전트에 도구셋 추가
agent = LlmAgent(
    name="api_agent",
    tools=[apihub_toolset],
    instruction="당신은 API를 사용하여 작업을 수행하는 에이전트입니다."
)

# 리소스 정리
await apihub_toolset.close()
```

### FunctionTool 사용

```python
from google.adk.tools import FunctionTool

def calculate_tax(amount: float, rate: float) -> float:
    """세금을 계산합니다."""
    return amount * rate

def send_email(to: str, subject: str, body: str) -> str:
    """이메일을 발송합니다."""
    # 이메일 발송 로직
    return f"이메일이 {to}로 발송되었습니다."

# 함수를 도구로 래핑
tax_tool = FunctionTool(calculate_tax)
email_tool = FunctionTool(send_email)

# 에이전트에 추가
agent = LlmAgent(
    name="assistant",
    tools=[tax_tool, email_tool]
)
```

### AgentTool 사용

```python
from google.adk.tools import AgentTool
from google.adk.agents import LlmAgent

# 전문 에이전트 생성
math_agent = LlmAgent(
    name="math_specialist",
    model="gemini-1.5-pro",
    instruction="당신은 수학 문제 해결 전문가입니다."
)

# 에이전트를 도구로 래핑
math_tool = AgentTool(
    agent=math_agent,
    skip_summarization=False
)

# 메인 에이전트에 도구로 추가
main_agent = LlmAgent(
    name="main_assistant",
    tools=[math_tool],
    instruction="수학 문제가 나오면 전문가에게 맡기세요."
)
```

### VertexAiSearchTool 사용

```python
from google.adk.tools import VertexAiSearchTool

# Vertex AI Search 도구 생성
search_tool = VertexAiSearchTool(
    data_store_id="projects/my-project/locations/us-central1/collections/default/dataStores/my-datastore",
    max_results=10
)

# 또는 검색 엔진 사용
search_engine_tool = VertexAiSearchTool(
    search_engine_id="projects/my-project/locations/us-central1/collections/default/engines/my-engine",
    filter="category:technical"
)

agent = LlmAgent(
    name="search_agent",
    tools=[search_tool],
    instruction="검색이 필요한 질문에 답변하세요."
)
```

### 에이전트 전송 사용

```python
from google.adk.tools import transfer_to_agent

# 에이전트에서 다른 에이전트로 전송하는 도구 사용
# (일반적으로 LLM이 자동으로 호출)

# transfer_to_agent("specialist_agent", tool_context)
```