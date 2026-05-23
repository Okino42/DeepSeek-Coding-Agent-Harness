from typing import Callable

from .file_tools import list_files, read_file, search_text, write_file


def get_tools() -> dict:
    # 返回一个字典{工具名: 工具函数}，供 agent 调用
    return {
        "read_file": read_file,
        "write_file": write_file,
        "list_files": list_files,
        "search_text": search_text,
    }


# Callable：它表示“可调用对象”，也就是函数。
def get_tool(name: str) -> Callable:
    tools = get_tools()

    if name not in tools:
        raise KeyError(f"Unknown tool: {name}")
    
    return tools[name]


# object 表示它可能返回任意类型
def run_tool(name: str, **kwargs) -> object:
    tool = get_tool(name)
    return tool(**kwargs)


def format_tool_result(result: object) -> str:
    if result is None:
        return "Done."
    
    if isinstance(result, list):
        lines = []

        for item in result:
            if isinstance(item, dict) and {"file", "line_number", "text"} <= item.keys():
                lines.append(f"{item['file']}:{item['line_number']}: {item['text']}")
            else:
                lines.append(str(item))

        return "\n".join(lines)
    
    return str(result)


# 把“执行工具 + 格式化结果”合成一步。
def run_tool_text(name: str, **kwargs) -> str:
    result = run_tool(name, **kwargs)
    return format_tool_result(result)