# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an MCP (Model Context Protocol) server for calling Gemini CLI. The project uses Python for the main implementation and Node.js for development tooling.

## Environment Setup

- **Python**: 3.11
- **Node.js**: 22
- **Package Manager**: uv for Python dependencies, npm for Node.js dependencies
- **Environment Management**: mise (configured in `mise.toml`)

## Common Commands

### Setup

```bash
mise run setup  # Initial project setup (runs npm ci and uv sync)
```

### Development

```bash
mise run format  # Format code with ruff and dprint/prettier
mise run lint    # Lint Python, markdown, YAML files and spell check
mise run test    # Run pytest tests in verbose mode
```

### Maintenance

```bash
mise run clean   # Clean node_modules and .venv
mise run update  # Update dependencies
```

## Code Quality Tools

- **Python**: ruff (linting and formatting)
- **Markdown/JSON/TOML**: dprint
- **YAML**: prettier
- **Spell checking**: cspell
- **Testing**: pytest with pytest-asyncio

## Project Structure

- `mcp_gemini_cli/`: Main Python package containing the MCP server
  - `server.py`: FastMCP-based server implementation with tools
  - `__main__.py`: Entry point for module execution
  - `__init__.py`: Package initialization
- `tests/`: Python tests directory
- `memory-bank/`: Project documentation and context
- `.mise/tasks/`: Contains shell scripts for common development tasks
- Configuration files:
  - `pyproject.toml`: Python project configuration and ruff settings
  - `dprint.json`: Formatting configuration for non-Python files
  - `mise.toml`: Environment and tool management

## CI/CD

The project uses GitHub Actions for:

- Code formatting checks (dprint, prettier)
- Spell checking (cspell)
- Python linting (ruff)

## Development Notes

- Use `mise run` commands instead of direct tool invocation for consistency
- Python virtual environment is automatically managed by mise
- The project follows strict code quality standards with comprehensive linting

## Running the MCP Server

### Development Mode

```bash
# Run the server directly
python -m mcp_gemini_cli

# Or using the MCP CLI
uv run mcp dev mcp_gemini_cli/server.py
```

### Dependencies

- **External**: Requires Gemini CLI to be installed and configured
- **Python**: FastMCP framework (`mcp[cli]>=1.0.0`)

## Configuration

### Environment Variables

The server supports the following environment variables for customization:

#### GEMINI_CLI_PATH

Set a custom path to the Gemini CLI executable. Useful when Gemini CLI is installed in a non-standard location or when using multiple versions.

**MCP Client Configuration Example:**

```json
{
  "mcpServers": {
    "gemini": {
      "command": "python",
      "args": ["-m", "mcp_gemini_cli"],
      "env": {
        "GEMINI_CLI_PATH": "/custom/path/to/gemini"
      }
    }
  }
}
```

**Behavior:**

- If `GEMINI_CLI_PATH` is set: Uses the specified path to call Gemini CLI
- If not set: Uses default `gemini` command from system PATH
- Path validation: Checks if the specified path exists and is executable

**Error Handling:**

- Invalid path: Returns clear error message with the problematic path
- Non-executable: Returns error message indicating permission issues
- Not found: Distinguishes between custom path and default command errors

#### GEMINI_CLI_CWD

Set a custom working directory for Gemini CLI execution. Useful when running Gemini CLI in a specific project context or when relative paths are required.

**Behavior:**

- If `GEMINI_CLI_CWD` is set: Changes to the specified directory before executing Gemini CLI
- If not set: Uses the parent process's current working directory
- Path validation: Checks if the specified path exists and is a directory

**Error Handling:**

- Directory not found: Returns clear error message with the problematic path
- Not a directory: Returns error message indicating the path is not a directory

**Combined Configuration Example:**

```json
{
  "mcpServers": {
    "gemini": {
      "command": "python",
      "args": ["-m", "mcp_gemini_cli"],
      "env": {
        "GEMINI_CLI_PATH": "/path/to/gemini-wrapper.sh",
        "GEMINI_CLI_CWD": "/Users/username/projects/target-project"
      }
    }
  }
}
```

## Available Tools

The server provides two MCP tools:

- `call_gemini(prompt, model)`: Send a prompt to Gemini CLI with specified model
- `list_gemini_models()`: List available Gemini models
