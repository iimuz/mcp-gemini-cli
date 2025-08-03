# Session Details: Environment Variable Support Enhancement

**Date**: 2025-08-02\
**Status**: Completed ✅\
**Session Type**: Feature Enhancement

## Objective

Add environment variable support to the MCP Gemini CLI server to allow users to specify custom Gemini CLI paths via the `GEMINI_CLI_PATH` environment variable in MCP client configuration.

## Context

### Current Implementation

- The server currently uses hardcoded `gemini` command in subprocess calls
- Assumes Gemini CLI is available in the system PATH
- No way to specify custom installation paths for Gemini CLI

### User Request

User wants to configure MCP server to call Gemini CLI from a specific path using environment variables in the MCP client configuration.

## Design Decisions

### Environment Variable Approach

- **Variable Name**: `GEMINI_CLI_PATH`
- **Behavior**:
  - If set: Use the specified path to call Gemini CLI
  - If not set: Fall back to default `gemini` command (current behavior)
- **Validation**: Check if the specified path exists and is executable

### Implementation Strategy

1. **Modify `call_gemini` function**:
   - Read `GEMINI_CLI_PATH` environment variable using `os.environ.get()`
   - Construct command path based on environment variable or default
   - Maintain backward compatibility with existing installations

2. **Error Handling Enhancement**:
   - Add path existence validation for custom paths
   - Provide clear error messages for invalid paths
   - Distinguish between "CLI not found" and "custom path invalid"

3. **Client Configuration**:
   - Document how to set environment variables in MCP client settings
   - Provide examples for common MCP clients (Claude Desktop, etc.)

## Technical Implementation

### Code Changes

#### Server Modification (`mcp_gemini_cli/server.py`)

```python
import os
import shutil

@mcp.tool()
async def call_gemini(prompt: str, model: str = "gemini-2.5-flash") -> str:
    """Call Gemini CLI with the given prompt and model."""
    # Get custom path from environment variable
    custom_gemini_path = os.environ.get("GEMINI_CLI_PATH")
    
    if custom_gemini_path:
        # Use custom path, validate it exists
        if not os.path.exists(custom_gemini_path):
            return f"Error: Custom Gemini CLI path not found: {custom_gemini_path}"
        if not os.access(custom_gemini_path, os.X_OK):
            return f"Error: Custom Gemini CLI path is not executable: {custom_gemini_path}"
        gemini_command = custom_gemini_path
    else:
        # Use default command from PATH
        gemini_command = "gemini"
    
    gemini_cli_path = f'{gemini_command} -m {model} -p "{prompt}"'
    
    # Rest of the function remains the same...
```

#### Client Configuration Example

```json
{
  "mcpServers": {
    "gemini": {
      "command": "python",
      "args": ["-m", "mcp_gemini_cli"],
      "env": {
        "GEMINI_CLI_PATH": "/custom/path/to/gemini"
      }
    }
  }
}
```

### Backward Compatibility

- **Existing Users**: No changes required, current behavior preserved
- **New Users**: Can optionally set environment variable for custom paths
- **Migration**: Zero migration needed, purely additive feature

## Testing Strategy

### Test Cases to Add

1. **Default Behavior**: Test that existing functionality works unchanged
2. **Valid Custom Path**: Test with valid custom Gemini CLI path
3. **Invalid Custom Path**: Test error handling for non-existent paths
4. **Non-executable Path**: Test error handling for non-executable files
5. **Environment Variable Priority**: Verify custom path takes precedence

### Test Implementation

```python
@pytest.mark.asyncio
async def test_call_gemini_with_custom_path(monkeypatch):
    """Test call_gemini with custom GEMINI_CLI_PATH"""
    # Mock environment variable
    monkeypatch.setenv("GEMINI_CLI_PATH", "/usr/local/bin/gemini")
    
    # Mock subprocess and file system checks
    # Test implementation...
```

## Documentation Updates

### Files to Update

1. **CLAUDE.md**: Add environment variable configuration section
2. **Memory Bank**: Update tech context and active context
3. **README** (if exists): Add configuration examples

