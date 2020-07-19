# ETL project

## Datasets

There are four datasets:

1. Data on immigration to the United States (I-94 Immigration Data) from the
[U.S. National Tourism and Trade Office](https://travel.trade.gov/research/reports/i94/historical/2016.html);
1. **World temperature data** from [Berkeley Earth on Kaggle](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data);
1. **U.S. city demographic data** from [Opendatasoft](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/);
1. **Airport code data** from <https://datahub.io/core/airport-codes#data>.

The following sections describe the datasets in more details.

### Immigration data

### World temperature data

### U.S. city demographic data

### Airport code data

The airport codes may refer to either [IATA](http://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code)
airport code, a three-letter code which is used in passenger reservation, ticketing and
baggage-handling systems, or the [ICAO](http://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code)
airport code, which is a four-letter code defined by the [International Civil Aviation Organization](https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization)
for air traffic control and airline operations such as flight planning.

The data contains the list of all airport codes. Some of the columns contain attributes identifying
airport locations, other codes (IATA, local if exist) that are relevant to identification of an
airport.

Data dictionary:

| Column name  | Has missing values? | Type                                   | Values                                                                                                                    |
|--------------|---------------------|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ident        | no                  | text up to 7 characters                | example: "00A"                                                                                                            |
| type         | no                  | text up to 14 characters               | possible values: "small_airport", "heliport", "medium_airport", "closed", "seaplane_base", "large_airport", "balloonport" |
| name         | no                  | text up to 128 characters              |                                                                                                                           |
| elevation_ft |                     | number with 6 decimal digits precision |                                                                                                                           |
| continent    |                     | text up to 2 characters                | possible values: "EU", "SA", "AS", "AF", "OC", "AN"                                                                       |
| iso_country  |                     | text up to 2 characters                |                                                                                                                           |
| iso_region   | no                  | text up to 7 characters                |                                                                                                                           |
| municipality |                     | text up to 60 characters               |                                                                                                                           |
| gps_code     |                     | text up to 4 characters                |                                                                                                                           |
| iata_code    |                     | text up to 3 characters                |                                                                                                                           |
| local_code   |                     | text up to 7 characters                |                                                                                                                           |
| coordinates  | no                  | text up to 43 characters               |                                                                                                                           |

Primary key = `ident`

## Instructions for running the ETL

### Setup

1. [PostgreSQL](resources/docs/postgresql.md)
1. [Airflow](resources/docs/airflow.md)

### Tests

Run `etl/scripts/tests.sh` (requires [shellcheck](https://github.com/koalaman/shellcheck) and
[markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli)).

### Analysis

The instructions are [here](resources/docs/analysis.md).

### Cleanup

After you are finished:

1. [Airflow](resources/docs/airflow.md#cleanup)
1. [PostgreSQL](resources/docs/postgresql.md#cleanup)
