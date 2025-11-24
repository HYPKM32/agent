# Google ADK Code Executors API Reference

`google.adk.code_executors` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseCodeExecutor

```python
pydantic model google.adk.code_executors.BaseCodeExecutor
```

**상속**: `BaseModel`

모든 코드 실행기의 추상 기본 클래스입니다.

코드 실행기는 에이전트가 모델 응답에서 코드 블록을 실행하고 실행 결과를 최종 응답에 통합할 수 있게 해줍니다.

#### 필드

- **optimize_data_file**: `bool` (기본값: False) - 모델 요청에서 데이터 파일 추출 및 처리 여부
- **stateful**: `bool` (기본값: False) - 코드 실행기가 상태를 유지하는지 여부
- **error_retry_attempts**: `int` (기본값: 2) - 연속적인 코드 실행 오류 시 재시도 횟수
- **code_block_delimiters**: `List[tuple[str, str]]` - 코드 블록을 식별하는 구분 기호 리스트
- **execution_result_delimiters**: `tuple[str, str]` - 코드 실행 결과를 포맷하는 구분 기호

#### 기본값

```python
code_block_delimiters = [('```tool_code\n', '\n```'), ('```python\n', '\n```')]
execution_result_delimiters = ('```tool_output\n', '\n```')
```

#### 코드 블록 예시

```python
# code_block_delimiters의 ('```python\n', '\n```')로 식별되는 형식:
```python
print("hello")
```
```

#### 추상 메소드

##### `execute_code(invocation_context, code_execution_input)`
코드를 실행하고 코드 실행 결과를 반환합니다.

- **반환 타입**: `CodeExecutionResult`
- **매개변수**:
  - **invocation_context**: 코드 실행의 호출 컨텍스트
  - **code_execution_input**: 코드 실행 입력
- **반환값**: 코드 실행 결과

---

### BuiltInCodeExecutor

```python
pydantic model google.adk.code_executors.BuiltInCodeExecutor
```

**상속**: `BaseCodeExecutor`

모델의 내장 코드 실행기를 사용하는 코드 실행기입니다.

> **참고**: 현재 Gemini 2.0+ 모델만 지원하지만, 다른 모델로 확장될 예정입니다.

#### 메소드

##### `execute_code(invocation_context, code_execution_input)`
코드를 실행하고 코드 실행 결과를 반환합니다.

- **반환 타입**: `CodeExecutionResult`

##### `process_llm_request(llm_request)`
Gemini 2.0+ 모델이 코드 실행 도구를 사용하도록 LLM 요청을 전처리합니다.

- **반환 타입**: `None`

---

### CodeExecutorContext

```python
class google.adk.code_executors.CodeExecutorContext(session_state)
```

**상속**: `object`

코드 실행기를 구성하는데 사용되는 지속적인 컨텍스트입니다.

#### 생성자

- **매개변수**: **session_state**: 코드 실행기 컨텍스트를 가져올 세션 상태

#### 메소드

##### 파일 관리
- `add_input_files(input_files)`: 입력 파일을 코드 실행기 컨텍스트에 추가
- `get_input_files()`: 입력 파일 리스트 반환 (`list[File]`)
- `clear_input_files()`: 입력 파일 및 처리된 파일명 제거
- `add_processed_file_names(file_names)`: 처리된 파일명을 세션 상태에 추가
- `get_processed_file_names()`: 처리된 파일명 리스트 반환 (`list[str]`)

##### 실행 ID 관리
- `get_execution_id()`: 코드 실행기의 세션 ID 반환 (`Optional[str]`)
- `set_execution_id(session_id)`: 코드 실행기의 세션 ID 설정

##### 오류 카운트 관리
- `get_error_count(invocation_id)`: 주어진 호출 ID의 오류 카운트 반환 (`int`)
- `increment_error_count(invocation_id)`: 오류 카운트 증가
- `reset_error_count(invocation_id)`: 오류 카운트 리셋

##### 상태 관리
- `get_state_delta()`: 지속적인 세션 상태에서 업데이트할 상태 델타 반환 (`dict[str, Any]`)
- `update_code_execution_result(invocation_id, code, result_stdout, result_stderr)`: 코드 실행 결과 업데이트

---

### ContainerCodeExecutor

