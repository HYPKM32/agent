# Google ADK Artifacts API Reference

`google.adk.artifacts` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseArtifactService

```python
class google.adk.artifacts.BaseArtifactService
```

**상속**: `ABC`

아티팩트 서비스를 위한 추상 기본 클래스입니다.

#### 추상 메소드

##### `async delete_artifact(*, app_name, user_id, session_id, filename)`
아티팩트를 삭제합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **filename**: 아티팩트 파일의 이름

##### `async list_artifact_keys(*, app_name, user_id, session_id)`
세션 내의 모든 아티팩트 파일명을 나열합니다.

- **반환 타입**: `list[str]`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
- **반환값**: 세션 내 모든 아티팩트 파일명의 리스트

##### `async list_versions(*, app_name, user_id, session_id, filename)`
아티팩트의 모든 버전을 나열합니다.

- **반환 타입**: `list[int]`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **filename**: 아티팩트 파일의 이름
- **반환값**: 아티팩트의 사용 가능한 모든 버전 리스트

##### `async load_artifact(*, app_name, user_id, session_id, filename, version=None)`
아티팩트 서비스 스토리지에서 아티팩트를 가져옵니다.

아티팩트는 앱 이름, 사용자 ID, 세션 ID, 파일명으로 식별되는 파일입니다.

- **반환 타입**: `Optional[Part]`
- **매개변수**:
  - **app_name**: 앱 이름
  - **user_id**: 사용자 ID
  - **session_id**: 세션 ID
  - **filename**: 아티팩트의 파일명
  - **version**: 아티팩트의 버전 (None일 경우 최신 버전 반환)
- **반환값**: 아티팩트 또는 찾을 수 없으면 None

##### `async save_artifact(*, app_name, user_id, session_id, filename, artifact)`
아티팩트를 아티팩트 서비스 스토리지에 저장합니다.

아티팩트는 앱 이름, 사용자 ID, 세션 ID, 파일명으로 식별되는 파일입니다. 아티팩트 저장 후 아티팩트 버전을 식별하는 개정 ID가 반환됩니다.

- **반환 타입**: `int`
- **매개변수**:
  - **app_name**: 앱 이름
  - **user_id**: 사용자 ID
  - **session_id**: 세션 ID
  - **filename**: 아티팩트의 파일명
  - **artifact**: 저장할 아티팩트
- **반환값**: 개정 ID (첫 번째 버전은 0, 성공적인 저장마다 1씩 증가)

---

### GcsArtifactService

```python
class google.adk.artifacts.GcsArtifactService(bucket_name, **kwargs)
```

**상속**: `BaseArtifactService`

Google Cloud Storage(GCS)를 사용하는 아티팩트 서비스 구현체입니다.

#### 생성자

GcsArtifactService를 초기화합니다.

- **매개변수**:
  - **bucket_name**: 사용할 버킷의 이름
  - **\*\*kwargs**: Google Cloud Storage 클라이언트에 전달할 키워드 인자

#### 메소드

##### `async delete_artifact(*, app_name, user_id, session_id, filename)`
아티팩트를 삭제합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **filename**: 아티팩트 파일의 이름

##### `async list_artifact_keys(*, app_name, user_id, session_id)`
세션 내의 모든 아티팩트 파일명을 나열합니다.

- **반환 타입**: `list[str]`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
- **반환값**: 세션 내 모든 아티팩트 파일명의 리스트

##### `async list_versions(*, app_name, user_id, session_id, filename)`
아티팩트의 모든 버전을 나열합니다.

- **반환 타입**: `list[int]`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **filename**: 아티팩트 파일의 이름
- **반환값**: 아티팩트의 사용 가능한 모든 버전 리스트

##### `async load_artifact(*, app_name, user_id, session_id, filename, version=None)`
아티팩트 서비스 스토리지에서 아티팩트를 가져옵니다.

아티팩트는 앱 이름, 사용자 ID, 세션 ID, 파일명으로 식별되는 파일입니다.

