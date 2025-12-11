import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm
from .config import (
    PROVIDER,
    MODEL_NAME,
    USER_ID_MANAGER_INSTRUCTION_KO,
    USER_ID_MANAGER_INSTRUCTION_EN

)

from .tool_box import ( 
                    search_users,
                    check_username,
                    create_user,
                    modify_user,
                    delete_user,
                    change_password,
                    resend_verification_email
                )



user_id_manager = Agent(
    model=LiteLlm(model=f"{PROVIDER}/{MODEL_NAME}"),
    name='user_id_manager',
    description="Agent responsible for registering new users by collecting and validating ID, password, email, and name.",
    instruction=USER_ID_MANAGER_INSTRUCTION_KO,
    tools=[
        search_users,
        check_username,
        create_user,
        modify_user,
        delete_user,
        change_password,
        resend_verification_email
    ]
)

