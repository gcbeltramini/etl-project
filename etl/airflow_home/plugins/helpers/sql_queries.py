import os


def read_sql(sql_file: str, **query_params) -> str:
    with open(os.path.realpath(sql_file), 'r') as f:
        return f.read().format(**query_params)
