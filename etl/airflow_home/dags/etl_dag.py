# flake8: noqa

from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators import (SQLFileOperator, CSVToTableOperator,
                       DataQualityOperator)

should_run = True  # use False for debugging

default_args_dag = {
    'owner': 'etl-data-pipelines',
    'start_date': datetime(2020, 7, 17),
    # 'depends_on_past': False,
    # 'retries': 3,
    # 'retry_delay': timedelta(minutes=5),
    # 'catchup': False,
    # 'email_on_retry': False,
}

dag = DAG(
    dag_id='etl_dag',
    default_args=default_args_dag,
    description='Load and transform data in PostgreSQL with Airflow',
    schedule_interval=None,
)

# table name -> checks
quality_checks = {
    'immigration': {'minimum_rows': 40790529,
                    'non_null_cols': ['cicid', 'i94yr', 'i94mon', 'i94res',
                                      'i94port', 'arrdate', 'i94visa', 'count',
                                      'admnum', 'visatype'],
                    'adhoc': [
                        {'query': "SELECT COUNT(*) FROM {table:s} WHERE gender NOT IN ('F', 'M', 'U', 'X');",
                         'comparison': '=', 'value': 0},
                        {'query': 'SELECT COUNT(*) FROM {table:s} WHERE biryear > i94yr;',
                         'comparison': '<=', 'value': 10},
                        {'query': 'SELECT COUNT(*) FROM {table:s} WHERE depdate < 0;',
                         'comparison': '<=', 'value': 52},
                        {'query': 'SELECT COUNT(*) FROM {table:s} WHERE i94bir != i94yr - biryear;',
                         'comparison': '=', 'value': 0},
                    ]},
    'airport_codes': {'minimum_rows': 55075,
                      'non_null_cols': ['ident', 'type', 'name', 'iso_region',
                                        'coordinates']},
    'global_temperatures': {'minimum_rows': 8599212,
                            'non_null_cols': ['dt', 'city', 'country',
                                              'latitude', 'longitude'],
                            'adhoc': [
                                {'query': "SELECT COUNT(*) AS day FROM {table:s} WHERE DATE_PART('DAY', dt) != 1;",
                                 'comparison': '=', 'value': 0},
                            ]},
    'us_cities': {'minimum_rows': 2891,
                  'non_null_cols': ['city', 'state', 'median_age',
                                    'total_population', 'state_code', 'race',
                                    'count'],
                  'adhoc': [
                      {'query': ('SELECT COUNT(*)\n'
                                 'FROM {table:s}\n'
                                 'WHERE\n'
                                 '  male_population + female_population != total_population\n'
                                 '  OR number_of_veterans > total_population\n'
                                 '  OR foreign_born >= total_population;'),
                       'comparison': '=', 'value': 0},
                      {'query': ('SELECT COUNT(*) FROM (\n'
                                 '  SELECT city, state\n'
                                 '  FROM {table:s}\n'
                                 '  GROUP BY 1, 2\n'
                                 '  HAVING SUM("count") < MIN(total_population)) AS race_sum;'),
                       'comparison': '<=', 'value': 7},
                  ]},
}

start_operator = DummyOperator(dag=dag, task_id='begin_execution')
end_operator = DummyOperator(dag=dag, task_id='stop_execution')

drop_tables = SQLFileOperator(dag=dag, task_id='drop_tables',
                              query_file='drop_tables.sql',
                              message='Dropping tables',
                              should_run=should_run)
create_tables = SQLFileOperator(dag=dag, task_id='create_tables',
                                query_file='create_tables.sql',
                                message='Creating tables',
                                should_run=should_run)

copy_immigration_table = CSVToTableOperator(dag=dag,
                                            task_id='copy_immigration_table',
                                            should_run=should_run)
copy_airport_codes_table = CSVToTableOperator(dag=dag,
                                              task_id='copy_airport_codes_table',
                                              should_run=should_run)
copy_global_temperatures_table = CSVToTableOperator(dag=dag,
                                                    task_id='copy_global_temperatures_table',
                                                    should_run=should_run)
copy_us_cities_table = CSVToTableOperator(dag=dag,
                                          task_id='copy_us_cities_table',
                                          should_run=should_run)
quality_checks_task = DataQualityOperator(dag=dag,
                                          task_id='data_quality_checks',
                                          quality_checks=quality_checks,
                                          should_run=should_run)

(start_operator
 >> drop_tables
 >> create_tables
 >> [copy_immigration_table,
     copy_airport_codes_table,
     copy_global_temperatures_table,
     copy_us_cities_table]
 >> quality_checks_task
 >> end_operator)
