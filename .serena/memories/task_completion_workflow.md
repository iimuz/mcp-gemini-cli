# Task Completion Workflow

## When Any Task is Completed

Always run these commands in sequence to ensure code quality:

1. **Format Code**
   ```bash
   mise run format
   ```

2. **Lint and Check**
   ```bash
   mise run lint
   ```

3. **Run Tests**
   ```bash
   mise run test
   ```

## Code Quality Checks

The lint command performs:

- Python code linting with ruff
- Markdown/JSON/TOML formatting checks with dprint
- YAML formatting checks with prettier
- Spell checking with cspell

## Test Requirements

- All tests must pass before completing a task
- Tests are located in `tests/` directory
- Use pytest with async support for testing async functions
- Test coverage should be maintained

## Pre-commit Requirements

- All formatting must be applied
- All linting issues must be resolved
- All tests must pass
- No spelling errors allowed

## Error Handling

If any step fails:

1. Fix the reported issues
2. Re-run the failed step
3. Continue with remaining steps
4. Do not consider task complete until all steps pass

## CI/CD Integration

The project uses GitHub Actions that mirror these local checks:

- Code formatting validation
- Spell checking
- Python linting
- All checks must pass for pull requests
