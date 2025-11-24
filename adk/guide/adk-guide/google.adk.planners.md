# Google ADK Planners API Reference

`google.adk.planners` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BasePlanner

```python
class google.adk.planners.BasePlanner
```

**상속**: `ABC`

모든 플래너의 추상 기본 클래스입니다.

플래너는 에이전트가 쿼리에 대한 계획을 생성하여 행동을 안내할 수 있게 해줍니다.

#### 추상 메소드

##### `build_planning_instruction(readonly_context, llm_request)`
계획 수립을 위해 LLM 요청에 추가될 시스템 지시사항을 구성합니다.

- **반환 타입**: `Optional[str]`
- **매개변수**:
  - **readonly_context**: 호출의 읽기 전용 컨텍스트
  - **llm_request**: LLM 요청 (읽기 전용)
- **반환값**: 계획 수립 시스템 지시사항, 또는 지시사항이 필요하지 않으면 None

##### `process_planning_response(callback_context, response_parts)`
계획 수립을 위한 LLM 응답을 처리합니다.

- **반환 타입**: `Optional[List[Part]]`
- **매개변수**:
  - **callback_context**: 호출의 콜백 컨텍스트
  - **response_parts**: LLM 응답 부분들 (읽기 전용)
- **반환값**: 처리된 응답 부분들, 또는 처리가 필요하지 않으면 None

---

### BuiltInPlanner

```python
class google.adk.planners.BuiltInPlanner(*, thinking_config)
```

**상속**: `BasePlanner`

모델의 내장 사고 기능을 사용하는 내장 플래너입니다.

#### 필드

- **thinking_config**: `ThinkingConfig` - 모델의 내장 사고 기능을 위한 설정

> ⚠️ **주의**: 사고 기능을 지원하지 않는 모델에 이 필드가 설정되면 오류가 반환됩니다.

#### 생성자

내장 플래너를 초기화합니다.

- **매개변수**:
  - **thinking_config**: 모델의 내장 사고 기능을 위한 설정

#### 메소드

##### `apply_thinking_config(llm_request)`
LLM 요청에 사고 설정을 적용합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **llm_request**: 사고 설정을 적용할 LLM 요청

##### `build_planning_instruction(readonly_context, llm_request)`
계획 수립을 위해 LLM 요청에 추가될 시스템 지시사항을 구성합니다.

- **반환 타입**: `Optional[str]`
- **매개변수**:
  - **readonly_context**: 호출의 읽기 전용 컨텍스트
  - **llm_request**: LLM 요청 (읽기 전용)
- **반환값**: 계획 수립 시스템 지시사항, 또는 지시사항이 필요하지 않으면 None

##### `process_planning_response(callback_context, response_parts)`
계획 수립을 위한 LLM 응답을 처리합니다.

- **반환 타입**: `Optional[List[Part]]`
- **매개변수**:
  - **callback_context**: 호출의 콜백 컨텍스트
  - **response_parts**: LLM 응답 부분들 (읽기 전용)
- **반환값**: 처리된 응답 부분들, 또는 처리가 필요하지 않으면 None

---

### PlanReActPlanner

```python
class google.adk.planners.PlanReActPlanner
```

**상속**: `BasePlanner`

어떤 행동/관찰 전에 계획을 생성하도록 LLM 응답을 제약하는 Plan-Re-Act 플래너입니다.

> **참고**: 이 플래너는 모델이 내장 사고 기능을 지원하거나 사고 설정을 설정할 필요가 없습니다.

#### 메소드

##### `build_planning_instruction(readonly_context, llm_request)`
계획 수립을 위해 LLM 요청에 추가될 시스템 지시사항을 구성합니다.

- **반환 타입**: `str`
- **매개변수**:
  - **readonly_context**: 호출의 읽기 전용 컨텍스트
  - **llm_request**: LLM 요청 (읽기 전용)
- **반환값**: 계획 수립 시스템 지시사항, 또는 지시사항이 필요하지 않으면 None

##### `process_planning_response(callback_context, response_parts)`
계획 수립을 위한 LLM 응답을 처리합니다.

- **반환 타입**: `Optional[List[Part]]`
- **매개변수**:
  - **callback_context**: 호출의 콜백 컨텍스트
  - **response_parts**: LLM 응답 부분들 (읽기 전용)
- **반환값**: 처리된 응답 부분들, 또는 처리가 필요하지 않으면 None

---

## 사용 예시

### BuiltInPlanner 사용

```python
from google.adk.planners import BuiltInPlanner
from google.adk.agents import LlmAgent
from google.genai import types

# 사고 설정을 가진 내장 플래너 생성
thinking_config = types.ThinkingConfig(
    include_thinking_process=True
)

built_in_planner = BuiltInPlanner(thinking_config=thinking_config)

# 에이전트에 플래너 적용
agent = LlmAgent(
    name="planning_agent",
    model="gemini-2.0-flash-thinking-exp",
    planner=built_in_planner,
    instruction="당신은 체계적으로 계획을 세우는 AI 어시스턴트입니다."
)
```

