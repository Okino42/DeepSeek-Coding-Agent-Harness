import os
from dotenv import load_dotenv

load_dotenv()



def get_api_key() -> str | None:
    return os.getenv("DEEPSEEK_API_KEY")


def get_model() -> str:
    return os.getenv("DEEPSEEK_MODEL", "deepseek-chat")


def get_base_url() -> str:
    return os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")


def require_api_key() -> str:
    api_key = get_api_key()
    if api_key is None:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set.")
    return api_key


def get_config() -> dict:
    return {
        "api_key": require_api_key(),
        "model": get_model(),
        "base_url": get_base_url(),
    }