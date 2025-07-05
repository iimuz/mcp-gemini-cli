# Project Brief: MCP Gemini CLI

## Project Overview

This project implements a Model Context Protocol (MCP) server that provides a bridge to the Gemini CLI tool. It allows LLM applications to interact with Google's Gemini AI models through a standardized MCP interface.

## Core Requirements

- **Primary Goal**: Create a minimal, functional MCP server that can call Gemini CLI
- **Key Features**:
  - Call Gemini CLI with custom prompts and model selection
  - List available Gemini models
  - Proper error handling for CLI tool not found scenarios
  - Async implementation for better performance

## Technical Constraints

- Python 3.11+ required
- Uses FastMCP framework for simplicity
- Minimal dependencies (only `mcp[cli]`)
- Follow existing project conventions (ruff, pytest, etc.)

## Success Criteria

- Server can be started via `python -m mcp_gemini_cli`
- Two functional tools: `call_gemini` and `list_gemini_models`
- Proper error handling and user feedback
- Basic test coverage
- Clean, maintainable code structure

## Architecture Decisions

- **FastMCP**: Chosen for simplicity and quick development
- **Async subprocess**: For non-blocking CLI calls
- **Package structure**: Standard Python package with `__main__.py` entry point
- **Testing**: pytest with async support and mocking
