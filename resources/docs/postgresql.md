# PostgreSQL

## Setup PostgreSQL database

Install PostgreSQL:

1. Install Homebrew (macOS): <http://brew.sh/>
1. Install PostgreSQL (macOS): `brew install postgresql`

Start service and create default user and database:

1. Start PostgreSQL with [homebrew-services](https://github.com/Homebrew/homebrew-services):
`brew services run postgresql`
    - Alternative: `pg_ctl -D /usr/local/var/postgres start`
    - `brew service start <service>` starts the `<service>` at login, while `brew services run` runs
    the `<service>` but doesn't start it at login (nor boot).
    - Check if it is running with `brew services list`
1. Connect to default PostgreSQL database and create user (must be superuser to `COPY` from a file):

    ```bash
    $ psql --dbname postgres
    postgres=# \du
    postgres=# CREATE ROLE airflow_etl WITH LOGIN CREATEDB SUPERUSER PASSWORD 'airflow_etl';
    postgres=# \du
    postgres=# \quit
    ```

1. Connect to default PostgreSQL database as the new user and create database and schema:

    ```bash
    $ psql --dbname postgres --username airflow_etl
    postgres=# \list
    postgres=# CREATE DATABASE etldb;
    postgres=# \list
    postgres=# GRANT ALL PRIVILEGES ON DATABASE etldb TO airflow_etl;
    postgres=# \list
    postgres=# \connect etldb
    etldb=# \dn
    etldb=# CREATE SCHEMA etl;
    etldb=# \dn
    etldb=# \quit
    ```

## Check schemas and tables, run queries

```bash
$ psql --dbname etldb --username airflow_etl
etldb=# \dn
etldb=# SHOW search_path;
etldb=# \dt
etldb=# \dt etl.*
etldb=# SET search_path TO etl;
etldb=# SHOW search_path;
etldb=# \dt
etldb=# \quit
```

## Cleanup

After everything is finished, and you want to remove all traces of the ETL:

1. Remove all tables (the `<schema_name>` is in `constants.py` --> `SCHEMA_NAME`):

    ```bash
    $ psql --dbname etldb
    sparkifydb=# \dn+
    sparkifydb=# DROP SCHEMA <schema_name> CASCADE;
    sparkifydb=# \dn+
    sparkifydb=# \quit
    ```

    Or remove the database and the user:

    ```bash
    $ psql --dbname postgres
    postgres=# \list
    postgres=# DROP DATABASE IF EXISTS etldb;
    postgres=# \list
    postgres=# \du
    postgres=# DROP USER airflow_etl;
    postgres=# \du
    postgres=# \quit
    ```

1. Stop the PostgreSQL service: `brew services stop postgresql`
    - Alternative: `pg_ctl -D /usr/local/var/postgres stop`
    - Check by listing all services managed by `brew services` (`postgresql` should be `stopped`):
    `brew services list`
