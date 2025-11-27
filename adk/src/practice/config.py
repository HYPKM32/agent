import os
from dotenv import load_dotenv

load_dotenv()

# 공통 설정
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL")
MODEL_NAME = os.getenv("ADK_MODEL", "llama3")
PROVIDER = os.getenv("PROVIDER", "ollama")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")
ROOT_INSTRUCTION = os.getenv("ROOT_INSTRUCTION")