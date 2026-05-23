from src.deepseek_coding_agent_harness.core.engine import parse_tool_command


tool_name, kwargs = parse_tool_command("/tool read_file path=README.md")

print(tool_name)
print(kwargs)