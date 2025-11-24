# Google ADK Tools Base Tool API Reference

`google.adk.tools.base_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseTool

```python
class google.adk.tools.base_tool.BaseTool(*, name, description, is_long_running=False)
```

**상속**: `ABC`

모든 도구의 기본 클래스입니다.

#### 필드

- **description**: `str` - 도구의 설명
- **is_long_running**: `bool` = False - 도구가 장기 실행 작업인지 여부, 일반적으로 리소스 ID를 먼저 반환하고 나중에 작업을 완료합니다.
- **name**: `str` - 도구의 이름

#### 메소드

##### `classmethod from_config(config, config_abs_path)`

구성에서 도구 인스턴스를 생성합니다.

서브클래스는 구성에서 사용자 정의 초기화를 수행하기 위해 이 메소드를 재정의하고 구현해야 합니다.

- **반환 타입**: `TypeVar`(`SelfTool`, bound= BaseTool)
- **매개변수**:
  - **config** – 도구의 구성
  - **config_abs_path** – 도구 구성이 포함된 구성 파일의 절대 경로
- **반환값**: 도구 인스턴스

##### `async process_llm_request(*, tool_context, llm_request)`

이 도구에 대한 나가는 LLM 요청을 처리합니다.

사용 사례:
- 가장 일반적인 사용 사례는 LLM 요청에 이 도구를 추가하는 것입니다.
- 일부 도구는 LLM 요청이 전송되기 전에 전처리만 할 수 있습니다.

- **반환 타입**: `None`
- **매개변수**:
  - **tool_context** – 도구의 컨텍스트
  - **llm_request** – 나가는 LLM 요청, 이 메소드에서 변경 가능

##### `async run_async(*, args, tool_context)`

주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Any`

> **참고**
> - 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다.
> - 그렇지 않으면 생략할 수 있습니다. 예: Gemini용 내장 GoogleSearch 도구의 경우.

**매개변수:**
- **args** – LLM이 채운 인자들
- **tool_context** – 도구의 컨텍스트

**반환값:** 도구 실행 결과

---

### BaseToolConfig

```python
pydantic model google.adk.tools.base_tool.BaseToolConfig
```

**상속**: `BaseModel`

모든 도구의 기본 구성입니다.

---

### ToolArgsConfig

```python
pydantic model google.adk.tools.base_tool.ToolArgsConfig
```

**상속**: `BaseModel`

도구 인자의 구성입니다.

이 구성은 도구 인자로 임의의 키-값 쌍을 허용합니다.

---

### ToolConfig

```python
pydantic model google.adk.tools.base_tool.ToolConfig
```

**상속**: `BaseModel`

도구의 구성입니다.

이 구성은 다음 유형의 도구를 지원합니다:
1. ADK 내장 도구
2. 사용자 정의 도구 인스턴스
3. 사용자 정의 도구 클래스
4. 도구 인스턴스를 생성하는 사용자 정의 함수
5. 사용자 정의 함수 도구

**예시:**

1. google.adk.tools 패키지의 ADK 내장 도구 인스턴스 또는 클래스의 경우, 이름과 선택적으로 구성으로 직접 참조할 수 있습니다.
```yaml
tools:
  - name: google_search
  - name: AgentTool
    config:
      agent: ./another_agent.yaml
      skip_summarization: true
```

2. 사용자 정의 도구 인스턴스의 경우, 이름은 도구 인스턴스의 완전한 경로입니다.
```yaml
tools:
  - name: my_package.my_module.my_tool
```

3. 사용자 정의 도구 클래스(사용자 정의 도구)의 경우, 이름은 도구 클래스의 완전한 경로이고 config는 도구의 인자입니다.
```yaml
tools:
  - name: my_package.my_module.my_tool_class
    config:
      my_tool_arg1: value1
      my_tool_arg2: value2
```

4. 도구 인스턴스를 생성하는 사용자 정의 함수의 경우, 이름은 함수의 완전한 경로이고 config는 함수에 인자로 전달됩니다.
```yaml
tools:
  - name: my_package.my_module.my_tool_function
    config:
      my_function_arg1: value1
      my_function_arg2: value2
```

함수는 다음 시그니처를 가져야 합니다:
```python
def my_function(config: ToolArgsConfig) -> BaseTool:
    ...
```

5. 사용자 정의 함수 도구의 경우, 이름은 함수의 완전한 경로입니다.
```yaml
tools:
  - name: my_package.my_module.my_function_tool
```

#### 필드

- **args**: `Optional[ToolArgsConfig]` = None - 도구의 인자
- **name**: `str` [필수] - 도구의 이름

##### `field args: Optional[ToolArgsConfig] = None`
도구의 인자입니다.

##### `field name: str [Required]`
도구의 이름입니다.

ADK 내장 도구의 경우, 이름은 도구의 이름입니다. 예: google_search 또는 AgentTool.
사용자 정의 도구의 경우, 이름은 도구의 완전한 경로입니다. 예: my_package.my_module.my_tool.