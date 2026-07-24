# Scripts

This directory contains preprocessing, analysis, and model scripts for the mobility-informed SIR repository.

## Recommended execution order

### 1. Preprocess subway mobility data

```bash
python scripts/preprocessing/seoul_preprocessing.py
python scripts/preprocessing/busan_preprocessing.py
python scripts/preprocessing/daegu_preprocessing.py
python scripts/preprocessing/daejeon_api_2016.py
python scripts/preprocessing/daejeon_preprocessing.py
python scripts/preprocessing/gwangju_preprocessing.py
```

### 2. Merge city-level mobility files

```bash
python scripts/preprocessing/merge_city_mobility.py
```

### 3. Construct mobility coefficients

```bash
python scripts/analysis/mobility_computation.py
```

### 4. Preprocess influenza case data

```bash
python scripts/preprocessing/case_preprocessing.py
```

### 5. Run the 2016-2017 model scripts

```bash
python scripts/model/2016-2017/regional_rt.py
```

## Notation rule

Use `xi` for the subway-ridership-based mobility coefficient \(\xi(t)\). Use `gamma` only for the SIR recovery-rate parameter \(\gamma\).
