# ETL project

## Datasets

There are four datasets:

1. **Data on immigration to the United States** (I-94 Immigration Data) from the
[U.S. National Tourism and Trade Office](https://travel.trade.gov/research/reports/i94/historical/2016.html);
1. **World temperature data** from [Berkeley Earth on Kaggle](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data);
1. **U.S. city demographic data** from [Opendatasoft](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/);
1. **Airport code data** from <https://datahub.io/core/airport-codes#data>.

A more thorough description, including the data dictionary, can be found [here](resources/docs/datasets.md).

## Instructions for running the ETL

### Setup

1. [PostgreSQL](resources/docs/postgresql.md)
1. [Airflow](resources/docs/airflow.md)

### Tests

Run `etl/scripts/tests.sh` (requires [shellcheck](https://github.com/koalaman/shellcheck),
[markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli) and
[remark-validate-links](https://github.com/remarkjs/remark-validate-links)).

### Analysis

The instructions are [here](resources/docs/analysis.md).

### Cleanup

After you are finished:

1. [Airflow](resources/docs/airflow.md#cleanup)
1. [PostgreSQL](resources/docs/postgresql.md#cleanup)

## Additional information

- [Description about scripts](etl/scripts/README.md)
- [Description about jupyter notebooks](resources/jupyter_notebooks/README.md)
- [Project structure](resources/docs/project-structure.md)
