# Google ADK Sessions API Reference

`google.adk.sessions` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseSessionService

```python
class google.adk.sessions.BaseSessionService
```

**상속**: `ABC`

세션 서비스를 위한 기본 클래스입니다.

세션과 이벤트를 관리하는 메소드 세트를 제공합니다.

#### 메소드

##### `async append_event(session, event)`
세션 객체에 이벤트를 추가합니다.

- **반환 타입**: `Event`
- **매개변수**:
  - **session**: 이벤트를 추가할 세션
  - **event**: 추가할 이벤트

#### 추상 메소드

##### `async create_session(*, app_name, user_id, state=None, session_id=None)`
새로운 세션을 생성합니다.

- **반환 타입**: `Session`
- **매개변수**:
  - **app_name**: 앱의 이름
  - **user_id**: 사용자의 ID
  - **state**: 세션의 초기 상태 (선택사항)
  - **session_id**: 클라이언트가 제공하는 세션 ID (미제공 시 생성된 ID 사용)
- **반환값**: 새로 생성된 세션 인스턴스

##### `async delete_session(*, app_name, user_id, session_id)`
세션을 삭제합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **app_name**: 앱의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID

##### `async get_session(*, app_name, user_id, session_id, config=None)`
세션을 가져옵니다.

- **반환 타입**: `Optional[Session]`
- **매개변수**:
  - **app_name**: 앱의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **config**: 설정 (선택사항)

##### `async list_sessions(*, app_name, user_id)`
모든 세션을 나열합니다.

- **반환 타입**: `ListSessionsResponse`
- **매개변수**:
  - **app_name**: 앱의 이름
  - **user_id**: 사용자의 ID

---

### Session

```python
pydantic model google.adk.sessions.Session
```

**상속**: `BaseModel`

사용자와 에이전트 간의 일련의 상호작용을 나타냅니다.

#### 필드

- **id**: `str` (필수) - 세션의 고유 식별자
- **app_name**: `str` (별칭: 'appName', 필수) - 앱의 이름
- **user_id**: `str` (별칭: 'userId', 필수) - 사용자의 ID
- **state**: `dict[str, Any]` (선택사항) - 세션의 상태
- **events**: `list[Event]` (선택사항) - 세션의 이벤트들 (사용자 입력, 모델 응답, 함수 호출/응답 등)
- **last_update_time**: `float` (별칭: 'lastUpdateTime', 기본값: 0.0) - 세션의 마지막 업데이트 시간

---

### State

```python
class google.adk.sessions.State(value, delta)
```

**상속**: `object`

현재 값과 커밋 대기 중인 델타를 유지하는 상태 딕셔너리입니다.

#### 상수

- **APP_PREFIX** = 'app:' - 앱 관련 상태 키 접두사
- **USER_PREFIX** = 'user:' - 사용자 관련 상태 키 접두사
- **TEMP_PREFIX** = 'temp:' - 임시 상태 키 접두사

#### 생성자

- **매개변수**:
  - **value**: 상태 딕셔너리의 현재 값
  - **delta**: 아직 커밋되지 않은 현재 값에 대한 델타 변경사항

#### 메소드

##### `get(key, default=None)`
주어진 키에 대한 상태 딕셔너리의 값을 반환합니다.

- **반환 타입**: `Any`
- **매개변수**:
  - **key**: 가져올 키
  - **default**: 키가 없을 때 기본값

##### `has_delta()`
상태에 대기 중인 델타가 있는지 확인합니다.

- **반환 타입**: `bool`

##### `to_dict()`
상태 딕셔너리를 반환합니다.

- **반환 타입**: `dict[str, Any]`

##### `update(delta)`
주어진 델타로 상태 딕셔너리를 업데이트합니다.

- **매개변수**:
  - **delta**: 적용할 델타 변경사항

---

### InMemorySessionService

```python
class google.adk.sessions.InMemorySessionService
```

