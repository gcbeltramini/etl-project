import os
from typing import List, NamedTuple, Optional


class CSV_Table(NamedTuple):
    table_name: str
    file_names: List[str]
    delimiter_char: Optional[str] = ','


airflow_home = os.environ['AIRFLOW_HOME']
data_path = os.path.join(airflow_home, 'resources', 'data')
QUERIES_PATH = os.path.join(airflow_home, 'resources', 'sql')

AIRFLOW_CONNECTION_ID = 'postgres_etl'
SCHEMA_NAME = 'etl'
immigration_csv_file_names = (
    'i94_jan16_sub.csv',
    'i94_feb16_sub.csv',
    'i94_mar16_sub.csv',
    'i94_apr16_sub.csv',
    'i94_may16_sub.csv',
    'i94_jun16_sub.csv',
    'i94_jul16_sub.csv',
    'i94_aug16_sub.csv',
    'i94_sep16_sub.csv',
    'i94_oct16_sub.csv',
    'i94_nov16_sub.csv',
    'i94_dec16_sub.csv',
)  # it takes ~20 seconds to load each file, so doing serially is not so bad
tables = [
    ('immigration',
     [os.path.join('18-83510-I94-Data-2016', 'csv', f)
      for f in immigration_csv_file_names],
     {}),
    ('airport_codes', ['airport-codes.csv'], {}),
    ('global_temperatures', ['GlobalLandTemperaturesByCity.csv'], {}),
    ('us_cities', ['us-cities-demographics.csv'], {'delimiter_char': ';'}),
]


def build_path(fname: List[str]) -> List[str]:
    return [f if f.startswith(data_path) else os.path.join(data_path, f)
            for f in fname]


CSV_TABLES = {name: CSV_Table(table_name=name,
                              file_names=build_path(csv),
                              **extra)
              for name, csv, extra in tables}
