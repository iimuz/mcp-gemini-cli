# Project Structure

## Main Directories

```
mcp-gemini-cli/
├── mcp_gemini_cli/          # Main Python package
│   ├── server.py            # FastMCP server implementation with tools
│   ├── __main__.py          # Entry point for module execution
│   └── __init__.py          # Package initialization
├── tests/                   # Python tests directory
├── memory-bank/             # Project documentation and context
├── .mise/tasks/             # Shell scripts for common development tasks
├── .github/                 # GitHub Actions workflows
├── .vscode/                 # VS Code configuration
└── .serena/                 # Serena MCP tool configuration
```

## Configuration Files

- `pyproject.toml`: Python project configuration and ruff settings
- `mise.toml`: Environment and tool management
- `dprint.json`: Formatting configuration for non-Python files
- `package.json`: Node.js dependencies for development tools
- `CLAUDE.md`: Project-specific guidance for Claude Code
- `.gitignore`: Git ignore patterns
- `.editorconfig`: Editor configuration
- `.cspell.json`: Spell checking configuration

## Task Scripts (.mise/tasks/)

- `setup.sh`: Initial project setup
- `format.sh`: Code formatting
- `lint.sh`: Code linting and spell checking
- `test.sh`: Run pytest tests
- `clean.sh`: Clean environment
- `update.sh`: Update dependencies

## Available Tools (MCP Server)

- `call_gemini(prompt, model)`: Send prompt to Gemini CLI
- `list_gemini_models()`: List available Gemini models
