#/app/src/kbri/sub_agents/access_authenticator/tool_box/auth_tools.py
import os
import requests
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

KBRI_API_BASE_URL = os.getenv("KBRI_API_BASE_URL")


def login(username: str, password: str) -> dict:
    """
    Authenticates a user and returns an access token.
    
    Args:
        username: User's login ID
        password: User's password
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/auth/login"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "username": username,
        "password": password
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def refresh_token(refresh_token: str) -> dict:
    """
    Refreshes the access token using a refresh token.
    
    Args:
        refresh_token: JWT refresh token
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/auth/refresh"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "refresh_token": refresh_token
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}