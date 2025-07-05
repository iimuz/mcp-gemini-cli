#!/usr/bin/env bash
#MISE description="Run all pytest tests in verbose mode"

set -eu
set -o pipefail

python -m pytest tests -v
