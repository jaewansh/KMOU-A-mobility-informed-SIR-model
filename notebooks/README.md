# Notebooks

This directory contains the five notebooks used to reproduce the manuscript workflow.

## Required notebook files

| Order | File | Purpose |
|---|---|---|
| 1 | `01_mobility_factor_2016_2017.ipynb` | Constructs the subway-ridership-based mobility coefficient for the 2016-2017 season. |
| 2 | `02_sir_negative_binomial_particle_smoothing.ipynb` | Runs the synthetic SIR validation under a negative binomial observation model and compares particle filtering with particle smoothing. |
| 3 | `03_rt_estimation_2016_2017.ipynb` | Estimates mobility-informed SIR trajectories, \(\beta(t)\), and \(R(t)\) for the 2016-2017 season. |
| 4 | `04_rt_heatmap_scenarios.ipynb` | Generates heatmaps of \(R(t)\) under observed mobility and 10-50% mobility-reduction scenarios. |
| 5 | `05_scenario_summary_tables.ipynb` | Computes scenario summary metrics for mean \(R(t)\), days with \(R(t)>1\), and excess transmission area. |

## Execution order

Run the notebooks in the following order:

```text
01_mobility_factor_2016_2017.ipynb
02_sir_negative_binomial_particle_smoothing.ipynb
03_rt_estimation_2016_2017.ipynb
04_rt_heatmap_scenarios.ipynb
05_scenario_summary_tables.ipynb
```

## Important notation

The manuscript denotes the mobility coefficient as \(\xi(t)\). The attached notebooks preserve the original code column name `gamma` for this same mobility coefficient.

| Notebook/code column | Manuscript notation | Meaning |
|---|---|---|
| `gamma` | \(\xi(t)\) | Observed subway-ridership-based mobility coefficient |
| `gamma_1` | \(0.9\xi(t)\) | 10% mobility-reduction scenario |
| `gamma_2` | \(0.8\xi(t)\) | 20% mobility-reduction scenario |
| `gamma_3` | \(0.7\xi(t)\) | 30% mobility-reduction scenario |
| `gamma_4` | \(0.6\xi(t)\) | 40% mobility-reduction scenario |
| `gamma_5` | \(0.5\xi(t)\) | 50% mobility-reduction scenario |

The SIR recovery rate is represented in the Rt estimation notebook as:

```python
sigma = 1.0 / 4.1
```

No `theta` parameter is used in the attached manuscript or notebooks.

## Input data expected by the notebooks

### Subway mobility input

Place city-level subway files in:

```text
data/metro/
```

Expected file names:

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

### NHIS influenza input

Place 2016-2017 city-level influenza case files in:

```text
data/NHIS/2016~2017/
```

Expected file names:

```text
Korea_cases(2016~2017).csv
Seoul&Gyeonggi_cases(2016~2017).csv
Busan_cases(2016~2017).csv
Daejeon_cases(2016~2017).csv
Daegu_cases(2016~2017).csv
Gwangju_cases(2016~2017).csv
```

## Outputs

The mobility-factor notebook writes:

```text
data/mobility_factor/2016~2017/Seoul_gamma.csv
data/mobility_factor/2016~2017/Busan_gamma.csv
data/mobility_factor/2016~2017/Daegu_gamma.csv
data/mobility_factor/2016~2017/Daejeon_gamma.csv
data/mobility_factor/2016~2017/Gwangju_gamma.csv
```

The Rt estimation notebook writes:

```text
data/Rt/2016~2017/Seoul_Rt(2016~2017).csv
data/Rt/2016~2017/Busan_Rt(2016~2017).csv
data/Rt/2016~2017/Daegu_Rt(2016~2017).csv
data/Rt/2016~2017/Daejeon_Rt(2016~2017).csv
data/Rt/2016~2017/Gwangju_Rt(2016~2017).csv
```

The heatmap and scenario-table notebooks expect Rt files for:

```text
2016~2017
2017~2018
2018~2019
2022~2023
```
