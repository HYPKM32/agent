import os
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

ollama_url = os.getenv("OLLAMA_BASE_URL")
model_name = os.getenv("ADK_MODEL")
provider = os.getenv("PROVIDER")

root_agent = Agent(
    model=LiteLlm(model=f"{provider}/{model_name}"),
    name='test_agent',
    description="Agent to answer questions in Korean",
    instruction='Answer user questions to the best of your knowledge',
    tools=[]
)
