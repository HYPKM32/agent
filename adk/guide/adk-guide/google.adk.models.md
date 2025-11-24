# Google ADK Models API Reference

`google.adk.models` 모듈의 API 레퍼런스 문서입니다.

모델을 지원하기 위한 인터페이스를 정의합니다.

## 클래스

### BaseLlm

```python
pydantic model google.adk.models.BaseLlm
```

**상속**: `BaseModel`

BaseLLM 클래스입니다.

#### 필드

- **model**: `str` (필수) - LLM의 이름 (예: gemini-1.5-flash 또는 gemini-1.5-flash-001)

#### 메소드

##### `classmethod supported_models()`
LlmRegistry를 위한 지원되는 모델들의 정규식 리스트를 반환합니다.

- **반환 타입**: `list[str]`

##### `connect(llm_request)`
LLM에 대한 라이브 연결을 생성합니다.

- **반환 타입**: `BaseLlmConnection`
- **매개변수**:
  - **llm_request**: LLM에 보낼 요청
- **반환값**: LLM에 대한 연결

##### `async generate_content_async(llm_request, stream=False)` (추상 메소드)
주어진 콘텐츠와 도구로부터 하나의 콘텐츠를 생성합니다.

- **반환 타입**: `AsyncGenerator[LlmResponse, None]`
- **매개변수**:
  - **llm_request**: LLM에 보낼 요청
  - **stream**: 스트리밍 호출 여부 (기본값: False)
- **Yields**: types.Content의 생성기
  - **비스트리밍 호출**: 하나의 Content만 yield
  - **스트리밍 호출**: 여러 Content를 yield할 수 있으며, 모든 yield된 콘텐츠는 parts 리스트를 병합하여 하나의 콘텐츠로 처리

---

### Gemini

```python
pydantic model google.adk.models.Gemini
```

**상속**: `BaseLlm`

Gemini 모델을 위한 통합 클래스입니다.

#### 필드

- **model**: `str` (기본값: 'gemini-1.5-flash') - Gemini 모델의 이름
- **retry_options**: `Optional[types.HttpRetryOptions]` (기본값: None) - Gemini가 실패한 응답을 재시도할 수 있도록 허용

#### 재시도 옵션 예시

```python
from google.genai import types

agent = Agent(
    model=Gemini(
        retry_options=types.HttpRetryOptions(initial_delay=1, attempts=2),
    )
)
```

#### 메소드

##### `static supported_models()`
지원되는 모델들의 리스트를 제공합니다.

- **반환 타입**: `list[str]`
- **반환값**: 지원되는 모델들의 리스트

##### `connect(llm_request)`
Gemini 모델에 연결하고 LLM 연결을 반환합니다.

- **반환 타입**: `BaseLlmConnection`
- **매개변수**:
  - **llm_request**: Gemini 모델에 보낼 요청
- **Yields**: Gemini 모델에 대한 연결

##### `async generate_content_async(llm_request, stream=False)`
Gemini 모델에 요청을 보냅니다.

- **반환 타입**: `AsyncGenerator[LlmResponse, None]`
- **매개변수**:
  - **llm_request**: Gemini 모델에 보낸 요청
  - **stream**: 스트리밍 호출 여부 (기본값: False)
- **Yields**: **LlmResponse** - 모델 응답

#### 속성

##### `property api_client: Client`
API 클라이언트를 제공합니다.

- **반환값**: API 클라이언트

---

### LLMRegistry

```python
class google.adk.models.LLMRegistry
```

**상속**: `object`

LLM을 위한 레지스트리입니다.

#### 정적 메소드

##### `static new_llm(model)`
새로운 LLM 인스턴스를 생성합니다.

- **반환 타입**: `BaseLlm`
- **매개변수**:
  - **model**: 모델 이름
- **반환값**: LLM 인스턴스

##### `static register(llm_cls)`
새로운 LLM 클래스를 등록합니다.

- **매개변수**:
  - **llm_cls**: 모델을 구현하는 클래스

##### `static resolve(model)`
모델을 BaseLlm 서브클래스로 해결합니다.

