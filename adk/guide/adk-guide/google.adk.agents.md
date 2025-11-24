# Google ADK Agents API Reference

`google.adk.agents` 패키지의 API 레퍼런스 문서입니다.

## 별칭

### Agent
```python
google.adk.agents.Agent
```
`LlmAgent`의 별칭입니다.

---

## 클래스

### BaseAgent

```python
pydantic model google.adk.agents.BaseAgent
```

**상속**: `BaseModel`

Agent Development Kit의 모든 에이전트를 위한 기본 클래스입니다.

#### 필드

- **name**: `str` (필수) - 에이전트의 이름
- **description**: `str` (기본값: '') - 에이전트 능력에 대한 설명
- **parent_agent**: `Optional[BaseAgent]` (기본값: None) - 이 에이전트의 부모 에이전트
- **sub_agents**: `list[BaseAgent]` (선택사항) - 이 에이전트의 하위 에이전트들
- **before_agent_callback**: 에이전트 실행 전에 호출되는 콜백
- **after_agent_callback**: 에이전트 실행 후에 호출되는 콜백

#### 주요 특징

- **에이전트 이름**: Python 식별자여야 하며 에이전트 트리 내에서 고유해야 함
- **에이전트 설명**: 모델이 에이전트에게 제어권을 위임할지 결정하는데 사용
- **하위 에이전트**: 에이전트는 한 번만 하위 에이전트로 추가 가능

#### 메소드

##### `classmethod from_config(cls, config, config_abs_path)`
설정으로부터 에이전트를 생성합니다.

- **반환 타입**: `TypeVar(SelfAgent, bound=BaseAgent)`
- **매개변수**:
  - **config**: 에이전트를 생성할 설정
  - **config_abs_path**: 에이전트 설정이 포함된 설정 파일의 절대 경로

##### `clone(update=None)`
이 에이전트 인스턴스의 복사본을 생성합니다.

- **반환 타입**: `TypeVar(SelfAgent, bound=BaseAgent)`
- **매개변수**:
  - **update**: 복제된 에이전트의 필드에 대한 새 값의 선택적 매핑

##### `find_agent(name)` / `find_sub_agent(name)`
주어진 이름의 에이전트를 찾습니다.

- **반환 타입**: `Optional[BaseAgent]`

##### `async run_async(parent_context)` / `async run_live(parent_context)`
에이전트를 실행합니다.

- **반환 타입**: `AsyncGenerator[Event, None]`
- **매개변수**: **parent_context**: 부모 에이전트의 호출 컨텍스트

#### 속성

- **root_agent**: `BaseAgent` - 이 에이전트의 루트 에이전트
- **canonical_before_agent_callbacks** / **canonical_after_agent_callbacks**: 콜백 리스트

---

### InvocationContext

```python
pydantic model google.adk.agents.InvocationContext
```

**상속**: `BaseModel`

에이전트의 단일 호출 데이터를 나타냅니다.

#### 호출 구조
- **호출(Invocation)**: 사용자 메시지로 시작해서 최종 응답으로 끝남
- **에이전트 호출(Agent Call)**: `agent.run()`에 의해 처리됨
- **단계(Step)**: LLM을 한 번만 호출하고 응답을 생성

#### 필드

- **invocation_id**: `str` (필수) - 호출 컨텍스트의 ID (읽기 전용)
- **agent**: `BaseAgent` (필수) - 호출 컨텍스트의 현재 에이전트 (읽기 전용)
- **session**: `Session` (필수) - 호출 컨텍스트의 현재 세션 (읽기 전용)
- **session_service**: `BaseSessionService` (필수)
- **user_content**: `Optional[types.Content]` (기본값: None) - 이 호출을 시작한 사용자 콘텐츠 (읽기 전용)
- **end_invocation**: `bool` (기본값: False) - 이 호출을 종료할지 여부
- **branch**: `Optional[str]` (기본값: None) - 호출 컨텍스트의 브랜치
- **plugin_manager**: `PluginManager` - 이 호출에서 플러그인을 추적하는 매니저
- **run_config**: `Optional[RunConfig]` (기본값: None) - 이 호출 하에서 라이브 에이전트에 대한 설정
- **artifact_service**: `Optional[BaseArtifactService]` (기본값: None)
- **memory_service**: `Optional[BaseMemoryService]` (기본값: None)
- **credential_service**: `Optional[BaseCredentialService]` (기본값: None)
- **live_request_queue**: `Optional[LiveRequestQueue]` (기본값: None) - 라이브 요청을 받는 큐
- **active_streaming_tools**: `Optional[dict[str, ActiveStreamingTool]]` (기본값: None) - 이 호출의 실행 중인 스트리밍 도구
- **transcription_cache**: `Optional[list[TranscriptionEntry]]` (기본값: None) - 전사에 필요한 데이터 캐시

