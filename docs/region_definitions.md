# Region definitions

This document records the analysis labels and input-file names used by the attached notebooks.

## Manuscript analysis labels

The manuscript reports analyses for:

```text
Seoul
Busan
Daegu
Daejeon
Gwangju
```

## Uploaded-code file-name convention

The uploaded notebooks use the label `Seoul` for output columns and figures, but some input files contain `Seoul&Gyeonggi` in the file name:

```text
seoul&g_metro.csv
Seoul&Gyeonggi_cases(2016~2017).csv
```

This repository preserves the uploaded-code convention so that the notebooks remain traceable to the original files.

## Input alignment rule

For each analysis label, the following inputs should be aligned before model fitting:

1. subway boarding counts used to construct the mobility coefficient;
2. influenza incidence series;
3. population denominator.

## Population denominators in the uploaded 2016-2017 mobility notebook

```text
seoul: 22689358.5
busan: 3484591
daejeon: 1508298.5
daegu: 2479894
gwangju: 1466492
```

These values are recorded in:

```text
data/population_denominators_2016_2017.csv
```

## Important note

The manuscript does not provide a separate administrative-code table. Therefore, this repository documents the analysis labels and input-file names used by the attached notebooks rather than introducing new regional definitions.