**상속**: `BaseSessionService`

세션 서비스의 인메모리 구현체입니다.

> ⚠️ **주의**: 멀티스레드 프로덕션 환경에는 적합하지 않습니다. 테스트 및 개발 목적으로만 사용하세요.

#### 메소드

모든 `BaseSessionService`의 추상 메소드를 구현하며, 추가로 동기식 메소드들도 제공합니다:

##### 비동기 메소드
- `async append_event(session, event)`
- `async create_session(*, app_name, user_id, state=None, session_id=None)`
- `async delete_session(*, app_name, user_id, session_id)`
- `async get_session(*, app_name, user_id, session_id, config=None)`
- `async list_sessions(*, app_name, user_id)`

##### 동기식 메소드 (테스트/개발용)
- `create_session_sync(*, app_name, user_id, state=None, session_id=None)`
- `delete_session_sync(*, app_name, user_id, session_id)`
- `get_session_sync(*, app_name, user_id, session_id, config=None)`
- `list_sessions_sync(*, app_name, user_id)`

---

### DatabaseSessionService

```python
class google.adk.sessions.DatabaseSessionService(db_url, **kwargs)
```

**상속**: `BaseSessionService`

저장을 위해 데이터베이스를 사용하는 세션 서비스입니다.

#### 생성자

데이터베이스 URL로 데이터베이스 세션 서비스를 초기화합니다.

- **매개변수**:
  - **db_url**: 데이터베이스 연결 URL
  - **\*\*kwargs**: 추가 키워드 인자

#### 메소드

모든 `BaseSessionService`의 추상 메소드를 구현합니다:

- `async append_event(session, event)`
- `async create_session(*, app_name, user_id, state=None, session_id=None)`
- `async delete_session(app_name, user_id, session_id)`
- `async get_session(*, app_name, user_id, session_id, config=None)`
- `async list_sessions(*, app_name, user_id)`

---

### VertexAiSessionService

```python
class google.adk.sessions.VertexAiSessionService(project=None, location=None, agent_engine_id=None)
```

**상속**: `BaseSessionService`

GenAI API 클라이언트를 사용하여 Vertex AI Agent Engine Session Service에 연결합니다.

참조: [Vertex AI Sessions Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/sessions/overview)

#### 생성자

VertexAiSessionService를 초기화합니다.

- **매개변수**:
  - **project**: 사용할 프로젝트의 프로젝트 ID
  - **location**: 사용할 프로젝트의 위치
  - **agent_engine_id**: 사용할 에이전트 엔진의 리소스 ID

#### 메소드

모든 `BaseSessionService`의 추상 메소드를 구현합니다:

- `async append_event(session, event)`
- `async create_session(*, app_name, user_id, state=None, session_id=None)`
- `async delete_session(*, app_name, user_id, session_id)`
- `async get_session(*, app_name, user_id, session_id, config=None)`
- `async list_sessions(*, app_name, user_id)`

---

## 사용 예시

### InMemorySessionService 사용 (개발/테스트)

```python
from google.adk.sessions import InMemorySessionService

# 인메모리 세션 서비스 생성
session_service = InMemorySessionService()

# 새 세션 생성
session = await session_service.create_session(
    app_name="my_app",
    user_id="user123",
    state={"preferences": {"language": "korean"}}
)

# 세션 조회
retrieved_session = await session_service.get_session(
    app_name="my_app",
    user_id="user123",
    session_id=session.id
)

# 이벤트 추가
from google.adk.events import Event
event = Event(
    invocation_id="inv_1",
    author="user",
    content="안녕하세요!"
)

updated_event = await session_service.append_event(session, event)

# 세션 목록 조회
sessions_response = await session_service.list_sessions(
    app_name="my_app",
    user_id="user123"
)

# 세션 삭제
await session_service.delete_session(
    app_name="my_app",
    user_id="user123",
    session_id=session.id
)
```

### DatabaseSessionService 사용

