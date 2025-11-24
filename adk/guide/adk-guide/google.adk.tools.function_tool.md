# Google ADK Tools Function Tool API Reference

`google.adk.tools.function_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### FunctionTool

```python
class google.adk.tools.function_tool.FunctionTool(func)
```

**상속**: `BaseTool`

사용자 정의 Python 함수를 래핑하는 도구입니다.

#### 필드

- **func** - 래핑할 함수

#### 생성자

호출 가능한 객체에서 메타데이터를 추출합니다.

#### 메소드

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