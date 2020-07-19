#!/usr/bin/env bash

set -euo pipefail

cur_dir=$(dirname "${BASH_SOURCE[0]}")

echo "Running 'shellcheck' (linter for shell files)..."
pushd "$cur_dir" 1>/dev/null || exit 1
find . -type f -name '*.sh' -exec shellcheck -x '{}' \;
popd 1>/dev/null || exit 1
echo "Done!"

echo "Running 'markdownlint-cli' (linter for Markdown files)..."
markdownlint .
echo "Done!"

echo "Running 'flake8' (linter for Python files)..."
flake8
echo "Done!"

echo "Running 'remark validate-links' (validates internal links in Markdown files)..."
remark --use validate-links --quiet --frail .
echo "Done!"
