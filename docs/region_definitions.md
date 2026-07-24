# Region definitions

This document records the spatial analysis units used in the repository.

The manuscript applies the same mobility-informed SIR framework independently to five metropolitan cities in Korea:

```text
Seoul
Busan
Daegu
Daejeon
Gwangju
```

The case counts, population denominators, and subway ridership data should be aligned to the same city-level analysis unit before model fitting.

## City-level analysis units

| Repository label | Analysis unit used in the manuscript | Mobility input | Case input | Population input |
|---|---|---|---|---|
| Seoul | Seoul metropolitan city-level analysis unit | Subway boarding counts | NHIS influenza-related counts | Resident registration population |
| Busan | Busan metropolitan city-level analysis unit | Subway boarding counts | NHIS influenza-related counts | Resident registration population |
| Daegu | Daegu metropolitan city-level analysis unit | Subway boarding counts | NHIS influenza-related counts | Resident registration population |
| Daejeon | Daejeon metropolitan city-level analysis unit | Subway boarding counts | NHIS influenza-related counts | Resident registration population |
| Gwangju | Gwangju metropolitan city-level analysis unit | Subway boarding counts | NHIS influenza-related counts | Resident registration population |

## Alignment rule

For each city and season, the following three quantities must refer to the same analysis unit:

1. daily influenza incidence;
2. subway boarding counts used to construct \(\xi(t)\);
3. population denominator used in the mobility and SIR calculations.

## Boundary note

The manuscript does not provide a separate administrative-code table. Therefore, this repository defines the public analysis labels at the city level reported in the manuscript. Any future change from these city-level analysis units should be documented in this file before rerunning the pipeline.
