#/app/src/kbri/tool_box/root_tools.py
import requests
from typing import Optional
from ..config import GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID
from ..config import KBRI_API_BASE_URL


def google_search(query: str) -> dict:
    """
    Performs a web search using the Google Custom Search API.
    
    Args:
        query: The search query string
        
    Returns:
        Dictionary with status and response data
    """
    if not GOOGLE_API_KEY or not GOOGLE_SEARCH_ENGINE_ID:
        return {"status": "error", "response": "Google API Key or Search Engine ID is missing."}

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_SEARCH_ENGINE_ID,
        "q": query,
        "num": 5
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def create_session(
    user_id: int,
    refresh_token: str,
    agent_name: str = "root_agent"
) -> dict:
    """
    Creates an agent session for the specified user.
    
    Args:
        user_id: The user's ID
        refresh_token: The refresh token for authentication
        agent_name: Name of the agent (default: "root_agent")
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/auth/agent/createAgentSession"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "user_id": user_id,
        "refresh_token": refresh_token,
        "agent_name": agent_name
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def check_session(token: str, user_id: int) -> dict:
    """
    Retrieves agent sessions for the specified user.
    
    Args:
        token: Bearer authentication token
        user_id: The user's ID
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/auth/agent/getAgentSessions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "user_id": user_id
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}