# Tech Context: MCP Gemini CLI

## Technologies Used

### Core Technologies

- **Python 3.11+**: Required for modern async features
- **FastMCP**: MCP server framework (`mcp[cli]>=1.0.0`)
- **asyncio**: For non-blocking subprocess calls
- **subprocess**: For CLI interaction

### Development Tools

- **uv**: Python package manager (configured in mise.toml)
- **mise**: Environment and tool management
- **ruff**: Code linting and formatting
- **pytest**: Testing framework with async support
- **pytest-asyncio**: Async test support

### Development Setup

#### Environment Management

```bash
# Install mise for environment management
mise install
mise run setup    # Install dependencies
```

#### Package Management

```bash
# Install dependencies
uv sync

# Add new dependency
uv add package-name
```

#### Development Commands

```bash
# Format code
mise run format

# Lint code
mise run lint

# Run tests
mise run test

# Clean environment
mise run clean
```

## Technical Constraints

### Python Version

- **Minimum**: Python 3.11
- **Reason**: Required for modern async features and FastMCP

### Dependencies

- **Minimal**: Only `mcp[cli]` required
- **CLI Support**: `[cli]` extra for command-line features
- **Testing**: Development dependencies for testing

### External Dependencies

- **Gemini CLI**: Must be installed separately
- **PATH**: Gemini CLI must be in system PATH
- **Authentication**: Gemini CLI must be configured with API keys

## Tool Usage Patterns

### MCP Server Operations

```bash
# Development mode
python -m mcp_gemini_cli

# Via MCP CLI (alternative)
uv run mcp dev mcp_gemini_cli/server.py

# Install for Claude Desktop
uv run mcp install mcp_gemini_cli/server.py
```

### Testing Patterns

```python
# Async test with mocking
@pytest.mark.asyncio
async def test_function():
    with patch("asyncio.create_subprocess_exec") as mock:
        # Setup mock
        result = await function_under_test()
        # Assert results
```

## Project Structure

```
mcp-gemini-cli/
├── mcp_gemini_cli/          # Main package
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Entry point
│   └── server.py            # MCP server implementation
├── tests/                   # Test suite
│   └── test_server.py       # Server tests
├── memory-bank/             # Project documentation
├── pyproject.toml           # Python project configuration
├── mise.toml               # Environment configuration
└── CLAUDE.md               # Development guidance
```

## Configuration Files

### pyproject.toml

- Python project metadata
- Dependencies specification
- Tool configuration (ruff, pytest)
- Build system configuration

### mise.toml

- Environment management
- Development tasks
- Tool versions

## Performance Considerations

- **Async Operations**: Non-blocking CLI calls
- **Error Handling**: Fast failure with clear messages
- **Resource Usage**: Minimal memory footprint
- **Startup Time**: Fast server initialization
