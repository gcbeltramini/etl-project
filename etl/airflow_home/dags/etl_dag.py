from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from operators import (CreateTablesOperator, CSVToTableOperator,
                       DataQualityOperator)

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

quality_checks = {
    'airport_codes': {'minimum_rows': 55075,
                      'non_null_cols': ['ident', 'type', 'name', 'iso_region',
                                        'coordinates']},
    'global_temperatures': {'minimum_rows': 8599212,
                            'non_null_cols': ['dt', 'city', 'country',
                                              'latitude', 'longitude']},
    'us_cities': {'minimum_rows': 2891,
                  'non_null_cols': ['city', 'state', 'median_age',
                                    'total_population', 'state_code', 'race',
                                    'count']},
}

start_operator = DummyOperator(dag=dag, task_id='begin_execution')
end_operator = DummyOperator(dag=dag, task_id='stop_execution')

create_tables = CreateTablesOperator(dag=dag, task_id='create_tables')
copy_airport_codes_table = CSVToTableOperator(dag=dag,
                                              task_id='copy_airport_codes_table')  # noqa: E501
copy_global_temperatures_table = CSVToTableOperator(dag=dag,
                                                    task_id='copy_global_temperatures_table')  # noqa: E501
copy_us_cities_table = CSVToTableOperator(dag=dag,
                                          task_id='copy_us_cities_table')
quality_checks = DataQualityOperator(dag=dag, task_id='data_quality_checks',
                                     quality_checks=quality_checks)

(start_operator
 >> create_tables
 >> [copy_airport_codes_table,
     copy_global_temperatures_table,
     copy_us_cities_table]
 >> quality_checks
 >> end_operator)
