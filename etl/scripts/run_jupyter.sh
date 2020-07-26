#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

if [[ -n "${AIRFLOW_HOME}" ]]; then
  echo "Using AIRFLOW_HOME='${AIRFLOW_HOME}'"
else
  echo "Please define the environment variable 'AIRFLOW_HOME'"
  exit 1
fi

enable_conda_in_script
conda activate "$CONDA_ENV_NAME"
jupyter notebook
conda deactivate
