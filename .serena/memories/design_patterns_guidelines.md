# Design Patterns and Guidelines

## MCP Server Patterns

- Use `FastMCP` for simplified server implementation
- Decorate functions with `@mcp.tool()` to expose as MCP tools
- Always provide comprehensive docstrings for MCP tools
- Use async/await for all I/O operations

## Error Handling Patterns

- Graceful degradation when external tools (Gemini CLI) are unavailable
- Return descriptive error messages rather than raising exceptions
- Use try/except blocks for subprocess operations
- Set timeouts for external command execution (60 seconds default)

## Async Programming Guidelines

- Use `asyncio.create_subprocess_shell()` for external commands
- Always use `asyncio.wait_for()` with timeouts
- Handle subprocess communication properly with `communicate()`
- Check return codes and handle stderr appropriately

## Code Organization

- Keep tool implementations in `server.py`
- Separate concerns: server setup, tool definitions, utility functions
- Use type hints for all function parameters and return values
- Follow single responsibility principle for functions

## Testing Patterns

- Mock external dependencies (subprocess calls)
- Test both success and error conditions
- Use `@pytest.mark.asyncio` for async test functions
- Follow AAA pattern: Arrange, Act, Assert

## Documentation Standards

- Every public function must have a docstring
- Use clear, concise parameter descriptions
- Include usage examples where helpful
- Maintain README.md with current setup instructions

## Security Considerations

- Sanitize input when constructing shell commands
- Use subprocess with proper input/output handling
- Set `stdin=asyncio.subprocess.DEVNULL` to prevent hanging
- Validate external tool availability before use
