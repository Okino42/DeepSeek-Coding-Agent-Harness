"""
CLI entry point for terminal input and output.
"""
from .config import get_config
from .core.engine import (
    create_initial_messages,
    get_help_text,
    run_turn,
    should_clear,
    should_exit,
    should_show_help,
    is_empty_input,
    parse_tool_command,
    should_run_tool,
)
from .tools.registry import run_tool_text


def main() -> None:
    config = get_config()
    messages = create_initial_messages()

    while True:
        user_text = input("You> ")

        if is_empty_input(user_text):
            continue

        if should_exit(user_text):
            break
        
        if should_clear(user_text):
            messages = create_initial_messages()
            print("Chat history cleared.")
            continue
        
        if should_show_help(user_text):
            print(f"Assistant> {get_help_text()}")
            continue
        
        if should_run_tool(user_text):
            try:
                tool_name, kwargs = parse_tool_command(user_text)
                result = run_tool_text(tool_name, **kwargs)
                print(f"Tool> {result}")
            except Exception as error:
                print(f"Tool error> {error}")
            continue

        reply = run_turn(config, messages, user_text)

        print(f"Assistant> {reply}")


if __name__ == "__main__":
    main()