#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

enable_conda_in_script
conda activate "$CONDA_ENV_NAME"

# Start the scheduler
echo "Starting Airflow scheduler"
if [[ -n "${AIRFLOW_HOME}" ]]; then
  airflow scheduler
else
  echo "Please define the environment variable 'AIRFLOW_HOME'"
  exit 1
fi
