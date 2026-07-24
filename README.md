# KMOU-A-mobility-informed-SIR-model

Research code and reproducibility materials for the manuscript:

**A Mobility-Informed SIR Model for Evaluating the Effects of Mobility Reduction on Epidemic Transmission and the Instantaneous Reproduction Number**

**Authors:** Jaewan Shin and Minsoo Kim
**Affiliation:** Major of Data Science, Korea Maritime & Ocean University, Busan, Republic of Korea

This repository contains the data-processing pipeline, mobility-factor construction code, and mobility-informed SIR modeling scripts used to evaluate how subway-ridership-based mobility changes are associated with influenza transmission dynamics and the instantaneous reproduction number, denoted as \(R(t)\).

---

## Overview

This project implements a mobility-informed SIR framework for influenza transmission analysis using aggregated public transportation mobility data.

The main idea is to construct a time-varying mobility coefficient, denoted as \(\xi(t)\), from daily subway boarding counts and incorporate it into the infection transmission term of the SIR model. This approach is designed for settings where detailed origin-destination (OD) mobility matrices are unavailable, but aggregated public transportation usage data are accessible.

The repository supports the following analyses:

1. preprocessing of influenza incidence and subway ridership data;
2. construction of subway-ridership-based mobility coefficients \(\xi(t)\);
3. simulation and validation of SIR dynamics under stochastic observation models;
4. estimation of time-varying transmission rates \(\beta(t)\) and instantaneous reproduction numbers \(R(t)\) using particle smoothing;
5. counterfactual mobility-reduction scenarios with 10%, 20%, 30%, 40%, and 50% reductions in observed mobility;
6. generation of model outputs, figures, and scenario summary metrics.

The model should be interpreted as a framework for evaluating transmission changes attributable to mobility variation. The mobility-reduction scenarios are not intended to estimate the full causal effect of a specific public health policy, because real interventions may also change mask use, gathering behavior, testing, hygiene, and other contact-related behaviors.

---

## Study scope

The associated manuscript analyzes four influenza seasons:

| Season label | Analysis period |
|---|---|
| 2016-2017 | 2016-09-01 to 2017-08-31 |
| 2017-2018 | 2017-09-01 to 2018-08-31 |
| 2018-2019 | 2018-09-01 to 2019-08-31 |
| 2022-2023 | 2022-09-01 to 2023-08-31 |

The same modeling framework is applied independently to five metropolitan cities in Korea:

- Seoul
- Busan
- Daegu
- Daejeon
- Gwangju

The currently organized executable pipeline in this repository is centered on the 2016-2017 season. The manuscript and supplementary material also report results for 2017-2018, 2018-2019, and 2022-2023. To reproduce all manuscript and supplementary figures and tables, the corresponding processed inputs and model outputs for those seasons should be added or generated under the same directory structure.

---

## Data sources

The analysis uses three main data types.

| Data type | Description | Use in this repository |
|---|---|---|
| NHIS influenza data | Daily influenza-related medical-use counts using diagnosis codes J09, J10, and J11 | Construction of daily incidence series |
| Subway ridership data | Daily station-level or city-level subway boarding counts | Construction of the mobility coefficient \(\xi(t)\) |
| Population data | Resident registration population statistics | Population denominator for mobility and SIR modeling |

Raw data files are not necessarily committed to this repository because some input files may require separate download, request, or redistribution permission. The raw-data folders are kept as placeholders so that users can place local copies before running the pipeline.

Data sources described in the manuscript include:

- NHIS influenza medical-use data: `https://www.data.go.kr/data/15089429/fileData.do`
- Subway mobility data from public data portals and relevant metropolitan transit authorities
- Resident registration population statistics from the Ministry of the Interior and Safety: `https://jumin.mois.go.kr`

---

## Model summary

### Mobility-informed SIR model

The model follows an SIR compartmental structure with susceptible \(S(t)\), infectious \(I(t)\), recovered \(R(t)\), and total population \(N\). The mobility coefficient \(\xi(t)\) modifies the infection transmission term:

