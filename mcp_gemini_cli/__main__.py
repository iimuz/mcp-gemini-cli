"""MCP Gemini CLI Server Entry Point."""

from .server import mcp

if __name__ == "__main__":
    mcp.run()