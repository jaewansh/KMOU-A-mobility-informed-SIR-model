# Data directory

This directory stores raw and processed data used by the mobility-informed SIR model.

## Raw data

Raw data files are not necessarily committed to this repository because some sources may require separate download, request, or redistribution permission.

Expected raw-data locations are:

```text
data/raw/nhis/
data/raw/seoul/
data/raw/busan/
data/raw/daegu/
data/raw/daejeon/
data/raw/gwangju/
```

## Processed data

Processed data should be stored under:

```text
data/processed/
```

Recommended processed influenza case files are:

```text
data/processed/cases/Korea_cases.csv
data/processed/cases/Seoul_cases.csv
data/processed/cases/Busan_cases.csv
data/processed/cases/Daegu_cases.csv
data/processed/cases/Daejeon_cases.csv
data/processed/cases/Gwangju_cases.csv
```

The recommended processed mobility file is:

```text
data/processed/all_city_metro.csv
```

## Required columns

Processed influenza case files should contain:

```text
date
city
cases
```

Processed mobility files should contain:

```text
date
city
people_in
people_out
```

The mobility coefficient used in the manuscript is constructed from `people_in`, which represents subway boarding counts. The `people_out` column may be preserved for completeness but is not used in the main mobility-factor calculation.

## Analysis periods

The manuscript analyzes the following influenza seasons:

```text
2016_2017: 2016-09-01 to 2017-08-31
2017_2018: 2017-09-01 to 2018-08-31
2018_2019: 2018-09-01 to 2019-08-31
2022_2023: 2022-09-01 to 2023-08-31
```

## Analysis cities

The city-level analyses are conducted independently for:

```text
Seoul
Busan
Daegu
Daejeon
Gwangju
```

## Reproducibility note

For complete reproduction of the manuscript and supplementary material, processed inputs or generated outputs should be available for all analysis cities and all analysis seasons listed above.
