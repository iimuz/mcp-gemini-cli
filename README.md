# MCP Gemini CLI

A Model Context Protocol (MCP) server that provides a bridge to the Gemini CLI tool, allowing LLM applications to interact with Google's Gemini AI models through a standardized interface.

## Features

- **Call Gemini CLI**: Send prompts to Gemini with custom model selection
- **List Models**: Get available Gemini models
- **Error Handling**: Graceful handling of CLI tool availability
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
