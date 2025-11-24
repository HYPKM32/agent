# Google ADK Tools Agent Tool API Reference

`google.adk.tools.agent_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### AgentTool

```python
class google.adk.tools.agent_tool.AgentTool(agent, skip_summarization=False)
```

**상속**: `BaseTool`

에이전트를 래핑하는 도구입니다.

이 도구는 더 큰 애플리케이션 내에서 에이전트를 도구로 호출할 수 있게 해줍니다. 에이전트의 입력 스키마가 도구의 입력 매개변수를 정의하는데 사용되고, 에이전트의 출력이 도구의 결과로 반환됩니다.

#### 속성

- **agent**: 래핑할 에이전트
- **skip_summarization**: 에이전트 출력의 요약을 건너뛸지 여부 (기본값: False)

#### 메소드

##### `classmethod from_config(config, config_abs_path)`
설정으로부터 도구 인스턴스를 생성합니다.

서브클래스는 설정으로부터 커스텀 초기화를 수행하기 위해 이 메소드를 오버라이드하고 구현해야 합니다.

- **반환 타입**: `AgentTool`
- **매개변수**:
  - **config**: 도구의 설정
  - **config_abs_path**: 도구 설정이 포함된 설정 파일의 절대 경로
- **반환값**: 도구 인스턴스

##### `populate_name()`
- **반환 타입**: `Any`

##### `async run_async(*, args, tool_context)`
주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`
- **매개변수**:
  - **args**: LLM이 채운 인자들
  - **tool_context**: 도구의 컨텍스트
- **반환값**: 도구 실행 결과

> **참고**: 
> - 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다
> - 그렇지 않으면 건너뛸 수 있습니다 (예: Gemini용 내장 GoogleSearch 도구)

---

### AgentToolConfig

```python
pydantic model google.adk.tools.agent_tool.AgentToolConfig
```

**상속**: `BaseToolConfig`

AgentTool을 위한 설정입니다.

#### 필드

- **agent**: `AgentRefConfig` (필수) - 에이전트 인스턴스에 대한 참조
- **skip_summarization**: `bool` (기본값: False) - 에이전트 출력의 요약을 건너뛸지 여부

#### 필드 설명

##### `field agent: AgentRefConfig [Required]`
에이전트 인스턴스에 대한 참조입니다.

##### `field skip_summarization: bool = False`
에이전트 출력의 요약을 건너뛸지 여부입니다.

---

## 사용 예시

### 기본 AgentTool 사용

```python
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents import LlmAgent

# 전문 에이전트 생성
specialist_agent = LlmAgent(
    name="math_specialist",
    model="gemini-1.5-pro",
    instruction="당신은 수학 문제 해결 전문가입니다. 복잡한 수학 문제를 단계별로 해결합니다."
)

# 에이전트를 도구로 래핑
math_tool = AgentTool(
    agent=specialist_agent,
    skip_summarization=False
)

# 메인 에이전트에서 도구로 사용
main_agent = LlmAgent(
    name="general_assistant",
    model="gemini-1.5-flash",
    tools=[math_tool],
    instruction="다양한 질문에 답변합니다. 수학 문제는 전문가 도구를 사용하세요."
)
```

### 요약 건너뛰기 설정

```python
from google.adk.tools.agent_tool import AgentTool

# 빠른 응답이 필요한 경우 요약 건너뛰기
quick_agent = LlmAgent(
    name="quick_responder",
    instruction="간단하고 직접적인 답변을 제공합니다."
)

quick_tool = AgentTool(
    agent=quick_agent,
    skip_summarization=True  # 요약 과정 생략
)
```

### 설정 파일을 통한 AgentTool 생성

```python
from google.adk.tools.agent_tool import AgentTool, AgentToolConfig
from google.adk.agents.common_configs import AgentRefConfig

# 설정 객체 생성
config = AgentToolConfig(
    agent=AgentRefConfig(
        name="data_analyst",
        config_path="./configs/data_analyst.yaml"
    ),
    skip_summarization=False
)

# 설정으로부터 도구 생성
agent_tool = AgentTool.from_config(
    config=config,
    config_abs_path="/path/to/config/directory"
)
```

### 다중 전문 에이전트 시스템

