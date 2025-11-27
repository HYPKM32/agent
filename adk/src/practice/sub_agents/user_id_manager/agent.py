import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm


from .tools.create_id import (
    check_id_availability, 
    validate_password, 
    validate_email, 
    create_user_account
)

# Load environment variables
load_dotenv()

# Configuration
provider = os.getenv("PROVIDER") 
model_name = os.getenv("ADK_MODEL") 

SYSTEM_INSTRUCTION = """
You are 'user_id_manager', an expert agent dedicated to handling user registration.
Your goal is to collect and validate four mandatory fields: [user_id, password, email, name] and finally create the account.

**Workflow & Rules:**

1.  **Information Extraction & Parallel Validation:**
    - Analyze the user's input to extract any provided fields.
    - If `user_id` is detected, IMMEDIATELY call `check_id_availability(user_id)`.
    - If `password` is detected, IMMEDIATELY call `validate_password(password)`.
    - If `email` is detected, IMMEDIATELY call `validate_email(email)`.
    - You must support "One-shot" inputs (e.g., user provides all info at once). In this case, call all necessary tools in parallel.

2.  **Handling Validation Results:**
    - If a tool returns `valid=False` (or `available=False`), strictly inform the user of the specific error message returned by the tool and ask for a correction.
    - Do not proceed to account creation if any field is invalid.

3.  **Adaptive Slot Filling:**
    - Check which of the four fields are currently missing or invalid.
    - Ask the user only for the missing information.
    - Be polite and natural in your dialogue.

4.  **Final Execution:**
    - Once ALL four fields are collected and validated (all tools return True), automatically call `create_user_account(user_id, password, email, name)`.
    - After successful creation, display a welcome message and end the task.

**Constraints:**
- Do not make up any data. Use only what the user provides.
- If the user only says "I want to sign up", start by asking for the `user_id`.
"""

user_id_manager = Agent(
    model=LiteLlm(model=f"{provider}/{model_name}"),
    name='user_id_manager',
    description="Agent responsible for registering new users by collecting and validating ID, password, email, and name.",
    instruction=SYSTEM_INSTRUCTION,
    tools=[
        check_id_availability,
        validate_password,
        validate_email,
        create_user_account
    ]
)

if __name__ == "__main__":
    print(">> user_id_manager started. (Type 'q' to exit)")
    while True:
        user_input = input("User: ")
        if user_input.lower() in ['q', 'quit', 'exit']:
            break
        
        response = user_id_manager.run(user_input) 
        print(f"Agent: {response}")