from src.deepseek_coding_agent_harness.tools.file_tools import list_files


for path in list_files("."):
    print(path)