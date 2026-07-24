# Data directory

This directory contains the input and generated data files used by the attached notebooks.

The directory names follow the paths used in the uploaded notebooks.

## Directory structure

```text
data/
├── metro/
├── NHIS/
│   └── 2016~2017/
├── mobility_factor/
│   └── 2016~2017/
├── Rt/
│   ├── 2016~2017/
│   ├── 2017~2018/
│   ├── 2018~2019/
│   └── 2022~2023/
└── population_denominators_2016_2017.csv
```

## Subway mobility input

Place the preprocessed city-level subway files in:

```text
data/metro/
```

Recommended file names used by the mobility-factor notebook:

```text
seoul&g_metro.csv
busan_metro.csv
daejeon_metro.csv
daegu_metro.csv
gwangju_metro.csv
```

Required columns:

```text
date
city
people_in
```

The manuscript uses subway boarding counts to construct the mobility coefficient. Therefore, `people_in` is the column used to calculate the mobility factor.

## NHIS influenza input

Place city-level influenza case files in:

```text
data/NHIS/2016~2017/
```

Expected file names used by the 2016-2017 \(R(t)\) notebook:

```text
Seoul&Gyeonggi_cases(2016~2017).csv
Busan_cases(2016~2017).csv
Daejeon_cases(2016~2017).csv
Daegu_cases(2016~2017).csv
Gwangju_cases(2016~2017).csv
```

The manuscript states that influenza-related diagnosis codes J09, J10, and J11 were used to construct the daily incidence data.

## Mobility-factor outputs

The mobility-factor notebook writes:

```text
data/mobility_factor/2016~2017/Seoul_gamma.csv
data/mobility_factor/2016~2017/Busan_gamma.csv
data/mobility_factor/2016~2017/Daegu_gamma.csv
data/mobility_factor/2016~2017/Daejeon_gamma.csv
data/mobility_factor/2016~2017/Gwangju_gamma.csv
```

Important: in these files, `gamma` means the mobility coefficient \(\xi(t)\) used in the manuscript. It is not the SIR recovery-rate parameter.

Expected mobility-factor columns include:

```text
city
date
people_in
pop
m
m_7
L
c
b
gamma
gamma_1
gamma_2
gamma_3
gamma_4
gamma_5
```

## Rt outputs

The \(R(t)\) notebook writes:

```text
data/Rt/2016~2017/Seoul_Rt(2016~2017).csv
data/Rt/2016~2017/Busan_Rt(2016~2017).csv
data/Rt/2016~2017/Daegu_Rt(2016~2017).csv
data/Rt/2016~2017/Daejeon_Rt(2016~2017).csv
data/Rt/2016~2017/Gwangju_Rt(2016~2017).csv
```

The heatmap and scenario-table notebooks expect the same naming pattern for:

```text
2017~2018
2018~2019
2022~2023
```

## Population denominators used in the attached 2016-2017 mobility notebook

The file below records the population denominators used in the uploaded mobility-factor notebook:

```text
data/population_denominators_2016_2017.csv
```