### PlanReActPlanner 사용

```python
from google.adk.planners import PlanReActPlanner
from google.adk.agents import LlmAgent

# Plan-Re-Act 플래너 생성
plan_react_planner = PlanReActPlanner()

# 에이전트에 플래너 적용
agent = LlmAgent(
    name="strategic_agent",
    model="gemini-1.5-pro",
    planner=plan_react_planner,
    instruction="문제를 해결하기 전에 항상 단계별 계획을 세우세요.",
    tools=[
        # 다양한 도구들
    ]
)
```

### 커스텀 플래너 구현

```python
from google.adk.planners import BasePlanner
from typing import Optional, List
from google.genai.types import Part

class CustomPlanner(BasePlanner):
    def __init__(self, planning_style="detailed"):
        self.planning_style = planning_style
    
    def build_planning_instruction(self, readonly_context, llm_request):
        if self.planning_style == "detailed":
            return """
            작업을 수행하기 전에 다음 형식으로 상세한 계획을 세우세요:
            
            **계획:**
            1. [첫 번째 단계]
            2. [두 번째 단계]
            3. [세 번째 단계]
            ...
            
            그런 다음 계획에 따라 단계별로 실행하세요.
            """
        elif self.planning_style == "brief":
            return "작업 전에 간단한 계획을 세우세요."
        return None
    
    def process_planning_response(self, callback_context, response_parts):
        # 응답에서 계획 부분을 추출하고 처리
        processed_parts = []
        for part in response_parts:
            if "**계획:**" in part.text:
                # 계획이 포함된 응답 처리
                processed_parts.append(part)
            else:
                processed_parts.append(part)
        
        return processed_parts if processed_parts else None

# 사용법
custom_planner = CustomPlanner(planning_style="detailed")

agent = LlmAgent(
    name="custom_planning_agent",
    planner=custom_planner,
    instruction="당신은 체계적인 계획 수립을 중시하는 AI입니다."
)
```

### 플래너와 도구 함께 사용

```python
from google.adk.planners import PlanReActPlanner
from google.adk.agents import LlmAgent
from google.adk.tools import FunctionTool

def search_web(query: str) -> str:
    """웹에서 정보를 검색합니다."""
    return f"'{query}'에 대한 검색 결과"

def calculate(expression: str) -> str:
    """수학 계산을 수행합니다."""
    try:
        result = eval(expression)
        return f"{expression} = {result}"
    except:
        return "계산 오류"

# 도구들을 가진 계획 기반 에이전트
planner = PlanReActPlanner()

agent = LlmAgent(
    name="tool_planning_agent",
    planner=planner,
    tools=[
        FunctionTool(search_web),
        FunctionTool(calculate)
    ],
    instruction="""
    당신은 도구를 사용하여 문제를 해결하는 AI입니다.
    항상 다음 순서를 따르세요:
    1. 문제 분석 및 계획 수립
    2. 필요한 도구 식별
    3. 단계별 실행
    4. 결과 종합
    """
)
```

### 조건부 계획 수립

```python
from google.adk.planners import BasePlanner

class ConditionalPlanner(BasePlanner):
    def __init__(self, enable_planning_for_complex_queries=True):
        self.enable_planning_for_complex_queries = enable_planning_for_complex_queries
    
    def build_planning_instruction(self, readonly_context, llm_request):
        # 요청의 복잡도에 따라 계획 수립 여부 결정
        request_text = " ".join([
            part.text for content in llm_request.contents 
            for part in content.parts if hasattr(part, 'text')
        ])
        
        # 복잡한 쿼리 키워드 확인
        complex_keywords = ['단계별', '계획', '분석', '비교', '전략']
        
        if (self.enable_planning_for_complex_queries and 
            any(keyword in request_text for keyword in complex_keywords)):
            return "이 요청은 복잡하므로 단계별 계획을 먼저 세우세요."
        
        return None
    
    def process_planning_response(self, callback_context, response_parts):
        # 기본 처리
        return response_parts

# 사용법
conditional_planner = ConditionalPlanner()
agent = LlmAgent(
    name="smart_planning_agent",
    planner=conditional_planner
)
```

---

## 주요 특징

### 계획 기반 추론
- 에이전트가 행동하기 전에 체계적인 계획을 수립
- 복잡한 작업을 작은 단계로 분해하여 처리

### 다양한 플래너 타입
- **BuiltInPlanner**: 모델의 내장 사고 기능 활용
- **PlanReActPlanner**: 명시적인 계획-행동-관찰 패턴 강제
- 커스텀 플래너 구현 가능

### 유연한 통합
- LLM 요청 전처리를 통한 계획 지시사항 주입
- LLM 응답 후처리를 통한 계획 추출 및 검증

### 모델 호환성
- 사고 기능 지원 모델과 일반 모델 모두 지원
- 모델별 최적화된 계획 수립 전략 적용

### 도구와의 시너지
- 도구 사용 전 계획 수립으로 효율성 향상
- 복잡한 도구 체인 실행 시 오류 감소