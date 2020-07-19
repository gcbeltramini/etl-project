import os
from typing import Dict

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import (read_sql, AIRFLOW_CONNECTION_ID, CSV_Table, CSV_TABLES,
                     QUERIES_PATH, SCHEMA_NAME)


class CreateTablesOperator(BaseOperator):
    ui_color = '#ededed'

    @apply_defaults
    def __init__(self,
                 schema_name: str = SCHEMA_NAME,
                 csv_tables: Dict[str, CSV_Table] = CSV_TABLES,
                 queries_path: str = QUERIES_PATH,
                 query_file: str = 'create_table.sql',
                 postgres_conn_id: str = AIRFLOW_CONNECTION_ID,
                 *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.schema_name = schema_name
        self.csv_tables = csv_tables
        self.queries_path = queries_path
        self.query_file = query_file
        self.postgres_conn_id = postgres_conn_id

    def execute(self, context):
        query_file = os.path.join(self.queries_path, self.query_file)
        self.log.info(f'Creating tables based on file "{query_file:s}"...')
        postgres = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        postgres.run(sql=read_sql(query_file,
                                  schema_name=self.schema_name,
                                  **{k: v.table_name
                                     for k, v in self.csv_tables.items()}))
        self.log.info('Done!')
