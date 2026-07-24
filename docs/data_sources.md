# Data sources

This document summarizes the data sources used in the manuscript and repository.

## Influenza incidence data

Daily influenza-related medical-use counts were obtained from the National Health Insurance Service (NHIS) data available through the Korean Open Government Data portal.

The manuscript uses influenza-related diagnosis codes:

```text
J09
J10
J11
```

The NHIS data source described in the manuscript is:

```text
https://www.data.go.kr/data/15089429/fileData.do
```

## Subway mobility data

Subway ridership data were collected from public data portals and relevant metropolitan transit authorities.

Only boarding counts are used to construct the mobility coefficient \(\xi(t)\). Alighting counts may be retained in processed files for completeness, but they are not used in the main mobility-factor calculation.

An example subway mobility source described in the manuscript is:

```text
https://www.data.go.kr/data/15048032/fileData.do
```

For specific periods not fully covered by public datasets, the manuscript states that additional subway data were obtained directly from the relevant authorities upon request.

## Population data

Population denominators were derived from resident registration population statistics released by the Ministry of the Interior and Safety.

The population data source described in the manuscript is:

```text
https://jumin.mois.go.kr
```

## Analysis periods

The manuscript analyzes the following influenza seasons:

```text
2016_2017: 2016-09-01 to 2017-08-31
2017_2018: 2017-09-01 to 2018-08-31
2018_2019: 2018-09-01 to 2019-08-31
2022_2023: 2022-09-01 to 2023-08-31
```

## Redistribution note

Raw data files may require separate download, request, or permission procedures. Therefore, raw files are not necessarily committed to this repository. Processed files required for reproducing the manuscript outputs should be included whenever redistribution is allowed.
