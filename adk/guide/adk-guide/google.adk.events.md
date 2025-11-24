# Google ADK Events API Reference

`google.adk.events` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### Event

```python
pydantic model google.adk.events.Event
```

**상속**: `LlmResponse`

에이전트와 사용자 간의 대화에서 발생하는 이벤트를 나타냅니다.

대화의 내용뿐만 아니라 함수 호출 등 에이전트가 수행한 액션들을 저장하는데 사용됩니다.

#### 필드

##### 필수 필드

- **invocation_id**: `str` (별칭: 'invocationId') - 이벤트의 호출 ID (세션에 추가하기 전에 비어있지 않아야 함)
- **author**: `str` - "user" 또는 에이전트의 이름 (이벤트를 세션에 추가한 주체)

##### 선택적 필드

- **actions**: `EventActions` (선택사항) - 에이전트가 수행한 액션들
- **long_running_tool_ids**: `Optional[set[str]]` (별칭: 'longRunningToolIds') - 장기 실행 함수 호출의 ID 집합
- **branch**: `Optional[str]` (기본값: None) - 이벤트의 브랜치
- **id**: `str` (기본값: '') - 이벤트의 고유 식별자
- **timestamp**: `float` (선택사항) - 이벤트의 타임스탬프

#### 브랜치 형식

브랜치는 `agent_1.agent_2.agent_3` 형태로, `agent_1`이 `agent_2`의 부모이고, `agent_2`가 `agent_3`의 부모임을 나타냅니다.

여러 하위 에이전트가 서로의 대화 기록을 보지 않아야 할 때 사용됩니다.

#### 메소드

##### `static new_id()`
새로운 고유 ID를 생성합니다.

##### `get_function_calls()`
이벤트에서 함수 호출들을 반환합니다.

- **반환 타입**: `list[FunctionCall]`

##### `get_function_responses()`
이벤트에서 함수 응답들을 반환합니다.

- **반환 타입**: `list[FunctionResponse]`

##### `has_trailing_code_execution_result()`
이벤트가 후행 코드 실행 결과를 가지고 있는지 확인합니다.

- **반환 타입**: `bool`

##### `is_final_response()`
이벤트가 에이전트의 최종 응답인지 확인합니다.

> **참고**: 이 메소드는 Agent Development Kit에서만 사용됩니다.
> 
> 여러 에이전트가 하나의 호출에 참여할 때, 각 참여 에이전트마다 `is_final_response()`가 True인 이벤트가 하나씩 있을 수 있습니다.

- **반환 타입**: `bool`

##### `model_post_init(_Event__context)`
이벤트의 후처리 초기화 로직입니다.

---

### EventActions

```python
pydantic model google.adk.events.EventActions
```

**상속**: `BaseModel`

이벤트에 첨부된 액션들을 나타냅니다.

#### 필드

##### 상태 및 전송 관련
- **state_delta**: `dict[str, object]` (별칭: 'stateDelta', 선택사항) - 주어진 델타로 상태를 업데이트함을 나타냄
- **transfer_to_agent**: `Optional[str]` (별칭: 'transferToAgent', 기본값: None) - 설정되면 지정된 에이전트로 전송
- **escalate**: `Optional[bool]` (기본값: None) - 에이전트가 상위 레벨 에이전트로 에스컬레이션

##### 아티팩트 관련
- **artifact_delta**: `dict[str, int]` (별칭: 'artifactDelta', 선택사항) - 이벤트가 아티팩트를 업데이트함을 나타냄
  - **키**: 파일명
  - **값**: 버전

##### 인증 관련
- **requested_auth_configs**: `dict[str, AuthConfig]` (별칭: 'requestedAuthConfigs', 선택사항) - 도구 응답에서 요청된 인증 설정
  - **키**: 함수 호출 ID (하나의 함수 응답 이벤트가 여러 함수 응답을 포함할 수 있음)
  - **값**: 요청된 인증 설정

##### 처리 제어
- **skip_summarization**: `Optional[bool]` (별칭: 'skipSummarization', 기본값: None) - True일 경우 함수 응답 요약을 위한 모델 호출을 하지 않음 (함수 응답 이벤트에만 사용)

---

## 사용 예시

### 기본 이벤트 생성

```python
from google.adk.events import Event, EventActions

# 사용자 이벤트 생성
user_event = Event(
    invocation_id="inv_123",
    author="user",
    content="안녕하세요!"
)

# 에이전트 응답 이벤트 생성
agent_event = Event(
    invocation_id="inv_123",
    author="my_agent",
    content="안녕하세요! 어떻게 도와드릴까요?",
    actions=EventActions(
        state_delta={"user_greeting": True}
    )
)
```

### 에이전트 전송 이벤트

```python
# 다른 에이전트로 전송하는 이벤트
transfer_event = Event(
    invocation_id="inv_123",
    author="agent1",
    content="이 문제는 전문가 에이전트가 처리하겠습니다.",
    actions=EventActions(
        transfer_to_agent="specialist_agent"
    )
)
```

### 아티팩트 업데이트 이벤트

```python
# 아티팩트를 업데이트하는 이벤트
artifact_event = Event(
    invocation_id="inv_123",
    author="document_agent",
    content="문서가 업데이트되었습니다.",
    actions=EventActions(
        artifact_delta={
            "report.pdf": 2,
            "summary.txt": 1
        }
    )
)
```

### 인증 요청 이벤트

```python
# 인증이 필요한 도구 사용 이벤트
auth_event = Event(
    invocation_id="inv_123",
    author="api_agent",
    actions=EventActions(
        requested_auth_configs={
            "call_123": AuthConfig(
                auth_type="oauth2",
                scopes=["read", "write"]
            )
        }
    )
)
```

### 브랜치별 이벤트

```python
# 특정 브랜치의 이벤트
branch_event = Event(
    invocation_id="inv_123",
    author="sub_agent",
    branch="main_agent.sub_agent",
    content="하위 에이전트의 응답입니다."
)
```

---

## 주요 특징

### 이벤트 추적
- **호출 ID**: 모든 이벤트는 호출 ID로 그룹화됩니다
- **작성자**: 각 이벤트는 작성자(사용자 또는 에이전트)를 명시합니다
- **타임스탬프**: 이벤트 발생 시간을 추적합니다

### 액션 시스템
- **상태 관리**: 세션 상태를 동적으로 업데이트
- **에이전트 전송**: 다른 에이전트로 제어권 이양
- **아티팩트 관리**: 파일 및 문서 버전 추적

### 브랜치 격리
- 하위 에이전트들 간의 대화 기록 격리
- 계층적 에이전트 구조 지원

### 장기 실행 도구
- 비동기 도구 실행 추적
- 함수 호출 ID로 장기 실행 작업 관리