import requests


def build_chat_url(base_url: str) -> str:
    return base_url.rstrip("/") + "/chat/completions"


# Build HTTP request header.
def build_headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }


def build_payload(model: str, messages: list[dict]) -> dict:
    return {
        "model": model,
        "messages": messages,
        "temperature": 0.2,
    }


def chat(
    api_key: str,
    base_url: str,
    model: str,
    messages: list[dict],
) -> str:
    url = build_chat_url(base_url)
    headers = build_headers(api_key) # 构造认证信息
    payload = build_payload(model, messages)# 构造要发送给模型的json内容

    response = requests.post(url, headers=headers, json=payload, timeout=60) # 发送HTTP POST请求
    response.raise_for_status() # 如果响应状态码不是200-299，则抛出异常

    data = response.json()
    return data["choices"][0]["message"]["content"] # 从 DeepSeek 返回结果里取出模型回复文本