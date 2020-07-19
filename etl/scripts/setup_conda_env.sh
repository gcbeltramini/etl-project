#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

# Create conda environment
echo "Creating conda environment '${CONDA_ENV_NAME}'"
conda create -yn "$CONDA_ENV_NAME" python=3.6
enable_conda_in_script
conda activate "$CONDA_ENV_NAME"

# Install
python -m pip install -r resources/requirements/requirements.txt
echo "Done!"

conda deactivate
