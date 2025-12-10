from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

from .config import (
    PROVIDER,
    MODEL_NAME,
    ROOT_AGENT_INSTRUCTION_KO,
)
from .tool_box import google_search_tool
from .sub_agents import user_id_manager


root_agent = Agent(
    model=LiteLlm(model=f"{PROVIDER}/{MODEL_NAME}"),
    name='root_agent',
    description="Main orchestrator for search and user registration delegation.",
    instruction=ROOT_AGENT_INSTRUCTION_KO,
    tools=[google_search_tool],
    sub_agents=[user_id_manager]
)