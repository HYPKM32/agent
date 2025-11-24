# Google ADK Plugins API Reference

`google.adk.plugins` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BasePlugin

```python
class google.adk.plugins.BasePlugin(name)
```

**상속**: `ABC`

플러그인 생성을 위한 기본 클래스입니다.

플러그인은 콜백 방식으로 중요한 실행 지점에서 에이전트, 도구, LLM 동작을 가로채고 수정할 수 있는 구조화된 방법을 제공합니다. 에이전트 콜백이 특정 에이전트에 적용되는 반면, 플러그인은 러너에 추가된 모든 에이전트에 전역적으로 적용됩니다.

#### 플러그인 vs 에이전트 콜백

##### 실행 순서
- 플러그인과 에이전트 콜백은 등록된 순서대로 실행됩니다
- 플러그인이 에이전트 콜백보다 우선순위를 가집니다
- 플러그인에서 값을 반환하면 나머지 모든 플러그인과 에이전트 콜백이 스킵됩니다

##### 변경 사항 전파
- 플러그인과 에이전트 콜백 모두 입력 매개변수를 수정할 수 있습니다
- 수정 사항은 체인의 다음 콜백으로 전달됩니다

#### 생성자

플러그인을 초기화합니다.

- **매개변수**:
  - **name**: 이 플러그인 인스턴스의 고유 식별자

---

## 콜백 메소드

### 에이전트 라이프사이클 콜백

#### `async before_agent_callback(*, agent, callback_context)`
에이전트의 주 로직이 호출되기 전에 실행되는 콜백입니다.

- **반환 타입**: `Optional[Content]`
- **매개변수**:
  - **agent**: 실행될 에이전트
  - **callback_context**: 에이전트 호출의 컨텍스트
- **반환값**: 
  - `types.Content` 객체를 반환하면 에이전트의 콜백과 실행을 우회하고 직접 반환
  - `None`을 반환하면 에이전트가 정상적으로 진행

#### `async after_agent_callback(*, agent, callback_context)`
에이전트의 주 로직이 완료된 후 실행되는 콜백입니다.

- **반환 타입**: `Optional[Content]`
- **매개변수**:
  - **agent**: 방금 실행된 에이전트
  - **callback_context**: 에이전트 호출의 컨텍스트
- **반환값**: 
  - `types.Content` 객체를 반환하면 에이전트의 원래 결과를 대체
  - `None`을 반환하면 원래의 수정되지 않은 결과 사용

### 모델 라이프사이클 콜백

#### `async before_model_callback(*, callback_context, llm_request)`
모델에 요청이 전송되기 전에 실행되는 콜백입니다.

- **반환 타입**: `Optional[LlmResponse]`
- **매개변수**:
  - **callback_context**: 현재 에이전트 호출의 컨텍스트
  - **llm_request**: 모델에 전송될 준비된 요청 객체
- **반환값**: 
  - `LlmResponse`를 반환하면 조기 종료하고 응답을 즉시 반환 (캐싱 구현 가능)
  - `None`을 반환하면 LLM 요청이 정상적으로 진행

#### `async after_model_callback(*, callback_context, llm_response)`
모델로부터 응답을 받은 후 실행되는 콜백입니다.

- **반환 타입**: `Optional[LlmResponse]`
- **매개변수**:
  - **callback_context**: 현재 에이전트 호출의 컨텍스트
  - **llm_response**: 모델로부터 받은 응답 객체
- **반환값**: 
  - `LlmResponse`를 반환하면 응답을 수정하거나 대체
  - `None`을 반환하면 원래 응답 사용

#### `async on_model_error_callback(*, callback_context, llm_request, error)`
모델 호출에서 오류가 발생했을 때 실행되는 콜백입니다.

- **반환 타입**: `Optional[LlmResponse]`
- **매개변수**:
  - **callback_context**: 현재 에이전트 호출의 컨텍스트
  - **llm_request**: 오류가 발생했을 때 모델에 전송된 요청
  - **error**: 모델 실행 중 발생한 예외
- **반환값**: 
  - `LlmResponse`를 반환하면 오류를 전파하지 않고 대신 사용
  - `None`을 반환하면 원래 오류가 발생

### 도구 라이프사이클 콜백

#### `async before_tool_callback(*, tool, tool_args, tool_context)`
도구가 호출되기 전에 실행되는 콜백입니다.

- **반환 타입**: `Optional[dict]`
- **매개변수**:
  - **tool**: 실행될 도구 인스턴스
  - **tool_args**: 도구 호출에 사용될 인자들의 딕셔너리
  - **tool_context**: 도구 실행에 특정한 컨텍스트
- **반환값**: 
  - 딕셔너리를 반환하면 도구 실행을 중단하고 이 응답을 즉시 반환
  - `None`을 반환하면 원래의 수정되지 않은 인자 사용

