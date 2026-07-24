# Code inventory

This document maps the uploaded notebooks to the manuscript analyses.

## Uploaded notebooks

| GitHub file | Source uploaded file | Manuscript or supplement connection |
|---|---|---|
| `notebooks/01_mobility_factor_2016_2017.ipynb` | `mobility factor(2016~2017).ipynb` | Manuscript Figure 4 and mobility-factor construction in Section 3 |
| `notebooks/02_sir_negative_binomial_particle_smoothing.ipynb` | `SIR_negative binomial.ipynb` | Manuscript Figure 3 and Supplementary Figure S1 |
| `notebooks/03_rt_estimation_2016_2017.ipynb` | `Rt(2016~2017).ipynb` | Manuscript Figures 5-6 and 2016-2017 Rt outputs |
| `notebooks/04_rt_heatmap_scenarios.ipynb` | `HeatMap.ipynb` | Manuscript Figure 7 and Supplementary Figures S6-S9 |
| `notebooks/05_scenario_summary_tables.ipynb` | `table.ipynb` | Manuscript Table 2 and Supplementary Tables S1-S4 |

## Main output dependencies

```text
01_mobility_factor_2016_2017.ipynb
        ↓
data/mobility_factor/2016~2017/*_gamma.csv
        ↓
03_rt_estimation_2016_2017.ipynb
        ↓
data/Rt/2016~2017/*_Rt(2016~2017).csv
        ↓
04_rt_heatmap_scenarios.ipynb
05_scenario_summary_tables.ipynb
```

## Important code terminology

The manuscript uses \(\xi(t)\) for the mobility coefficient.

The uploaded code uses the following mobility-factor columns:

```text
gamma
gamma_1
gamma_2
gamma_3
gamma_4
gamma_5
```

These names are retained because they are already used across the attached notebooks.

The SIR recovery rate is represented in the \(R(t)\) estimation notebook as:

```python
sigma = 1.0 / 4.1
```

The attached mobility-factor notebook does not contain a `theta` parameter. Its scenario logic is based on direct mobility reductions:

```text
gamma_1 = 0.9 * gamma
gamma_2 = 0.8 * gamma
gamma_3 = 0.7 * gamma
gamma_4 = 0.6 * gamma
gamma_5 = 0.5 * gamma
```

No `theta` parameter is used in the attached code or manuscript.
