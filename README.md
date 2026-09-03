# mcp_develop_tools
Un repositorio de Model Context Protocol (MCP) que centraliza herramientas de desarrollo de software para potenciar la productividad mediante la integración de Notion, Lucid, Asana y el sistema de archivos local. Diseñado para optimizar los flujos de trabajo de ingeniería, facilita la generación automatizada de documentación técnica.

# Ejemplo de configuracion Claude 
{
  "mcpServers": {
    "company-db-server": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:3000/sse"
      ]
    },
    "mcp_server_notion": {
      "command": "/users/lverdiguel/Server/MCP/MCP_FASTMCP/.venv/bin/python",
      "args": [
        "/Users/lverdiguel/Server/MCP/MCP_FASTMCP/server.py"
      ]
    },
    "lucid": {
          "command": "npx",
          "args": ["-y", "mcp-remote", "https://mcp.lucid.app/mcp"]
        }
  },