```python
from google.adk.tools.agent_tool import AgentTool
from google.adk.agents import LlmAgent

# 다양한 전문 에이전트들 생성
code_agent = LlmAgent(
    name="code_specialist",
    instruction="프로그래밍 관련 질문에 전문적으로 답변합니다."
)

science_agent = LlmAgent(
    name="science_specialist", 
    instruction="과학 관련 질문에 전문적으로 답변합니다."
)

writing_agent = LlmAgent(
    name="writing_specialist",
    instruction="글쓰기와 언어 관련 질문에 전문적으로 답변합니다."
)

# 각 에이전트를 도구로 래핑
code_tool = AgentTool(agent=code_agent, skip_summarization=False)
science_tool = AgentTool(agent=science_agent, skip_summarization=False)
writing_tool = AgentTool(agent=writing_agent, skip_summarization=True)

# 코디네이터 에이전트 생성
coordinator = LlmAgent(
    name="coordinator",
    tools=[code_tool, science_tool, writing_tool],
    instruction="""
    당신은 질문을 적절한 전문가에게 라우팅하는 코디네이터입니다.
    - 프로그래밍 질문: code_specialist 사용
    - 과학 질문: science_specialist 사용  
    - 글쓰기 질문: writing_specialist 사용
    """
)
```

### 계층적 에이전트 구조

```python
from google.adk.tools.agent_tool import AgentTool

# 하위 레벨 에이전트들
research_agent = LlmAgent(
    name="researcher",
    instruction="주제에 대한 깊이 있는 연구를 수행합니다."
)

analysis_agent = LlmAgent(
    name="analyzer", 
    instruction="데이터와 정보를 분석하여 인사이트를 제공합니다."
)

# 중간 레벨 에이전트
middle_agent = LlmAgent(
    name="processor",
    tools=[
        AgentTool(research_agent),
        AgentTool(analysis_agent)
    ],
    instruction="연구와 분석을 조합하여 종합적인 답변을 제공합니다."
)

# 최상위 에이전트
top_agent = LlmAgent(
    name="director",
    tools=[AgentTool(middle_agent)],
    instruction="복잡한 요청을 처리하고 최종 결과를 제공합니다."
)
```

### 비동기 에이전트 도구 실행

```python
from google.adk.tools.agent_tool import AgentTool
import asyncio

async def demonstrate_agent_tool():
    # 에이전트 도구 설정
    specialist = LlmAgent(
        name="specialist",
        instruction="전문적인 답변을 제공합니다."
    )
    
    agent_tool = AgentTool(
        agent=specialist,
        skip_summarization=False
    )
    
    # 도구 컨텍스트 설정 (실제 구현에서는 프레임워크가 제공)
    # tool_context = ToolContext(...)
    
    # 도구 실행
    # result = await agent_tool.run_async(
    #     args={"query": "복잡한 질문입니다"},
    #     tool_context=tool_context
    # )
    
    print("에이전트 도구가 성공적으로 실행되었습니다.")

# 실행
# asyncio.run(demonstrate_agent_tool())
```

### 설정 기반 에이전트 도구 팩토리

```python
from google.adk.tools.agent_tool import AgentTool, AgentToolConfig
from typing import Dict, Any

class AgentToolFactory:
    def __init__(self, config_base_path: str):
        self.config_base_path = config_base_path
    
    def create_agent_tool(self, config_data: Dict[str, Any]) -> AgentTool:
        """설정 데이터로부터 AgentTool 생성"""
        config = AgentToolConfig(**config_data)
        
        return AgentTool.from_config(
            config=config,
            config_abs_path=self.config_base_path
        )
    
    def create_multiple_tools(self, configs: List[Dict[str, Any]]) -> List[AgentTool]:
        """여러 에이전트 도구를 한 번에 생성"""
        return [self.create_agent_tool(config) for config in configs]

# 사용 예시
factory = AgentToolFactory("/path/to/configs")

tool_configs = [
    {
        "agent": {
            "name": "translator",
            "config_path": "translator.yaml"
        },
        "skip_summarization": True
    },
    {
        "agent": {
            "name": "summarizer", 
            "config_path": "summarizer.yaml"
        },
        "skip_summarization": False
    }
]

agent_tools = factory.create_multiple_tools(tool_configs)
```

---

## 주요 특징

### 에이전트 도구화
- 기존 에이전트를 도구로 변환하여 다른 에이전트에서 사용 가능
- 에이전트의 입력 스키마를 도구 인터페이스로 자동 매핑
- 에이전트 간 계층적 구조 구축 지원

### 요약 제어
- `skip_summarization` 옵션으로 출력 요약 과정 제어
- 빠른 응답이 필요한 경우 요약 생략 가능
- 상세한 출력이 필요한 경우 요약 과정 포함

### 설정 기반 생성
- `AgentToolConfig`를 통한 선언적 설정
- `from_config` 메소드로 설정 파일 기반 생성
- 재사용 가능한 도구 설정 관리

### 유연한 아키텍처
- 단일 전문 에이전트부터 복잡한 다단계 시스템까지 지원
- 동적 에이전트 라우팅 및 위임 패턴 구현
- 비동기 실행을 통한 성능 최적화

### 통합성
- BaseTool 인터페이스 준수로 다른 도구들과 일관된 사용법
- LLM 에이전트 시스템과 완전 통합
- 기존 에이전트 코드 재사용 가능