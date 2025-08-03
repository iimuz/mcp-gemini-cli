# Code Style and Conventions

## Python Code Style

- **Formatter**: ruff (Black-compatible settings)
- **Line Length**: 88 characters
- **Indentation**: 4 spaces
- **Quote Style**: Double quotes for strings
- **Type Hints**: Full type annotations required throughout codebase
- **Docstrings**: Required for public functions and classes

## ruff Configuration

- **Enabled Rules**: `ALL` (comprehensive rule set)
- **Ignored Rules**:
  - `D203`, `D213`: Docstring formatting conflicts
  - `COM812`, `ISC001`: Formatter conflicts
  - `RUF003`: Japanese characters in comments allowed
- **Fixable**: All rules when using `--fix`

## File Formatting

- **Markdown/JSON/TOML**: dprint formatting
- **YAML**: prettier formatting
- **Spell Check**: cspell for all file types

## Naming Conventions

- **Functions/Variables**: snake_case
- **Classes**: PascalCase
- **Constants**: UPPER_SNAKE_CASE
- **Private Members**: Leading underscore

## Test Code Conventions

- **Location**: `tests/` directory
- **Framework**: pytest with pytest-asyncio
- **Naming**: `test_*.py` files, `test_*` functions
- **Async Tests**: Use `@pytest.mark.asyncio` decorator
- **Allowed in Tests**: Assert statements (`S101`), private member access (`SLF001`)
