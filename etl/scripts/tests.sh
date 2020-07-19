#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")

echo "Running 'shellcheck'..."
pushd "$cur_dir" 1>/dev/null || exit 1
find . -type f -name '*.sh' -exec shellcheck -x '{}' \;
popd 1>/dev/null || exit 1
echo "Done!"
