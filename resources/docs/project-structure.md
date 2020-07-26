# Project structure

```text
.
├── .gitignore: files to be ignored by git
├── .markdownlint.json: markdownlint configuration file
├── README.md: project documentation
├── etl: ETL files
│   ├── airflow_home: Airflow home folder
│   │   ├── dags
│   │   │   └── etl_dag.py: Airflow DAG definition
│   │   ├── plugins
│   │   │   ├── helpers: helpers files (constants and functions)
│   │   │   └── operators: Airflow operators
│   │   └── resources
│   │       ├── data
│   │       │   ├── 18-83510-I94-Data-2016: sas7bdat and CSV files
│   │       │   │   └── csv: folder with CSV files
│   │       │   ├── GlobalLandTemperaturesByCity.csv
│   │       │   ├── airport-codes.csv
│   │       │   ├── immigration_data_sample.csv
│   │       │   └── us-cities-demographics.csv
│   │       └── sql: SQL files
│   └── scripts: shell scripts
└── resources
    ├── docs: additional documentation
    ├── jupyter_notebooks: folder with jupyter notebooks
    └── requirements: Python requirement files
```
