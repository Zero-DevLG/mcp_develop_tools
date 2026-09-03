from contextlib import asynccontextmanager
from fastmcp import Client
from .auth import build_notion_auth

NOTION_MCP_URL = "https://mcp.notion.com/mcp"

@asynccontextmanager
async def notion_client():
    auth = build_notion_auth()
    async with Client(NOTION_MCP_URL, auth=auth) as client:
        yield client