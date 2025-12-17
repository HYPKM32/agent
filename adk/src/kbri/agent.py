#/app/src/kbri/agent.py
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .config import (
    PROVIDER,
    MODEL_NAME,
    ROOT_AGENT_INSTRUCTION_KO,
    ROOT_AGENT_INSTRUCTION_EN
)
from .tool_box import (google_search, create_session, check_session)
from .sub_agents import (user_id_manager,project_manager)

root_agent = Agent(
    model=LiteLlm(model=f"{PROVIDER}/{MODEL_NAME}"),
    name='root_agent',
    description="Main orchestrator for search and user registration delegation.",
    instruction=ROOT_AGENT_INSTRUCTION_KO,
    tools=[google_search],
    sub_agents=[user_id_manager, project_manager]
)