# Datasets

The following sections describe the datasets in more details. To understand their content (column
names, missing values, data types, possivle values), the jupyter notebook [Explore_supplementary_CSV_files.ipynb](../jupyter_notebooks/Explore_supplementary_CSV_files.ipynb)
was used.

References for the PostgreSQL data types:

- [Date/Time Types](https://www.postgresql.org/docs/current/datatype-datetime.html)
- [Numeric Types](https://www.postgresql.org/docs/current/datatype-numeric.html)

In the "Values" column below, "example" is a fake value representing a possible entry; "possible
values" is the list of actual possible values that can be in that column.

## Immigration data

TODO

## World temperature data

This data is repackaged from a compilation put together by the [Berkeley Earth](http://berkeleyearth.org/about/),
which is affiliated with Lawrence Berkeley National Laboratory. The Berkeley Earth Surface Temperature
Study combines 1.6 billion temperature reports from 16 pre-existing archives. The dataset used here
is `GlobalLandTemperaturesByCity.csv`.

Data dictionary (primary key = `(city, country, latitude, longitude, dt)`):

<!-- markdownlint-disable MD013 -->
| Column name                     | Has missing values? | Type                                                  | Values              |
|---------------------------------|---------------------|-------------------------------------------------------|---------------------|
| dt                              | no                  | date (no time of day)                                 | example: 2000-01-02 |
| average_temperature             | yes                 | number (up to 21 digits, 19 decimal digits precision) | example: 19.876     |
| average_temperature_uncertainty | yes                 | number (up to 19 digits, 18 decimal digits precision) | example: 0.245      |
| city                            | no                  | text (up to 25 characters)                            | example: "Foo"      |
| country                         | no                  | text (up to 34 characters)                            | example: "Foobar"   |
| latitude                        | no                  | text (up to 6 characters)                             | example: "12.43N"   |
| longitude                       | no                  | text (up to 7 characters)                             | example: "3.75E"    |
<!-- markdownlint-enable MD013 -->

## U.S. city demographic data

This dataset contains information about the demographics of all US cities and census-designated
places with a population greater or equal to 65,000. This data comes from the US Census Bureau's
2015 American Community Survey.

Data dictionary (primary key = `(city, state, race)`):

<!-- markdownlint-disable MD013 -->
| Column name            | Has missing values? | Type                                | Values                                                                                                                    |
|------------------------|---------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| city                   | no                  | text (up to 47 characters)          | example: "Foo Bar"                                                                                                        |
| state                  | no                  | text (up to 20 characters)          | example: "Foo"                                                                                                            |
| median_age             | no                  | number (6 decimal digits precision) | example: 31.2                                                                                                             |
| male_population        | yes                 | signed integer (4 bytes)            | example: 1234                                                                                                             |
| female_population      | yes                 | signed integer (4 bytes)            | example: 1243                                                                                                             |
| total_population       | no                  | signed integer (4 bytes)            | example: 2477                                                                                                             |
| number_of_veterans     | yes                 | signed integer (4 bytes)            | example: 432                                                                                                              |
| foreign_born           | yes                 | signed integer (4 bytes)            | example: 657                                                                                                              |
| average_household_size | yes                 | number (6 decimal digits precision) | example: 2.67                                                                                                             |
| state_code             | no                  | text (up to 2 characters)           | example: "XY"                                                                                                             |
| race                   | no                  | text (up to 33 characters)          | possible values: "Hispanic or Latino", "White", "Black or African-American", "Asian", "American Indian and Alaska Native" |
| count                  | no                  | signed integer (4 bytes)            | example: 2103                                                                                                             |
<!-- markdownlint-enable MD013 -->

## Airport code data

The airport codes may refer to either [IATA](http://en.wikipedia.org/wiki/International_Air_Transport_Association_airport_code)
airport code, a three-letter code which is used in passenger reservation, ticketing and
baggage-handling systems, or the [ICAO](http://en.wikipedia.org/wiki/International_Civil_Aviation_Organization_airport_code)
airport code, which is a four-letter code defined by the [International Civil Aviation Organization](https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization)
for air traffic control and airline operations such as flight planning.

The data contains the list of all airport codes. Some of the columns contain attributes identifying
airport locations, other codes (IATA, local if exist) that are relevant to identification of an
airport.

Data dictionary (primary key = `ident`):

<!-- markdownlint-disable MD013 -->
| Column name  | Has missing values? | Type                                | Values                                                                                                                    |
|--------------|---------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ident        | no                  | text (up to 7 characters)           | example: "00A"                                                                                                            |
| type         | no                  | text (up to 14 characters)          | possible values: "small_airport", "heliport", "medium_airport", "closed", "seaplane_base", "large_airport", "balloonport" |
| name         | no                  | text (up to 128 characters)         | example: "Foo Bar Airport"                                                                                                |
| elevation_ft | yes                 | number (6 decimal digits precision) | example: 1234.5                                                                                                           |
| continent    | yes                 | text (up to 2 characters)           | possible values: "EU", "SA", "AS", "AF", "OC", "AN"                                                                       |
| iso_country  | yes                 | text (up to 2 characters)           | example: "US"                                                                                                             |
| iso_region   | no                  | text (up to 7 characters)           | example: "US-XY"                                                                                                          |
| municipality | yes                 | text (up to 60 characters)          | example: "Foo Bar"                                                                                                        |
| gps_code     | yes                 | text (up to 4 characters)           | example: "00A"                                                                                                            |
| iata_code    | yes                 | text (up to 3 characters)           | example: "XYZ"                                                                                                            |
| local_code   | yes                 | text (up to 7 characters)           | example: "00A"                                                                                                            |
| coordinates  | no                  | text (up to 43 characters)          | example: "12.3456, -76.54321"                                                                                             |
<!-- markdownlint-enable MD013 -->
