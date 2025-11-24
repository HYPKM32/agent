# Google ADK Telemetry API Reference

`google.adk.telemetry` 모듈의 API 레퍼런스 문서입니다.

## 함수

### trace_call_llm

```python
google.adk.telemetry.trace_call_llm(invocation_context, event_id, llm_request, llm_response)
```

LLM 호출을 추적합니다.

이 함수는 현재 OpenTelemetry 스팬의 속성으로 LLM 요청 및 응답에 대한 세부 정보를 기록합니다.

#### 매개변수

- **invocation_context**: 현재 에이전트 실행의 호출 컨텍스트
- **event_id**: 이벤트의 ID
- **llm_request**: LLM 요청 객체
- **llm_response**: LLM 응답 객체

#### 사용 예시

```python
from google.adk.telemetry import trace_call_llm

# LLM 호출 추적
trace_call_llm(
    invocation_context=current_context,
    event_id="event_123",
    llm_request=my_llm_request,
    llm_response=received_response
)
```

---

### trace_merged_tool_calls

```python
google.adk.telemetry.trace_merged_tool_calls(response_event_id, function_response_event)
```

병합된 도구 호출 이벤트를 추적합니다.

이 함수는 텔레메트리 목적으로는 호출할 필요가 없습니다. 이는 `/debug/trace` 요청(일반적으로 웹 UI에서 전송)을 방지하기 위해 제공됩니다.

#### 매개변수

- **response_event_id**: 응답 이벤트의 ID
- **function_response_event**: 병합된 응답 이벤트

#### 사용 예시

```python
from google.adk.telemetry import trace_merged_tool_calls

# 병합된 도구 호출 추적 (디버그 용도)
trace_merged_tool_calls(
    response_event_id="response_456",
    function_response_event=merged_event
)
```

---

### trace_send_data

```python
google.adk.telemetry.trace_send_data(invocation_context, event_id, data)
```

에이전트로 데이터 전송을 추적합니다.

이 함수는 현재 OpenTelemetry 스팬의 속성으로 에이전트에게 전송된 데이터에 대한 세부 정보를 기록합니다.

#### 매개변수

- **invocation_context**: 현재 에이전트 실행의 호출 컨텍스트
- **event_id**: 이벤트의 ID
- **data**: 콘텐츠 객체들의 리스트

#### 사용 예시

```python
from google.adk.telemetry import trace_send_data
from google.genai.types import Content, Part

# 데이터 전송 추적
data_to_send = [
    Content(parts=[Part(text="사용자 메시지")])
]

trace_send_data(
    invocation_context=current_context,
    event_id="send_789",
    data=data_to_send
)
```

---

### trace_tool_call

```python
google.adk.telemetry.trace_tool_call(tool, args, function_response_event)
```

도구 호출을 추적합니다.

#### 매개변수

- **tool**: 호출된 도구
- **args**: 도구 호출의 인자들
- **function_response_event**: 함수 응답 세부 정보가 포함된 이벤트

#### 사용 예시

```python
from google.adk.telemetry import trace_tool_call
from google.adk.tools import FunctionTool

def my_function(param1: str, param2: int) ->