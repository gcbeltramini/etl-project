#!/usr/bin/env bash

set -euo pipefail

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

if [[ -z "$CONDA_ENV_NAME" ]]; then
  echo "ERROR: 'CONDA_ENV_NAME' is not set."
  exit 1
fi

echo "Removing conda environment..."
enable_conda_in_script
conda activate "base"
conda env remove -n "$CONDA_ENV_NAME"
echo "Done!"