#### `async after_tool_callback(*, tool, tool_args, tool_context, result)`
도구가 호출된 후 실행되는 콜백입니다.

- **반환 타입**: `Optional[dict]`
- **매개변수**:
  - **tool**: 방금 실행된 도구 인스턴스
  - **tool_args**: 도구에 전달된 원래 인자들
  - **tool_context**: 도구 실행에 특정한 컨텍스트
  - **result**: 도구 호출에서 반환된 딕셔너리
- **반환값**: 
  - 딕셔너리를 반환하면 원래 결과를 대체
  - `None`을 반환하면 원래의 수정되지 않은 결과 사용

#### `async on_tool_error_callback(*, tool, tool_args, tool_context, error)`
도구 호출에서 오류가 발생했을 때 실행되는 콜백입니다.

- **반환 타입**: `Optional[dict]`
- **매개변수**:
  - **tool**: 오류가 발생한 도구 인스턴스
  - **tool_args**: 도구에 전달된 인자들
  - **tool_context**: 도구 실행에 특정한 컨텍스트
  - **error**: 도구 실행 중 발생한 예외
- **반환값**: 
  - 딕셔너리를 반환하면 오류를 전파하지 않고 도구 응답으로 사용
  - `None`을 반환하면 원래 오류가 발생

### 러너 라이프사이클 콜백

#### `async before_run_callback(*, invocation_context)`
ADK 러너가 실행되기 전에 실행되는 콜백입니다.

- **반환 타입**: `Optional[Content]`
- **매개변수**:
  - **invocation_context**: 세션 정보, 루트 에이전트 등을 포함한 전체 호출의 컨텍스트
- **반환값**: 
  - `Event`를 반환하면 러너 실행을 중단하고 해당 이벤트로 종료
  - `None`을 반환하면 정상적으로 진행

#### `async after_run_callback(*, invocation_context)`
ADK 러너 실행이 완료된 후 실행되는 콜백입니다.

- **반환 타입**: `None`
- **매개변수**:
  - **invocation_context**: 전체 호출의 컨텍스트

### 이벤트 및 메시지 콜백

#### `async on_event_callback(*, invocation_context, event)`
러너에서 이벤트가 생성된 후 실행되는 콜백입니다.

- **반환 타입**: `Optional[Event]`
- **매개변수**:
  - **invocation_context**: 전체 호출의 컨텍스트
  - **event**: 러너에서 발생한 이벤트
- **반환값**: 
  - `Event`를 반환하면 원래 이벤트를 수정하거나 대체
  - `None`을 반환하면 원래 이벤트 사용

#### `async on_user_message_callback(*, invocation_context, user_message)`
호출이 시작되기 전에 사용자 메시지를 받았을 때 실행되는 콜백입니다.

- **반환 타입**: `Optional[Content]`
- **매개변수**:
  - **invocation_context**: 전체 호출의 컨텍스트
  - **user_message**: 사용자가 입력한 메시지 내용
- **반환값**: 
  - `types.Content`를 반환하면 사용자 메시지를 대체
  - `None`을 반환하면 정상적으로 진행

---

## 사용 예시

### 기본 로깅 플러그인

```python
from google.adk.plugins import BasePlugin
from google.adk.tools import BaseTool
from google.adk.tools import ToolContext
from typing import Any

class ToolLoggerPlugin(BasePlugin):
    def __init__(self):
        super().__init__(name="tool_logger")
    
    async def before_tool_callback(
        self, *, tool: BaseTool, tool_args: dict[str, Any], tool_context: ToolContext
    ):
        print(f"[{self.name}] Calling tool '{tool.name}' with args: {tool_args}")
    
    async def after_tool_callback(
        self, *, tool: BaseTool, tool_args: dict, tool_context: ToolContext, result: dict
    ):
        print(f"[{self.name}] Tool '{tool.name}' finished with result: {result}")

# 러너에 플러그인 추가
# runner = Runner(
#     ...
#     plugins=[ToolLoggerPlugin()],
# )
```

### 캐싱 플러그인

```python
from google.adk.plugins import BasePlugin
import hashlib
import json

class ModelCachePlugin(BasePlugin):
    def __init__(self):
        super().__init__(name="model_cache")
        self.cache = {}
    
    def _generate_cache_key(self, llm_request):
        # 요청을 기반으로 캐시 키 생성
        request_str = json.dumps({
            "contents": str(llm_request.contents),
            "tools": str(llm_request.tools) if llm_request.tools else None
        }, sort_keys=True)
        return hashlib.md5(request_str.encode()).hexdigest()
    
    async def before_model_callback(self, *, callback_context, llm_request):
        cache_key = self._generate_cache_key(llm_request)
        
        if cache_key in self.cache:
            print(f"[{self.name}] Cache hit for request")
            return self.cache[cache_key]  # 캐시된 응답 반환
        
        return None  # 캐시 미스, 정상 진행
    
    async def after_model_callback(self, *, callback_context, llm_response):
        # 응답을 캐시에 저장
        cache_key = self._generate_cache_key(callback_context.llm_request)
        self.cache[cache_key] = llm_response
        print(f"[{self.name}] Cached response for future use")
        
        return None  # 원래 응답 사용
```

