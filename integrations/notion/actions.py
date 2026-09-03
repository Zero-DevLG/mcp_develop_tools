from .client import notion_client

async def create_page(title: str, markdown_content:str) -> dict:
    async with notion_client() as client:
        response = await client.call_tool(
            "notion-create-pages",
            {"pages": [{"properties": {"title": title}, "content": markdown_content}]},
        )
        if response.is_error:
            raise RuntimeError(f"Notion rechazó la operación: {response.content}")
        return response.content
    
async def search(query: str) -> list:
    async with notion_client() as client:
        response = await client.call_tool("notion-search", {"query": query})

        return response.content