$$
\frac{dS}{dt} = -\xi(t)\beta(t)\frac{S(t)I(t)}{N},
$$

$$
\frac{dI}{dt} = \xi(t)\beta(t)\frac{S(t)I(t)}{N} - \gamma I(t),
$$

$$
\frac{dR}{dt} = \gamma I(t).
$$

The recovery parameter is fixed using the mean infectious period:

$$
\gamma^{-1} = 4.1 \text{ days}.
$$

### Mobility-weighted instantaneous reproduction number

The instantaneous reproduction number is calculated as:

$$
R(t) = \frac{\xi(t)\beta(t)}{\gamma}\frac{S(t)}{N}.
$$

When \(R(t)>1\), transmission is sufficient to sustain epidemic growth under the model assumptions. When \(R(t)<1\), epidemic decline is expected under the same assumptions.

---

## Mobility-factor construction

The mobility coefficient \(\xi(t)\) is constructed from daily subway boarding counts.

Let \(X(t)\) be the total number of subway boardings on day \(t\), and let \(Pop\) be the population denominator. The per-capita mobility intensity is:

$$
m(t) = \frac{X(t)}{Pop}.
$$

The baseline mobility level over the observation period \(T\) is:

$$
L = \frac{1}{|T|}\sum_{t \in T}m(t).
$$

The normalized daily mobility variation is:

$$
c(t) = \frac{m(t)}{L}.
$$

A centered 7-day moving average is applied to reduce weekday-weekend fluctuations:

$$
b(t) = \frac{1}{|W(t)|}\sum_{\mu \in W(t)}c(\mu),
\quad W(t)=\{\mu \in T: |\mu-t|\leq 3\}.
$$

The final mobility coefficient used in the manuscript is:

$$
\xi(t) = b(t).
$$

---

## Mobility-reduction scenarios

The manuscript evaluates counterfactual scenarios in which observed mobility is reduced by a fixed proportion \(c\):

$$
\xi_c(t) = (1-c)\xi(t),
\quad c \in \{0.1,0.2,0.3,0.4,0.5\}.
$$

The scenario-specific instantaneous reproduction number is:

$$
R_c(t) = \frac{\xi_c(t)\beta(t)}{\gamma}\frac{S(t)}{N}.
$$

Scenario summaries include:

$$
\Delta R_c(t) = R_0(t) - R_c(t),
$$

$$
D_c = \sum_t \mathbf{1}\{R_c(t)>1\},
$$

$$
E_c = \sum_t \max(R_c(t)-1,0),
$$

where \(D_c\) is the number of days with \(R(t)>1\), and \(E_c\) is the excess transmission area above the threshold \(R(t)=1\).

---

## Repository structure

```text
KMOU-A-mobility-informed-SIR-model/
├── data/
│ ├── raw/
│ │ ├── busan/
│ │ ├── daegu/
│ │ ├── daejeon/
│ │ ├── gwangju/
│ │ ├── nhis/
│ │ └── seoul/
│ └── processed/
│ └── cases/
├── results/
│ ├── mobility/
│ │ └── 2016_2017/
│ ├── model/
│ │ └── 2016_2017/
│ │ ├── Rt/
│ └── figures/
│ └── model/
│ └── 2016_2017/
├── scripts/
│ ├── preprocessing/
│ │ ├── seoul_preprocessing.py
│ │ ├── busan_preprocessing.py
│ │ ├── daegu_preprocessing.py
│ │ ├── daejeon_api_2016.py
│ │ ├── daejeon_preprocessing.py
│ │ ├── gwangju_preprocessing.py
│ │ ├── merge_city_mobility.py
│ │ └── case_preprocessing.py
│ ├── analysis/
│ │ └── mobility_computation.py
│ └── model/
│ └── 2016-2017/
├── src/
│ └── preprocessing/
│ ├── common.py
│ ├── date_utils.py
│ ├── io_utils.py
│ └── region_utils.py
├── CITATION.cff
├── LICENSE
├── README.md
└── requirements.txt
```

