#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

enable_conda_in_script
conda activate base
conda install -n base nb_conda_kernels
conda activate "$CONDA_ENV_NAME"
python -m pip install -r resources/requirements/requirements_dev.txt
conda deactivate
