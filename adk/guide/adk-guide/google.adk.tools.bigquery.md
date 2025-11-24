# Google ADK Tools BigQuery API Reference

`google.adk.tools.bigquery` 모듈의 API 레퍼런스 문서입니다.

BigQuery Tools (실험적 기능).

이 모듈 아래의 BigQuery 도구들은 수작업으로 제작되고 맞춤화되었으며, `google.adk.tools.google_api_tool` 아래의 도구들은 API 정의를 기반으로 자동 생성됩니다. 맞춤 도구를 제공하는 이유는 다음과 같습니다:

- BigQuery API들은 기능이 중복되어 LLM이 어떤 도구를 사용할지 구분할 수 없습니다
- BigQuery API들은 많은 매개변수를 가지고 있으며 일부는 거의 사용되지 않아 LLM 친화적이지 않습니다
- 예측, RAG, 세분화 등과 같은 더 높은 수준의 도구를 제공하고 싶습니다
- 이러한 도구에서 추가적인 접근 가드레일을 제공하고 싶습니다. 예를 들어, execute_sql은 기존 데이터를 임의로 변경할 수 없습니다

## 모델

### BigQueryCredentialsConfig

```python
pydantic model google.adk.tools.bigquery.BigQueryCredentialsConfig
```

**상속**: `BaseModel`

Google API 도구 구성 (실험적 기능).

나중에 폐지될 수 있으므로 프로덕션에서 사용하지 마세요.

#### 필드

- **client_id**: `str | None`
- **client_secret**: `str | None`  
- **credentials**: `google.auth.credentials.Credentials | None`
- **scopes**: `List[str] | None`

#### 검증자

- **__post_init__** » 모든 필드

##### `field client_id: Optional[str] = None`
사용할 OAuth 클라이언트 ID입니다.

**검증자**: __post_init__

##### `field client_secret: Optional[str] = None`
사용할 OAuth 클라이언트 시크릿입니다.

**검증자**: __post_init__

##### `field credentials: Optional[google.auth.credentials.Credentials] = None`
사용할 기존 인증 자격 증명입니다. 설정된 경우, 이 자격 증명이 모든 최종 사용자에게 사용되며, 최종 사용자는 OAuth 플로우에 참여할 필요가 없습니다. 이 필드는 client_id, client_secret 및 scopes와 상호 배타적입니다. 이 자격 증명이 모든 최종 사용자의 데이터에 액세스할 권한이 있다고 확신하지 않는 한 이 필드를 설정하지 마세요.

**사용 예시 1**: 에이전트가 Google Cloud 환경에 배포되고 서비스 계정(애플리케이션 기본 자격 증명으로 사용됨)이 필요한 모든 BigQuery 리소스에 액세스할 수 있는 경우. 최종 사용자가 OAuth 플로우를 거치지 않고도 BigQuery 리소스에 액세스할 수 있도록 이 자격 증명을 설정합니다.

애플리케이션 기본 자격 증명을 얻으려면: `google.auth.default(...)` 사용. 자세한 내용은 https://cloud.google.com/docs/authentication/application-default-credentials 참조.

**사용 예시 2**: 에이전트가 서비스 계정 키 자격 증명을 사용하여 사용자의 BigQuery 리소스에 액세스하려는 경우.

서비스 계정 키 자격 증명을 로드하려면: `google.auth.load_credentials_from_file(...)` 사용. 자세한 내용은 https://cloud.google.com/iam/docs/service-account-creds#user-managed-keys 참조.

배포된 환경에서 기존 자격 증명을 제공할 수 없는 경우, 최종 사용자가 OAuth 플로우를 거쳐 에이전트가 사용자 데이터에 액세스할 수 있도록 아래의 client_id, client_secret 및 scope 설정을 고려하세요.

**검증자**: __post_init__

##### `field scopes: Optional[List[str]] = None`
사용할 스코프입니다.

**검증자**: __post_init__

## 클래스

### BigQueryTool

```python
class google.adk.tools.bigquery.BigQueryTool(func, *, credentials_config=None, bigquery_tool_config=None)
```

**상속**: `FunctionTool`

Google API를 호출하는 도구를 위한 GoogleApiTool 클래스입니다.

이 클래스는 개발자가 API 사양을 기반으로 Google API 도구를 자동 생성하는 대신 맞춤형 Google API 도구를 수작업으로 제작할 수 있도록 합니다.

이 클래스는 모든 OAuth 복잡성, 자격 증명 관리 및 일반적인 Google API 패턴을 처리하므로 서브클래스는 특정 기능에 집중할 수 있습니다.

#### 생성자

Google API 도구를 초기화합니다.

**매개변수:**
- **func** – 도구의 로직을 구현하는 호출 가능 객체, 하나의 'credential' 매개변수를 받을 수 있습니다
- **credentials_config** – Google API 호출에 사용되는 자격 증명 구성. None인 경우 인증 로직을 처리하지 않습니다

#### 메소드

##### `async run_async(*, args, tool_context)`

자격 증명 처리를 포함한 도구 실행의 주요 진입점입니다.

이 메소드는 모든 OAuth 복잡성을 처리한 다음 서브클래스의 run_async_with_credential 메소드에 위임합니다.

- **반환 타입**: `Any`

---

### BigQueryToolset

```python
class google.adk.tools.bigquery.BigQueryToolset(*, tool_filter=None, credentials_config=None, bigquery_tool_config=None)
```

**상속**: `BaseToolset`

BigQuery Toolset은 BigQuery 데이터 및 메타데이터와 상호 작용하기 위한 도구들을 포함합니다.

#### 메소드

##### `async close()`

툴셋이 보유한 리소스를 정리하고 해제합니다.

> **참고**
> 이 메소드는 예를 들어 에이전트 서버의 생명주기 끝이나 툴셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 모든 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되어 누수를 방지하도록 해야 합니다.

##### `async get_tools(readonly_context=None)`

툴셋에서 도구를 가져옵니다.

- **반환 타입**: `List[BaseTool]`