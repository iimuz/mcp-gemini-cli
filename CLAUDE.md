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

- `.mise/tasks/`: Contains shell scripts for common development tasks
- `tests/`: Python tests directory
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