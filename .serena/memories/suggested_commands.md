# Suggested Commands

## Development Setup

```bash
# Initial project setup
mise run setup

# Install mise for environment management
mise install
```

## Daily Development Commands

```bash
# Format all code
mise run format

# Lint all code and check spelling
mise run lint

# Run tests
mise run test

# Clean environment
mise run clean

# Update dependencies
mise run update
```

## Running the Server

```bash
# Run server directly as Python module
python -m mcp_gemini_cli

# Run using MCP CLI (development mode)
uv run mcp dev mcp_gemini_cli/server.py
```

## Manual Tool Commands (when mise is not available)

```bash
# Python formatting and linting
uv run ruff format .
uv run ruff check --fix --exit-zero .

# Non-Python file formatting
npx dprint fmt
npx prettier --write "**/*.{yml,yaml}"

# Linting
uv run ruff check .
npx dprint check
npx prettier --check '**/*.{yml,yaml}'
npx cspell lint . --no-progress

# Testing
python -m pytest tests -v
```

## System Commands (macOS/Darwin)

- `ls`, `cd`, `grep`, `find`: Standard Unix commands
- `git`: Version control operations
- `which`: Find command locations
- `open`: Open files/directories in Finder
