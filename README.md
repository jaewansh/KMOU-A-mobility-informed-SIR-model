# KMOU-A-mobility-informed-SIR-model

Research code and reproducibility materials for the manuscript:

**A Mobility-Informed SIR Model for Evaluating the Effects of Mobility Reduction on Epidemic Transmission and the instantaneous Reproduction Number**

**Authors:** Jaewan Shin and Minsoo Kim  
**Affiliation:** Major of Data Science, Korea Maritime & Ocean University, Busan, Republic of Korea

This repository contains the notebooks and supporting documentation used to construct subway-ridership-based mobility coefficients, estimate time-varying transmission dynamics with a mobility-informed SIR model, and evaluate mobility-reduction scenarios for influenza transmission.

---

## Overview

This study proposes a mobility-informed SIR model for epidemic simulation when detailed origin-destination mobility matrices are unavailable.

The workflow uses daily aggregated subway boarding counts to construct a time-varying mobility coefficient, denoted by \(\xi(t)\) in the manuscript. The coefficient modifies the infection transmission term in the SIR model. Time-varying transmission rates \(\beta(t)\) and instantaneous reproduction numbers \(R(t)\) are then estimated using particle smoothing under a negative binomial observation model.

The repository is organized around the five uploaded notebooks:

| Order | Notebook | Main role |
|---|---|---|
| 1 | `notebooks/01_mobility_factor_2016_2017.ipynb` | Constructs \(m(t)\), \(L\), \(c(t)\), \(b(t)\), and mobility-reduction scenario columns from subway boarding data |
| 2 | `notebooks/02_sir_negative_binomial_particle_smoothing.ipynb` | Validates particle filtering and particle smoothing using a synthetic SIR trajectory with a negative binomial observation model |
| 3 | `notebooks/03_rt_estimation_2016_2017.ipynb` | Estimates \(\beta(t)\), simulated incidence, and \(R(t)\) for the 2016-2017 influenza season |
| 4 | `notebooks/04_rt_heatmap_scenarios.ipynb` | Generates heatmaps of \(R(t)\) under observed mobility and 10-50% mobility-reduction scenarios |
| 5 | `notebooks/05_scenario_summary_tables.ipynb` | Generates scenario summary metrics such as mean \(R(t)\), days with \(R(t)>1\), and excess transmission area |

---

## Important source-code notation

The manuscript denotes the mobility coefficient as:

\[
\xi(t)
\]

However, the uploaded mobility-factor notebook stores this same mobility coefficient in columns named:

```text
gamma
gamma_1
gamma_2
gamma_3
gamma_4
gamma_5
```

In this repository, these column names are preserved because they are used by the attached notebooks. They should be interpreted as follows:

| Code column | Manuscript notation | Meaning |
|---|---|---|
| `gamma` | \(\xi(t)\) | Observed subway-ridership-based mobility coefficient |
| `gamma_1` | \(0.9\xi(t)\) | 10% mobility-reduction scenario |
| `gamma_2` | \(0.8\xi(t)\) | 20% mobility-reduction scenario |
| `gamma_3` | \(0.7\xi(t)\) | 30% mobility-reduction scenario |
| `gamma_4` | \(0.6\xi(t)\) | 40% mobility-reduction scenario |
| `gamma_5` | \(0.5\xi(t)\) | 50% mobility-reduction scenario |

The SIR recovery rate is not stored in these mobility-factor columns. In the `Rt(2016~2017).ipynb` notebook, the recovery rate is represented by:

```python
sigma = 1.0 / 4.1
```

No `theta` parameter is used in the attached manuscript or the attached notebooks.

---

## Study scope

The manuscript analyzes four influenza seasons:

| Season label | Analysis period |
|---|---|
| `2016~2017` | 2016-09-01 to 2017-08-31 |
| `2017~2018` | 2017-09-01 to 2018-08-31 |
| `2018~2019` | 2018-09-01 to 2019-08-31 |
| `2022~2023` | 2022-09-01 to 2023-08-31 |

The model is applied independently to five analysis labels:

```text
Seoul
Busan
Daegu
Daejeon
Gwangju
```

The attached executable `Rt(2016~2017).ipynb` notebook focuses on the 2016-2017 season. The heatmap and scenario-table notebooks expect \(R(t)\) files for all four seasons.

---

## Model summary

The mobility-informed SIR model is:

\[
\frac{dS}{dt} = -\xi(t)\beta(t)\frac{S(t)I(t)}{N},
\]