> Note: If the repository currently contains `.CITATION.cff`, rename it to `CITATION.cff` so that GitHub can recognize the citation metadata more clearly.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/jaewansh/KMOU-A-mobility-informed-SIR-model.git
cd KMOU-A-mobility-informed-SIR-model
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Main Python dependencies include:

- `numpy`
- `pandas`
- `scipy`
- `matplotlib`
- `requests`
- `openpyxl`

---

## Data preparation

### 1. NHIS influenza data

Place the NHIS influenza input file in:

```text
data/raw/nhis/
```

The current preprocessing script expects the following file name:

```text
국민건강보험공단_감염성질환(인플루엔자) 의료이용정보_20241231.xlsx
```

The script generates daily influenza case series for:
- Seoul
- Busan
- Daegu
- Daejeon
- Gwangju

### 2. Subway mobility data

Place raw subway mobility files in the corresponding folders:

```text
data/raw/seoul/
data/raw/busan/
data/raw/daegu/
data/raw/daejeon/
data/raw/gwangju/
```

The preprocessing scripts harmonize the mobility data into daily city-level files with columns such as:

```text
date
city
people_in
people_out
```

The mobility coefficient \(\xi(t)\) is constructed from `people_in`, which represents boarding counts. The `people_out` column may be preserved for completeness, but it is not used in the main mobility-factor construction.

### 3. Daejeon API data

The Daejeon 2016 preprocessing script uses an API key through the following environment variable:

```bash
export DAEJEON_API_KEY="YOUR_KEY_HERE"
```

This step is required only when regenerating the 2016 Daejeon mobility input through the API script.

---

## Reproducibility pipeline

Run the scripts in the following order.

### Step 1. Preprocess city-level subway data

```bash
python scripts/preprocessing/seoul_preprocessing.py
python scripts/preprocessing/busan_preprocessing.py
python scripts/preprocessing/daegu_preprocessing.py
python scripts/preprocessing/daejeon_api_2016.py
python scripts/preprocessing/daejeon_preprocessing.py
python scripts/preprocessing/gwangju_preprocessing.py
```

This creates city-level processed mobility files under `data/processed/`, such as:

```text
data/processed/seoul_metro_daily.csv
data/processed/busan_metro.csv
data/processed/daegu_metro.csv
data/processed/daejeon_metro.csv
data/processed/gwangju_metro.csv
```

### Step 2. Merge city-level subway data

```bash
python scripts/preprocessing/merge_city_mobility.py
```

Expected output:

```text
data/processed/all_city_metro.csv
```

### Step 3. Compute mobility factors

```bash
python scripts/analysis/mobility_computation.py
```

Expected output directories:

```text
results/mobility/2016_2017/
```

Preferred mobility output file names are:

```text
Seoul_xi.csv
Busan_xi.csv
Daegu_xi.csv
Daejeon_xi.csv
Gwangju_xi.csv
```

### Step 4. Preprocess NHIS influenza case data

```bash
python scripts/preprocessing/case_preprocessing.py
```

Expected output directory:

```text
data/processed/cases/
```

Expected case files include:

```text
Seoul_cases.csv
Busan_cases.csv
Daegu_cases.csv
Daejeon_cases.csv
Gwangju_cases.csv
```

### Step 5. Run mobility-informed SIR models


Expected output directories:

```text
results/model/2016_2017/
```

For quick tests, the particle count can be reduced through an environment variable if supported by the script:

```bash
export N_PARTICLES=200000
```

---

## Expected outputs

After a successful run, the repository generates:

| Output type | Directory | Description |
|---|---|---|
| Processed mobility data | `data/processed/` | Daily city-level subway boarding data |
| Processed case data | `data/processed/cases/` | Daily influenza incidence series |
| Mobility coefficients | `results/mobility/2016_2017/{theta}/` | Estimated \(\xi(t)\) time series |
| Transmission rates | `results/model/2016_2017/{theta}/beta/` | Estimated \(\beta(t)\) time series |
| Reproduction numbers | `results/model/2016_2017/{theta}/rt/` | Estimated \(R(t)\) time series |
| Figures | `results/figures/model/2016_2017/{theta}/` | Model-fitting and transmission-dynamics figures |

---

## Manuscript and supplementary output map

The manuscript and supplementary material include the following outputs.

| Output | Description | Repository component |
|---|---|---|
| Figure 1 | Conceptual mobility-informed SIR diagram | Conceptual figure; not necessarily generated by script |
| Figure 2 | Mobility-factor construction pipeline | Mobility construction documentation and script |
| Figure 3 | Particle filtering vs. particle smoothing validation | Synthetic validation workflow |
| Figure 4 | Seoul subway-based mobility factor \(\xi(t)\) | `mobility_computation.py` |
| Figure 5 | Observed and simulated incidence, 2016-2017 | model scripts under `scripts/model/2016-2017/` |
| Figure 6 | Estimated \(R(t)\) and \(\beta(t)\), 2016-2017 | model scripts under `scripts/model/2016-2017/` |
| Figure 7 | Seoul heatmaps under mobility-reduction scenarios | scenario output generated from \(R(t)\) files |
| Table 2 | Seoul scenario summary metrics | scenario summary from \(R(t)\) files |
| Figure S1 | RMSE comparison for particle filtering and smoothing | synthetic validation workflow |
| Figures S2-S5 | Additional model-fitting results by season | requires additional seasonal outputs |
| Figures S6-S9 | Heatmaps for Busan, Daegu, Daejeon, and Gwangju | requires scenario outputs for each city |
| Tables S1-S4 | Scenario summary metrics for Busan, Daegu, Daejeon, and Gwangju | requires scenario summary outputs |

To fully reproduce all manuscript and supplementary outputs, add or generate the corresponding files for:

```text
2017_2018
2018_2019
2022_2023
```

using the same structure as:

```text
results/model/2016_2017/
results/figures/model/2016_2017/
results/mobility/2016_2017/
```

---

## Interpretation notes

- Subway boarding counts are used as an aggregated mobility-intensity proxy, not as an origin-destination matrix.
- The mobility coefficient \(\xi(t)\) modifies the transmission term in the SIR model.
- The estimated \(\beta(t)\) should be interpreted as a transmission parameter within the mobility-informed model, not as a purely biological infection rate with all behavioral, environmental, and demographic effects removed.
- Mobility-reduction scenarios scale the observed mobility coefficient only. They should be interpreted as reductions in transmission attributable to changes in mobility, not as the full causal effect of social distancing policies.
- Other forms of travel, vaccination rates, age-specific contact patterns, environmental factors, and behavioral interventions are not explicitly modeled in the current framework.



---

## Citation

If you use this repository, please cite the associated manuscript and this software repository.

Suggested manuscript citation:

> Shin J, Kim M. A Mobility-Informed SIR Model for Evaluating the Effects of Mobility Reduction on Epidemic Transmission and the Instantaneous Reproduction Number. Mathematical Biosciences and Engineering. 2024.

Suggested software citation:

> Shin J, Kim M. KMOU-A-mobility-informed-SIR-model: Research code for a mobility-informed SIR model using subway ridership data and mobility-reduction scenarios. GitHub repository. https://github.com/jaewansh/KMOU-A-mobility-informed-SIR-model

---

## License

This repository is distributed under the GPL-3.0 license. See `LICENSE` for details.

The associated manuscript is a separate scholarly work. The license of the manuscript and the license of this code repository should be interpreted separately.

---

## Contact

For questions about the manuscript or model implementation, please contact:

**Minsoo Kim**
Major of Data Science, Korea Maritime & Ocean University
Email: `hikims@kmou.ac.kr`
