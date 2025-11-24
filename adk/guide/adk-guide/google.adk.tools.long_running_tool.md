# Google ADK Tools Long Running Tool API Reference

`google.adk.tools.long_running_tool` 모듈의 API 레퍼런스 문서입니다.

## 클래스

### LongRunningFunctionTool

```python
class google.adk.tools.long_running_tool.LongRunningFunctionTool(func)
```

**상속**: `FunctionTool`

결과를 비동기적으로 반환하는 함수 도구입니다.

이 도구는 완료하는 데 상당한 시간이 걸릴 수 있는 장기 실행 작업에 사용됩니다. 프레임워크가 함수를 호출합니다. 함수가 반환되면, function_call_id로 식별되는 프레임워크에 응답이 비동기적으로 반환됩니다.

#### 예시

```python
tool = LongRunningFunctionTool(a_long_running_function)
```

#### 필드

- **is_long_running** - 도구가 장기 실행 작업인지 여부

#### 생성자

호출 가능한 객체에서 메타데이터를 추출합니다.