#!/usr/bin/env bash

set -euxo pipefail

if [[ -z "$AIRFLOW_HOME" ]]; then
  echo "ERROR: 'AIRFLOW_HOME' is not set."
  exit 1
fi

echo "Removing Airflow files from '${AIRFLOW_HOME}'"
pushd "$AIRFLOW_HOME" 1>/dev/null || exit 1
rm airflow.cfg || :
rm airflow.db || :
rm unittests.cfg || :
rm -rf logs || :
popd 1>/dev/null || exit 1
echo "Done!"
