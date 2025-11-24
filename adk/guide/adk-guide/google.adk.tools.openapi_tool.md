# Google ADK Tools OpenAPI Tool API Reference

`google.adk.tools.openapi_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### OpenAPIToolset

```python
class google.adk.tools.openapi_tool.OpenAPIToolset(*, spec_dict=None, spec_str=None, spec_str_type='json', auth_scheme=None, auth_credential=None, tool_filter=None)
```

**상속**: `BaseToolset`

OpenAPI 사양을 RestApiTool 목록으로 파싱하는 클래스입니다.

#### 사용법

```python
# 사양 문자열에서 OpenAPI 툴셋 초기화
openapi_toolset = OpenAPIToolset(spec_str=openapi_spec_str,
  spec_str_type="json")
# 또는, 사양 딕셔너리에서 OpenAPI 툴셋 초기화
openapi_toolset = OpenAPIToolset(spec_dict=openapi_spec_dict)

# 에이전트에 모든 도구 추가
agent = Agent(
  tools=[*openapi_toolset.get_tools()]
)
# 또는, 에이전트에 단일 도구 추가
agent = Agent(
  tools=[openapi_toolset.get_tool('tool_name')]
)
```

#### 생성자

OpenAPIToolset을 초기화합니다.

**매개변수:**
- **spec_dict** – OpenAPI 사양 딕셔너리. 제공되면 문자열에서 사양을 로드하는 대신 이것이 사용됩니다.
- **spec_str** – JSON 또는 YAML 형식의 OpenAPI 사양 문자열. spec_dict가 제공되지 않을 때 사용됩니다.
- **spec_str_type** – OpenAPI 사양 문자열의 타입. "json" 또는 "yaml"일 수 있습니다.
- **auth_scheme** – 모든 도구에 사용할 인증 스키마. AuthScheme을 사용하거나 google.adk.tools.openapi_tool.auth.auth_helpers의 헬퍼를 사용하세요.
- **auth_credential** – 모든 도구에 사용할 인증 자격 증명. AuthCredential을 사용하거나 google.adk.tools.openapi_tool.auth.auth_helpers의 헬퍼를 사용하세요.
- **tool_filter** – 툴셋의 도구를 필터링하는 데 사용되는 필터. 도구 술어 또는 노출할 도구의 도구 이름 목록일 수 있습니다.

#### 메소드

##### `async close()`

툴셋이 보유한 리소스를 정리하고 해제합니다.

> **참고**
> 이 메소드는 예를 들어 에이전트 서버의 생명주기 끝이나 툴셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 모든 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되어 누수를 방지하도록 해야 합니다.

##### `get_tool(tool_name)`

이름으로 도구를 가져옵니다.

- **반환 타입**: `Optional[RestApiTool]`

##### `async get_tools(readonly_context=None)`

툴셋의 모든 도구를 가져옵니다.

- **반환 타입**: `List[RestApiTool]`

---

### RestApiTool

```python
class google.adk.tools.openapi_tool.RestApiTool(name, description, endpoint, operation, auth_scheme=None, auth_credential=None, should_parse_operation=True)
```

**상속**: `BaseTool`

REST API와 상호 작용하는 범용 도구입니다.

요청 매개변수와 본문을 생성하고 API 호출에 인증 자격 증명을 첨부합니다.

#### 예시

```python
# 사양의 각 API 작업은 자체 도구로 변환됩니다
# 도구의 이름은 해당 작업의 operationId이며, snake case로 표시됩니다
operations = OperationGenerator().parse(openapi_spec_dict)
tool = [RestApiTool.from_parsed_operation(o) for o in operations]
```

#### 생성자

주어진 매개변수로 RestApiTool을 초기화합니다.

OpenAPI 사양에서 RestApiTool을 생성하려면 OperationGenerator를 사용하세요.

**힌트**: auth_scheme과 auth_credential을 구성하려면 google.adk.tools.openapi_tool.auth.auth_helpers를 사용하세요.

**매개변수:**
- **name** – 도구의 이름
- **description** – 도구의 설명
- **endpoint** – 도구의 base_url, path, method를 포함
- **operation** – Pydantic 객체 또는 딕셔너리. OpenAPI Operation 객체를 나타냄 (https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#operation-object)
- **auth_scheme** – 도구의 인증 스키마. OpenAPI SecurityScheme 객체를 나타냄 (https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0.md#security-scheme-object)
- **auth_credential** – 도구의 인증 자격 증명
- **should_parse_operation** – 작업을 파싱할지 여부

#### 필드

- **description**: `str` - 도구의 설명
- **name**: `str` - 도구의 이름

#### 메소드

##### `async call(*, args, tool_context)`

REST API 호출을 실행합니다.

- **반환 타입**: `Dict[str, Any]`
- **매개변수**:
  - **args** – 작업 매개변수를 나타내는 키워드 인자
  - **tool_context** – 도구 컨텍스트 (여기서는 사용되지 않지만 인터페이스에서 필요)
- **반환값**: 딕셔너리로서의 API 응답

##### `configure_auth_credential(auth_credential=None)`

API 호출을 위한 인증 자격 증명을 구성합니다.

**매개변수:**
- **auth_credential** – AuthCredential|dict - 인증 자격 증명. 딕셔너리는 AuthCredential 객체로 변환됩니다.

##### `configure_auth_scheme(auth_scheme)`

API 호출을 위한 인증 스키마를 구성합니다.

**매개변수:**
- **auth_scheme** – AuthScheme|dict - 인증 스키마. 딕셔너리는 AuthScheme 객체로 변환됩니다.

##### `classmethod from_parsed_operation(parsed)`

ParsedOperation 객체에서 RestApiTool을 초기화합니다.

- **반환 타입**: `RestApiTool`
- **매개변수**:
  - **parsed** – ParsedOperation 객체
- **반환값**: RestApiTool 객체

##### `classmethod from_parsed_operation_str(parsed_operation_str)`

딕셔너리에서 RestApiTool을 초기화합니다.

- **반환 타입**: `RestApiTool`
- **매개변수**:
  - **parsed** – ParsedOperation 객체의 딕셔너리 표현
- **반환값**: RestApiTool 객체

##### `async run_async(*, args, tool_context)`

주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Dict[str, Any]`

> **참고**
> - 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다.
> - 그렇지 않으면 생략할 수 있습니다. 예: Gemini용 내장 GoogleSearch 도구의 경우.

**매개변수:**
- **args** – LLM이 채운 인자들
- **tool_context** – 도구의 컨텍스트

**반환값:** 도구 실행 결과