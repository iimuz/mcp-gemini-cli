#!/usr/bin/env bash
#MISE description="Bump dependencies."

set -eu
set -o pipefail

mise up
npm install --include=dev cspell@latest dprint@latest prettier@latest
dprint config update
uv lock --upgrade
