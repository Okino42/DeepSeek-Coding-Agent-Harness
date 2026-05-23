"""
Core engine for the DeepSeek Coding Agent Harness.
聊天状态和模型调用

"""
from .llm_client import chat

def create_initial_messages() -> list[dict]:
    return [
        {"role": "system", "content": "You are a helpful assistant."}
    ]


# 输入：配置、历史消息、用户本轮输入
# 过程：追加 user 消息 -> 调模型 -> 追加 assistant 消息
# 输出：模型回复
def run_turn(config: dict, messages: list[dict], user_text: str) -> str:
    messages.append({"role": "user", "content": user_text})
    
    reply = chat(
        api_key=config["api_key"],
        base_url=config["base_url"],
        model=config["model"],
        messages=messages,
    )

    messages.append({"role": "assistant", "content": reply})
    return reply


def should_exit(user_text: str) -> bool:
    return user_text.strip() == "exit"


def should_clear(user_text: str) -> bool:
    return user_text.strip() == "/clear"


def should_show_help(user_text: str) -> bool:
    return user_text.strip() == "/help"


def get_help_text() -> str:
    return (
        "commands:\n"
        "  exit\n"
        "  /clear\n"
        "  /help\n"
        "  /tool read_file path=README.md\n"
        "  /tool search_text query=get_config"
    )


def is_empty_input(user_text: str) -> bool:
    return user_text.strip() == ""


def should_run_tool(user_text: str) -> bool:
    return user_text.strip().startswith("/tool ")


def parse_tool_command(user_text: str) -> tuple[str, dict]:
    text = user_text.strip()
    parts = text.split()

    if len(parts) < 2:
        raise ValueError("Usage: /tool <name> key=value")

    tool_name = parts[1]
    kwargs = {}

    for part in parts[2:]:
        if "=" not in part:
            raise ValueError(f"Invalid tool argument: {part}")
        key, value = part.split("=", 1)
        kwargs[key] = value

    return tool_name, kwargs