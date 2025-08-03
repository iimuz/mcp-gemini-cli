# MCP Gemini CLI

A Model Context Protocol (MCP) server that provides a bridge to the Gemini CLI tool, allowing LLM applications to interact with Google's Gemini AI models through a standardized interface.

## Features

- **Call Gemini CLI**: Send prompts to Gemini with custom model selection
- **List Models**: Get available Gemini models
- **Custom Path Support**: Configure custom Gemini CLI installation paths
- **Working Directory Control**: Set custom working directories for execution
- **mise Integration**: Full support for mise-managed Gemini CLI installations
- **Error Handling**: Graceful handling of CLI tool availability and path validation
- **Async Operations**: Non-blocking operations for better performance

## Installation

### Prerequisites

1. **Gemini CLI**: Install and configure the Gemini CLI tool

   ```bash
   # Follow Google's installation instructions for Gemini CLI
   # Ensure it's in your PATH and configured with API keys
   ```

2. **Python 3.11+**: Required for modern async features

### Setup

```bash
# Clone the repository
git clone https://github.com/iimuz/mcp-gemini-cli.git
cd mcp-gemini-cli

# Install dependencies
uv sync

# Or using pip
pip install -e .
```

## Usage

### Running the Server

```bash
# Run directly as a Python module
python -m mcp_gemini_cli

# Or using MCP CLI (development mode)
uv run mcp dev mcp_gemini_cli/server.py
```

### MCP Client Configuration

#### Claude Desktop Configuration

Add the following to your Claude Desktop configuration file:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "python",
      "args": ["-m", "mcp_gemini_cli"],
      "env": {
        "GEMINI_CLI_PATH": "/path/to/gemini",
        "GEMINI_CLI_CWD": "/path/to/working/directory"
      }
    }
  }
}
```

#### Environment Variables

The server supports the following environment variables for customization:

- **GEMINI_CLI_PATH** (optional): Custom path to Gemini CLI executable
  - If not set: Uses default `gemini` command from system PATH
  - If set: Uses the specified path (must exist and be executable)

- **GEMINI_CLI_CWD** (optional): Custom working directory for Gemini CLI execution
  - If not set: Uses the parent process's current working directory
  - If set: Changes to the specified directory before executing Gemini CLI

#### Configuration for mise-managed Gemini CLI

If you're using mise to manage your Gemini CLI installation, create a wrapper script:

1. Create `gemini-wrapper.sh`:

   ```bash
   #!/bin/bash
   eval "$(mise activate bash)"
   gemini "$@"
   ```

2. Make it executable:

   ```bash
   chmod +x gemini-wrapper.sh
   ```

3. Configure Claude Desktop:
   ```json
   {
     "mcpServers": {
       "gemini": {
         "command": "uv",
         "args": [
           "run",
           "--directory",
           "/absolute/path/to/mcp-gemini-cli",
           "--with",
           "mcp[cli]",
           "mcp",
           "run",
           "mcp_gemini_cli/server.py"
         ],
         "env": {
           "GEMINI_CLI_PATH": "/absolute/path/mcp-gemini-cli/gemini-wrapper.sh",
           "GEMINI_CLI_CWD": "/absolute/path/working/directory"
         }
       }
     }
   }
   ```

### Available Tools

The server provides two MCP tools:

#### `call_gemini(prompt, model)`

Send a prompt to Gemini CLI with the specified model.

**Parameters:**

- `prompt` (str): The text prompt to send to Gemini
- `model` (str, optional): The Gemini model to use (default: "gemini-1.5-flash")

**Returns:** The response from Gemini CLI

#### `list_gemini_models()`

List available Gemini models.

**Returns:** List of available models

## Development

### Setup Development Environment

```bash
# Install mise for environment management
mise install

# Setup project dependencies
mise run setup
```

### Common Commands

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

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=mcp_gemini_cli
```

## Architecture

The server is built using:

- **FastMCP**: Simplified MCP server framework
- **Async Design**: Non-blocking subprocess calls
- **Error Handling**: Comprehensive error management
- **Type Safety**: Full type annotations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

[Add your license information here]

## Requirements

- Python 3.11+
- Gemini CLI (external dependency)
- FastMCP (`mcp[cli]>=1.0.0`)
