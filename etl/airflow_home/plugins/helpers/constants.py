import os
from typing import NamedTuple, Optional


class CSV_Table(NamedTuple):
    table_name: str
    file_name: str
    delimiter_char: Optional[str] = ','


airflow_home = os.environ['AIRFLOW_HOME']
data_path = os.path.join(airflow_home, 'resources', 'data')
QUERIES_PATH = os.path.join(airflow_home, 'resources', 'sql')

AIRFLOW_CONNECTION_ID = 'postgres_etl'
SCHEMA_NAME = 'etl'
tables = [
    ('airport_codes', 'airport-codes.csv', {}),
    ('global_temperatures', 'GlobalLandTemperaturesByCity.csv', {}),
    ('us_cities', 'us-cities-demographics.csv', {'delimiter_char': ';'}),
]
CSV_TABLES = {tt[0]: CSV_Table(table_name=tt[0],
                               file_name=os.path.join(data_path, tt[1]),
                               **tt[2])
              for tt in tables}
