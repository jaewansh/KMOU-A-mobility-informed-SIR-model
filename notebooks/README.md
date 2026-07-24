# Notebooks

This directory contains the five notebooks uploaded with the manuscript materials.

## Required notebook file names

Rename the uploaded notebooks as follows before uploading them to GitHub.

| Uploaded file | GitHub file name |
|---|---|
| `mobility factor(2016~2017).ipynb` | `01_mobility_factor_2016_2017.ipynb` |
| `SIR_negative binomial.ipynb` | `02_sir_negative_binomial_particle_smoothing.ipynb` |
| `Rt(2016~2017).ipynb` | `03_rt_estimation_2016_2017.ipynb` |
| `HeatMap.ipynb` | `04_rt_heatmap_scenarios.ipynb` |
| `table.ipynb` | `05_scenario_summary_tables.ipynb` |

## Execution order

```text
01_mobility_factor_2016_2017.ipynb
02_sir_negative_binomial_particle_smoothing.ipynb
03_rt_estimation_2016_2017.ipynb
04_rt_heatmap_scenarios.ipynb
05_scenario_summary_tables.ipynb
```

## Notebook roles

### 01_mobility_factor_2016_2017.ipynb

Constructs the mobility coefficient from subway boarding counts.

Main calculations in the uploaded code:

```text
m(t) = X(t) / Pop
m_7(t) = centered 7-day moving average of m(t)
L = city-level mean of m_7(t)
c(t) = m(t) / L
b(t) = centered 7-day moving average of c(t)
gamma = b(t)
```

In manuscript notation, the notebook column `gamma` corresponds to \(\xi(t)\).

Scenario columns:

```text
gamma_1 = 0.9 * b(t)
gamma_2 = 0.8 * b(t)
gamma_3 = 0.7 * b(t)
gamma_4 = 0.6 * b(t)
gamma_5 = 0.5 * b(t)
```

### 02_sir_negative_binomial_particle_smoothing.ipynb

Runs a synthetic SIR experiment using a negative binomial observation model and compares particle filtering with particle smoothing.

### 03_rt_estimation_2016_2017.ipynb

Runs the mobility-informed SIR model for Seoul, Busan, Daegu, Daejeon, and Gwangju for the 2016-2017 season.

The notebook uses:

```python
sigma = 1.0 / 4.1
```

as the SIR recovery rate.

### 04_rt_heatmap_scenarios.ipynb

Generates heatmaps of \(R(t)\) for the observed-mobility baseline and 10%, 20%, 30%, 40%, and 50% mobility-reduction scenarios.

### 05_scenario_summary_tables.ipynb

Computes scenario summary metrics:

```text
Mean Rt
Delta Mean Rt
Mean reduction percentage
Days Rt > 1
Days reduction percentage
Excess area
```

## Important note

No `theta` parameter is used in these notebooks.
