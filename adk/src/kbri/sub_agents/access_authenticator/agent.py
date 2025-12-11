#/app/src/kbri/sub_agents/access_authenticator/agent.py
import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .config import (
    PROVIDER,
    MODEL_NAME,
    ACCESS_AUTHENTICATOR_INSTRUCTION_KO,
    ACCESS_AUTHENTICATOR_INSTRUCTION_EN
)
from .tool_box import ( 
                login,
                refresh_token
            )



access_authenticator = Agent(
    model=LiteLlm(model=f"{PROVIDER}/{MODEL_NAME}"),
    name='access_authenticator',
    description="Agent responsible for user account management including creation, retrieval, modification, deletion, and email verification.",
    instruction=ACCESS_AUTHENTICATOR_INSTRUCTION_KO,
    tools=[login, refresh_token]
)