```python
from google.adk.sessions import DatabaseSessionService

# 데이터베이스 세션 서비스 생성
db_session_service = DatabaseSessionService(
    db_url="postgresql://user:password@localhost:5432/sessions_db"
)

# 세션 생성 및 관리 (API는 InMemorySessionService와 동일)
session = await db_session_service.create_session(
    app_name="production_app",
    user_id="user456",
    state={"context": "customer_support"}
)
```

### VertexAiSessionService 사용

```python
from google.adk.sessions import VertexAiSessionService

# Vertex AI 세션 서비스 생성
vertex_session_service = VertexAiSessionService(
    project="my-gcp-project",
    location="us-central1",
    agent_engine_id="my-agent-engine"
)

# Vertex AI에서 세션 관리
session = await vertex_session_service.create_session(
    app_name="vertex_app",
    user_id="vertex_user",
    state={"ai_context": "advanced_reasoning"}
)
```

### State 객체 사용

```python
from google.adk.sessions import State

# 초기 상태와 델타로 State 생성
initial_state = {"user:name": "Alice", "app:theme": "dark"}
delta_changes = {"user:preference": "korean", "temp:session_start": "2024-01-01"}

state = State(value=initial_state, delta=delta_changes)

# 상태 값 조회
name = state.get("user:name")  # "Alice"
preference = state.get("user:preference")  # "korean" (델타에서)
missing = state.get("nonexistent", "default")  # "default"

# 델타 확인
has_changes = state.has_delta()  # True

# 전체 상태 딕셔너리 가져오기
full_state = state.to_dict()

# 추가 델타 적용
additional_delta = {"app:version": "2.0"}
state.update(additional_delta)
```

### 동기식 메소드 사용 (테스트용)

```python
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()

# 동기식 메소드 사용 (테스트/개발용)
session = session_service.create_session_sync(
    app_name="test_app",
    user_id="test_user"
)

sessions = session_service.list_sessions_sync(
    app_name="test_app",
    user_id="test_user"
)

session_service.delete_session_sync(
    app_name="test_app",
    user_id="test_user",
    session_id=session.id
)
```

### Runner와 함께 사용

```python
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from google.adk.agents import LlmAgent

# 세션 서비스 설정
session_service = DatabaseSessionService(
    db_url="postgresql://localhost/mydb"
)

# 에이전트와 러너 생성
agent = LlmAgent(name="chat_agent", model="gemini-1.5-flash")
runner = Runner(
    app_name="ChatApp",
    agent=agent,
    session_service=session_service
)

# 세션이 자동으로 관리됨
async for event in runner.run_async(
    user_id="user123",
    session_id="chat_session_1",
    new_message="안녕하세요!"
):
    print(f"Event: {event}")
```

---

## 주요 특징

### 추상화된 세션 관리
- `BaseSessionService`를 통해 다양한 저장 백엔드를 통합된 인터페이스로 사용
- 개발부터 프로덕션까지 일관된 API 제공

### 다양한 구현체
- **InMemorySessionService**: 개발/테스트용 메모리 기반
- **DatabaseSessionService**: 관계형 데이터베이스 기반
- **VertexAiSessionService**: Google Cloud Vertex AI 관리형 서비스

### 상태 관리 시스템
- `State` 클래스를 통한 구조화된 상태 관리
- 델타 기반 상태 업데이트 지원
- 접두사를 통한 상태 네임스페이스 관리

### 이벤트 추적
- 세션별 이벤트 히스토리 관리
- 사용자 입력, 에이전트 응답, 함수 호출 등 모든 상호작용 추적

### 스케일링 지원
- 메모리 기반부터 클라우드 기반까지 확장 가능
- 멀티테넌트 지원을 위한 앱/사용자별 격리

### 개발 편의성
- 동기식 메소드 제공 (InMemorySessionService)
- 테스트용 간소화된 API
- Runner와의 자동 통합