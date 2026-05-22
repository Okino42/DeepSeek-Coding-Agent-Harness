"""
Core engine for the DeepSeek Coding Agent Harness.
聊天状态和模型调用

"""
def create_initial_messages() -> list[dict]:
    return [
        {"role": "system", "content": "You are a helpful assistant."}
    ]