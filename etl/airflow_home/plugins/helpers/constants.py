import os
from typing import NamedTuple, Optional


class CSV_Table(NamedTuple):
    table_name: str
    file_name: str
    delimiter_char: Optional[str] = ','

airflow_home = os.environ['AIRFLOW_HOME']
data_path = os.path.join(airflow_home, 'resources', 'data')
QUERIES_PATH = os.path.join(airflow_home, 'resources', 'sql')
SCHEMA_NAME = 'etl'
CSV_TABLES = {
    'airport_codes': CSV_Table(table_name='airport_codes',
                               file_name=os.path.join(data_path,
                                                      'airport-codes.csv')),
    'global_temperatures': CSV_Table(table_name='global_temperatures',
                                     file_name=os.path.join(data_path,
                                                            'GlobalLandTemperaturesByCity.csv')),
    'us_cities': CSV_Table(table_name='us_cities',
                           file_name=os.path.join(data_path,
                                                  'us-cities-demographics.csv'),
                           delimiter_char=';'),
}
