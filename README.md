# KMOU-A-mobility-informed-SIR-model

## Overview

This repository provides reproducible code for a mobility-informed SIR model to analyze regional influenza transmission dynamics in Korea.

The study integrates:

* subway boarding-based mobility data from five metropolitan cities (Seoul, Busan, Daegu, Daejeon, and Gwangju),
* NHIS influenza case data,
* a mobility-weighted SIR framework,
* particle filtering and particle smoothing for time-varying transmission inference.

---

## Study Scope

This repository accompanies the manuscript:

**A mobility-informed SIR model for regional transmission dynamics: Evidence from subway mobility data in Korea, 2016–2023**

The goal of this study is to quantify how human mobility affects regional transmission intensity and to distinguish mobility-driven effects from intrinsic transmission dynamics.

---

## Note on Seasonal Analyses

The analyses in the manuscript were conducted for four influenza seasons:

* 2016–2017
* 2017–2018
* 2018–2019
* 2022–2023

Due to data access restrictions and to maintain clarity, this repository provides a fully reproducible pipeline for a **representative season (2016–2017)**.

The same modeling framework and code structure were applied to all other seasons with identical preprocessing and parameter settings.

---

## Repository Structure

```text
data/
├── raw/
│   ├── seoul/
│   ├── busan/
│   ├── daejeon/
│   ├── daegu/
│   ├── gwangju/
│   └── nhis/                # NHIS raw data (not included)
├── processed/
│   ├── metro/              # preprocessed metro data
│   └── cases/              # preprocessed case data
└── sample/                 # optional sample data

scripts/
├── preprocessing/
│   ├── *_preprocessing.py
│   ├── daejeon_api_2016.py
│   ├── daejeon_preprocessing.py
│   ├── merge_city_mobility.py
│   └── case_preprocessing.py
├── analysis/
│   └── mobility_computation.py
└── model/
    └── regional_rt_theta_001.py

results/
├── mobility/
├── model/
└── figures/

src/
└── preprocessing/
```

---

## Reproducibility (Execution Order)

To reproduce the results, run the scripts in the following order:

### 1. City-level metro preprocessing

```bash
python scripts/preprocessing/seoul_preprocessing.py
python scripts/preprocessing/busan_preprocessing.py
python scripts/preprocessing/daegu_preprocessing.py
python scripts/preprocessing/gwangju_preprocessing.py
python scripts/preprocessing/daejeon_api_2016.py
python scripts/preprocessing/daejeon_preprocessing.py
```

### 2. Merge metro data

```bash
python scripts/preprocessing/merge_city_mobility.py
```

### 3. Compute mobility factor

```bash
python scripts/analysis/mobility_computation.py
```

### 4. Preprocess NHIS influenza case data

```bash
python scripts/preprocessing/case_preprocessing.py
```

### 5. Run the regional SIR model

```bash
python scripts/model/regional_rt_theta_001.py
```

---

## Mobility Construction

The mobility factor is constructed through the following steps:

1. Per-capita mobility intensity from daily subway boardings
2. Regional mobility level normalization
3. Temporal smoothing using a centered 7-day moving average
4. Mobility-adjusted transmission modifier with elasticity parameter ( \theta )

---

## Data Availability

This study uses two main data sources:

### 1. NHIS influenza case data

* Not publicly available due to data privacy restrictions
* Users with authorized access should place raw data in:

```text
data/raw/nhis/
```

### 2. Subway mobility data

* Derived from metropolitan subway boarding records across five cities
* Raw metro data are not included due to data usage and licensing constraints
* Users should place raw data in:

```text
data/raw/{city}/
```

All preprocessing pipelines are fully provided, and the repository includes all steps required to reconstruct the processed datasets used in the analysis.

---

## Code Availability

All code used in this study is publicly available at:

https://github.com/jaewansh/KMOU-A-mobility-informed-SIR-model

The version used for manuscript submission corresponds to:

```text
v1.0.0
```

---

## Dependencies

Install required packages using:

```bash
pip install -r requirements.txt
```

---

## Citation

If you use this repository, please cite the associated manuscript and this code repository.

(Full citation will be updated upon publication.)

---

## License

GNU General Public License v3.0
