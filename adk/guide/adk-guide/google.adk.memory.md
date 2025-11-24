# Google ADK Memory API Reference

`google.adk.memory` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseMemoryService

```python
class google.adk.memory.BaseMemoryService
```

**상속**: `ABC`

메모리 서비스를 위한 기본 클래스입니다.

이 서비스는 세션을 메모리에 수집하여 사용자 쿼리에 메모리를 사용할 수 있는 기능을 제공합니다.

#### 추상 메소드

##### `async add_session_to_memory(session)`
세션을 메모리 서비스에 추가합니다.

세션은 수명 동안 여러 번 추가될 수 있습니다.

- **매개변수**:
  - **session**: 추가할 세션

##### `async search_memory(*, app_name, user_id, query)`
쿼리와 일치하는 세션을 검색합니다.

- **반환 타입**: `SearchMemoryResponse`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **query**: 검색할 쿼리
- **반환값**: 일치하는 메모리가 포함된 SearchMemoryResponse

---

### InMemoryMemoryService

```python
class google.adk.memory.InMemoryMemoryService
```

**상속**: `BaseMemoryService`

프로토타이핑 목적으로만 사용되는 인메모리 메모리 서비스입니다.

의미론적 검색 대신 키워드 매칭을 사용합니다.

> ⚠️ **주의**: 이 클래스는 스레드 안전하지만, 테스트 및 개발 목적으로만 사용해야 합니다.

#### 메소드

##### `async add_session_to_memory(session)`
세션을 메모리 서비스에 추가합니다.

세션은 수명 동안 여러 번 추가될 수 있습니다.

- **매개변수**:
  - **session**: 추가할 세션

##### `async search_memory(*, app_name, user_id, query)`
쿼리와 일치하는 세션을 검색합니다.

- **반환 타입**: `SearchMemoryResponse`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **query**: 검색할 쿼리
- **반환값**: 일치하는 메모리가 포함된 SearchMemoryResponse

---

### VertexAiMemoryBankService

```python
class google.adk.memory.VertexAiMemoryBankService(project=None, location=None, agent_engine_id=None)
```

**상속**: `BaseMemoryService`

Vertex AI Memory Bank를 사용한 BaseMemoryService의 구현체입니다.

#### 생성자

VertexAiMemoryBankService를 초기화합니다.

- **매개변수**:
  - **project**: 사용할 Memory Bank의 프로젝트 ID
  - **location**: 사용할 Memory Bank의 위치
  - **agent_engine_id**: Memory Bank에 사용할 에이전트 엔진의 ID

#### 에이전트 엔진 ID 예시

```
'projects/my-project/locations/us-central1/reasoningEngines/456'에서 '456' 부분
```

#### 메소드

##### `async add_session_to_memory(session)`
세션을 메모리 서비스에 추가합니다.

세션은 수명 동안 여러 번 추가될 수 있습니다.

- **매개변수**:
  - **session**: 추가할 세션

##### `async search_memory(*, app_name, user_id, query)`
쿼리와 일치하는 세션을 검색합니다.

- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **query**: 검색할 쿼리
- **반환값**: 일치하는 메모리가 포함된 SearchMemoryResponse

---

### VertexAiRagMemoryService

```python
class google.adk.memory.VertexAiRagMemoryService(rag_corpus=None, similarity_top_k=None, vector_distance_threshold=10)
```

**상속**: `BaseMemoryService`

저장 및 검색을 위해 Vertex AI RAG를 사용하는 메모리 서비스입니다.

#### 생성자

VertexAiRagMemoryService를 초기화합니다.

- **매개변수**:
  - **rag_corpus**: 사용할 Vertex AI RAG 코퍼스의 이름
  - **similarity_top_k**: 검색할 컨텍스트의 수
  - **vector_distance_threshold**: 벡터 거리 임계값 (기본값: 10)

#### RAG 코퍼스 형식

```
projects/{project}/locations/{location}/ragCorpora/{rag_corpus_id}
또는
{rag_corpus_id}
```

#### 메소드

##### `async add_session_to_memory(session)`
세션을 메모리 서비스에 추가합니다.