- **반환 타입**: `type[BaseLlm]`
- **매개변수**:
  - **model**: 모델 이름
- **반환값**: BaseLlm 서브클래스
- **예외**: **ValueError** - 모델을 찾을 수 없는 경우

---

## 사용 예시

### Gemini 모델 기본 사용

```python
from google.adk.models import Gemini
from google.genai import types

# 기본 Gemini 모델 생성
gemini_model = Gemini()

# 특정 Gemini 모델 사용
gemini_pro = Gemini(model="gemini-1.5-pro")

# 재시도 옵션과 함께 Gemini 모델 사용
gemini_with_retry = Gemini(
    model="gemini-1.5-flash",
    retry_options=types.HttpRetryOptions(
        initial_delay=1,
        attempts=3
    )
)
```

### 콘텐츠 생성

```python
from google.adk.models import Gemini

# Gemini 모델 인스턴스 생성
model = Gemini(model="gemini-1.5-flash")

# 비스트리밍 콘텐츠 생성
async def generate_response(llm_request):
    async for response in model.generate_content_async(llm_request, stream=False):
        return response

# 스트리밍 콘텐츠 생성
async def generate_streaming_response(llm_request):
    responses = []
    async for response in model.generate_content_async(llm_request, stream=True):
        responses.append(response)
        print(f"스트리밍 응답: {response}")
    return responses
```

### LLMRegistry 사용

```python
from google.adk.models import LLMRegistry, Gemini

# Gemini 클래스 등록 (보통 자동으로 등록됨)
LLMRegistry.register(Gemini)

# 모델 이름으로 LLM 인스턴스 생성
model_instance = LLMRegistry.new_llm("gemini-1.5-flash")

# 모델 이름으로 클래스 해결
model_class = LLMRegistry.resolve("gemini-1.5-flash")
```

### 커스텀 LLM 구현

```python
from google.adk.models import BaseLlm, LLMRegistry
from typing import AsyncGenerator

class CustomLlm(BaseLlm):
    model: str = "custom-model-v1"
    
    @classmethod
    def supported_models(cls):
        return ["custom-model-.*"]
    
    async def generate_content_async(self, llm_request, stream=False):
        # 커스텀 모델 로직 구현
        if stream:
            # 스트리밍 응답 구현
            for i in range(3):
                yield LlmResponse(content=f"스트리밍 응답 {i}")
        else:
            # 단일 응답 구현
            yield LlmResponse(content="커스텀 모델 응답")

# 커스텀 LLM 등록
LLMRegistry.register(CustomLlm)

# 사용
custom_model = LLMRegistry.new_llm("custom-model-v1")
```

### 에이전트와 함께 사용

```python
from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.genai import types

# Gemini 모델을 사용하는 에이전트 생성
agent = LlmAgent(
    name="gemini_agent",
    model=Gemini(
        model="gemini-1.5-pro",
        retry_options=types.HttpRetryOptions(
            initial_delay=2,
            attempts=3
        )
    ),
    instruction="당신은 도움이 되는 AI 어시스턴트입니다."
)
```

### 연결 관리

```python
from google.adk.models import Gemini

model = Gemini()

# LLM 연결 생성
connection = model.connect(llm_request)

# 연결을 통한 라이브 통신
# (연결 사용 로직)
```

---

## 주요 특징

### 모델 추상화
- `BaseLlm`을 통해 다양한 LLM 모델을 통합된 인터페이스로 사용
- 모델별 구체적인 구현은 각 서브클래스에서 처리

### Gemini 통합
- Google의 Gemini 모델과의 직접적인 통합
- 재시도 옵션, API 클라이언트 관리 등 고급 기능 지원

### 레지스트리 시스템
- `LLMRegistry`를 통한 중앙화된 모델 관리
- 동적 모델 등록 및 해결
- 정규식 기반 모델 매칭

### 스트리밍 지원
- 실시간 응답을 위한 스트리밍 API 지원
- 비스트리밍과 스트리밍 모드 모두 지원

### 확장성
- 커스텀 LLM 구현을 위한 명확한 인터페이스
- 플러그인 방식의 모델 등록 시스템