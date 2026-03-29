# KMOU-A-mobility-informed-SIR-model

## Overview

This repository provides reproducible code for a mobility-informed SIR model that incorporates subway-based mobility to analyze regional influenza transmission dynamics in Korea.

## Study Description

This study integrates mobility data derived from subway boarding records into an SIR framework to capture spatial heterogeneity in influenza transmission. The model estimates transmission dynamics while accounting for region-specific mobility patterns across major metropolitan areas.

## Repository Structure

```
data/
├── raw/              # Raw data (not publicly available)
├── processed/        # Preprocessed data
└── sample/           # Example/sample data (if provided)

scripts/
├── preprocessing/    # Data preprocessing scripts
├── analysis/         # Mobility computation
└── model/            # SIR model execution

results/
├── mobility/         # Computed mobility outputs
├── model/            # Model outputs (beta, Rt)
└── figures/          # Figures for manuscript
```

## Reproducibility (Execution Order)

To reproduce the results, run the scripts in the following order:

1. **City-level preprocessing**

```
scripts/preprocessing/seoul_preprocessing.py
scripts/preprocessing/busan_preprocessing.py
scripts/preprocessing/daegu_preprocessing.py
scripts/preprocessing/gwangju_preprocessing.py
scripts/preprocessing/daejeon_api_2016.py
scripts/preprocessing/daejeon_preprocessing.py
```

2. **Merge city mobility data**

```
scripts/preprocessing/merge_city_mobility.py
```

3. **Compute mobility variables**

```
scripts/analysis/mobility_computation.py
```

4. **Preprocess NHIS case data**

```
scripts/preprocessing/case_preprocessing.py
```

5. **Run SIR model**

```
scripts/model/regional_rt_theta_001.py
```

## Data Availability

Raw NHIS data are not publicly available due to data privacy restrictions.

Users with authorized access should place raw data in:

```
data/raw/nhis/
```

and run the preprocessing scripts.

## Code Availability

The code used in this study is publicly available at:

https://github.com/jaewansh/KMOU-A-mobility-informed-SIR-model

## Citation

If you use this code, please cite:

(Your paper citation will be added after publication)

## License

MIT License
