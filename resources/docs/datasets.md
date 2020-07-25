# Datasets

The following sections describe the datasets in more details. To understand their content (column
names, missing values, data types, possivle values), the jupyter notebook [Explore_supplementary_CSV_files.ipynb](../jupyter_notebooks/Explore_supplementary_CSV_files.ipynb)
was used.

References for the PostgreSQL data types:

- [Date/Time Types](https://www.postgresql.org/docs/current/datatype-datetime.html)
- [Numeric Types](https://www.postgresql.org/docs/current/datatype-numeric.html)
- [Character Types](https://www.postgresql.org/docs/current/datatype-character.html)

In the "Values" column below, "example" is a fake value representing a possible entry; "possible
values" is the list of actual possible values that can be in that column.

## Immigration data

Data on immigration to the United States (I-94 Immigration Data) from the U.S. National Tourism and
Trade Office.

<!-- markdownlint-disable MD013 -->
| Column name |  Has missing values? | Type                      | Values                                                                  |
|-------------|----------------------|---------------------------|-------------------------------------------------------------------------|
| cicid       | no                   | signed integer (4 bytes)  | example: 4567                                                           |
| i94yr       | no                   | signed integer (2 bytes)  | example: 2016                                                           |
| i94mon      | no                   | signed integer (2 bytes)  | example: 12                                                             |
| i94cit      | yes                  | signed integer (2 bytes)  | possible values: [labels descriptions](I94_SAS_Labels_Descriptions.SAS) |
| i94res      | no                   | signed integer (2 bytes)  | possible values: [labels descriptions](I94_SAS_Labels_Descriptions.SAS) |
| i94port     | no                   | text (3 characters)       | possible values: [labels descriptions](I94_SAS_Labels_Descriptions.SAS) |
| arrdate     | no                   | signed integer (4 bytes)  | example: 20748                                                          |
| i94mode     | yes                  | signed integer (2 bytes)  | possible values: [labels descriptions](I94_SAS_Labels_Descriptions.SAS) |
| i94addr     | yes                  | text (up to 2 characters) | possible values: [labels descriptions](I94_SAS_Labels_Descriptions.SAS) |
| depdate     | yes                  | signed integer (4 bytes)  | example: 21432                                                          |
| i94bir      | yes                  | signed integer (2 bytes)  | example: 29                                                             |
| i94visa     | no                   | signed integer (2 bytes)  | possible values: [labels descriptions](I94_SAS_Labels_Descriptions.SAS) |
| "count"     | no                   | signed integer (2 bytes)  | example: 1                                                              |
| dtadfile    | yes                  | text (up to 8 characters) | example: 20161024                                                       |
| visapost    | yes                  | text (3 characters)       | example: "MDD"                                                          |
| occup       | yes                  | text (3 characters)       | example: "STU"                                                          |
| entdepa     | yes                  | text (1 character)        | example: "T"                                                            |
| entdepd     | yes                  | text (1 character)        | example: "K"                                                            |
| entdepu     | yes                  | text (1 character)        | example: "U"                                                            |
| matflag     | yes                  | text (1 character)        | example: "M"                                                            |
| biryear     | yes                  | signed integer (2 bytes)  | example: 1989                                                           |
| dtaddto     | yes                  | text (up to 8 characters) | example: "01062017"                                                     |
| gender      | yes                  | text (1 character)        | example: "F"                                                            |
| insnum      | yes                  | text (up to 6 characters) | example: "06122"                                                        |
| airline     | yes                  | text (up to 3 characters) | example: "LH"                                                           |
| admnum      | no                   | signed integer (8 bytes)  | example: 346608285                                                      |
| fltno       | yes                  | text (up to 5 characters) | example: 424                                                            |
| visatype    | no                   | text (up to 3 characters) | example: "F1"                                                           |
<!-- markdownlint-enable MD013 -->

## World temperature data

This data is repackaged from a compilation put together by the [Berkeley Earth](http://berkeleyearth.org/about/),
which is affiliated with Lawrence Berkeley National Laboratory. The Berkeley Earth Surface Temperature
Study combines 1.6 billion temperature reports from 16 pre-existing archives. The dataset used here
is `GlobalLandTemperaturesByCity.csv`.

The dataset contains:
- location information (city, country, latitude, longitude)
- measurement date
- the average temperature with the measurement uncertainty

Column description (primary key = `(city, country, latitude, longitude, dt)`):

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

## United States (U.S.) city demographic data

This dataset contains information about the demographics of all US cities and census-designated
places with a population greater or equal to 65,000. This data comes from the US Census Bureau's
2015 American Community Survey.

The information available is:
- US city (city and state)
- median age; average household size
- male and female population; total population (sum of male and female population)
- number of veterans; foreign born
- count per race (the sum may be higher than the total population)

Column description (primary key = `(city, state, race)`):

<!-- markdownlint-disable MD013 -->
| Column name            | Has missing values? | Type                                | Values                                                                                                                    |
|------------------------|---------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| city                   | no                  | text (up to 47 characters)          | example: "Boston"                                                                                                        |
| state                  | no                  | text (up to 20 characters)          | example: "Massachusetts"                                                                                                            |
| median_age             | no                  | number (6 decimal digits precision) | example: 31.2                                                                                                             |
| male_population        | yes                 | signed integer (4 bytes)            | example: 1234                                                                                                             |
| female_population      | yes                 | signed integer (4 bytes)            | example: 1243                                                                                                             |
| total_population       | no                  | signed integer (4 bytes)            | example: 2477                                                                                                             |
| number_of_veterans     | yes                 | signed integer (4 bytes)            | example: 432                                                                                                              |
| foreign_born           | yes                 | signed integer (4 bytes)            | example: 657                                                                                                              |
| average_household_size | yes                 | number (6 decimal digits precision) | example: 2.67                                                                                                             |
| state_code             | no                  | text (up to 2 characters)           | example: "NY"                                                                                                             |
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

Column description (primary key = `ident`):

<!-- markdownlint-disable MD013 -->
| Column name  | Has missing values? | Type                                | Values                                                                                                                    |
|--------------|---------------------|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ident        | no                  | text (up to 7 characters)           | example: "00A"                                                                                                            |
| type         | no                  | text (up to 14 characters)          | possible values: "small_airport", "heliport", "medium_airport", "closed", "seaplane_base", "large_airport", "balloonport" |
| name         | no                  | text (up to 128 characters)         | example: "Fulton Airport"                                                                                                |
| elevation_ft | yes                 | number (6 decimal digits precision) | example: 1234.5                                                                                                           |
| continent    | yes                 | text (up to 2 characters)           | possible values: "EU", "SA", "AS", "AF", "OC", "AN"                                                                       |
| iso_country  | yes                 | text (up to 2 characters)           | example: "US"                                                                                                             |
| iso_region   | no                  | text (up to 7 characters)           | example: "US-OK"                                                                                                          |
| municipality | yes                 | text (up to 60 characters)          | example: "Chicago"                                                                                                        |
| gps_code     | yes                 | text (up to 4 characters)           | example: "00A"                                                                                                            |
| iata_code    | yes                 | text (up to 3 characters)           | example: "ORD"                                                                                                            |
| local_code   | yes                 | text (up to 7 characters)           | example: "00A"                                                                                                            |
| coordinates  | no                  | text (up to 43 characters)          | example: "12.3456, -76.54321"                                                                                             |
<!-- markdownlint-enable MD013 -->
