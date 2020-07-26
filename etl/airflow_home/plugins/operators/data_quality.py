import operator
from typing import Any, Callable, Dict, List

from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import AIRFLOW_CONNECTION_ID, SCHEMA_NAME


class DataQualityOperator(BaseOperator):
    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 quality_checks: Dict[str, Dict[str, Any]],
                 schema_name: str = SCHEMA_NAME,
                 postgres_conn_id: str = AIRFLOW_CONNECTION_ID,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quality_checks = quality_checks
        self.schema_name = schema_name
        self.postgres_conn_id = postgres_conn_id

    def check_result_not_empty(self, records: list, table: str) -> bool:
        contains_result = True
        if len(records) < 1 or len(records[0]) < 1:
            contains_result = False
            self.log.error('Data quality check failed: '
                           f'"{table:s}" returned no results.')
        return contains_result

    @staticmethod
    def str_to_op(op: str) -> Callable[[Any, Any], bool]:
        str_to_op_dict = {
            '<=': operator.le,
            '<': operator.lt,
            '>=': operator.ge,
            '>': operator.gt,
            '=': operator.eq,
            '!=': operator.ne,
        }
        if op not in str_to_op_dict:
            raise ValueError(f'Invalid operator "{op:s}"')
        return str_to_op_dict[op]

    def has_correct_value(self, table: str, sql: str, value: List[tuple],
                          comparison: str, postgres: PostgresHook) -> bool:
        has_error = False
        query = sql.format(table=table)
        self.log.info(f'Running query\n{query:s}')
        records = postgres.get_records(query)
        contains_result = self.check_result_not_empty(records, table)

        if not contains_result:
            has_error = True
            return has_error

        self.log.info(f'Result: {records}')

        comparison_op = self.str_to_op(comparison)
        msg = f'{records} {comparison:s} {value}'
        if comparison_op(records, value):
            self.log.info(f'Success: {msg:s}')
        else:
            has_error = True
            self.log.error(f'Expected: {msg:s}')
            return has_error

        return has_error

    def execute(self, context):
        self.log.info('Running data quality checks...')
        postgres = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        has_error = []
        for table, check in self.quality_checks.items():
            full_table_name = f'{self.schema_name:s}.{table:s}'

            if 'minimum_rows' in check:
                sql = 'SELECT COUNT(*) FROM {table:s};'
                not_ok = self.has_correct_value(full_table_name,
                                                sql,
                                                [(check['minimum_rows'],)],
                                                '>=',
                                                postgres)
                has_error.append(not_ok)

            if 'non_null_cols' in check:
                for col in check['non_null_cols']:
                    sql = (f'SELECT COUNT(*) FROM {{table:s}}\n'
                           f'WHERE {col:s} IS NULL;')
                    not_ok = self.has_correct_value(full_table_name,
                                                    sql, [(0,)], '=',
                                                    postgres)
                    has_error.append(not_ok)

        if any(has_error):
            raise ValueError('Data quality check failed. '
                             'Check the error log messages.')
        else:
            self.log.info('Data quality check finished successfully!')
