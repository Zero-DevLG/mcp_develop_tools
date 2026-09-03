from fastmcp.client.auth import OAuth
from config import NOTION_SCOPES

def build_notion_auth() -> OAuth:
    return OAuth(
        scopes=NOTION_SCOPES,
        additional_client_metadata={"token_endpoint_auth_method": "none"}
    )