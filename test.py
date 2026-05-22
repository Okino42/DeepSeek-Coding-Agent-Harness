from src.deepseek_coding_agent_harness.config import get_config
from src.deepseek_coding_agent_harness.core.llm_client import chat

config = get_config()
reply = chat(
    api_key=config["api_key"],
    base_url=config["base_url"],
    model=config["model"],
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello in one short sentence."}
    ],
)

print(reply)