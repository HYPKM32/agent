#/app/src/kbri/sub_agents/user_id_manager/tool_box/user_tools.py
import requests
from typing import Optional
from ..config import KBRI_API_BASE_URL



def search_users(token: str, page: int = 1, count: int = 20) -> dict:
    """
    Searches for users with pagination.
    
    Args:
        token: Bearer authentication token
        page: Page number
        count: Number of items per page
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/searchUsers"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
    }
    payload = {
        "page": page,
        "count": count
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def check_username(token: str, username: str) -> dict:
    """
    Checks if a username is already taken.
    
    Args:
        token: Bearer authentication token
        username: Username to check for availability
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/checkUsername"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
    }
    payload = {
        "username": username
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}

    
def create_user(
    token: str,
    username: str,
    email: str,
    password: str,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    affiliation: Optional[str] = None,
    department: Optional[str] = None,
    degree: Optional[int] = None
) -> dict:
    """
    Creates a new user account.
    
    Args:
        token: Bearer authentication token
        username: User's login ID (lowercase letters and numbers, min 4 characters)
        email: User's email address (must be unique)
        password: User's password
        first_name: User's first name
        last_name: User's last name
        affiliation: User's affiliated organization
        department: User's department
        degree: User's degree level (1=Doctorate, 2=Master's, 3=Bachelor's)
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/createUser"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
    }
    payload = {
        "username": username,
        "email": email,
        "password": password
    }
    
    if first_name is not None:
        payload["first_name"] = first_name
    if last_name is not None:
        payload["last_name"] = last_name
    if affiliation is not None:
        payload["affiliation"] = affiliation
    if department is not None:
        payload["department"] = department
    if degree is not None:
        payload["degree"] = degree
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}

    
def modify_user(
    token: str,
    user_id: int,
    first_name: Optional[str] = None,
    last_name: Optional[str] = None,
    username: Optional[str] = None,
    email: Optional[str] = None,
    affiliation: Optional[str] = None,
    department: Optional[str] = None,
    password: Optional[str] = None,
    degree: Optional[int] = None,
    status: Optional[int] = None
) -> dict:
    """
    Modifies an existing user's information.
    
    Args:
        token: Bearer authentication token
        user_id: Target user's ID
        first_name: User's first name
        last_name: User's last name
        username: User's login ID
        email: User's email address
        affiliation: User's affiliated organization
        department: User's department
        password: User's password
        degree: User's degree level
        status: User's account status
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/modifyUser"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
    }
    payload = {
        "user_id": user_id
    }
    
    if first_name is not None:
        payload["first_name"] = first_name
    if last_name is not None:
        payload["last_name"] = last_name
    if username is not None:
        payload["username"] = username
    if email is not None:
        payload["email"] = email
    if affiliation is not None:
        payload["affiliation"] = affiliation
    if department is not None:
        payload["department"] = department
    if password is not None:
        payload["password"] = password
    if degree is not None:
        payload["degree"] = degree
    if status is not None:
        payload["status"] = status
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def delete_user(token: str, user_id: int) -> dict:
    """
    Deletes an existing user account.
    
    Args:
        token: Bearer authentication token
        user_id: Target user's ID to delete
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/deleteUser"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
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


def change_password(
    token: str,
    user_id: int,
    current_password: str,
    new_password: str
) -> dict:
    """
    Changes a user's password.
    
    Args:
        token: Bearer authentication token
        user_id: Target user's ID
        current_password: User's current password
        new_password: User's new password
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/changePassword"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
    }
    payload = {
        "user_id": user_id,
        "current_password": current_password,
        "new_password": new_password
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}
    


def resend_verification_email(token: str, email: str) -> dict:
    """
    Resends the verification email to the specified email address.
    
    Args:
        token: Bearer authentication token
        email: User's email address to resend verification
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/users/resendVerificationEmail"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Request-Source": "agent"
    }
    payload = {
        "email": email
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}