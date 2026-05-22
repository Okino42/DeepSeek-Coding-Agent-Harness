"""
只负责输入输出和聊天状态管理，模型调用放在llm_client里
"""
from .config import get_config
from .core.llm_client import chat
from .core.engine import create_initial_messages


def main() -> None:
    config = get_config()
    messages = create_initial_messages()

    while True:
        user_text = input("You> ")

        if user_text == "exit":
            break
        
        if user_text == "/clear":
            messages = create_initial_messages()
            print("Chat history cleared.")
            continue

        messages.append({"role": "user", "content": user_text})

        reply = chat(
            api_key=config["api_key"],
            base_url=config["base_url"],
            model=config["model"],
            messages=messages,
        )

        print(f"Assistant> {reply}")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()