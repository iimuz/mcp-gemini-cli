"""MCP server for Gemini CLI integration."""

import asyncio
import os
import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Gemini CLI")


def _validate_custom_gemini_path(custom_path: str) -> str | None:
    """Validate custom Gemini CLI path.

    Returns error message if invalid, None if valid.
    """
    if not Path(custom_path).exists():
        return f"Error: Custom Gemini CLI path not found: {custom_path}"
    if not os.access(custom_path, os.X_OK):
        return f"Error: Custom Gemini CLI path is not executable: {custom_path}"
    return None


def _get_gemini_cwd() -> tuple[str | None, str | None]:
    """Get Gemini CLI working directory from environment variable.
    
    Returns (cwd, error) tuple.
    """
    custom_cwd = os.environ.get("GEMINI_CLI_CWD")
    if custom_cwd:
        if not Path(custom_cwd).exists():
            return None, f"Error: Custom working directory not found: {custom_cwd}"
        if not Path(custom_cwd).is_dir():
            return None, f"Error: Custom working directory is not a directory: {custom_cwd}"
        return custom_cwd, None
    return None, None


def _get_gemini_command() -> tuple[str, str | None]:
    """Get Gemini command and validation error if any. Returns (command, error)."""
    custom_gemini_path = os.environ.get("GEMINI_CLI_PATH")
    if custom_gemini_path:
        error = _validate_custom_gemini_path(custom_gemini_path)
        if error:
            return "", error
        return custom_gemini_path, None
    return "gemini", None


@mcp.tool()
async def call_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """Call Gemini CLI with the given prompt and model."""
    gemini_command, validation_error = _get_gemini_command()
    if validation_error:
        return validation_error

    gemini_cwd, cwd_error = _get_gemini_cwd()
    if cwd_error:
        return cwd_error

    gemini_cli_path = f'{gemini_command} -m {model} -p "{prompt}"'
    try:
        result = await asyncio.create_subprocess_shell(
            gemini_cli_path,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            stdin=asyncio.subprocess.DEVNULL,
            cwd=gemini_cwd,
        )
        stdout, stderr = await asyncio.wait_for(result.communicate(), timeout=60)

        if result.returncode != 0:
            return f"Error: {stderr.decode()}"

        return stdout.decode() if stdout else ""
    except FileNotFoundError:
        custom_path = os.environ.get("GEMINI_CLI_PATH")
        if custom_path:
            return f"Error: Custom Gemini CLI not found: {custom_path}"
        return "Error: Gemini CLI not found. Please install it first."
    except subprocess.SubprocessError as e:
        return f"Error: {e!s}"


@mcp.tool()
async def list_gemini_models() -> str:
    """List available Gemini models."""
    return "gemini-2.5-pro, gemini-2.5-flash"


if __name__ == "__main__":
    mcp.run(transport="stdio")
