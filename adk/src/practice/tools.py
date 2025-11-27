import requests
from typing import Dict, Any, List
from .config import GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID

def google_search_tool(query: str) -> str:
    """Google Custom Search API를 사용한 웹 검색"""
    if not GOOGLE_API_KEY or not GOOGLE_SEARCH_ENGINE_ID:
        return "Error: Google API Key or Search Engine ID is missing."

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_SEARCH_ENGINE_ID,
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
            formatted_results += f"{i}. {title}\n   {snippet}\n   {link}\n\n"
            
        return formatted_results

    except requests.exceptions.RequestException as e:
        return f"Search error: {str(e)}"