\[
\frac{dI}{dt} = \xi(t)\beta(t)\frac{S(t)I(t)}{N} - \gamma I(t),
\]

\[
\frac{dR}{dt} = \gamma I(t).
\]

The mobility-weighted instantaneous reproduction number is:

\[
R(t)=\frac{\xi(t)\beta(t)}{\gamma}\frac{S(t)}{N}.
\]

The recovery parameter is fixed using a mean infectious period of 4.1 days:

\[
\gamma^{-1}=4.1.
\]

---

## Mobility-factor construction

The mobility coefficient is constructed from daily subway boarding counts.

Let \(X(t)\) be the total number of subway boardings on day \(t\), and let \(Pop\) be the population denominator. The per-capita mobility intensity is:

\[
m(t)=\frac{X(t)}{Pop}.
\]

The baseline mobility level in the manuscript is:

\[
L=\frac{1}{|T|}\sum_{t\in T}m(t).
\]

The normalized mobility variation is:

\[
c(t)=\frac{m(t)}{L}.
\]

A centered 7-day moving average is applied:

\[
b(t)=\frac{1}{|W(t)|}\sum_{\mu\in W(t)}c(\mu),
\quad W(t)=\{\mu\in T: |\mu-t|\leq 3\}.
\]

The final manuscript mobility factor is:

\[
\xi(t)=b(t).
\]

Implementation note: the uploaded `mobility factor(2016~2017).ipynb` notebook first creates `m_7`, a centered 7-day moving average of `m`, and then computes `L` as the city-level mean of `m_7`. The notebook then computes `c = m / L`, `b` as a centered 7-day moving average of `c`, and writes `gamma = b`. This implementation note is documented here so that the GitHub explanation follows the attached code exactly.

---

## Mobility-reduction scenarios

The uploaded mobility-factor notebook creates five reduced-mobility columns:

\[
0.9\xi(t),\;0.8\xi(t),\;0.7\xi(t),\;0.6\xi(t),\;0.5\xi(t).
\]

These correspond to 10%, 20%, 30%, 40%, and 50% reductions in observed mobility.

For each scenario, the notebook computes:

\[
R_c(t)=\frac{\xi_c(t)\beta(t)}{\gamma}\frac{S(t)}{N}.
\]

The scenario summary notebook computes:

\[
\Delta R_c(t)=R_0(t)-R_c(t),
\]

\[
D_c=\sum_t \mathbf{1}\{R_c(t)>1\},
\]

\[
E_c=\sum_t \max(R_c(t)-1,0).
\]

---

## Repository structure

```text
KMOU-A-mobility-informed-SIR-model/
├── README.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── environment.yml
├── data/
│   ├── README.md
│   ├── metro/
│   ├── NHIS/
│   │   └── 2016~2017/
│   ├── mobility_factor/
│   │   └── 2016~2017/
│   ├── Rt/
│   │   ├── 2016~2017/
│   │   ├── 2017~2018/
│   │   ├── 2018~2019/
│   │   └── 2022~2023/
│   └── population_denominators_2016_2017.csv
├── notebooks/
│   ├── README.md
│   ├── 01_mobility_factor_2016_2017.ipynb
│   ├── 02_sir_negative_binomial_particle_smoothing.ipynb
│   ├── 03_rt_estimation_2016_2017.ipynb
│   ├── 04_rt_heatmap_scenarios.ipynb
│   └── 05_scenario_summary_tables.ipynb
├── figures/
│   ├── README.md
│   ├── mobility_factor/
│   ├── 2016~2017/
│   ├── HeatMap/
│   └── validation/
├── results/
│   ├── README.md
│   ├── tables/
│   │   └── scenario_summary_reference.csv
│   └── validation/
├── paper/
│   ├── README.md
│   ├── Manuscript.pdf
│   └── MBE_suppliments.pdf
├── scripts/
│   ├── patch_notebook_paths.py
│   └── check_repository.py
└── docs/
    ├── code_inventory.md
    ├── data_sources.md
    ├── model_and_notation.md
    ├── output_manifest.md
    ├── region_definitions.md
    └── reproducibility_checklist.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jaewansh/KMOU-A-mobility-informed-SIR-model.git
cd KMOU-A-mobility-informed-SIR-model
```

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Alternatively, create the conda environment:

```bash
conda env create -f environment.yml
conda activate mobility-informed-sir
```

---

## Required input files

### Subway mobility input

