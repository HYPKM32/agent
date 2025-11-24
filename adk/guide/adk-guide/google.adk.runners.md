# Google ADK Runners API Reference

`google.adk.runners` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### Runner

```python
class google.adk.runners.Runner(
    *, 
    app_name, 
    agent, 
    plugins=None, 
    artifact_service=None, 
    session_service, 
    memory_service=None, 
    credential_service=None
)
```

**상속**: `object`

에이전트를 실행하는데 사용되는 Runner 클래스입니다.

세션 내에서 에이전트의 실행을 관리하며, 메시지 처리, 이벤트 생성, 아티팩트 저장, 세션 관리, 메모리와 같은 다양한 서비스와의 상호작용을 처리합니다.

#### 필드

- **app_name**: `str` - 러너의 애플리케이션 이름
- **agent**: `BaseAgent` - 실행할 루트 에이전트
- **artifact_service**: `Optional[BaseArtifactService]` (기본값: None) - 러너의 아티팩트 서비스
- **session_service**: `BaseSessionService` - 러너의 세션 서비스
- **memory_service**: `Optional[BaseMemoryService]` (기본값: None) - 러너의 메모리 서비스
- **credential_service**: `Optional[BaseCredentialService]` (기본값: None) - 러너의 자격 증명 서비스
- **plugin_manager**: `PluginManager` - 러너의 플러그인 매니저

#### 생성자

Runner를 초기화합니다.

- **매개변수**:
  - **app_name**: 러너의 애플리케이션 이름
  - **agent**: 실행할 루트 에이전트
  - **plugins**: 플러그인 리스트 (선택사항)
  - **artifact_service**: 러너의 아티팩트 서비스 (선택사항)
  - **session_service**: 러너의 세션 서비스 (필수)
  - **memory_service**: 러너의 메모리 서비스 (선택사항)
  - **credential_service**: 러너의 자격 증명 서비스 (선택사항)

#### 메소드

##### `run(*, user_id, session_id, new_message, run_config=RunConfig(...))`
에이전트를 실행합니다 (동기식).

- **반환 타입**: `Generator[Event, None, None]`
- **매개변수**:
  - **user_id**: 세션의 사용자 ID
  - **session_id**: 세션의 세션 ID
  - **new_message**: 세션에 추가할 새로운 메시지
  - **run_config**: 에이전트의 실행 설정 (기본값: RunConfig())
- **Yields**: 에이전트가 생성한 이벤트들

> **참고**: 이 동기식 인터페이스는 로컬 테스트 및 편의 목적으로만 사용됩니다. 프로덕션에서는 `run_async` 사용을 고려하세요.

##### `async run_async(*, user_id, session_id, new_message, state_delta=None, run_config=RunConfig(...))`
이 러너에서 에이전트를 실행하는 주요 진입 메소드입니다.

- **반환 타입**: `AsyncGenerator[Event, None]`
- **매개변수**:
  - **user_id**: 세션의 사용자 ID
  - **session_id**: 세션의 세션 ID
  - **new_message**: 세션에 추가할 새로운 메시지
  - **state_delta**: 상태 변화 (선택사항)
  - **run_config**: 에이전트의 실행 설정 (기본값: RunConfig())
- **Yields**: 에이전트가 생성한 이벤트들

##### `async run_live(*, user_id=None, session_id=None, live_request_queue, run_config=RunConfig(...), session=None)`
라이브 모드에서 에이전트를 실행합니다 (실험적 기능).

- **반환 타입**: `AsyncGenerator[Event, None]`
- **매개변수**:
  - **user_id**: 세션의 사용자 ID (session이 None일 때 필수)
  - **session_id**: 세션의 세션 ID (session이 None일 때 필수)
  - **live_request_queue**: 라이브 요청을 위한 큐
  - **run_config**: 에이전트의 실행 설정 (기본값: RunConfig())
  - **session**: 사용할 세션 (더 이상 사용되지 않음, user_id와 session_id 사용 권장)
- **Yields**: 에이전트의 라이브 실행 중 생성되는 Event 객체들

> ⚠️ **경고**: 이 기능은 실험적이며 향후 릴리스에서 API나 동작이 변경될 수 있습니다.
> 
> **참고**: session 또는 user_id와 session_id 둘 다 제공되어야 합니다.

##### `async close()`
러너를 종료합니다.

---

### InMemoryRunner

```python
class google.adk.runners.InMemoryRunner(
    agent, 
    *, 
    app_name='InMemoryRunner', 
    plugins=None
)
```

**상속**: `Runner`

테스트 및 개발을 위한 인메모리 Runner입니다.

이 러너는 아티팩트, 세션, 메모리 서비스에 대해 인메모리 구현을 사용하여 에이전트 실행을 위한 가벼우며 자체 포함된 환경을 제공합니다.

#### 필드

- **agent**: 실행할 루트 에이전트
- **app_name**: 러너의 애플리케이션 이름 (기본값: 'InMemoryRunner')
- **_in_memory_session_service**: 더 이상 사용되지 않는 필드

#### 생성자

InMemoryRunner를 초기화합니다.

- **매개변수**:
  - **agent**: 실행할 루트 에이전트
  - **app_name**: 러너의 애플리케이션 이름 (기본값: 'InMemoryRunner')
  - **plugins**: 플러그인 리스트 (선택사항)

---

## 사용 예시

### 기본 Runner 사용

