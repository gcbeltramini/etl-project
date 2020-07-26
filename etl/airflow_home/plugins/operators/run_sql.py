import os
from typing import Dict

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import (read_sql, AIRFLOW_CONNECTION_ID, CSV_Table, CSV_TABLES,
                     QUERIES_PATH, SCHEMA_NAME)


class SQLFileOperator(BaseOperator):
    ui_color = '#ededed'

    @apply_defaults
    def __init__(self,
                 query_file: str,
                 message: str,
                 queries_path: str = QUERIES_PATH,
                 schema_name: str = SCHEMA_NAME,
                 csv_tables: Dict[str, CSV_Table] = CSV_TABLES,
                 postgres_conn_id: str = AIRFLOW_CONNECTION_ID,
                 should_run: bool = True,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.query_file = query_file
        self.message = message
        self.queries_path = queries_path
        self.schema_name = schema_name
        self.csv_tables = csv_tables
        self.postgres_conn_id = postgres_conn_id
        self.should_run = should_run

    def execute(self, context):
        query_file = os.path.join(self.queries_path, self.query_file)
        self.log.info(f'{self.message:s} based on file "{query_file:s}"...')
        postgres = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        sql = read_sql(query_file,
                       schema_name=self.schema_name,
                       **{name: csv_table.table_name
                          for name, csv_table in self.csv_tables.items()})
        if self.should_run:
            postgres.run(sql=sql)
            self.log.info('Done!')
        else:
            self.log.info(sql)
            self.log.info('Skipping this task.')
