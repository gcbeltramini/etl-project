#!/usr/bin/env bash

cur_dir=$(dirname "${BASH_SOURCE[0]}")
# shellcheck source=./utils.sh
source "${cur_dir}/utils.sh"

# List the DAGs
if [[ -z "$AIRFLOW_HOME" ]]; then
  echo "ERROR: 'AIRFLOW_HOME' not set."
  exit 1
else
  echo "Using AIRFLOW_HOME='${AIRFLOW_HOME}'"
fi

enable_conda_in_script
conda activate "$CONDA_ENV_NAME"

# Check if nothing is wrong (there should be no error message)
if ! python -m "etl.airflow_home.dags.etl_dag"; then
  echo "Something went wrong."
  exit 1
fi

echo "Listing all the DAGs"
airflow list_dags
# To remove the examples, set `load_examples = False` in `${AIRFLOW_HOME}/airflow.cfg`.

conda deactivate

echo "Your DAG should appear in the list above."
