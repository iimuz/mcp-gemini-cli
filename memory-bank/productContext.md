# Product Context: MCP Gemini CLI

## Why This Project Exists
The Model Context Protocol (MCP) provides a standardized way for LLM applications to access external data and functionality. This project bridges the gap between MCP-enabled applications and Google's Gemini AI models by wrapping the Gemini CLI tool in an MCP server.

## Problems It Solves
- **CLI Integration**: Allows LLM applications to use Gemini CLI without direct command-line access
- **Standardization**: Provides a consistent MCP interface for Gemini interactions
- **Model Flexibility**: Supports different Gemini models (flash, pro, etc.)
- **Error Handling**: Gracefully handles CLI tool availability and execution errors

## How It Should Work
1. **Server Startup**: Start the MCP server with `python -m mcp_gemini_cli`
2. **Tool Usage**: LLM applications can call two main tools:
   - `call_gemini(prompt, model)`: Send a prompt to Gemini and get response
   - `list_gemini_models()`: Get available Gemini models
3. **Error Handling**: Clear error messages when Gemini CLI is not available
4. **Async Operation**: Non-blocking operation for better performance

## User Experience Goals
- **Simple Setup**: Minimal configuration required
- **Clear Errors**: Helpful error messages guide users to solutions
- **Flexible Usage**: Support for different Gemini models
- **Reliable Operation**: Robust error handling and recovery

## Integration Points
- **MCP Clients**: Any MCP-compatible LLM application
- **Gemini CLI**: Requires external Gemini CLI tool installation
- **FastMCP Framework**: Built on top of FastMCP for ease of development