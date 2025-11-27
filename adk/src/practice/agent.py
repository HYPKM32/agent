
#/app/src/practice/agent.py
import os
import requests
from typing import List, Dict, Any
from dotenv import load_dotenv
from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm


from .sub_agents import user_id_manager

load_dotenv()

# Configuration
ollama_url = os.getenv("OLLAMA_BASE_URL")
model_name = os.getenv("ADK_MODEL")
provider = os.getenv("PROVIDER")
google_api_key = os.getenv("GOOGLE_API_KEY")
google_search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")


def google_search_tool(query: str) -> str:
    """Performs a web search using the Google Custom Search JSON API."""
    if not google_api_key or not google_search_engine_id:
        return "Error: Google API Key or Search Engine ID is missing."

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": google_api_key,
        "cx": google_search_engine_id,
        "q": query,
        "num": "5"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        search_results = data.get("items", [])
        if not search_results:
            return "No results found."

        formatted_results = ""
        for i, item in enumerate(search_results, 1):
            title = item.get("title", "No Title")
            snippet = item.get("snippet", "No Snippet")
            link = item.get("link", "No Link")
            formatted_results += f"{i}. Title: {title}\n   Snippet: {snippet}\n   Source: {link}\n\n"
            
        return formatted_results

    except requests.exceptions.RequestException as e:
        return f"Error during Google Search: {str(e)}"



ROOT_INSTRUCTION = """
You are the 'Root Agent', the central orchestrator of this system. 
Your primary role is to understand the user's intent and route the task to either the appropriate sub-agent or a specific tool.

**Routing Logic (Strictly Follow Priority):**

1. **User Registration & Account Management (Priority 1):**
   - **Trigger:** If the user mentions "sign up", "create account", "make ID", "register", "password", or "user info".
   - **Action:** DO NOT handle this yourself. IMMEDIATEY delegate control to the `user_id_manager` sub-agent.
   - **Note:** Do not ask for the ID yourself. Let the sub-agent start its workflow.

2. **Information Retrieval & News (Priority 2):**
   - **Trigger:** If the user asks for "latest news", "current events", "weather", "real-time info", or specific facts you don't know.
   - **Action:** Use the `Google Search_tool`.
   - **Output:** Summarize the search results in Korean.

3. **General Chit-Chat (Priority 3):**
   - **Trigger:** Greetings, general knowledge questions, or casual conversation.
   - **Action:** Answer naturally and helpfully in Korean using your own knowledge.

**Behavior:**
- Always classify the intent first.
- If delegating to a sub-agent, simply activate them without extra commentary.
"""


root_agent = Agent(
    model=LiteLlm(model=f"{provider}/{model_name}"),
    name='root_agent',
    description="Main orchestrator for search and user registration delegation.",
    instruction=ROOT_INSTRUCTION,
    tools=[google_search_tool],
    sub_agents=[user_id_manager]
)