# Output manifest

This document defines recommended output names and columns for reproducible analysis.

## Mobility coefficient outputs

Recommended path pattern:

```text
results/mobility/{season}/{theta}/{city}_xi.csv
```

Recommended columns:

```text
date
city
season
theta
people_in
population
m
L
c
b
xi
```

## Transmission-rate outputs

Recommended path pattern:

```text
results/model/{season}/{theta}/beta/{city}_beta.csv
```

Recommended columns:

```text
date
city
season
theta
beta
```

## Reproduction-number outputs

Recommended path pattern:

```text
results/model/{season}/{theta}/rt/{city}_rt.csv
```

Recommended columns:

```text
date
city
season
theta
xi
beta
S
I
R
Rt
```

## Scenario outputs

Recommended path pattern:

```text
results/model/{season}/{theta}/scenario/{city}_scenario_rt.csv
```

Recommended columns:

```text
date
city
season
theta
scenario
reduction
xi_scenario
Rt
```

## Summary table outputs

Recommended path:

```text
results/tables/scenario_summary.csv
```

Recommended columns:

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