The mobility-factor notebook expects city-level daily subway files. Place them in:

```text
data/metro/
```

Recommended file names:

```text
seoul&g_metro.csv
busan_metro.csv
daejeon_metro.csv
daegu_metro.csv
gwangju_metro.csv
```

Required columns:

```text
date
city
people_in
```

The analysis uses `people_in`, corresponding to subway boarding counts.

### NHIS influenza input

The \(R(t)\) estimation notebook expects city-level daily influenza case files in:

```text
data/NHIS/2016~2017/
```

Expected 2016-2017 file names:

```text
Seoul&Gyeonggi_cases(2016~2017).csv
Busan_cases(2016~2017).csv
Daejeon_cases(2016~2017).csv
Daegu_cases(2016~2017).csv
Gwangju_cases(2016~2017).csv
```

The notebooks use diagnosis-code-based daily influenza incidence prepared from J09, J10, and J11 records.

---

## Notebook path update

The uploaded notebooks originally contained local absolute paths from the author’s computer. After renaming the notebooks, run:

```bash
python scripts/patch_notebook_paths.py
```

Then verify that no local absolute paths remain:

```bash
python scripts/check_repository.py
```

---

## Notebook execution order

Run the notebooks in this order.

### 1. Construct mobility factors

```text
notebooks/01_mobility_factor_2016_2017.ipynb
```

Main outputs:

```text
data/mobility_factor/2016~2017/Seoul_gamma.csv
data/mobility_factor/2016~2017/Busan_gamma.csv
data/mobility_factor/2016~2017/Daegu_gamma.csv
data/mobility_factor/2016~2017/Daejeon_gamma.csv
data/mobility_factor/2016~2017/Gwangju_gamma.csv
```

### 2. Validate particle smoothing under negative binomial observation

```text
notebooks/02_sir_negative_binomial_particle_smoothing.ipynb
```

Main outputs:

```text
results/validation/daily_rmse_results.csv
figures/validation/SIR Mathematical Model Negative binomial distribution RMSE.eps
```

### 3. Estimate \(R(t)\) for the 2016-2017 season

```text
notebooks/03_rt_estimation_2016_2017.ipynb
```

Main outputs:

```text
data/Rt/2016~2017/Seoul_Rt(2016~2017).csv
data/Rt/2016~2017/Busan_Rt(2016~2017).csv
data/Rt/2016~2017/Daegu_Rt(2016~2017).csv
data/Rt/2016~2017/Daejeon_Rt(2016~2017).csv
data/Rt/2016~2017/Gwangju_Rt(2016~2017).csv
```

### 4. Generate heatmaps

```text
notebooks/04_rt_heatmap_scenarios.ipynb
```

This notebook reads \(R(t)\) files from:

```text
data/Rt/2016~2017/
data/Rt/2017~2018/
data/Rt/2018~2019/
data/Rt/2022~2023/
```

and generates heatmaps for Seoul, Busan, Daegu, Daejeon, and Gwangju.

### 5. Generate scenario summary tables

```text
notebooks/05_scenario_summary_tables.ipynb
```

This notebook computes mean \(R(t)\), reduction in mean \(R(t)\), days with \(R(t)>1\), reduction in days with \(R(t)>1\), and excess transmission area.

---

## Output column conventions

For a city named `City`, the \(R(t)\) CSV files use the following columns:

| Column | Meaning |
|---|---|
| `date` | Daily date |
| `City_Rt` | Baseline \(R(t)\) using observed mobility |
| `City_Rt_1` | \(R(t)\) under 10% mobility reduction |
| `City_Rt_2` | \(R(t)\) under 20% mobility reduction |
| `City_Rt_3` | \(R(t)\) under 30% mobility reduction |
| `City_Rt_4` | \(R(t)\) under 40% mobility reduction |
| `City_Rt_5` | \(R(t)\) under 50% mobility reduction |

---

## Reference scenario summary

A reference summary table transcribed from the manuscript and supplementary material is provided at:

```text
results/tables/scenario_summary_reference.csv
```

This file includes the Seoul Table 2 values and Supplementary Tables S1-S4 for Busan, Daegu, Daejeon, and Gwangju.

---


## License

The manuscript is distributed under the Creative Commons Attribution License as stated in the article.

The code repository is distributed under the license specified in the `LICENSE` file.

---

## Contact

**Minsoo Kim**  
Major of Data Science, Korea Maritime & Ocean University  
Email: hikims@kmou.ac.kr
