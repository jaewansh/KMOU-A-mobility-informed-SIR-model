# KMOU-A-mobility-informed-SIR-model

Code and data-processing pipeline for the mobility-informed SIR model developed in:

**A mobility-informed SIR model for regional transmission dynamics: Evidence from subway mobility data in Korea, 2016–2023**

## Overview

This repository implements a mobility-informed SIR framework for influenza transmission analysis in Korea using:

- **NHIS daily influenza diagnosis counts**
- **regional subway boarding data** as a proxy for mobility intensity
- a **mobility-adjusted SIR model**
- **particle smoothing** to estimate time-varying transmission rates and effective reproduction numbers

The main purpose of the project is to separate:

1. transmission variability associated with regional mobility, and  
2. intrinsic transmission variability that remains after accounting for mobility.

A key advantage of the framework is that it can be applied **without an inter-regional origin–destination (OD) matrix**. Instead of reconstructing where people traveled, the model uses aggregate boarding activity as an indicator of **how much mobility occurred within each region**.

## Study scope

The manuscript analyzes four influenza seasons:

- **2016–2017**
- **2017–2018**
- **2018–2019**
- **2022–2023**

The current GitHub repository is organized around a **representative executable pipeline for the 2016–2017 season**, including preprocessing, mobility construction, and model execution. The same modeling logic and code structure were used for the additional seasons discussed in the manuscript.

## Regional units used in this repository

The analyses are conducted at two spatial levels:

- **Korea** (national level)
- **five metropolitan regions** used for regional comparison:
  - Seoul
  - Busan
  - Daegu
  - Daejeon
  - Gwangju

### Important note on the `Seoul` label in this repository

In the manuscript, the metropolitan comparison is described using the label **Seoul**. In this GitHub repository, however, the operational definition used in preprocessing/modeling is intentionally broader than the strict administrative boundary of Seoul city.

Here, **`Seoul` is used as a Seoul-centered metropolitan commuting-area proxy** so that the mobility/case definition better reflects real subway-linked daily movement. In practice, the case preprocessing step aggregates the relevant regional codes used in the codebase, and the population input is also aligned with this broader operational definition.

This means:

- `Seoul` in the repository should be interpreted as a **modeling convention for a broader Seoul metropolitan area**, not as a strict legal-administrative boundary.
- This convention is used to make the README, code, and manuscript interpretation consistent.

## Mobility construction

The regional mobility factor is constructed from daily subway **boarding counts** (`people_in`) through the following steps:

1. Convert daily boardings to **per-capita mobility intensity**
2. Compute each region’s **structural mobility level**
3. Normalize the daily series by the regional level
4. Apply a **centered 7-day moving average**
5. Construct the final mobility factor

\[
\xi_i(t) = \left(\frac{L_i}{L_{ref}}\right)^{\theta} b_i(t)
\]

where:

- \(L_i\) is the regional structural mobility level,
- \(L_{ref}\) is the reference mobility level across metropolitan regions,
- \(b_i(t)\) is the smoothed within-region temporal mobility variation,
- \(\theta\) is the mobility elasticity parameter.

This repository includes model scripts for three elasticity settings:

- **0.01**
- **0.5**
- **1.0**

## Repository structure

```text
KMOU-A-mobility-informed-SIR-model/
├─ data/
│  ├─ raw/
│  │  ├─ seoul/
│  │  ├─ busan/
│  │  ├─ daegu/
│  │  ├─ daejeon/
│  │  ├─ gwangju/
│  │  └─ nhis/
│  └─ processed/
│     ├─ seoul_metro_daily.csv
│     ├─ busan_metro.csv
│     ├─ daegu_metro.csv
│     ├─ daejeon_metro.csv
│     ├─ gwangju_metro.csv
│     ├─ all_city_metro.csv
│     └─ cases/
│        ├─ Korea_cases.csv
│        ├─ Seoul_cases.csv
│        ├─ Busan_cases.csv
│        ├─ Daegu_cases.csv
│        ├─ Daejeon_cases.csv
│        └─ Gwangju_cases.csv
├─ scripts/
│  ├─ preprocessing/
│  │  ├─ seoul_preprocessing.py
│  │  ├─ busan_preprocessing.py
│  │  ├─ daegu_preprocessing.py
│  │  ├─ daejeon_api_2016.py
│  │  ├─ daejeon_preprocessing.py
│  │  ├─ gwangju_preprocessing.py
│  │  ├─ merge_city_mobility.py
│  │  └─ case_preprocessing.py
│  ├─ analysis/
│  │  └─ mobility_computation.py
│  └─ model/
│     └─ 2016-2017/
│        ├─ regional_rt_theta_001.py
│        ├─ regional_rt_theta_05.py
│        └─ regional_rt_theta_1.py
├─ results/
│  ├─ mobility/
│  │  └─ 2016_2017/
│  │     ├─ 0.01/
│  │     ├─ 0.5/
│  │     └─ 1/
│  ├─ model/
│  │  └─ 2016_2017/
│  │     ├─ 0.01/
│  │     ├─ 0.5/
│  │     └─ 1/
│  └─ figures/
│     └─ model/
│        └─ 2016_2017/
│           ├─ 0.01/
│           ├─ 0.5/
│           └─ 1/
├─ src/
├─ requirements.txt
├─ LICENSE
└─ README.md
```

