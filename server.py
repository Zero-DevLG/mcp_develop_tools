from fastmcp import FastMCP
from integrations.notion.actions import create_page, search
from integrations.filessystem.actions import read_file_project, list_files 


mcp = FastMCP("MCP SERVER")

@mcp.tool
async def save_note_in_notion(title:str, content: str) -> dict:
    """Crea una página en Notion con el contenido dado."""
    return await create_page(title, content)

@mcp.tool
async def list_files_project(sub_dir: str) -> list[str]:
    """Lista los archivos del directorio"""
    return  list_files(sub_dir)


@mcp.tool
async def read_file(relative_path: str) -> str:
    """Lee el contenido completo de una archivo del proyecto, dada su ruta relativa."""
    try:
        return read_file_project(relative_path)
    except Exception as e:
        return f"Error al leer el archivo: {str(e)}"


if __name__ == "__main__":
    mcp.run()
    



