import os


PROJECT_ROOT = "/Users/lverdiguel/Server/MCP/MCP_FASTMCP"

def _resolver_secure_path(relative_path: str) -> str:
    """Evita que se salga del priyecto con ../../ etc"""
    absolute_path = os.path.abspath(os.path.join(PROJECT_ROOT, relative_path ))
    
    if not absolute_path.startswith(PROJECT_ROOT):
        raise ValueError("Ruta fuera del proyecto permitido")
    return absolute_path

def list_files(sub_dir: str = "") -> list[str]:
    """Lista los archivos del proyecto"""
    base = _resolver_secure_path(sub_dir)
    result = []
    
    for root, _, files in os.walk(base):
        for f in files:
            result.append(os.path.relpath(os.path.join(root,f), PROJECT_ROOT))
    return result

def read_file_project(relative_path:str) -> str:
    path = _resolver_secure_path(relative_path)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()