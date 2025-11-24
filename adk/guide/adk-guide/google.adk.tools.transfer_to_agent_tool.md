# Google ADK Tools Transfer to Agent Tool API Reference

`google.adk.tools.transfer_to_agent_tool` 모듈의 API 레퍼런스 문서입니다.

## 함수

### transfer_to_agent

```python
google.adk.tools.transfer_to_agent_tool.transfer_to_agent(agent_name, tool_context)
```

질문을 다른 에이전트로 전송합니다.

이 도구는 에이전트의 설명에 따라 사용자의 질문에 답변하기에 더 적합한 다른 에이전트가 있을 때 제어권을 넘깁니다.

**매개변수:**
- **agent_name** – 전송할 에이전트 이름