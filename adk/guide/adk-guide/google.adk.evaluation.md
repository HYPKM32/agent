# Google ADK Evaluation API Reference

`google.adk.evaluation` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### AgentEvaluator

```python
class google.adk.evaluation.AgentEvaluator
```

**상속**: `object`

에이전트를 위한 평가기로, 주로 테스트 케이스를 도와주는 역할을 합니다.

#### 정적 메소드

##### `async static evaluate(agent_module, eval_dataset_file_path_or_dir, num_runs=2, agent_name=None, initial_session_file=None)`

평가 데이터가 주어진 에이전트를 평가합니다.

- **매개변수**:
  - **agent_module**: 에이전트 정의가 포함된 Python 모듈의 경로. 로드된 모듈에서 'root_agent'를 찾는 규칙이 있습니다.
  - **eval_dataset_file_path_or_dir**: 평가 데이터셋. 평가 데이터셋이 포함된 파일의 전체 경로를 나타내는 문자열이거나, `.test.json` 접미사를 가진 모든 파일을 재귀적으로 탐색하는 디렉터리일 수 있습니다.
  - **num_runs**: 평가 데이터셋의 모든 항목을 평가할 횟수 (기본값: 2)
  - **agent_name**: 에이전트의 이름 (선택사항)
  - **initial_session_file**: 평가 데이터셋의 모든 평가에 필요한 초기 세션 상태가 포함된 파일 (선택사항)

##### `async static evaluate_eval_set(agent_module, eval_set, criteria, num_runs=2, agent_name=None, print_detailed_results=True)`

주어진 EvalSet을 사용하여 에이전트를 평가합니다.

- **매개변수**:
  - **agent_module**: 에이전트 정의가 포함된 Python 모듈의 경로. 로드된 모듈에서 'root_agent'를 찾는 규칙이 있습니다.
  - **eval_set**: 평가 세트
  - **criteria**: 평가 기준 - 메트릭 이름과 각각의 임계값을 매핑하는 딕셔너리
  - **num_runs**: 평가 데이터셋의 모든 항목을 평가할 횟수 (기본값: 2)
  - **agent_name**: root 에이전트가 아닌 다른 에이전트를 평가하려는 경우의 에이전트 이름. 비어있거나 None이면 root 에이전트가 평가됩니다.
  - **print_detailed_results**: 각 메트릭 평가에 대한 상세 결과를 출력할지 여부 (기본값: True)

##### `static find_config_for_test_file(test_file)`

테스트 파일과 같은 폴더에 있는 test_config.json 파일을 찾습니다.

- **매개변수**:
  - **test_file**: 테스트 파일의 경로

##### `static migrate_eval_data_to_new_schema(old_eval_data_file, new_eval_data_file, initial_session_file=None)`

평가 데이터를 EvalSet으로 지원되는 새로운 스키마로 마이그레이션하는 유틸리티입니다.

- **매개변수**:
  - **old_eval_data_file**: 기존 평가 데이터 파일
  - **new_eval_data_file**: 새로운 평가 데이터 파일
  - **initial_session_file**: 초기 세션 파일 (선택사항)

---

## 사용 예시

### 기본 평가 실행

```python
# 에이전트 모듈과 평가 데이터셋으로 평가 실행
await AgentEvaluator.evaluate(
    agent_module="path/to/my_agent.py",
    eval_dataset_file_path_or_dir="path/to/eval_data.test.json",
    num_runs=3
)

# 디렉터리의 모든 테스트 파일로 평가 실행
await AgentEvaluator.evaluate(
    agent_module="path/to/my_agent.py",
    eval_dataset_file_path_or_dir="path/to/test_directory/",
    num_runs=5,
    agent_name="my_specific_agent"
)
```

### EvalSet을 사용한 평가

```python
# 평가 기준과 함께 EvalSet 사용
criteria = {
    "accuracy": 0.85,
    "response_time": 2.0,
    "relevance": 0.9
}

await AgentEvaluator.evaluate_eval_set(
    agent_module="path/to/my_agent.py",
    eval_set=my_eval_set,
    criteria=criteria,
    num_runs=3,
    print_detailed_results=True
)
```

### 테스트 설정 파일 찾기

```python
# 테스트 파일에 대한 설정 파일 찾기
config = AgentEvaluator.find_config_for_test_file("tests/my_test.test.json")
```

### 평가 데이터 마이그레이션

```python
# 기존 평가 데이터를 새로운 스키마로 마이그레이션
AgentEvaluator.migrate_eval_data_to_new_schema(
    old_eval_data_file="old_format.json",
    new_eval_data_file="new_format.test.json",
    initial_session_file="initial_session.json"
)
```

---

## 주요 특징

### 에이전트 모듈 규칙
- 에이전트 모듈에서 `root_agent`라는 이름의 에이전트를 자동으로 찾습니다
- 다른 이름의 에이전트를 평가하려면 `agent_name` 매개변수를 사용하세요

### 평가 데이터셋 형식
- **단일 파일**: `.test.json` 확장자를 가진 파일
- **디렉터리**: `.test.json` 접미사를 가진 모든 파일을 재귀적으로 검색

### 평가 기준
- 메트릭 이름과 임계값을 매핑하는 딕셔너리 형태
- 각 메트릭은 설정된 임계값과 비교하여 평가됩니다

### 다중 실행
- `num_runs` 매개변수로 평가의 일관성과 신뢰성을 높일 수 있습니다
- 여러 번 실행하여 평균 성능을 측정할 수 있습니다