"""Test cases for MCP Gemini CLI Server."""

from unittest.mock import ANY, AsyncMock, patch

import pytest

from mcp_gemini_cli.server import call_gemini, list_gemini_models


@pytest.mark.asyncio
async def test_call_gemini_success() -> None:
    """Test successful Gemini CLI call."""
    with patch("asyncio.create_subprocess_exec") as mock_subprocess:
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (b"Hello from Gemini", b"")
        mock_process.returncode = 0
        mock_subprocess.return_value = mock_process

        result = await call_gemini("Hello", "gemini-1.5-flash")

        assert result == "Hello from Gemini"
        mock_subprocess.assert_called_once_with(
            "gemini",
            "-m",
            "gemini-1.5-flash",
            "Hello",
            stdout=ANY,
            stderr=ANY,
        )


@pytest.mark.asyncio
async def test_call_gemini_error() -> None:
    """Test Gemini CLI call with error."""
    with patch("asyncio.create_subprocess_exec") as mock_subprocess:
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (b"", b"Error message")
        mock_process.returncode = 1
        mock_subprocess.return_value = mock_process

        result = await call_gemini("Hello")

        assert result == "Error: Error message"


@pytest.mark.asyncio
async def test_call_gemini_not_found() -> None:
    """Test Gemini CLI not found."""
    with patch("asyncio.create_subprocess_exec", side_effect=FileNotFoundError):
        result = await call_gemini("Hello")

        assert result == "Error: Gemini CLI not found. Please install it first."


@pytest.mark.asyncio
async def test_list_gemini_models_success() -> None:
    """Test successful model listing."""
    with patch("asyncio.create_subprocess_exec") as mock_subprocess:
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (
            b"gemini-1.5-flash\ngemini-1.5-pro",
            b"",
        )
        mock_process.returncode = 0
        mock_subprocess.return_value = mock_process

        result = await list_gemini_models()

        assert result == "gemini-1.5-flash\ngemini-1.5-pro"
        mock_subprocess.assert_called_once_with(
            "gemini",
            "models",
            stdout=ANY,
            stderr=ANY,
        )