```python
from google.adk.runners import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.memory import InMemoryMemoryService

# 서비스들 설정
session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()
memory_service = InMemoryMemoryService()

# 에이전트 생성
agent = LlmAgent(
    name="my_agent",
    model="gemini-1.5-flash",
    instruction="당신은 도움이 되는 AI 어시스턴트입니다."
)

# Runner 생성
runner = Runner(
    app_name="MyApp",
    agent=agent,
    session_service=session_service,
    artifact_service=artifact_service,
    memory_service=memory_service
)

# 에이전트 실행
async for event in runner.run_async(
    user_id="user123",
    session_id="session456",
    new_message="안녕하세요!"
):
    print(f"Event: {event}")

# 리소스 정리
await runner.close()
```

### InMemoryRunner 사용 (개발/테스트)

```python
from google.adk.runners import InMemoryRunner
from google.adk.agents import LlmAgent

# 간단한 에이전트 생성
agent = LlmAgent(
    name="test_agent",
    model="gemini-1.5-flash",
    instruction="테스트용 에이전트입니다."
)

# InMemoryRunner 생성 (서비스들이 자동으로 인메모리로 설정됨)
runner = InMemoryRunner(
    agent=agent,
    app_name="TestApp"
)

# 테스트 실행
async for event in runner.run_async(
    user_id="test_user",
    session_id="test_session",
    new_message="테스트 메시지"
):
    print(f"Test Event: {event}")
```

### 플러그인과 함께 사용

```python
from google.adk.runners import Runner
from google.adk.plugins import BasePlugin

class LoggingPlugin(BasePlugin):
    def __init__(self):
        super().__init__(name="logger")
    
    async def before_agent_callback(self, *, agent, callback_context):
        print(f"Starting agent: {agent.name}")
    
    async def after_agent_callback(self, *, agent, callback_context):
        print(f"Finished agent: {agent.name}")

# 플러그인과 함께 Runner 생성
runner = Runner(
    app_name="MyApp",
    agent=my_agent,
    session_service=session_service,
    plugins=[LoggingPlugin()]
)
```

### 라이브 모드 사용

```python
from google.adk.runners import Runner
from google.adk.agents import LiveRequestQueue, RunConfig

# 라이브 요청 큐 생성
live_queue = LiveRequestQueue()

# 라이브 모드용 RunConfig 설정
live_config = RunConfig(
    streaming_mode=StreamingMode.BIDI,
    response_modalities=["AUDIO"],
    speech_config=SpeechConfig(
        voice_config=VoiceConfig(language_code="ko-KR")
    )
)

# 라이브 모드로 실행
async for event in runner.run_live(
    user_id="live_user",
    session_id="live_session", 
    live_request_queue=live_queue,
    run_config=live_config
):
    print(f"Live Event: {event}")
    
    # 실시간으로 사용자 입력 전송
    if some_condition:
        live_queue.send_content("사용자의 실시간 입력")
```

### 커스텀 RunConfig 사용

```python
from google.adk.agents import RunConfig
from google.genai.types import SpeechConfig, VoiceConfig

# 커스텀 실행 설정
custom_config = RunConfig(
    max_llm_calls=10,  # LLM 호출 제한
    streaming_mode=StreamingMode.SSE,
    speech_config=SpeechConfig(
        voice_config=VoiceConfig(
            language_code="ko-KR",
            name="ko-KR-Wavenet-A"
        )
    ),
    save_input_blobs_as_artifacts=True,
    enable_affective_dialog=True
)

# 커스텀 설정으로 실행
async for event in runner.run_async(
    user_id="user123",
    session_id="session456",
    new_message="안녕하세요!",
    run_config=custom_config
):
    print(f"Event with custom config: {event}")
```

### 상태 변화와 함께 실행

```python
# 세션 상태 변화 적용
state_delta = {
    "user_preferences": {
        "language": "korean",
        "tone": "friendly"
    },
    "context": {
        "topic": "programming",
        "level": "beginner"
    }
}

async for event in runner.run_async(
    user_id="user123",
    session_id="session456",
    new_message="파이썬에 대해 알려주세요",
    state_delta=state_delta
):
    print(f"Event with state: {event}")
```

### 동기식 실행 (테스트용)

```python
# 동기식 인터페이스 사용 (테스트/개발용)
for event in runner.run(
    user_id="test_user",
    session_id="test_session",
    new_message="동기식 테스트"
):
    print(f"Sync Event: {event}")
```

---

## 주요 특징

### 유연한 서비스 구성
- 아티팩트, 세션, 메모리, 자격 증명 서비스를 독립적으로 설정 가능
- 개발/테스트용 인메모리 구현부터 프로덕션용 클라우드 서비스까지 지원

### 다양한 실행 모드
- **비동기 실행**: 프로덕션 환경에 적합한 `run_async`
- **동기 실행**: 테스트/개발용 `run`  
- **라이브 모드**: 실시간 상호작용을 위한 `run_live`

### 플러그인 시스템 통합
- 플러그인 매니저를 통한 전역 동작 수정
- 로깅, 모니터링, 캐싱 등 횡단 관심사 처리

### 상태 관리
- 세션별 상태 유지 및 관리
- 동적 상태 변화 적용 가능

### 개발 편의성
- InMemoryRunner를 통한 빠른 프로토타이핑
- 테스트용 동기식 인터페이스 제공
- 자동 리소스 관리 및 정리