세션은 수명 동안 여러 번 추가될 수 있습니다.

- **매개변수**:
  - **session**: 추가할 세션

##### `async search_memory(*, app_name, user_id, query)`
rag.retrieval_query를 사용하여 쿼리와 일치하는 세션을 검색합니다.

- **반환 타입**: `SearchMemoryResponse`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **query**: 검색할 쿼리
- **반환값**: 일치하는 메모리가 포함된 SearchMemoryResponse

---

## 사용 예시

### InMemoryMemoryService 사용

```python
from google.adk.memory import InMemoryMemoryService

# 개발/테스트용 메모리 서비스 생성
memory_service = InMemoryMemoryService()

# 세션을 메모리에 추가
await memory_service.add_session_to_memory(my_session)

# 메모리 검색
results = await memory_service.search_memory(
    app_name="my_app",
    user_id="user123",
    query="Python 프로그래밍 질문"
)
```

### VertexAiMemoryBankService 사용

```python
from google.adk.memory import VertexAiMemoryBankService

# Vertex AI Memory Bank 서비스 생성
memory_service = VertexAiMemoryBankService(
    project="my-project",
    location="us-central1",
    agent_engine_id="456"
)

# 세션을 Memory Bank에 추가
await memory_service.add_session_to_memory(conversation_session)

# Memory Bank에서 검색
search_results = await memory_service.search_memory(
    app_name="chatbot_app",
    user_id="user456",
    query="이전에 논의한 API 사용법"
)
```

### VertexAiRagMemoryService 사용

```python
from google.adk.memory import VertexAiRagMemoryService

# RAG 기반 메모리 서비스 생성
rag_memory_service = VertexAiRagMemoryService(
    rag_corpus="projects/my-project/locations/us-central1/ragCorpora/my-corpus",
    similarity_top_k=5,
    vector_distance_threshold=0.8
)

# 세션을 RAG 코퍼스에 추가
await rag_memory_service.add_session_to_memory(user_session)

# 의미론적 검색 수행
semantic_results = await rag_memory_service.search_memory(
    app_name="knowledge_bot",
    user_id="expert_user",
    query="머신러닝 모델 최적화 방법"
)
```

### 메모리 서비스 통합 사용

```python
# 에이전트에서 메모리 서비스 사용
class SmartAgent:
    def __init__(self, memory_service):
        self.memory_service = memory_service
    
    async def process_query(self, app_name, user_id, query):
        # 관련 메모리 검색
        memory_results = await self.memory_service.search_memory(
            app_name=app_name,
            user_id=user_id,
            query=query
        )
        
        # 메모리 결과를 컨텍스트로 활용
        context = self._extract_context(memory_results)
        
        # 컨텍스트를 기반으로 응답 생성
        response = self._generate_response(query, context)
        
        return response
    
    async def save_conversation(self, session):
        # 대화를 메모리에 저장
        await self.memory_service.add_session_to_memory(session)

# 사용법
memory_service = VertexAiMemoryBankService(
    project="my-project",
    location="us-central1",
    agent_engine_id="123"
)

agent = SmartAgent(memory_service)
```

---

## 주요 특징

### 추상화된 메모리 인터페이스
- `BaseMemoryService`를 통해 다양한 메모리 백엔드를 동일한 인터페이스로 사용
- 개발 환경과 프로덕션 환경 간 쉬운 전환

### 다양한 구현체
- **InMemoryMemoryService**: 개발/테스트용 간단한 구현
- **VertexAiMemoryBankService**: Google Cloud의 관리형 메모리 서비스
- **VertexAiRagMemoryService**: RAG 기반 의미론적 검색

### 세션 중심 메모리 관리
- 전체 세션을 메모리 단위로 관리
- 세션의 수명 동안 지속적인 업데이트 지원

### 사용자별 격리
- 앱과 사용자 ID를 통한 메모리 격리
- 개인정보 보호 및 멀티테넌트 지원

### 검색 최적화
- 벡터 거리 기반 유사도 검색
- 상위 K개 결과 제한으로 성능 최적화