#### 메소드

##### `increment_llm_call_count()`
LLM 호출 수를 추적합니다.

- **예외**: `LlmCallsLimitExceededError` - LLM 호출 수가 설정된 임계값을 초과한 경우

#### 속성

- **app_name**: `str` - 애플리케이션 이름
- **user_id**: `str` - 사용자 ID

---

### LiveRequest

```python
pydantic model google.adk.agents.LiveRequest
```

**상속**: `BaseModel`

라이브 에이전트에게 보내는 요청입니다.

#### 필드

- **content**: `Optional[types.Content]` (기본값: None) - 턴 바이 턴 모드에서 모델에게 보낼 콘텐츠
- **blob**: `Optional[types.Blob]` (기본값: None) - 실시간 모드에서 모델에게 보낼 blob
- **activity_start**: `Optional[types.ActivityStart]` (기본값: None) - 사용자 활동 시작 신호
- **activity_end**: `Optional[types.ActivityEnd]` (기본값: None) - 사용자 활동 종료 신호
- **close**: `bool` (기본값: False) - 큐를 닫을지 여부

---

### LiveRequestQueue

```python
class google.adk.agents.LiveRequestQueue
```

**상속**: `object`

라이브(양방향 스트리밍) 방식으로 LiveRequest를 보내는데 사용되는 큐입니다.

#### 메소드

##### `async get()`
- **반환 타입**: `LiveRequest`

##### `send(req)` / `send_content(content)` / `send_realtime(blob)`
요청, 콘텐츠, 실시간 blob을 보냅니다.

##### `send_activity_start()` / `send_activity_end()`
사용자 입력의 시작/종료를 표시하는 활동 신호를 보냅니다.

##### `close()`
큐를 닫습니다.

---

### LlmAgent

```python
pydantic model google.adk.agents.LlmAgent
```

**상속**: `BaseAgent`

LLM 기반 에이전트입니다.

#### 주요 필드

##### 모델 및 설정
- **model**: `Union[str, BaseLlm]` (기본값: '') - 에이전트에 사용할 모델
- **generate_content_config**: `Optional[types.GenerateContentConfig]` (기본값: None) - 추가 콘텐츠 생성 설정
- **instruction**: `Union[str, InstructionProvider]` (기본값: '') - LLM 모델에 대한 지시사항
- **global_instruction**: `Union[str, InstructionProvider]` (기본값: '') - 전체 에이전트 트리에 대한 지시사항

##### 도구 및 기능
- **tools**: `list[ToolUnion]` (선택사항) - 이 에이전트에서 사용 가능한 도구들
- **code_executor**: `Optional[BaseCodeExecutor]` (기본값: None) - 모델 응답에서 코드 블록을 실행할 수 있게 해주는 코드 실행기
- **planner**: `Optional[BasePlanner]` (기본값: None) - 단계별 계획을 세우고 실행하도록 지시

##### 입출력 스키마
- **input_schema**: `Optional[type[BaseModel]]` (기본값: None) - 에이전트가 도구로 사용될 때의 입력 스키마
- **output_schema**: `Optional[type[BaseModel]]` (기본값: None) - 에이전트가 응답할 때의 출력 스키마
- **output_key**: `Optional[str]` (기본값: None) - 에이전트의 출력을 저장할 세션 상태의 키

##### 콜백
- **before_model_callback** / **after_model_callback**: LLM 호출 전후의 콜백
- **before_tool_callback** / **after_tool_callback**: 도구 호출 전후의 콜백

##### 제어 설정
- **disallow_transfer_to_parent**: `bool` (기본값: False) - 부모 에이전트로의 LLM 제어 전달을 금지
- **disallow_transfer_to_peers**: `bool` (기본값: False) - 피어 에이전트로의 LLM 제어 전달을 금지
- **include_contents**: `Literal['default', 'none']` (기본값: 'default') - 모델 요청에서의 콘텐츠 포함 제어

