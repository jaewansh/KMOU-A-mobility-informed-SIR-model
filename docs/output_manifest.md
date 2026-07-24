# Output manifest

This document defines the file names and columns expected by the attached notebooks.

## Mobility-factor outputs

Path pattern:

```text
data/mobility_factor/2016~2017/{City}_gamma.csv
```

Expected files:

```text
data/mobility_factor/2016~2017/Seoul_gamma.csv
data/mobility_factor/2016~2017/Busan_gamma.csv
data/mobility_factor/2016~2017/Daegu_gamma.csv
data/mobility_factor/2016~2017/Daejeon_gamma.csv
data/mobility_factor/2016~2017/Gwangju_gamma.csv
```

Expected columns:

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

Column interpretation:

```text
gamma   = xi(t)
gamma_1 = 10% reduction scenario
gamma_2 = 20% reduction scenario
gamma_3 = 30% reduction scenario
gamma_4 = 40% reduction scenario
gamma_5 = 50% reduction scenario
```

## Rt outputs

Path pattern:

```text
data/Rt/{Season}/{City}_Rt({Season}).csv
```

Expected 2016-2017 files:

```text
data/Rt/2016~2017/Seoul_Rt(2016~2017).csv
data/Rt/2016~2017/Busan_Rt(2016~2017).csv
data/Rt/2016~2017/Daegu_Rt(2016~2017).csv
data/Rt/2016~2017/Daejeon_Rt(2016~2017).csv
data/Rt/2016~2017/Gwangju_Rt(2016~2017).csv
```

The heatmap and summary-table notebooks expect the same naming pattern for:

```text
2017~2018
2018~2019
2022~2023
```

Expected columns for a city named `City`:

```text
date
City_Rt
City_Rt_1
City_Rt_2
City_Rt_3
City_Rt_4
City_Rt_5
```

Column interpretation:

```text
City_Rt   = baseline Rt using observed mobility
City_Rt_1 = Rt under 10% mobility reduction
City_Rt_2 = Rt under 20% mobility reduction
City_Rt_3 = Rt under 30% mobility reduction
City_Rt_4 = Rt under 40% mobility reduction
City_Rt_5 = Rt under 50% mobility reduction
```

## Scenario summary outputs

The uploaded `table.ipynb` notebook originally writes outputs under:

```text
rt_metric_outputs/
```

After running `scripts/patch_notebook_paths.py`, the recommended repository output location is:

```text
results/tables/rt_metric_outputs/
```

Recommended final reference CSV name:

```text
results/tables/scenario_summary_reference.csv
```

Expected columns:

```text
city
scenario
mean_Rt
delta_mean_Rt
mean_reduction_percent
days_Rt_gt_1
days_reduction_percent
excess_area
```

## Validation outputs

The negative binomial synthetic validation notebook writes:

```text
daily_rmse_results.csv
SIR Mathematical Model Negative binomial distribution.eps
SIR Mathematical Model Negative binomial distribution RMSE.eps
```

After running `scripts/patch_notebook_paths.py`, the recommended repository locations are:

```text
results/validation/daily_rmse_results.csv
figures/validation/SIR Mathematical Model Negative binomial distribution.eps
figures/validation/SIR Mathematical Model Negative binomial distribution RMSE.eps
```
