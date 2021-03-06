import os
from typing import Dict

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import (read_sql, AIRFLOW_CONNECTION_ID, CSV_Table, CSV_TABLES,
                     QUERIES_PATH, SCHEMA_NAME)


class CSVToTableOperator(BaseOperator):
    ui_color = '#ededed'

    @apply_defaults
    def __init__(self,
                 schema_name: str = SCHEMA_NAME,
                 csv_tables: Dict[str, CSV_Table] = CSV_TABLES,
                 queries_path: str = QUERIES_PATH,
                 query_file: str = 'copy_csv_data.sql',
                 postgres_conn_id: str = AIRFLOW_CONNECTION_ID,
                 should_run: bool = True,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        task_id = str(kwargs['task_id'])
        if task_id.startswith('copy_') and task_id.endswith('_table'):
            # len('copy_') = 5; len('_table') = 6
            self.table = task_id[5:-6]
        else:
            raise ValueError(f'Invalid task_id="{task_id}"')
        self.schema_name = schema_name
        self.csv_tables = csv_tables
        self.queries_path = queries_path
        self.query_file = query_file
        self.postgres_conn_id = postgres_conn_id
        self.should_run = should_run

    def execute(self, context):
        query_file = os.path.join(self.queries_path, self.query_file)
        self.log.info(f'Running query from file "{query_file:s}" into table '
                      f'"{self.schema_name:s}.{self.table}"...')
        postgres = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        csv_table = self.csv_tables[self.table]._asdict()
        for csv in csv_table['file_names']:
            sql = read_sql(query_file,
                           schema_name=self.schema_name,
                           **csv_table,
                           file_name=csv)
            if self.should_run:
                postgres.run(sql=sql)
                self.log.info('Done!')
            else:
                self.log.info(sql)
                self.log.info('Skipping this task.')
