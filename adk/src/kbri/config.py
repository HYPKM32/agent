#/app/src/kbri/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ===========================================
# 기본 경로 설정
# ===========================================
BASE_DIR = Path(__file__).parent
INSTRUCTIONS_DIR = BASE_DIR / "instructions"

# ===========================================
# 공통 설정
# ===========================================
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL")
MODEL_NAME = os.getenv("ADK_MODEL", "llama3")
PROVIDER = os.getenv("PROVIDER", "ollama")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_SEARCH_ENGINE_ID = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

# ===========================================
# Instruction 로더
# ===========================================
def load_instruction(filename: str) -> str:
    """instructions 폴더에서 파일 로드"""
    file_path = INSTRUCTIONS_DIR / filename
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Instruction 파일을 찾을 수 없습니다: {file_path}")

# ===========================================
# Agent Instructions
# ===========================================
# Root Agent
ROOT_AGENT_INSTRUCTION_KO = load_instruction("root_agent_ko.md")
ROOT_AGENT_INSTRUCTION_EN = load_instruction("root_agent_en.md")

