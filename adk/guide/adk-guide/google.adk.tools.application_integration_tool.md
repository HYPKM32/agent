# Google ADK Tools Application Integration API Reference

`google.adk.tools.application_integration_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### ApplicationIntegrationToolset

```python
class google.adk.tools.application_integration_tool.ApplicationIntegrationToolset(
    project, 
    location, 
    integration=None, 
    triggers=None, 
    connection=None, 
    entity_operations=None, 
    actions=None, 
    tool_name_prefix='', 
    tool_instructions='', 
    service_account_json=None, 
    auth_scheme=None, 
    auth_credential=None, 
    tool_filter=None
)
```

**상속**: `BaseToolset`

주어진 Application Integration 또는 Integration Connector 리소스로부터 도구들을 생성합니다.

#### 매개변수

##### 필수 매개변수
- **project**: GCP 프로젝트 ID
- **location**: GCP 위치

##### Integration 관련 매개변수
- **integration**: 통합(integration) 이름
- **triggers**: 통합에서 트리거 이름들의 리스트

##### Connection 관련 매개변수
- **connection**: 연결(connection) 이름
- **entity_operations**: 연결에서 지원하는 엔티티 작업들
- **actions**: 연결에서 지원하는 액션들

##### 기타 매개변수
- **tool_name_prefix**: 생성된 도구들의 이름 접두사
- **tool_instructions**: 도구에 대한 지시사항
- **service_account_json**: 딕셔너리 형태의 서비스 계정 설정
- **auth_scheme**: 인증 스킴
- **auth_credential**: 인증 자격증명
- **tool_filter**: 도구 필터링에 사용되는 필터

#### 생성 조건

다음 조건 중 하나를 만족해야 합니다:
1. `integration`이 제공되어야 함
2. `connection`이 제공되고 `entity_operations` 또는 `actions` 중 하나 이상이 제공되어야 함

#### 예외

- **ValueError**: 위 조건들이 만족되지 않을 때 발생
- **Exception**: 통합 또는 연결 클라이언트 초기화 중 오류 발생 시

#### 사용 예시

##### API 트리거가 있는 통합 사용

```python
# API 트리거가 있는 통합의 모든 사용 가능한 도구 가져오기
application_integration_toolset = ApplicationIntegrationToolset(
    project="test-project",
    location="us-central1",
    integration="test-integration",
    triggers=["api_trigger/test_trigger"],
    service_account_json={...},
)
```

##### 연결을 사용한 엔티티 작업 및 액션

```python
# 엔티티 작업과 액션을 사용하는 연결의 모든 사용 가능한 도구 가져오기
application_integration_toolset = ApplicationIntegrationToolset(
    project="test-project",
    location="us-central1",
    connection="test-connection",
    entity_operations={
        "EntityId1": ["LIST", "CREATE"], 
        "EntityId2": []  # 빈 리스트는 엔티티의 모든 작업이 지원됨을 의미
    },
    actions=["action1"],
    service_account_json={...},
)
```

##### 에이전트에 도구셋 추가

```python
# 에이전트에 도구셋 제공
agent = LlmAgent(tools=[
    # 다른 도구들...
    application_integration_toolset,
])
```

> **참고**: 연결에서 지원하는 엔티티 작업과 액션 목록은 Integration Connector API를 사용하여 찾을 수 있습니다:
> [Connection Schema Metadata API](https://cloud.google.com/integration-connectors/docs/reference/rest/v1/projects.locations.connections.connectionSchemaMetadata)

#### 메소드

##### `async close()`
도구셋이 보유한 리소스를 정리하고 해제합니다.

- **반환 타입**: `None`

이 메소드는 에이전트 서버의 생명주기 끝에서 또는 도구셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 메모리 누수를 방지하기 위해 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되도록 해야 합니다.

##### `async get_tools(readonly_context=None)`
제공된 컨텍스트를 기반으로 도구셋의 모든 도구를 반환합니다.

- **반환 타입**: `List[RestApiTool]`
- **매개변수**:
  - **readonly_context**: 에이전트에서 사용 가능한 도구를 필터링하는데 사용되는 컨텍스트 (선택사항)
- **반환값**: 지정된 컨텍스트에서 사용 가능한 도구들의 리스트

---

### IntegrationConnectorTool

```python
class google.adk.tools.application_integration_tool.IntegrationConnectorTool(
    name, 
    description, 
    connection_name, 
    connection_host, 
    connection_service_name, 
    entity, 
    operation, 
    action, 
    rest_api_tool, 
    auth_scheme=None, 
    auth_credential=None
)
```

**상속**: `BaseTool`

특정 Application Integration 엔드포인트와 상호작용하기 위해 RestApiTool을 래핑하는 도구입니다.

이 도구는 RestApiTool에서 처리하는 기본 REST API 호출에 연결 세부 정보, 엔티티, 작업, 액션과 같은 Application Integration 특정 컨텍스트를 추가합니다. 인자를 준비한 다음 실제 API 호출 실행을 포함된 RestApiTool 인스턴스에 위임합니다.

#### 기능

- 요청 매개변수와 본문 생성
- API 호출에 인증 자격증명 첨부

#### 매개변수

- **name**: 도구의 이름 (API 작업에서 파생, 고유해야 하며 Gemini 함수 명명 규칙 준수)
- **description**: 도구가 수행하는 작업에 대한 설명
- **connection_name**: Integration Connector 연결의 이름
- **connection_host**: 연결의 호스트명 또는 IP 주소
- **connection_service_name**: 호스트 내의 특정 서비스 이름
- **entity**: 대상이 되는 Integration Connector 엔티티
- **operation**: 엔티티에서 수행되는 특정 작업
- **action**: 작업과 관련된 액션 (예: 'execute')
- **rest_api_tool**: OpenAPI 사양 작업을 기반으로 기본 REST API 통신을 처리하는 초기화된 RestApiTool 인스턴스
- **auth_scheme**: 인증 스킴 (선택사항)
- **auth_credential**: 인증 자격증명 (선택사항)

#### 상수

- **EXCLUDE_FIELDS**: `['connection_name', 'service_name', 'host', 'entity', 'operation', 'action', 'dynamic_auth_config']`
- **OPTIONAL_FIELDS**: `['page_size', 'page_token', 'filter', 'sortByColumns']`

#### 도구 생성 예시

```python
# 스펙의 각 API 작업은 자체 도구로 변환됨
# 도구의 이름은 해당 작업의 operationId를 스네이크 케이스로 변환한 것
operations = OperationGenerator().parse(openapi_spec_dict)
tools = [RestApiTool.from_parsed_operation(o) for o in operations]
```

#### 메소드

##### `async run_async(*, args, tool_context)`
주어진 인자와 컨텍스트로 도구를 실행합니다.

- **반환 타입**: `Dict[str, Any]`
- **매개변수**:
  - **args**: LLM이 채운 인자들
  - **tool_context**: 도구의 컨텍스트
- **반환값**: 도구 실행 결과

> **참고**: 이 도구가 클라이언트 측에서 실행되어야 하는 경우 필수입니다. 그렇지 않으면 건너뛸 수 있습니다 (예: Gemini용 내장 GoogleSearch 도구).

---

## 완전한 사용 예시

### Integration을 사용한 워크플로우 자동화

```python
from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset
from google.adk.agents import LlmAgent
import json

