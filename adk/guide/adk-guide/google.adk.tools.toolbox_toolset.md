# Google ADK Tools Toolbox Toolset API Reference

`google.adk.tools.toolbox_toolset` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### ToolboxToolset

```python
class google.adk.tools.toolbox_toolset.ToolboxToolset(server_url, toolset_name=None, tool_names=None, auth_token_getters=None, bound_params=None)
```

**상속**: `BaseToolset`

툴박스 툴셋에 대한 액세스를 제공하는 클래스입니다.

#### 예시

```python
toolbox_toolset = ToolboxToolset("http://127.0.0.1:5000", toolset_name="my-toolset")
```

#### 생성자

**매개변수:**
- **server_url** – 툴박스 서버의 URL
- **toolset_name** – 로드할 툴박스 툴셋의 이름
- **tool_names** – 로드할 도구의 이름들
- **auth_token_getters** – 인증 서비스 이름을 해당 인증 토큰을 반환하는 호출 가능 객체에 매핑하는 매핑. 자세한 내용은 https://github.com/googleapis/mcp-toolbox-sdk-python/tree/main/packages/toolbox-core#authenticating-tools 참조
- **bound_params** – 매개변수 이름을 특정 값 또는 필요에 따라 값을 생성하기 위해 호출되는 호출 가능 객체에 바인딩하는 매핑. 자세한 내용은 https://github.com/googleapis/mcp-toolbox-sdk-python/tree/main/packages/toolbox-core#binding-parameter-values 참조

결과 ToolboxToolset은 tool_names와 toolset_name으로 로드된 도구를 모두 포함합니다.

#### 메소드

##### `async close()`

툴셋이 보유한 리소스를 정리하고 해제합니다.

> **참고**
> 이 메소드는 예를 들어 에이전트 서버의 생명주기 끝이나 툴셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 모든 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되어 누수를 방지하도록 해야 합니다.

##### `async get_tools(readonly_context=None)`

제공된 컨텍스트를 기반으로 툴셋의 모든 도구를 반환합니다.

- **반환 타입**: `list[BaseTool]`
- **매개변수**:
  - **readonly_context** (ReadonlyContext, optional) – 에이전트가 사용할 수 있는 도구를 필터링하는 데 사용되는 컨텍스트. None인 경우 툴셋의 모든 도구가 반환됩니다.
- **반환값**: 지정된 컨텍스트에서 사용 가능한 도구 목록