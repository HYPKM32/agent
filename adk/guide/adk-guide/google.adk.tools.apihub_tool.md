# Google ADK Tools APIHub Tool API Reference

`google.adk.tools.apihub_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### APIHubToolset

```python
class google.adk.tools.apihub_tool.APIHubToolset(
    *, 
    apihub_resource_name, 
    access_token=None, 
    service_account_json=None, 
    name='', 
    description='', 
    lazy_load_spec=False, 
    auth_scheme=None, 
    auth_credential=None, 
    apihub_client=None, 
    tool_filter=None
)
```

**상속**: `BaseToolset`

주어진 API Hub 리소스로부터 도구들을 생성하는 APIHubTool입니다.

#### 매개변수

- **apihub_resource_name**: API Hub의 API 리소스 이름 (API 이름 필수, API 버전 및 스펙 이름 선택사항)
- **access_token**: Google Access Token (`gcloud auth print-access-token`으로 생성)
- **service_account_json**: JSON 문자열 형태의 서비스 계정 설정
- **apihub_client**: 선택적 커스텀 API Hub 클라이언트
- **name**: 도구셋의 이름 (선택사항)
- **description**: 도구셋의 설명 (선택사항)
- **auth_scheme**: 도구셋의 모든 도구에 적용되는 인증 스킴
- **auth_credential**: 도구셋의 모든 도구에 적용되는 인증 자격증명
- **lazy_load_spec**: True일 경우 필요할 때 스펙을 지연 로딩
- **tool_filter**: 도구를 필터링하는데 사용되는 필터 (도구 술어 또는 도구 이름 리스트)

#### 리소스 이름 형식

- **형식**: `projects/xxx/locations/us-central1/apis/apiname/...`
- **콘솔 URL**: `https://console.cloud.google.com/apigee/api-hub/apis/apiname?project=xxx`

#### 스펙 로딩 규칙

- **스펙 리소스 이름 포함**: `apihub_resource_name`에 스펙 리소스 이름이 포함된 경우, 해당 스펙의 내용을 사용하여 도구 생성
- **API 또는 버전 이름만**: API 또는 버전 이름만 포함된 경우, 해당 API의 첫 번째 버전의 첫 번째 스펙을 사용

#### 인증 설정

- **access_token**: API Hub에서 API 스펙을 가져오는데 사용
- **service_account_json**: 기본 서비스 자격증명을 사용하지 않는 경우 필수
- **apihub_client**: 커스텀 API Hub 클라이언트 사용 가능

#### 도구 필터링

`tool_filter` 매개변수는 다음 중 하나가 될 수 있습니다:
- **함수**: `lambda tool, ctx=None: tool.name in ('tool1', 'tool2')`
- **리스트**: `['tool1', 'tool2']`

#### 생성자

APIHubTool을 주어진 매개변수로 초기화합니다.

#### 사용 예시

##### 기본 사용법

```python
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/test-project/locations/us-central1/apis/test-api",
    service_account_json="...",
    tool_filter=lambda tool, ctx=None: tool.name in ('my_tool', 'my_other_tool')
)

# 모든 사용 가능한 도구 가져오기
agent = LlmAgent(tools=apihub_toolset)
```

##### 전체 도구셋 사용

```python
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/test-project/locations/us-central1/apis/test-api",
    service_account_json="...",
)

# 모든 사용 가능한 도구 가져오기
agent = LlmAgent(tools=[apihub_toolset])
```

##### 특정 도구만 사용

```python
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/test-project/locations/us-central1/apis/test-api",
    service_account_json="...",
    tool_filter=['my_tool']
)

# 특정 도구 가져오기
agent = LlmAgent(tools=[
    # 다른 도구들...
    apihub_toolset,
])
```

#### 메소드

##### `async close()`
도구셋이 보유한 리소스를 정리하고 해제합니다.

이 메소드는 에이전트 서버의 생명주기 끝에서 또는 도구셋이 더 이상 필요하지 않을 때 호출됩니다. 구현체는 메모리 누수를 방지하기 위해 열린 연결, 파일 또는 기타 관리되는 리소스가 적절히 해제되도록 해야 합니다.

##### `async get_tools(readonly_context=None)`
사용 가능한 모든 도구를 검색합니다.

- **반환 타입**: `List[RestApiTool]`
- **매개변수**:
  - **readonly_context**: 읽기 전용 컨텍스트 (선택사항)
- **반환값**: 사용 가능한 모든 RestApiTool 객체의 리스트

---

## 완전한 사용 예시

### 기본 APIHub 통합

```python
from google.adk.tools.apihub_tool import APIHubToolset
from google.adk.agents import LlmAgent
import json

# 서비스 계정 설정
service_account_config = {
    "type": "service_account",
    "project_id": "my-project",
    "private_key_id": "key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "service-account@my-project.iam.gserviceaccount.com",
    "client_id": "123456789",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token"
}

# APIHub 도구셋 생성
apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/my-api",
    service_account_json=json.dumps(service_account_config),
    name="MyAPI Tools",
    description="My API의 도구들"
)

# 에이전트에 도구셋 추가
agent = LlmAgent(
    name="api_agent",
    model="gemini-1.5-flash",
    tools=[apihub_toolset],
    instruction="당신은 API를 사용하여 작업을 수행하는 에이전트입니다."
)

# 사용 후 리소스 정리
await apihub_toolset.close()
```

### Access Token 사용

```python
import subprocess
from google.adk.tools.apihub_tool import APIHubToolset

# gcloud에서 액세스 토큰 생성
def get_access_token():
    result = subprocess.run(
        ["gcloud", "auth", "print-access-token"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

# Access Token으로 APIHub 도구셋 생성
access_token = get_access_token()

apihub_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/analytics-api",
    access_token=access_token,
    lazy_load_spec=True  # 필요할 때 로딩
)
```

