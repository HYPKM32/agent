import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .config import (
    PROVIDER,
    MODEL_NAME,
    PROJECT_MANAGER_INSTRUCTION_KO,
    PROJECT_MANAGER_INSTRUCTION_EN
)

from .tool_box import (
    search_projects,
    create_project,
    modify_project,
    check_duplicate_project,
    get_project_detail,
    delete_project
)


project_manager = Agent(
    model=LiteLlm(model=f"{PROVIDER}/{MODEL_NAME}"),
    name='project_manager',
    description="Agent responsible for managing research projects including creation, modification, deletion, and search.",
    instruction=PROJECT_MANAGER_INSTRUCTION_KO,
    tools=[
        search_projects,
        create_project,
        modify_project,
        check_duplicate_project,
        get_project_detail,
        delete_project
    ]
)