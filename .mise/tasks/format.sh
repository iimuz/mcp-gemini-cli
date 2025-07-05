#!/usr/bin/env bash
#MISE description="Format."

set -eu
set -o pipefail

echo "Format..."
uv run ruff format .
uv run ruff check --fix --exit-zero .
npx dprint fmt
npx prettier --write "**/*.{yml,yaml}"
