#!/usr/bin/env bash

set -euo pipefail

cur_dir=$(dirname "${BASH_SOURCE[0]}")

echo "Running 'shellcheck'..."
pushd "$cur_dir" 1>/dev/null || exit 1
find . -type f -name '*.sh' -exec shellcheck -x '{}' \;
popd 1>/dev/null || exit 1
echo "Done!"

echo "Running 'markdownlint-cli'..."
markdownlint .
echo "Done!"

echo "Running 'flake8'..."
flake8
echo "Done!"
