# Google ADK Examples API Reference

`google.adk.examples` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### BaseExampleProvider

```python
class google.adk.examples.BaseExampleProvider
```

**상속**: `ABC`

예시 제공자를 위한 기본 클래스입니다.

이 클래스는 주어진 쿼리에 대한 예시를 제공하는 인터페이스를 정의합니다.

#### 추상 메소드

##### `get_examples(query)`
주어진 쿼리에 대한 예시 리스트를 반환합니다.

- **반환 타입**: `list[Example]`
- **매개변수**:
  - **query**: 예시를 가져올 쿼리
- **반환값**: Example 객체들의 리스트

---

### Example

```python
pydantic model google.adk.examples.Example
```

**상속**: `BaseModel`

Few-shot 예시를 나타내는 클래스입니다.

#### 필드

- **input**: `Content` (필수) - 예시의 입력 콘텐츠
- **output**: `list[Content]` (필수) - 예시의 예상 출력 콘텐츠

#### 필드 설명

##### `field input: Content [Required]`
예시의 입력 부분을 나타내는 콘텐츠입니다.

##### `field output: list[Content] [Required]`
예시의 출력 부분을 나타내는 콘텐츠 리스트입니다.

---

### VertexAiExampleStore

```python
class google.adk.examples.VertexAiExampleStore(examples_store_name)
```

**상속**: `BaseExampleProvider`

Vertex 예시 스토어에서 예시를 제공하는 클래스입니다.

#### 생성자

VertexAiExampleStore를 초기화합니다.

- **매개변수**:
  - **examples_store_name**: Vertex 예시 스토어의 리소스 이름

#### 리소스 이름 형식

```
projects/{project}/locations/{location}/exampleStores/{example_store}
```

#### 메소드

##### `get_examples(query)`
주어진 쿼리에 대한 예시 리스트를 반환합니다.

- **반환 타입**: `list[Example]`
- **매개변수**:
  - **query**: 예시를 가져올 쿼리
- **반환값**: Example 객체들의 리스트

---

## 사용 예시

### Example 객체 생성

```python
from google.adk.examples import Example
from google.genai.types import Content

# 단순한 텍스트 예시 생성
example = Example(
    input=Content(parts=["사용자 질문: 파이썬이란 무엇인가요?"]),
    output=[Content(parts=["파이썬은 프로그래밍 언어입니다."])]
)

# 복잡한 대화 예시 생성
complex_example = Example(
    input=Content(parts=["코딩 도움이 필요합니다."]),
    output=[
        Content(parts=["어떤 프로그래밍 언어를 사용하고 계신가요?"]),
        Content(parts=["어떤 문제를 해결하려고 하시는지 알려주세요."])
    ]
)
```

### VertexAiExampleStore 사용

```python
from google.adk.examples import VertexAiExampleStore

# Vertex AI 예시 스토어 초기화
example_store = VertexAiExampleStore(
    examples_store_name="projects/my-project/locations/us-central1/exampleStores/my-store"
)

# 쿼리에 따른 예시 가져오기
examples = example_store.get_examples("Python programming help")

# 가져온 예시들 사용
for example in examples:
    print(f"Input: {example.input}")
    print(f"Output: {example.output}")
```

### 커스텀 ExampleProvider 구현

```python
from google.adk.examples import BaseExampleProvider, Example
from google.genai.types import Content

class CustomExampleProvider(BaseExampleProvider):
    def __init__(self, examples_database):
        self.examples_database = examples_database
    
    def get_examples(self, query):
        # 쿼리에 따라 데이터베이스에서 예시 검색
        raw_examples = self.examples_database.search(query)
        
        # Example 객체로 변환
        examples = []
        for raw_example in raw_examples:
            example = Example(
                input=Content(parts=[raw_example['input']]),
                output=[Content(parts=[raw_example['output']])]
            )
            examples.append(example)
        
        return examples

# 사용법
custom_provider = CustomExampleProvider(my_database)
examples = custom_provider.get_examples("API 사용법")
```

### Few-shot Learning에서 활용

```python
# Few-shot 프롬프트 구성에 예시 활용
def create_few_shot_prompt(query, example_provider):
    examples = example_provider.get_examples(query)
    
    prompt_parts = ["다음은 몇 가지 예시입니다:\n"]
    
    for i, example in enumerate(examples, 1):
        prompt_parts.append(f"예시 {i}:")
        prompt_parts.append(f"입력: {example.input.parts[0]}")
        for j, output in enumerate(example.output):
            prompt_parts.append(f"출력: {output.parts[0]}")
        prompt_parts.append("")
    
    prompt_parts.append(f"이제 다음 질문에 답해주세요: {query}")
    
    return "\n".join(prompt_parts)

# 사용법
example_store = VertexAiExampleStore("projects/my-project/locations/us-central1/exampleStores/qa-store")
prompt = create_few_shot_prompt("파이썬 함수 작성법", example_store)
```

---

## 주요 특징

### 추상화된 인터페이스
- `BaseExampleProvider`를 통해 다양한 예시 소스를 통합된 인터페이스로 사용 가능
- 로컬 데이터베이스, 클라우드 서비스, API 등 다양한 소스 지원

### Vertex AI 통합
- `VertexAiExampleStore`를 통해 Google Cloud의 Vertex AI 예시 스토어와 직접 통합
- 관리형 예시 저장소의 이점 활용

### Few-shot Learning 지원
- `Example` 클래스를 통해 구조화된 입력-출력 쌍 관리
- 다중 출력 지원으로 복잡한 대화 패턴 표현 가능

### 확장성
- 커스텀 `ExampleProvider` 구현을 통해 특정 요구사항에 맞는 예시 관리 시스템 구축 가능
- 동적 예시 선택 및 필터링 로직 구현 가능