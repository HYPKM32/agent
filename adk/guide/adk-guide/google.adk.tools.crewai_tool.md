# Google ADK Tools CrewAI Tool API Reference

`google.adk.tools.crewai_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### CrewaiTool

```python
class google.adk.tools.crewai_tool.CrewaiTool(tool, *, name, description)
```

**상속**: `FunctionTool`

CrewAI 도구를 래핑하는 데 사용하는 클래스입니다.

원래 도구의 이름과 설명이 적합하지 않은 경우, 생성자에서 이를 재정의할 수 있습니다.

호출 가능한 객체에서 메타데이터를 추출합니다.

#### 필드

- **tool**: `BaseTool` - 래핑된 CrewAI 도구