# Google ADK Tools Authenticated Function Tool API Reference

`google.adk.tools.authenticated_function_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### AuthenticatedFunctionTool

```python
class google.adk.tools.authenticated_function_tool.AuthenticatedFunctionTool(*, func, auth_config=None, response_for_auth_required=None)
```

**상속**: `FunctionTool`

실제 도구 로직이 호출되기 전에 인증을 처리하는 FunctionTool입니다. 함수는 사용할 수 있도록 준비된 자격 증명인 특별한 credential 인자를 받을 수 있습니다. (실험적 기능)

#### 생성자

AuthenticatedFunctionTool을 초기화합니다.

**매개변수:**
- **func** – 호출할 함수
- **auth_config** – 인증 구성
- **response_for_auth_required** – 도구가 클라이언트로부터 인증 자격 증명을 요청할 때 반환할 응답. 두 가지 경우가 있을 수 있습니다: 도구가 자격 증명을 구성하지 않은 경우(auth_config.raw_auth_credential이 누락됨) 또는 구성된 자격 증명이 도구 인증에 충분하지 않은 경우(예: OAuth 클라이언트 ID와 클라이언트 시크릿이 구성됨)이고 클라이언트 입력이 필요한 경우(예: 클라이언트가 최종 사용자를 OAuth 플로우에 참여시키고 OAuth 응답을 받아야 하는 경우)

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