## Data requirements

### 1. NHIS influenza data

Place the NHIS input file in:

```text
data/raw/nhis/
```

The current preprocessing script expects the file name:

```text
국민건강보험공단_감염성질환(인플루엔자) 의료이용정보_20241231.xlsx
```

The script uses influenza-related diagnosis counts and generates daily case series for:

- Korea
- Seoul
- Busan
- Daegu
- Daejeon
- Gwangju

### 2. Subway mobility data

Place raw metro data in the corresponding folders:

```text
data/raw/seoul/
data/raw/busan/
data/raw/daegu/
data/raw/daejeon/
data/raw/gwangju/
```

The preprocessing scripts produce city-level daily totals with the following harmonized columns:

- `date`
- `city`
- `people_in`
- `people_out`

### 3. Daejeon API data

The Daejeon 2016 preprocessing script uses an API key through the environment variable:

```bash
export DAEJEON_API_KEY="YOUR_KEY_HERE"
```

This script writes the 2016 Daejeon mobility file that is then merged with the later Daejeon data.

## Installation

A recommended setup is:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

This repository uses the following Python packages:

- numpy
- pandas
- scipy
- matplotlib
- requests
- openpyxl

To make repeated runs easier, you may optionally keep environment variables in a small shell file such as `env.example.sh` and load it before running the pipeline:

```bash
source env.example.sh
```

Variables used in this repository:

- `DAEJEON_API_KEY`: required only for `scripts/preprocessing/daejeon_api_2016.py`
- `N_PARTICLES`: optional override for the model particle count during quick tests

## Reproducibility pipeline

Run the scripts in the following order.

### Step 1. Preprocess city-level metro data

```bash
python scripts/preprocessing/seoul_preprocessing.py
python scripts/preprocessing/busan_preprocessing.py
python scripts/preprocessing/daegu_preprocessing.py
python scripts/preprocessing/daejeon_api_2016.py
python scripts/preprocessing/daejeon_preprocessing.py
python scripts/preprocessing/gwangju_preprocessing.py
```

### Step 2. Merge all city-level metro data

```bash
python scripts/preprocessing/merge_city_mobility.py
```

This creates:

```text
data/processed/all_city_metro.csv
```

### Step 3. Compute mobility factors

```bash
python scripts/analysis/mobility_computation.py
```

This creates mobility-factor files under:

```text
results/mobility/2016_2017/0.01/
results/mobility/2016_2017/0.5/
results/mobility/2016_2017/1/
```

### Step 4. Preprocess NHIS influenza case data

```bash
python scripts/preprocessing/case_preprocessing.py
```

This creates daily case series under:

```text
data/processed/cases/
```

### Step 5. Run the model

For each elasticity setting:

```bash
python scripts/model/2016-2017/regional_rt_theta_001.py
python scripts/model/2016-2017/regional_rt_theta_05.py
python scripts/model/2016-2017/regional_rt_theta_1.py
```

Optional: for quick tests, you may reduce the particle count through an environment variable:

```bash
export N_PARTICLES=200000
```

If `N_PARTICLES` is not set, the scripts use their default value.

## Output summary

### Mobility outputs

Generated by `mobility_computation.py`:

```text
results/mobility/2016_2017/{0.01,0.5,1}/
├─ Seoul_gamma.csv
├─ Busan_gamma.csv
├─ Daegu_gamma.csv
├─ Daejeon_gamma.csv
└─ Gwangju_gamma.csv
```

### Model outputs

Generated by the regional model scripts:

```text
results/model/2016_2017/{theta}/beta/
results/model/2016_2017/{theta}/rt/
results/figures/model/2016_2017/{theta}/
```

These outputs include:

- estimated transmission-rate time series (`beta`)
- estimated effective reproduction number time series (`Rt`)
- comparison figures for observed vs. fitted epidemic dynamics

## Interpretation notes

- The model uses **subway boarding counts as a mobility-intensity proxy**, not as an OD matrix.
- `people_out` is preserved in preprocessing outputs for completeness, but the mobility factor is constructed from **boarding counts (`people_in`)**.
- The repository focuses on **regional epidemic heterogeneity**, separating mobility-driven amplification from residual within-region transmission.

## Citation

If you use this repository, please cite both:

1. the associated manuscript, and  
2. this GitHub repository.

Suggested manuscript citation:

> Shin J, Ahn S, Kim M. *A mobility-informed SIR model for regional transmission dynamics: Evidence from subway mobility data in Korea, 2016–2023*.

## License

This repository is distributed under the **GPL-3.0** license. See `LICENSE` for details.
