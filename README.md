# KMOU-A-mobility-informed-SIR-model

## Overview

This repository provides reproducible code for a mobility-informed SIR model to analyze regional influenza transmission dynamics in Korea.
The study integrates subway-based mobility data and NHIS case data to estimate transmission dynamics across metropolitan areas.

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
│   └── nhis/                # NHIS raw data
├── processed/
│   ├── metro/              # preprocessed metro data
│   └── cases/              # preprocessed case data
└── sample/                 # optional sample data

scripts/
├── preprocessing/
│   ├── *_preprocessing.py
│   ├── daejeon_api_2016.py
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
```

---

## Reproducibility (Execution Order)

To reproduce the results, run the scripts in the following order:

### 1. City-level preprocessing

```bash
python scripts/preprocessing/seoul_preprocessing.py
python scripts/preprocessing/busan_preprocessing.py
python scripts/preprocessing/daegu_preprocessing.py
python scripts/preprocessing/gwangju_preprocessing.py
python scripts/preprocessing/daejeon_api_2016.py
python scripts/preprocessing/daejeon_preprocessing.py
```

### 2. Merge mobility data

```bash
python scripts/preprocessing/merge_city_mobility.py
```

### 3. Compute mobility variables

```bash
python scripts/analysis/mobility_computation.py
```

### 4. Preprocess NHIS case data

```bash
python scripts/preprocessing/case_preprocessing.py
```

### 5. Run SIR model

```bash
python scripts/model/regional_rt_theta_001.py
```

---

## Data Availability

NHIS data are not publicly available due to privacy restrictions.

Users with authorized access should place raw data in:

```text
data/raw/nhis/
```

Metro data should be placed in:

```text
data/raw/{city}/
```

The directory structure must be preserved for the scripts to run correctly.

---

## Code Availability

The code used in this study is publicly available at:

https://github.com/jaewansh/KMOU-A-mobility-informed-SIR-model

The version used for manuscript submission corresponds to release:

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

If you use this code, please cite:

> (To be updated with the published article)

---

## License

MIT License
