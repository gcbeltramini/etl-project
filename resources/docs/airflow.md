# Airflow

## Set up and run the ETL locally

Run all scripts below from the project folder.

```bash
# Set Airflow home (default: ~/airflow)
base_dir="$(pwd)" # project folder
export AIRFLOW_HOME="${base_dir}/etl/airflow_home"

# Setup (run only once)
etl/scripts/setup_conda_env.sh
etl/scripts/setup_airflow.sh
# To remove the examples, when running 'airflow list_dags', set `load_examples = False` in
# '${AIRFLOW_HOME}/airflow.cfg'.

# Check Airflow setup
etl/scripts/airflow_check.sh

# Airflow UI
etl/scripts/airflow_ui.sh

# Scheduler (in another terminal):
etl/scripts/airflow_scheduler.sh
```

To open the Airflow UI, visit <localhost:8080> in the browser.

## PostgreSQL configuration

Add connect to PostgreSQL database:

1. <http://localhost:8080/> --> menu "Admin" --> "Connections"
1. Tab "Create":
   - Conn Id: "postgres_etl"
   - Conn Type: "Postgres"
   - Host: "localhost"
   - Schema: "etldb"
   - Login: "airflow_etl"
   - Password: "airflow_etl"
   - Port: 5432
1. "Save"
  
## Cleanup

1. Airflow files: run `etl/scripts/airflow_cleanup.sh`
1. `conda` environment: run `etl/scripts/conda_cleanup.sh`
