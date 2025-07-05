#!/usr/bin/env bash
#MISE description="Setup this project."
#
# 環境構築を行うためのスクリプト。

set -eu
set -o pipefail

echo "setup project root directory"

npm ci
uv sync

