"""MCP server for Gemini CLI integration."""

import asyncio
import subprocess

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Gemini CLI")


@mcp.tool()
async def call_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """Call Gemini CLI with the given prompt and model."""
    GEMINI_CLI_PATH = f"gemini -m {model} -p \"{prompt}\""
    try:
        result = await asyncio.create_subprocess_shell(
            GEMINI_CLI_PATH,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.DEVNULL,
        )
        stdout, stderr = await asyncio.wait_for(result.communicate(), timeout=60)

        if result.returncode != 0:
            return f"Error: {stderr.decode()}"

        return stdout.decode() if stdout else ''
    except FileNotFoundError:
        return "Error: Gemini CLI not found. Please install it first."
    except subprocess.SubprocessError as e:
        return f"Error: {e!s}"


@mcp.tool()
async def list_gemini_models() -> str:
    """List available Gemini models."""
    return "gemini-2.5-pro, gemini-2.5-flash"


if __name__ == "__main__":
    mcp.run(transport="stdio")
