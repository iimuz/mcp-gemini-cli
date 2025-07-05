#!/usr/bin/env bash
#MISE description="Lint."

set -eu
set -o pipefail

echo "Lint Python files..."
uv run ruff check .

echo "Lint markdown files..."
npx dprint check

echo "Lint yaml files..."
npx prettier --check '**/*.{yml,yaml}'

echo "Check spell..."
npx cspell lint . --no-progress