# 서비스 계정 설정
service_account_config = {
    "type": "service_account",
    "project_id": "my-integration-project",
    "private_key_id": "key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "integration-service@my-project.iam.gserviceaccount.com",
    "client_id": "123456789"
}

# 워크플로우 통합 도구셋 생성
workflow_toolset = ApplicationIntegrationToolset(
    project="my-integration-project",
    location="us-central1",
    integration="order-processing-workflow",
    triggers=[
        "api_trigger/order_received",
        "api_trigger/payment_confirmed"
    ],
    service_account_json=service_account_config,
    tool_name_prefix="workflow_",
    tool_instructions="주문 처리 워크플로우를 관리합니다."
)

# 에이전트 생성
workflow_agent = LlmAgent(
    name="workflow_manager",
    model="gemini-1.5-pro",
    tools=[workflow_toolset],
    instruction="""
    당신은 주문 처리 워크플로우를 관리하는 에이전트입니다.
    - 새 주문이 접수되면 order_received 트리거를 사용하세요
    - 결제가 확인되면 payment_confirmed 트리거를 사용하세요
    """
)
```

### 데이터베이스 연결을 통한 CRUD 작업

```python
from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset

# 데이터베이스 연결 도구셋 생성
database_toolset = ApplicationIntegrationToolset(
    project="my-data-project",
    location="us-west1",
    connection="postgres-main-db",
    entity_operations={
        "users": ["LIST", "CREATE", "UPDATE", "DELETE"],
        "orders": ["LIST", "CREATE", "UPDATE"],
        "products": ["LIST"]  # 읽기 전용
    },
    service_account_json=service_account_config,
    tool_name_prefix="db_",
    tool_filter=lambda tool, ctx: not tool.name.endswith('_delete')  # 삭제 작업 제외
)