### 오류 처리 플러그인

```python
from google.adk.plugins import BasePlugin
from google.genai.types import Content, Part

class ErrorHandlerPlugin(BasePlugin):
    def __init__(self):
        super().__init__(name="error_handler")
    
    async def on_model_error_callback(self, *, callback_context, llm_request, error):
        print(f"[{self.name}] Model error occurred: {error}")
        
        # 모델 오류 시 기본 응답 제공
        fallback_response = LlmResponse(
            content=Content(parts=[Part(text="죄송합니다. 일시적인 오류가 발생했습니다. 다시 시도해 주세요.")])
        )
        return fallback_response
    
    async def on_tool_error_callback(self, *, tool, tool_args, tool_context, error):
        print(f"[{self.name}] Tool '{tool.name}' error: {error}")
        
        # 도구 오류 시 오류 메시지 반환
        return {
            "error": f"도구 '{tool.name}' 실행 중 오류 발생: {str(error)}",
            "success": False
        }
```

### 모니터링 플러그인

```python
from google.adk.plugins import BasePlugin
import time

class MonitoringPlugin(BasePlugin):
    def __init__(self):
        super().__init__(name="monitoring")
        self.metrics = {
            "agent_calls": 0,
            "tool_calls": 0,
            "model_calls": 0,
            "total_time": 0
        }
        self.start_time = None
    
    async def before_run_callback(self, *, invocation_context):
        self.start_time = time.time()
        print(f"[{self.name}] Starting invocation: {invocation_context.invocation_id}")
    
    async def after_run_callback(self, *, invocation_context):
        if self.start_time:
            total_time = time.time() - self.start_time
            self.metrics["total_time"] = total_time
        
        print(f"[{self.name}] Invocation completed. Metrics: {self.metrics}")
    
    async def before_agent_callback(self, *, agent, callback_context):
        self.metrics["agent_calls"] += 1
        print(f"[{self.name}] Agent '{agent.name}' starting")
    
    async def before_tool_callback(self, *, tool, tool_args, tool_context):
        self.metrics["tool_calls"] += 1
        print(f"[{self.name}] Tool '{tool.name}' called")
    
    async def before_model_callback(self, *, callback_context, llm_request):
        self.metrics["model_calls"] += 1
        print(f"[{self.name}] Model call initiated")
```

### 사용자 입력 검증 플러그인

```python
from google.adk.plugins import BasePlugin
from google.genai.types import Content, Part

class InputValidationPlugin(BasePlugin):
    def __init__(self, forbidden_words=None):
        super().__init__(name="input_validation")
        self.forbidden_words = forbidden_words or []
    
    async def on_user_message_callback(self, *, invocation_context, user_message):
        # 사용자 메시지에서 금지 단어 검사
        message_text = ""
        for part in user_message.parts:
            if hasattr(part, 'text'):
                message_text += part.text
        
        for forbidden_word in self.forbidden_words:
            if forbidden_word.lower() in message_text.lower():
                print(f"[{self.name}] Blocked message containing: {forbidden_word}")
                
                # 차단 메시지로 대체
                return Content(parts=[Part(text="죄송합니다. 부적절한 내용이 포함된 메시지는 처리할 수 없습니다.")])
        
        return None  # 정상 진행
```

### 러너에서 플러그인 사용

```python
from google.adk.runner import Runner

# 여러 플러그인을 함께 사용
plugins = [
    ToolLoggerPlugin(),
    ModelCachePlugin(),
    ErrorHandlerPlugin(),
    MonitoringPlugin(),
    InputValidationPlugin(forbidden_words=["spam", "abuse"])
]

runner = Runner(
    agent=my_agent,
    plugins=plugins
)

# 플러그인들이 자동으로 적용됨
result = await runner.run_async(user_input="안녕하세요!")
```

---

## 주요 특징

### 전역 적용
- 러너에 등록된 모든 에이전트에 자동으로 적용
- 일관된 동작과 정책을 모든 에이전트에 강제

### 우선순위 시스템
- 플러그인이 에이전트 콜백보다 먼저 실행
- 값을 반환하면 후속 콜백들을 스킵

### 유연한 개입 지점
- 에이전트, 도구, 모델의 전체 라이프사이클을 커버
- 오류 상황에서도 개입 가능

### 체인 방식 처리
- 여러 플러그인이 순차적으로 실행
- 이전 플러그인의 수정 사항이 다음으로 전파

### 다양한 용도
- 로깅 및 모니터링
- 캐싱 및 성능 최적화
- 보안 및 입력 검증
- 오류 처리 및 복구
- 커스텀 비즈니스 로직 주입