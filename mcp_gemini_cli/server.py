import asyncio
import subprocess
from typing import Any

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Gemini CLI")


@mcp.tool()
async def call_gemini(prompt: str, model: str = "gemini-1.5-flash") -> str:
    """Call Gemini CLI with the given prompt and model."""
    try:
        result = await asyncio.create_subprocess_exec(
            "gemini",
            "-m",
            model,
            prompt,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await result.communicate()
        
        if result.returncode != 0:
            return f"Error: {stderr.decode()}"
        
        return stdout.decode()
    except FileNotFoundError:
        return "Error: Gemini CLI not found. Please install it first."
    except Exception as e:
        return f"Error: {str(e)}"


@mcp.tool()
async def list_gemini_models() -> str:
    """List available Gemini models."""
    try:
        result = await asyncio.create_subprocess_exec(
            "gemini",
            "models",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await result.communicate()
        
        if result.returncode != 0:
            return f"Error: {stderr.decode()}"
        
        return stdout.decode()
    except FileNotFoundError:
        return "Error: Gemini CLI not found. Please install it first."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    mcp.run()