```python
pydantic model google.adk.code_executors.ContainerCodeExecutor
```

**상속**: `BaseCodeExecutor`

커스텀 컨테이너를 사용하여 코드를 실행하는 코드 실행기입니다.

#### 필드

- **base_url**: `Optional[str]` (기본값: None) - 사용자가 호스팅하는 Docker 클라이언트의 기본 URL (선택사항)
- **image**: `str` (기본값: None) - 컨테이너에서 실행할 사전 정의된 이미지 또는 커스텀 이미지의 태그
- **docker_path**: `str` (기본값: None) - Dockerfile이 포함된 디렉터리 경로
- **optimize_data_file**: `bool` (기본값: False) - 데이터 파일 최적화 여부
- **stateful**: `bool` (기본값: False) - 상태 유지 여부

#### 생성자

- **매개변수**:
  - **base_url**: Docker 클라이언트 기본 URL (선택사항)
  - **image**: 컨테이너 이미지 태그 (`docker_path` 또는 `image` 중 하나 필수)
  - **docker_path**: Dockerfile 경로 (`docker_path` 또는 `image` 중 하나 필수)
  - **\*\*data**: 추가 초기화 데이터

#### 메소드

##### `execute_code(invocation_context, code_execution_input)`
코드를 실행하고 코드 실행 결과를 반환합니다.

- **반환 타입**: `CodeExecutionResult`

##### `model_post_init(context, /)`
private 속성을 초기화하는 BaseModel 메소드입니다.

- **반환 타입**: `None`

---

### UnsafeLocalCodeExecutor

```python
pydantic model google.adk.code_executors.UnsafeLocalCodeExecutor
```

**상속**: `BaseCodeExecutor`

현재 로컬 컨텍스트에서 안전하지 않게 코드를 실행하는 코드 실행기입니다.

> ⚠️ **경고**: 이 실행기는 보안상 위험할 수 있습니다. 신뢰할 수 있는 코드만 실행하세요.

#### 필드

- **optimize_data_file**: `bool` (기본값: False) - 데이터 파일 최적화 여부
- **stateful**: `bool` (기본값: False) - 상태 유지 여부

#### 메소드

##### `execute_code(invocation_context, code_execution_input)`
코드를 실행하고 코드 실행 결과를 반환합니다.

- **반환 타입**: `CodeExecutionResult`

---

### VertexAiCodeExecutor

```python
pydantic model google.adk.code_executors.VertexAiCodeExecutor
```

**상속**: `BaseCodeExecutor`

Vertex Code Interpreter Extension을 사용하여 코드를 실행하는 코드 실행기입니다.

#### 필드

- **resource_name**: `str` (기본값: None) - 기존 코드 인터프리터 확장의 리소스 이름

#### 리소스 이름 형식

```
projects/123/locations/us-central1/extensions/456
```

#### 생성자

- **매개변수**:
  - **resource_name**: 기존 코드 인터프리터 확장의 리소스 이름 (새로 생성하지 않고 기존 것을 로드)
  - **\*\*data**: 기본 클래스에 전달할 추가 키워드 인자

#### 메소드

##### `execute_code(invocation_context, code_execution_input)`
코드를 실행하고 코드 실행 결과를 반환합니다.

- **반환 타입**: `CodeExecutionResult`

##### `model_post_init(context, /)`
private 속성을 초기화하는 BaseModel 메소드입니다.

- **반환 타입**: `None`

---

## 사용 예시

### 기본 사용법

```python
# 내장 코드 실행기 사용 (Gemini 2.0+)
executor = BuiltInCodeExecutor()

# 컨테이너 기반 실행기 사용
executor = ContainerCodeExecutor(
    image="python:3.9",
    stateful=True,
    optimize_data_file=True
)

# Vertex AI 코드 실행기 사용
executor = VertexAiCodeExecutor(
    resource_name="projects/my-project/locations/us-central1/extensions/my-extension"
)
```

### 코드 블록 구분 기호 커스터마이징

```python
executor = BuiltInCodeExecutor(
    code_block_delimiters=[
        ('```python\n', '\n```'),
        ('```javascript\n', '\n```')
    ],
    execution_result_delimiters=('===OUTPUT===\n', '\n===END===')
)
```