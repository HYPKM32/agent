#/app/src/kbri/sub_agents/project_manager/tool_box/project_tools.py
import os
import requests
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

KBRI_API_BASE_URL = os.getenv("KBRI_API_BASE_URL")


def search_projects(
    token: str,
    page: int = 1,
    count: int = 10,
    sort: str = "registry_date",
    user_id: int = 0,
    owner_only: Optional[bool] = None,
    research_field: Optional[int] = None,
    status: Optional[int] = None
) -> dict:
    """
    Searches for projects with pagination and filtering.
    
    Args:
        token: Bearer authentication token
        page: Page number
        count: Number of items per page
        sort: Sort criteria
        user_id: Logged in user's ID (0 for non-members)
        owner_only: If true, only shows projects owned by or team-associated with user
        research_field: Research field filter
        status: Status filter
        
    Returns:
        Dictionary with status and response data containing project list and pagination info
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/projects/searchProjects"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "page": page,
        "count": count,
        "sort": sort,
        "user_id": user_id
    }
    
    if owner_only is not None:
        payload["owner_only"] = owner_only
    if research_field is not None:
        payload["research_field"] = research_field
    if status is not None:
        payload["status"] = status
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}

    
def create_project(
    token: str,
    user_id: int,
    project_name: str,
    principal_investigator: str,
    research_field: int,
    research_start: str,
    research_end: str,
    privacy_settings: int,
    description: Optional[str] = None,
    research_fund: Optional[str] = None,
    required_skills: Optional[str] = None,
    ethics_approval: Optional[bool] = None,
    share_approval: Optional[bool] = None,
    items: Optional[list] = None
) -> dict:
    """
    Creates a new project.
    
    Args:
        token: Bearer authentication token
        user_id: Project owner's user ID
        project_name: Name of the project
        principal_investigator: Principal investigator's name
        research_field: Research field code
        research_start: Research start date
        research_end: Research end date
        privacy_settings: Privacy level (1=public, 2=researchers, 3=approved, 4=team only)
        description: Project description
        research_fund: Research funding information
        required_skills: Required skills for the project
        ethics_approval: Ethics approval status
        share_approval: Data sharing approval status
        items: Project items list
        
    Returns:
        Dictionary with status and response data containing new project_id
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/projects/createProject"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "user_id": user_id,
        "project_name": project_name,
        "principal_investigator": principal_investigator,
        "research_field": research_field,
        "research_start": research_start,
        "research_end": research_end,
        "privacy_settings": privacy_settings
    }
    
    if description is not None:
        payload["description"] = description
    if research_fund is not None:
        payload["research_fund"] = research_fund
    if required_skills is not None:
        payload["required_skills"] = required_skills
    if ethics_approval is not None:
        payload["ethics_approval"] = ethics_approval
    if share_approval is not None:
        payload["share_approval"] = share_approval
    if items is not None:
        payload["items"] = items
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}
    

def modify_project(
    token: str,
    project_id: int,
    user_id: int,
    project_name: Optional[str] = None,
    description: Optional[str] = None,
    principal_investigator: Optional[str] = None,
    research_field: Optional[int] = None,
    research_start: Optional[str] = None,
    research_end: Optional[str] = None,
    research_fund: Optional[str] = None,
    required_skills: Optional[str] = None,
    ethics_approval: Optional[bool] = None,
    share_approval: Optional[bool] = None,
    privacy_settings: Optional[int] = None,
    items: Optional[list] = None
) -> dict:
    """
    Modifies an existing project.
    
    Args:
        token: Bearer authentication token
        project_id: Target project's ID
        user_id: User's ID (must be project owner)
        project_name: Name of the project
        description: Project description
        principal_investigator: Principal investigator's name
        research_field: Research field code
        research_start: Research start date
        research_end: Research end date
        research_fund: Research funding information
        required_skills: Required skills for the project
        ethics_approval: Ethics approval status
        share_approval: Data sharing approval status
        privacy_settings: Privacy level (1=public, 2=researchers, 3=approved, 4=team only)
        items: Project items list
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/projects/modifyProject"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "project_id": project_id,
        "user_id": user_id
    }
    
    if project_name is not None:
        payload["project_name"] = project_name
    if description is not None:
        payload["description"] = description
    if principal_investigator is not None:
        payload["principal_investigator"] = principal_investigator
    if research_field is not None:
        payload["research_field"] = research_field
    if research_start is not None:
        payload["research_start"] = research_start
    if research_end is not None:
        payload["research_end"] = research_end
    if research_fund is not None:
        payload["research_fund"] = research_fund
    if required_skills is not None:
        payload["required_skills"] = required_skills
    if ethics_approval is not None:
        payload["ethics_approval"] = ethics_approval
    if share_approval is not None:
        payload["share_approval"] = share_approval
    if privacy_settings is not None:
        payload["privacy_settings"] = privacy_settings
    if items is not None:
        payload["items"] = items
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def check_duplicate_project(
    token: str,
    project_name: str,
    exclude_id: Optional[int] = None
) -> dict:
    """
    Checks if a project name is already taken.
    
    Args:
        token: Bearer authentication token
        project_name: Project name to check for duplication
        exclude_id: Project ID to exclude from check (for modifying existing project)
        
    Returns:
        Dictionary with status and response data containing isDuplicate flag
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/projects/checkDuplicateProject"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "project_name": project_name
    }
    
    if exclude_id is not None:
        payload["exclude_id"] = exclude_id
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}


def delete_project(token: str, project_id: int, user_id: int) -> dict:
    """
    Deletes an existing project (soft delete).
    
    Args:
        token: Bearer authentication token
        project_id: Target project's ID to delete
        user_id: User's ID (must be project owner)
        
    Returns:
        Dictionary with status and response data
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/projects/deleteProject"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "project_id": project_id,
        "user_id": user_id
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}
    

def get_project_detail(token: str, project_id: int, user_id: int = 0) -> dict:
    """
    Gets detailed information of a specific project.
    
    Args:
        token: Bearer authentication token
        project_id: Target project's ID
        user_id: Logged in user's ID (0 for non-members)
        
    Returns:
        Dictionary with status and response data containing project details, research teams, and permissions
    """
    url = f"{KBRI_API_BASE_URL}/api/kbri/projects/getProjectDetail"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "project_id": project_id,
        "user_id": user_id
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return {"status": "success", "response": response.json()}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "response": str(e)}