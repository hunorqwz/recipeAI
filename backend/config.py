import os
from dotenv import load_dotenv


def get_prompt():
    print(OLLAMA_SYSTEM_PROMPT_FILE)
    with open(OLLAMA_SYSTEM_PROMPT_FILE) as prompt_file:
        return prompt_file.read()


load_dotenv()

API_PREFIX = os.getenv('API_PREFIX')
API_PORT = int(os.getenv('API_PORT'))
API_HOST = os.getenv('API_HOST')
API_TITLE = os.getenv('API_TITLE')

API_SECURITY_CORS: str = os.getenv('API_SECURITY_CORS')

STATIC_FILES_DIRECTORY = os.getenv('STATIC_FILES_DIRECTORY')
STATIC_FILES = os.getenv('STATIC_FILES')

OLLAMA_MODEL: str = os.getenv('OLLAMA_MODEL')  # type: ignore
OLLAMA_SYSTEM_PROMPT_FILE: str = os.getenv('OLLAMA_SYSTEM_PROMPT_FILE')  # type: ignore
OLLAMA_SYSTEM_PROMPT = get_prompt()
