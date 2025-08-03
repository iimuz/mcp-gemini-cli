"""Test cases for MCP Gemini CLI Server."""

from unittest.mock import ANY, AsyncMock, patch

import pytest

from mcp_gemini_cli.server import call_gemini, list_gemini_models


@pytest.mark.asyncio
async def test_call_gemini_success() -> None:
    """Test successful Gemini CLI call."""
    with patch("asyncio.create_subprocess_shell") as mock_subprocess:
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (b"Hello from Gemini", b"")
        mock_process.returncode = 0
        mock_subprocess.return_value = mock_process

        result = await call_gemini("Hello", "gemini-1.5-flash")

        assert result == "Hello from Gemini"
        mock_subprocess.assert_called_once_with(
            'gemini -m gemini-1.5-flash -p "Hello"',
            stdout=ANY,
            stderr=ANY,
            stdin=ANY,
            cwd=None,
        )


@pytest.mark.asyncio
async def test_call_gemini_error() -> None:
    """Test Gemini CLI call with error."""
    with patch("asyncio.create_subprocess_shell") as mock_subprocess:
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (b"", b"Error message")
        mock_process.returncode = 1
        mock_subprocess.return_value = mock_process

        result = await call_gemini("Hello")

        assert result == "Error: Error message"


@pytest.mark.asyncio
async def test_call_gemini_not_found() -> None:
    """Test Gemini CLI not found."""
    with patch("asyncio.create_subprocess_shell", side_effect=FileNotFoundError):
        result = await call_gemini("Hello")

        assert result == "Error: Gemini CLI not found. Please install it first."


@pytest.mark.asyncio
async def test_list_gemini_models_success() -> None:
    """Test successful model listing."""
    result = await list_gemini_models()
    assert result == "gemini-2.5-pro, gemini-2.5-flash"


@pytest.mark.asyncio
async def test_call_gemini_with_custom_path_success(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with custom GEMINI_CLI_PATH."""
    # Set environment variable
    monkeypatch.setenv("GEMINI_CLI_PATH", "/custom/path/to/gemini")

    # Mock file system checks
    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("os.access", return_value=True),
        patch("asyncio.create_subprocess_shell") as mock_subprocess,
    ):
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (b"Custom Gemini response", b"")
        mock_process.returncode = 0
        mock_subprocess.return_value = mock_process

        result = await call_gemini("Hello", "gemini-2.5-flash")

        assert result == "Custom Gemini response"
        mock_subprocess.assert_called_once_with(
            '/custom/path/to/gemini -m gemini-2.5-flash -p "Hello"',
            stdout=ANY,
            stderr=ANY,
            stdin=ANY,
            cwd=None,
        )


@pytest.mark.asyncio
async def test_call_gemini_custom_path_not_found(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with non-existent custom path."""
    monkeypatch.setenv("GEMINI_CLI_PATH", "/nonexistent/path/to/gemini")

    with patch("pathlib.Path.exists", return_value=False):
        result = await call_gemini("Hello")

        assert (
            result
            == "Error: Custom Gemini CLI path not found: /nonexistent/path/to/gemini"
        )


@pytest.mark.asyncio
async def test_call_gemini_custom_path_not_executable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with non-executable custom path."""
    monkeypatch.setenv("GEMINI_CLI_PATH", "/path/to/non-executable")

    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("os.access", return_value=False),
    ):
        result = await call_gemini("Hello")

        msg = "Error: Custom Gemini CLI path is not executable: /path/to/non-executable"
        assert result == msg


@pytest.mark.asyncio
async def test_call_gemini_custom_path_not_found_subprocess_error(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with custom path that fails at subprocess level."""
    monkeypatch.setenv("GEMINI_CLI_PATH", "/custom/path/to/gemini")

    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("os.access", return_value=True),
        patch("asyncio.create_subprocess_shell", side_effect=FileNotFoundError),
    ):
        result = await call_gemini("Hello")

        assert result == "Error: Custom Gemini CLI not found: /custom/path/to/gemini"


@pytest.mark.asyncio
async def test_call_gemini_with_custom_cwd_success(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with custom GEMINI_CLI_CWD."""
    monkeypatch.setenv("GEMINI_CLI_CWD", "/custom/working/directory")

    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("pathlib.Path.is_dir", return_value=True),
        patch("asyncio.create_subprocess_shell") as mock_subprocess,
    ):
        mock_process = AsyncMock()
        mock_process.communicate.return_value = (b"Response from custom cwd", b"")
        mock_process.returncode = 0
        mock_subprocess.return_value = mock_process

        result = await call_gemini("Hello", "gemini-2.5-flash")

        assert result == "Response from custom cwd"
        mock_subprocess.assert_called_once_with(
            'gemini -m gemini-2.5-flash -p "Hello"',
            stdout=ANY,
            stderr=ANY,
            stdin=ANY,
            cwd="/custom/working/directory",
        )


@pytest.mark.asyncio
async def test_call_gemini_custom_cwd_not_found(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with non-existent custom working directory."""
    monkeypatch.setenv("GEMINI_CLI_CWD", "/nonexistent/directory")

    with patch("pathlib.Path.exists", return_value=False):
        result = await call_gemini("Hello")

        expected_msg = (
            "Error: Custom working directory not found: /nonexistent/directory"
        )
        assert result == expected_msg


@pytest.mark.asyncio
async def test_call_gemini_custom_cwd_not_directory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Test call_gemini with custom cwd that is not a directory."""
    monkeypatch.setenv("GEMINI_CLI_CWD", "/path/to/file.txt")

    with (
        patch("pathlib.Path.exists", return_value=True),
        patch("pathlib.Path.is_dir", return_value=False),
    ):
        result = await call_gemini("Hello")

        expected_msg = (
            "Error: Custom working directory is not a directory: /path/to/file.txt"
        )
        assert result == expected_msg