### 도구 필터링 전략

```python
from google.adk.tools.apihub_tool import APIHubToolset

# 함수 기반 필터링
def api_tool_filter(tool, ctx=None):
    """읽기 전용 작업만 허용하는 필터"""
    readonly_operations = ['get', 'list', 'search', 'read']
    return any(op in tool.name.lower() for op in readonly_operations)

# 보안이 중요한 환경에서 사용
secure_toolset = APIHubToolset(
    apihub_resource_name="projects/secure-project/locations/us-central1/apis/data-api",
    service_account_json=service_account_json,
    tool_filter=api_tool_filter
)

# 리스트 기반 필터링 (명시적 허용 목록)
allowed_tools = [
    'get_user_profile',
    'list_products', 
    'search_orders',
    'get_analytics_data'
]

restricted_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/business-api",
    service_account_json=service_account_json,
    tool_filter=allowed_tools
)
```

### 인증 스킴 설정

```python
from google.adk.tools.apihub_tool import APIHubToolset
from google.adk.auth import AuthScheme, AuthCredential

# API Key 인증 설정
api_key_auth = AuthScheme(
    type="api_key",
    location="header",
    name="X-API-Key"
)

api_key_credential = AuthCredential(
    value="your-api-key-here"
)

# 인증이 설정된 도구셋 생성
authenticated_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/external-api",
    service_account_json=service_account_json,
    auth_scheme=api_key_auth,
    auth_credential=api_key_credential
)
```

### 다중 API 통합

```python
from google.adk.tools.apihub_tool import APIHubToolset
from google.adk.agents import LlmAgent

# 여러 API에서 도구셋 생성
user_api_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/user-api",
    service_account_json=service_account_json,
    tool_filter=['get_user', 'update_user', 'list_users']
)

product_api_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/product-api", 
    service_account_json=service_account_json,
    tool_filter=['get_product', 'search_products', 'get_inventory']
)

order_api_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/order-api",
    service_account_json=service_account_json,
    tool_filter=['create_order', 'get_order_status', 'cancel_order']
)

# 통합 에이전트 생성
integrated_agent = LlmAgent(
    name="business_agent",
    model="gemini-1.5-pro",
    tools=[user_api_toolset, product_api_toolset, order_api_toolset],
    instruction="""
    당신은 비즈니스 프로세스를 관리하는 에이전트입니다.
    - 사용자 관리: user-api 도구 사용
    - 제품 관리: product-api 도구 사용  
    - 주문 관리: order-api 도구 사용
    """
)
```

### 지연 로딩과 성능 최적화

```python
from google.adk.tools.apihub_tool import APIHubToolset

# 대용량 API 스펙의 경우 지연 로딩 사용
large_api_toolset = APIHubToolset(
    apihub_resource_name="projects/my-project/locations/us-central1/apis/large-api",
    service_account_json=service_account_json,
    lazy_load_spec=True,  # 필요할 때만 로딩
    tool_filter=lambda tool, ctx: 'high_priority' in tool.description.lower()
)

# 도구 미리 로딩 (선택사항)
async def preload_tools():
    tools = await large_api_toolset.get_tools()
    print(f"사전 로딩된 도구 수: {len(tools)}")
    return tools

# preloaded_tools = await preload_tools()
```

### 에러 처리와 리소스 관리

```python
from google.adk.tools.apihub_tool import APIHubToolset
import asyncio

class APIHubManager:
    def __init__(self):
        self.toolsets = []
    
    async def create_toolset(self, resource_name, **kwargs):
        """안전한 도구셋 생성"""
        try:
            toolset = APIHubToolset(
                apihub_resource_name=resource_name,
                **kwargs
            )
            self.toolsets.append(toolset)
            return toolset
        except Exception as e:
            print(f"도구셋 생성 실패: {e}")
            return None
    
    async def cleanup_all(self):
        """모든 도구셋 정리"""
        cleanup_tasks = [toolset.close() for toolset in self.toolsets]
        await asyncio.gather(*cleanup_tasks, return_exceptions=True)
        self.toolsets.clear()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.cleanup_all()

# 사용 예시
async def main():
    async with APIHubManager() as manager:
        toolset1 = await manager.create_toolset(
            "projects/proj1/locations/us-central1/apis/api1",
            service_account_json=service_account_json
        )
        
        toolset2 = await manager.create_toolset(
            "projects/proj1/locations/us-central1/apis/api2",
            service_account_json=service_account_json
        )
        
        # 도구셋 사용...
        
        # 컨텍스트 매니저가 자동으로 정리

# asyncio.run(main())
```

---

## 주요 특징

### 자동 도구 생성
- API Hub의 OpenAPI 스펙으로부터 자동으로 REST API 도구 생성
- 스펙의 각 엔드포인트가 개별 도구로 변환
- 매개변수, 응답 스키마 자동 매핑

### 유연한 인증
- Google Cloud 서비스 계정 지원
- Access Token 기반 인증
- 커스텀 인증 스킴 설정 가능
- 도구별 개별 인증 설정

### 지능형 필터링
- 함수 기반 동적 필터링
- 명시적 도구 이름 리스트
- 보안 정책 기반 접근 제어
- 컨텍스트 기반 조건부 필터링

### 성능 최적화
- 지연 로딩으로 초기화 시간 단축
- 필요한 도구만 선택적 로딩
- 리소스 자동 관리 및 정리

### 통합성
- BaseToolset 인터페이스 준수
- LLM 에이전트와 완전 통합
- 다른 도구들과 원활한 조합 가능