#### 메소드

##### `classmethod from_config(cls, config, config_abs_path)`
설정으로부터 에이전트를 생성합니다.

- **반환 타입**: `LlmAgent`

##### `async canonical_instruction(ctx)` / `async canonical_global_instruction(ctx)`
지시사항을 해결합니다.

- **반환 타입**: `tuple[str, bool]`
- **반환값**: (instruction, bypass_state_injection) 튜플

##### `async canonical_tools(ctx=None)`
컨텍스트를 기반으로 도구들을 해결합니다.

- **반환 타입**: `list[BaseTool]`

#### 속성

- **canonical_model**: `BaseLlm` - 해결된 모델
- **canonical_before_model_callbacks** / **canonical_after_model_callbacks**: 모델 콜백 리스트
- **canonical_before_tool_callbacks** / **canonical_after_tool_callbacks**: 도구 콜백 리스트

---

### LoopAgent

```python
pydantic model google.adk.agents.LoopAgent
```

**상속**: `BaseAgent`

하위 에이전트들을 루프로 실행하는 셸 에이전트입니다.

#### 필드

- **max_iterations**: `Optional[int]` (기본값: None) - 루프 에이전트를 실행할 최대 반복 횟수

#### 동작
- 하위 에이전트가 escalate 이벤트를 생성하거나 max_iterations에 도달하면 중지
- max_iterations가 설정되지 않으면 하위 에이전트가 escalate할 때까지 무한 실행

---

### ParallelAgent

```python
pydantic model google.adk.agents.ParallelAgent
```

**상속**: `BaseAgent`

하위 에이전트들을 격리된 방식으로 병렬 실행하는 셸 에이전트입니다.

#### 사용 사례
- 다양한 알고리즘을 동시에 실행
- 후속 평가 에이전트가 검토할 여러 응답 생성
- 단일 작업에 대한 다양한 관점이나 시도가 필요한 시나리오

---

### RunConfig

```python
pydantic model google.adk.agents.RunConfig
```

**상속**: `BaseModel`

에이전트의 런타임 동작에 대한 설정입니다.

#### 필드

##### 기본 설정
- **max_llm_calls**: `int` (기본값: 500) - 주어진 실행에 대한 LLM 호출 총 수의 제한
- **streaming_mode**: `StreamingMode` (기본값: StreamingMode.NONE) - 스트리밍 모드
- **support_cfc**: `bool` (기본값: False) - CFC(Compositional Function Calling) 지원 여부

##### 오디오 및 음성 설정
- **speech_config**: `Optional[types.SpeechConfig]` (기본값: None) - 라이브 에이전트의 음성 설정
- **input_audio_transcription**: `Optional[types.AudioTranscriptionConfig]` (기본값: None) - 사용자의 오디오 입력에 대한 입력 전사
- **output_audio_transcription**: `Optional[types.AudioTranscriptionConfig]` (기본값: None) - 오디오 응답에 대한 출력 전사
- **response_modalities**: `Optional[list[str]]` (기본값: None) - 출력 양식 (기본값: AUDIO)

##### 고급 설정
- **enable_affective_dialog**: `Optional[bool]` (기본값: None) - 감정을 감지하고 그에 따라 응답을 조정
- **proactivity**: `Optional[types.ProactivityConfig]` (기본값: None) - 모델의 능동성 설정
- **realtime_input_config**: `Optional[types.RealtimeInputConfig]` (기본값: None) - 사용자의 오디오 입력에 대한 실시간 입력 설정
- **session_resumption**: `Optional[types.SessionResumptionConfig]` (기본값: None) - 세션 재개 메커니즘 설정
- **save_input_blobs_as_artifacts**: `bool` (기본값: False) - 입력 blob을 아티팩트로 저장할지 여부

---

### SequentialAgent

```python
pydantic model google.adk.agents.SequentialAgent
```

**상속**: `BaseAgent`

하위 에이전트들을 순차적으로 실행하는 셸 에이전트입니다.

#### 메소드

##### `classmethod from_config(cls, config, config_abs_path)`
설정으로부터 에이전트를 생성합니다.

- **반환 타입**: `SequentialAgent`