# 데이터 관리 에이전트
data_agent = LlmAgent(
    name="data_manager",
    tools=[database_toolset],
    instruction="""
    데이터베이스 작업을 수행합니다.
    - 사용자 정보 조회/생성/수정
    - 주문 정보 관리
    - 제품 정보 조회 (읽기 전용)
    삭제 작업은 수행하지 않습니다.
    """
)
```

### API 연결을 통한 외부 서비스 통합

```python
from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset

# 외부 API 연결 도구셋
external_api_toolset = ApplicationIntegrationToolset(
    project="my-integration-project",
    location="europe-west1",
    connection="salesforce-connector",
    entity_operations={
        "Account": ["LIST", "CREATE", "UPDATE"],
        "Contact": ["LIST", "CREATE", "UPDATE"],
        "Opportunity": ["LIST", "CREATE", "UPDATE"]
    },
    actions=[
        "sync_data",
        "validate_record",
        "send_notification"
    ],
    service_account_json=service_account_config,
    tool_name_prefix="sf_"
)

# CRM 통합 에이전트
crm_agent = LlmAgent(
    name="crm_integrator",
    tools=[external_api_toolset],
    instruction="""
    Salesforce CRM과의 통합을 관리합니다.
    - 계정, 연락처, 기회 데이터 동기화
    - 데이터 검증 및 알림 전송
    - 양방향 데이터 흐름 유지
    """
)
```

### 조건부 도구 필터링

```python
from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset

def create_filtered_toolset(user_role="viewer"):
    """사용자 역할에 따른 도구 필터링"""
    
    if user_role == "admin":
        # 관리자는 모든 도구 사용 가능
        tool_filter = None
    elif user_role == "editor":
        # 편집자는 읽기/쓰기 가능, 삭제 불가
        tool_filter = lambda tool, ctx: "delete" not in tool.name.lower()
    else:  # viewer
        # 뷰어는 읽기 전용
        tool_filter = lambda tool, ctx: any(
            op in tool.name.lower() for op in ["list", "get", "read", "view"]
        )
    
    return ApplicationIntegrationToolset(
        project="security-demo-project",
        location="us-central1",
        connection="secure-database",
        entity_operations={
            "sensitive_data": ["LIST", "CREATE", "UPDATE", "DELETE"]
        },
        service_account_json=service_account_config,
        tool_filter=tool_filter
    )

# 역할별 도구셋 생성
admin_toolset = create_filtered_toolset("admin")
editor_toolset = create_filtered_toolset("editor") 
viewer_toolset = create_filtered_toolset("viewer")
```

### 배치 처리 및 페이지네이션

```python
from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset

# 대용량 데이터 처리를 위한 도구셋
batch_processing_toolset = ApplicationIntegrationToolset(
    project="big-data-project",
    location="us-central1",
    connection="data-warehouse",
    entity_operations={
        "large_dataset": ["LIST"],  # 페이지네이션 지원
        "batch_jobs": ["CREATE", "LIST"]
    },
    actions=["process_batch", "export_data"],
    service_account_json=service_account_config,
    tool_instructions="""
    대용량 데이터 처리 시 다음 매개변수를 사용하세요:
    - page_size: 한 번에 가져올 레코드 수 (기본값: 100)
    - page_token: 다음 페이지를 위한 토큰
    - filter: 데이터 필터링 조건
    - sortByColumns: 정렬 기준 컬럼
    """
)

# 대용량 데이터 처리 에이전트
batch_agent = LlmAgent(
    name="batch_processor",
    tools=[batch_processing_toolset],
    instruction="""
    대용량 데이터를 효율적으로 처리합니다.
    - 적절한 페이지 크기 설정
    - 필터를 사용하여 필요한 데이터만 조회
    - 배치 작업으로 대량 처리 수행
    """
)
```

### 리소스 관리 및 정리

```python
import asyncio
from google.adk.tools.application_integration_tool import ApplicationIntegrationToolset

class IntegrationManager:
    def __init__(self):
        self.toolsets = []
    
    def create_toolset(self, **kwargs):
        """도구셋 생성 및 추적"""
        toolset = ApplicationIntegrationToolset(**kwargs)
        self.toolsets.append(toolset)
        return toolset
    
    async def cleanup_all(self):
        """모든 도구셋 정리"""
        tasks = [toolset.close() for toolset in self.toolsets]
        await asyncio.gather(*tasks, return_exceptions=True)
        self.toolsets.clear()
        print(f"정리된 도구셋 수: {len(tasks)}")
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup_all()

# 사용 예시
async def integration_workflow():
    async with IntegrationManager() as manager:
        # 여러 통합 도구셋 생성
        crm_toolset = manager.create_toolset(
            project="project1",
            location="us-central1",
            connection="crm-connector",
            entity_operations={"contacts": ["LIST", "CREATE"]},
            service_account_json=service_account_config
        )
        
        erp_toolset = manager.create_toolset(
            project="project1", 
            location="us-central1",
            integration="erp-integration",
            triggers=["data_sync"],
            service_account_json=service_account_config
        )
        
        # 도구셋 사용...
        crm_tools = await crm_toolset.get_tools()
        erp_tools = await erp_toolset.get_tools()
        
        print(f"CRM 도구 수: {len(crm_tools)}")
        print(f"ERP 도구 수: {len(erp_tools)}")
        
        # 컨텍스트 매니저가 자동으로 정리

# asyncio.run(integration_workflow())
```

---

## 주요 특징

### 이중 통합 지원
- **Application Integration**: 워크플로우 기반 통합, API 트리거 지원
- **Integration Connector**: 외부 시스템과의 직접 연결, 엔티티 작업 및 액션 지원

### 자동 도구 생성
- OpenAPI 스펙 기반 REST API 도구 자동 생성
- 각 API 엔드포인트가 개별 도구로 변환
- 매개변수, 응답 스키마 자동 매핑

### 컨텍스트 인식
- Application Integration 특정 컨텍스트 자동 주입
- 연결 정보, 엔티티, 작업, 액션 정보 포함
- 동적 인증 설정 지원

### 유연한 필터링
- 역할 기반 접근 제어
- 작업 유형별 필터링 (읽기 전용, 쓰기 전용 등)
- 보안 정책 기반 도구 노출 제어

### 페이지네이션 지원
- 대용량 데이터 처리를 위한 페이지네이션
- 필터링 및 정렬 기능
- 배치 처리 최적화

### 리소스 관리
- 자동 리소스 정리 및 해제
- 연결 풀링 및 재사용
- 메모리 누수 방지