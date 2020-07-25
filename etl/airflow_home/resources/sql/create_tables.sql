CREATE TABLE IF NOT EXISTS {schema_name:s}.{immigration:s} (
  cicid INTEGER NOT NULL,
  i94yr SMALLINT NOT NULL,
  i94mon SMALLINT NOT NULL,
  i94cit SMALLINT,
  i94res SMALLINT NOT NULL,
  i94port CHAR(3) NOT NULL,
  arrdate INTEGER NOT NULL,
  i94mode SMALLINT,
  i94addr VARCHAR(2),
  depdate INTEGER,
  i94bir SMALLINT,
  i94visa SMALLINT NOT NULL,
  "count" SMALLINT NOT NULL,
  dtadfile VARCHAR(8),
  visapost VARCHAR(16),
  occup VARCHAR(16),
  entdepa CHAR(1),
  entdepd CHAR(1),
  entdepu CHAR(1),
  matflag CHAR(1),
  biryear SMALLINT,
  dtaddto VARCHAR(8),
  gender CHAR(1),
  insnum VARCHAR(16),  -- it contains number and text
  airline VARCHAR(16),
  admnum BIGINT NOT NULL,
  fltno VARCHAR(16),
  visatype VARCHAR(16) NOT NULL,
  PRIMARY KEY(i94yr, i94mon, cicid)
);

CREATE TABLE IF NOT EXISTS {schema_name:s}.{airport_codes:s} (
  ident VARCHAR(7) NOT NULL PRIMARY KEY,
  type VARCHAR(14) NOT NULL,
  name VARCHAR(128) NOT NULL,
  elevation_ft REAL,
  continent VARCHAR(2),
  iso_country VARCHAR(2),
  iso_region VARCHAR(7) NOT NULL,
  municipality VARCHAR(60),
  gps_code VARCHAR(4),
  iata_code VARCHAR(3),
  local_code VARCHAR(7),
  coordinates VARCHAR(43) NOT NULL
);

CREATE TABLE IF NOT EXISTS {schema_name:s}.{global_temperatures:s} (
  dt DATE NOT NULL,
  average_temperature DECIMAL(6, 4),
  average_temperature_uncertainty DECIMAL(6, 4),
  city VARCHAR(25) NOT NULL,
  country VARCHAR(34) NOT NULL,
  latitude VARCHAR(6) NOT NULL,
  longitude VARCHAR(7) NOT NULL,
  PRIMARY KEY(city, country, latitude, longitude, dt)
);

CREATE TABLE IF NOT EXISTS {schema_name:s}.{us_cities:s} (
  city VARCHAR(47) NOT NULL,
  state VARCHAR(20) NOT NULL,
  median_age REAL NOT NULL,
  male_population INTEGER,
  female_population INTEGER,
  total_population INTEGER NOT NULL,
  number_of_veterans INTEGER,
  foreign_born INTEGER,
  average_household_size REAL,
  state_code VARCHAR(2) NOT NULL,
  race VARCHAR(33) NOT NULL,
  count INTEGER NOT NULL,
  PRIMARY KEY(city, state, race)
);
