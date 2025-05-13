import uvicorn
from fastmcp import FastMCP
from src.mcp.main import register_all

# Create an MCP server
mcp = FastMCP("Citadel")

# Register all MCP resources and tools
register_all(mcp)

# Get a Starlette app instance for Streamable HTTP transport (recommended)
http_app = mcp.http_app(path="/mcp")

if __name__ == "__main__":
    uvicorn.run(http_app, host="0.0.0.0", port=8000)
