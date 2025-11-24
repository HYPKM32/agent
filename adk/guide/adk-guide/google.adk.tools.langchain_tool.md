# Google ADK Tools Langchain Tool API Reference

`google.adk.tools.langchain_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### LangchainTool

```python
class google.adk.tools.langchain_tool.LangchainTool(tool, name=None, description=None)
```

**상속**: `FunctionTool`

ADK에서 사용하기 위해 Langchain 도구를 래핑하는 어댑터 클래스입니다.

이 어댑터는 Langchain 도구를 Google의 생성형 AI 함수 호출 인터페이스와 호환되는 형식으로 변환합니다. 스키마를 적응시키면서 도구의 이름, 설명 및 기능을 보존합니다.

필요한 경우 원래 도구의 이름과 설명을 재정의할 수 있습니다.

#### 생성자

호출 가능한 객체에서 메타데이터를 추출합니다.

**매개변수:**
- **tool** – 래핑할 Langchain 도구 (BaseTool 또는 .run 메소드가 있는 도구)
- **name** – 도구 이름의 선택적 재정의
- **description** – 도구 설명의 선택적 재정의

#### 예시

```python
from langchain.tools import DuckDuckGoSearchTool
from google.genai.tools import LangchainTool

search_tool = DuckDuckGoSearchTool()
wrapped_tool = LangchainTool(search_tool)
```