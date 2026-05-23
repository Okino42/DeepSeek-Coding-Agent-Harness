from pathlib import Path


def read_file(path: str) -> str:
    file_path = Path(path)

    if not file_path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
    
    return file_path.read_text(encoding="utf-8")


def write_file(path: str, content: str) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding="utf-8")


# 列出项目文件，并避开 .env/tmp/.git 等
def list_files(path: str = ".") -> list[str]:
    root = Path(path)

    if not root.is_dir():
        raise NotADirectoryError(f"Directory not found: {path}")
    
    ignored_parts = {".git", "__pycache__", ".pytest_cache", ".venv", "venv", "tmp"}
    ignored_names = {".env"}

    return [
        str(file_path)
        for file_path in root.rglob("*")
        if file_path.is_file()
        and file_path.name not in ignored_names
        and not any(part in ignored_parts for part in file_path.parts)
    ]


def search_text(query: str, path: str = ".") -> list[dict]:
    query = query.strip()

    if query == "":
        return []
    results = []

    for file_path in list_files(path):
        content = read_file(file_path)

        for line_number, line in enumerate(content.splitlines(), start=1):
            if query in line:
                results.append(
                    {
                        "file": file_path,
                        "line_number": line_number,
                        "text": line,
                    }
                )

    return results