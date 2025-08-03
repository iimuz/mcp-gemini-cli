# Project Overview

## Purpose

MCP Gemini CLI is a Model Context Protocol (MCP) server that provides a bridge to the Gemini CLI tool, allowing LLM applications to interact with Google's Gemini AI models through a standardized interface.

## Key Features

- **Call Gemini CLI**: Send prompts to Gemini with custom model selection
- **List Models**: Get available Gemini models
- **Error Handling**: Graceful handling of CLI tool availability
- **Async Operations**: Non-blocking operations for better performance

## Target Use Case

This server acts as an intermediary between MCP-compatible applications and Google's Gemini CLI, enabling seamless integration of Gemini AI capabilities into various LLM workflows.

## Dependencies

- **External**: Requires Gemini CLI to be installed and configured on the system
- **Python**: FastMCP framework (`mcp[cli]>=1.0.0`)
- **Python Version**: 3.11+ (required for modern async features)
