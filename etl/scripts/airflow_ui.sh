#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

enable_conda_in_script
conda activate "$CONDA_ENV_NAME"

# Start the web server, default port is 8080
echo "Starting Airflow UI"
if [[ -n "${AIRFLOW_HOME}" ]]; then
  airflow webserver -p 8080
else
  echo "Please define the environment variable 'AIRFLOW_HOME'"
  exit 1
fi
