# System Patterns: MCP Gemini CLI

## Architecture Overview
The system follows a simple, layered architecture:

```
LLM Application
      ↓
  MCP Protocol
      ↓
  FastMCP Server
      ↓
  Subprocess Calls
      ↓
  Gemini CLI
```

## Key Technical Decisions

### FastMCP Framework
- **Why**: Simplifies MCP server creation with decorators
- **Pattern**: Use `@mcp.tool()` decorator for exposing functions
- **Benefits**: Automatic type inference, built-in error handling

### Async Subprocess Pattern
```python
result = await asyncio.create_subprocess_exec(
    "gemini", "-m", model, prompt,
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE,
)
```
- **Why**: Non-blocking CLI calls for better performance
- **Error Handling**: Separate stdout/stderr capture
- **Timeout**: Implicit timeout through asyncio

### Error Handling Strategy
1. **CLI Not Found**: `FileNotFoundError` → User-friendly message
2. **CLI Errors**: Non-zero return code → Return stderr content
3. **General Exceptions**: Catch-all for unexpected errors

## Component Relationships

### Core Components
- `server.py`: Main server implementation with tools
- `__main__.py`: Entry point for module execution
- `__init__.py`: Package initialization

### Tool Implementation Pattern
```python
@mcp.tool()
async def tool_name(param: type) -> str:
    """Tool description."""
    try:
        # Async subprocess call
        result = await asyncio.create_subprocess_exec(...)
        # Process result
        return processed_output
    except FileNotFoundError:
        return "Error: Tool not found message"
    except Exception as e:
        return f"Error: {str(e)}"
```

## Critical Implementation Paths

### Server Startup
1. Import FastMCP
2. Create server instance: `mcp = FastMCP("Gemini CLI")`
3. Define tools with decorators
4. Run server: `mcp.run()`

### Tool Execution
1. MCP client calls tool
2. FastMCP routes to decorated function
3. Function executes async subprocess
4. Result returned through MCP protocol

## Design Patterns

### Decorator Pattern
- Used for tool registration with `@mcp.tool()`
- Automatic type inference and validation
- Clean separation of concerns

### Error Wrapper Pattern
- Consistent error handling across all tools
- User-friendly error messages
- Graceful degradation when CLI unavailable