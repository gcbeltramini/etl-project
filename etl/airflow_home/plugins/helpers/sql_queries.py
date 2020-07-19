import os


def read_sql(filename: str, **query_params) -> str:
    with open(os.path.realpath(filename), 'r') as f:
        return f.read().format(**query_params)
