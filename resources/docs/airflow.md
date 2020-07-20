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

## Operators

Three different operators were created to:

1. create the tables;
1. copy the CSV data into the tables;
1. run checks on data quality.

### Create tables operator

This operator uses a SQL statement to remove the existing tables and create new ones in a PostgreSQL
database, whose connection parameters are defined on the Airflow connections properties.

### CSV to table operator

Operator that uses a SQL statement to copy the contents of a CSV file into the corresponding tables
created by the "create tables operator".

### Data quality operator

Operator to run checks on the data. It receives one or more SQL-based test cases along with the
expected results and executes the tests. For each test, the test result and expected result are
checked and, if there is no match, the operator raises an exception. For example, one can check the
minimum number of rows in a table or if there is any missing value in a specific column.
