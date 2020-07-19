#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

enable_conda_in_script
conda activate "$CONDA_ENV_NAME"

# Initialize the database
echo "Initializing the Airflow metadata database"
airflow initdb

conda deactivate

echo "Using AIRFLOW_HOME='${AIRFLOW_HOME}'"
