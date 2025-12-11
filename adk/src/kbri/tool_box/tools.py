#/app/src/kbri/tool_box/tools.py
import requests
from ..config import GOOGLE_API_KEY, GOOGLE_SEARCH_ENGINE_ID


def google_search(query: str) -> str:
    """
    Performs a web search using the Google Custom Search API.
    
    Args:
        query: The search query string
        
    Returns:
        A formatted string containing the search results
    """
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
            formatted_results += f"{i}. Title: {title}\n   Snippet: {snippet}\n   Source: {link}\n\n"
            
        return formatted_results

    except requests.exceptions.RequestException as e:
        return f"Error during Google Search: {str(e)}"