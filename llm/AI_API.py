import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).parent / ".env"

# reload your AI_API_KEY
load_dotenv(dotenv_path=env_path)

"""
Function:Find the .env file in the same directory as this file.
"""

DASHSCOPE_API = os.getenv("DASHSCOPE")