### Documentation Content

- Clear explanation of GEMINI_CLI_PATH usage
- MCP client configuration examples
- Troubleshooting guide for common path issues

## Benefits

1. **Flexibility**: Users can install Gemini CLI in custom locations
2. **Isolation**: Better support for containerized or virtual environments
3. **Multiple Versions**: Ability to use specific Gemini CLI versions
4. **Enterprise**: Support for enterprise environments with restricted PATH

## Risks and Mitigation

### Risks

- **Security**: Users might point to malicious executables
- **Compatibility**: Custom builds might have different CLI interfaces

### Mitigation

- **Path Validation**: Verify file exists and is executable
- **Clear Documentation**: Document requirements for custom Gemini CLI
- **Error Messages**: Provide clear feedback for configuration issues

## Success Criteria

1. **Functionality**: Environment variable properly read and used
2. **Compatibility**: Existing installations continue to work
3. **Error Handling**: Clear error messages for invalid configurations
4. **Documentation**: Comprehensive configuration guide
5. **Testing**: Full test coverage for new functionality

## Timeline

1. **Implementation**: Modify server code with environment variable support
2. **Testing**: Add comprehensive test coverage
3. **Documentation**: Update all relevant documentation
4. **Validation**: Test with real MCP client configurations

## Implementation Results ✅

### Successfully Completed

1. **Environment Variable Support**: `GEMINI_CLI_PATH` fully implemented and tested
2. **Path Validation**: Comprehensive validation for existence and executability
3. **Error Handling**: Clear, actionable error messages for all failure scenarios
4. **Testing**: Complete test coverage with 8 test cases covering all scenarios
5. **Documentation**: Updated CLAUDE.md with configuration examples and usage instructions
6. **Code Quality**: All lint checks pass, proper type annotations, clean code structure

### Final Implementation Features

- **Backward Compatibility**: Existing installations continue to work unchanged
- **Custom Path Support**: Users can specify any Gemini CLI installation path
- **Robust Validation**: File existence and permission checks before execution
- **Clear Error Messages**: Distinguishes between different failure types
- **Comprehensive Testing**: All scenarios covered including edge cases

### Validation Results

- **All Tests Pass**: 8/8 test cases successful
- **Lint Checks Pass**: Code meets quality standards
- **Functionality Verified**: Environment variable support works as designed
- **Documentation Complete**: Clear setup instructions and examples provided

## Additional Implementation: Working Directory Support

### GEMINI_CLI_CWD Environment Variable

After initial implementation, added support for custom working directory:

1. **New Environment Variable**: `GEMINI_CLI_CWD` for specifying execution directory
2. **Path Validation**: Directory existence and type validation
3. **Enhanced Testing**: Added 3 additional test cases for cwd functionality
4. **Documentation Update**: Extended CLAUDE.md with combined configuration examples

### Wrapper Script for mise Integration

Created solution for mise-managed Gemini CLI integration:

1. **Wrapper Script**: `gemini-wrapper.sh` that loads mise environment
2. **mise Integration**: `eval "$(mise activate bash)"` for proper environment loading
3. **Node.js Dependency Resolution**: Automatic PATH resolution for Node.js dependencies
4. **Universal Solution**: Works with any mise-managed tool configuration

### Final Configuration Example

```json
{
  "mcpServers": {
    "gemini": {
      "command": "python",
      "args": ["-m", "mcp_gemini_cli"],
      "env": {
        "GEMINI_CLI_PATH": "/path/to/gemini-wrapper.sh",
        "GEMINI_CLI_CWD": "/Users/username/projects/target-project"
      }
    }
  }
}
```

## Next Steps for Users

1. **Configuration**: Set both `GEMINI_CLI_PATH` and `GEMINI_CLI_CWD` in MCP client configuration
2. **Wrapper Script**: Use wrapper script for mise-managed installations
3. **Testing**: Verify custom path and working directory work with actual installations
4. **Deployment**: Ready for production use with enhanced flexibility and mise integration
