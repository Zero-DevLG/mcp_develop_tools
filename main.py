from fastmcp import Client
from fastmcp.client.auth import OAuth
import asyncio

auth = OAuth(
    scopes=["user"],
    additional_client_metadata={"token_endpoint_auth_method": "none"}
    )

async def main():
    async with Client("https://mcp.notion.com/mcp", auth=auth) as client:
        tools = await client.list_tools()
        for tool in tools:
            print(f"-{tool.name}: {tool.description}")
            print(f" esquema: {tool.inputSchema}")
            
if __name__ == "__main__":
    mcp.run()