- **반환 타입**: `Optional[Part]`
- **매개변수**:
  - **app_name**: 앱 이름
  - **user_id**: 사용자 ID
  - **session_id**: 세션 ID
  - **filename**: 아티팩트의 파일명
  - **version**: 아티팩트의 버전 (None일 경우 최신 버전 반환)
- **반환값**: 아티팩트 또는 찾을 수 없으면 None

##### `async save_artifact(*, app_name, user_id, session_id, filename, artifact)`
아티팩트를 아티팩트 서비스 스토리지에 저장합니다.

아티팩트는 앱 이름, 사용자 ID, 세션 ID, 파일명으로 식별되는 파일입니다. 아티팩트 저장 후 아티팩트 버전을 식별하는 개정 ID가 반환됩니다.

- **반환 타입**: `int`
- **매개변수**:
  - **app_name**: 앱 이름
  - **user_id**: 사용자 ID
  - **session_id**: 세션 ID
  - **filename**: 아티팩트의 파일명
  - **artifact**: 저장할 아티팩트
- **반환값**: 개정 ID (첫 번째 버전은 0, 성공적인 저장마다 1씩 증가)

---

### InMemoryArtifactService

```python
pydantic model google.adk.artifacts.InMemoryArtifactService
```

**상속**: `BaseArtifactService`, `BaseModel`

아티팩트 서비스의 메모리 내 구현체입니다.

> ⚠️ **주의**: 멀티스레드 프로덕션 환경에는 적합하지 않습니다. 테스트 및 개발 목적으로만 사용하세요.

#### 필드

- **artifacts**: `dict[str, list[google.genai.types.Part]]` (선택사항) - 아티팩트들을 저장하는 딕셔너리

#### 메소드

##### `async delete_artifact(*, app_name, user_id, session_id, filename)`
아티팩트를 삭제합니다.

- **반환 타입**: `None`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **filename**: 아티팩트 파일의 이름

##### `async list_artifact_keys(*, app_name, user_id, session_id)`
세션 내의 모든 아티팩트 파일명을 나열합니다.

- **반환 타입**: `list[str]`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
- **반환값**: 세션 내 모든 아티팩트 파일명의 리스트

##### `async list_versions(*, app_name, user_id, session_id, filename)`
아티팩트의 모든 버전을 나열합니다.

- **반환 타입**: `list[int]`
- **매개변수**:
  - **app_name**: 애플리케이션의 이름
  - **user_id**: 사용자의 ID
  - **session_id**: 세션의 ID
  - **filename**: 아티팩트 파일의 이름
- **반환값**: 아티팩트의 사용 가능한 모든 버전 리스트

##### `async load_artifact(*, app_name, user_id, session_id, filename, version=None)`
아티팩트 서비스 스토리지에서 아티팩트를 가져옵니다.

아티팩트는 앱 이름, 사용자 ID, 세션 ID, 파일명으로 식별되는 파일입니다.

- **반환 타입**: `Optional[Part]`
- **매개변수**:
  - **app_name**: 앱 이름
  - **user_id**: 사용자 ID
  - **session_id**: 세션 ID
  - **filename**: 아티팩트의 파일명
  - **version**: 아티팩트의 버전 (None일 경우 최신 버전 반환)
- **반환값**: 아티팩트 또는 찾을 수 없으면 None

##### `async save_artifact(*, app_name, user_id, session_id, filename, artifact)`
아티팩트를 아티팩트 서비스 스토리지에 저장합니다.

아티팩트는 앱 이름, 사용자 ID, 세션 ID, 파일명으로 식별되는 파일입니다. 아티팩트 저장 후 아티팩트 버전을 식별하는 개정 ID가 반환됩니다.

- **반환 타입**: `int`
- **매개변수**:
  - **app_name**: 앱 이름
  - **user_id**: 사용자 ID
  - **session_id**: 세션 ID
  - **filename**: 아티팩트의 파일명
  - **artifact**: 저장할 아티팩트
- **반환값**: 개정 ID (첫 번째 버전은 0, 성공적인 저장마다 1씩 증가)