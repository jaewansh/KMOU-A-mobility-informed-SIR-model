# Results directory

This directory stores generated mobility coefficients, model outputs, figures, validation results, and scenario summary tables.

Recommended structure:

```text
results/mobility/
results/model/
results/figures/
results/tables/
results/validation/
```

## Mobility outputs

Mobility outputs should contain the subway-ridership-based mobility coefficient \(\xi(t)\).

Preferred file names:

```text
Seoul_xi.csv
Busan_xi.csv
Daegu_xi.csv
Daejeon_xi.csv
Gwangju_xi.csv
```

Older local outputs named `*_gamma.csv` should be interpreted as legacy mobility-coefficient files, not as the SIR recovery-rate parameter \(\gamma\).

## Model outputs

Model outputs should contain estimated \(\beta(t)\), compartment trajectories, and \(R(t)\).

Recommended columns:

```text
date
season
city
theta
xi
beta
S
I
R
Rt
```

## Scenario outputs

Scenario outputs should include the observed-mobility baseline and 10%, 20%, 30%, 40%, and 50% mobility-reduction scenarios.

Recommended columns:

```text
date
season
city
scenario
reduction
Rt
```

## Scenario summary tables

Scenario summary tables should include:

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

A reference table transcribed from the manuscript and supplementary material is provided at:

```text
results/tables/scenario_summary_reference.csv
```
