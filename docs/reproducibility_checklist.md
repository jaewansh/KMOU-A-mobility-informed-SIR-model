# Reproducibility checklist

This checklist links repository files to the manuscript and supplementary material.

## Main manuscript

| Output | Manuscript location | Repository component |
|---|---|---|
| Figure 1 | Mobility-informed SIR conceptual diagram | Manuscript figure |
| Figure 2 | Mobility-factor construction pipeline | `01_mobility_factor_2016_2017.ipynb` and `docs/model_and_notation.md` |
| Figure 3 | Particle filtering and particle smoothing comparison | `02_sir_negative_binomial_particle_smoothing.ipynb` |
| Figure 4 | Seoul subway-based mobility factor \(\xi(t)\) | `01_mobility_factor_2016_2017.ipynb` |
| Figure 5 | 2016-2017 observed and simulated incidence | `03_rt_estimation_2016_2017.ipynb` |
| Figure 6 | 2016-2017 \(R(t)\) and \(\beta(t)\) | `03_rt_estimation_2016_2017.ipynb` |
| Figure 7 | Seoul heatmaps under mobility-reduction scenarios | `04_rt_heatmap_scenarios.ipynb` |
| Table 2 | Seoul scenario summary metrics | `05_scenario_summary_tables.ipynb` and `results/tables/scenario_summary_reference.csv` |

## Supplementary material

| Output | Supplementary location | Repository component |
|---|---|---|
| Figure S1 | Time-resolved RMSE comparison | `02_sir_negative_binomial_particle_smoothing.ipynb` |
| Figure S2 | Gwangju 2016-2017 fitting result | `03_rt_estimation_2016_2017.ipynb` |
| Figure S3 | 2017-2018 fitting and transmission dynamics | requires 2017-2018 Rt outputs |
| Figure S4 | 2018-2019 fitting and transmission dynamics | requires 2018-2019 Rt outputs |
| Figure S5 | 2022-2023 fitting and transmission dynamics | requires 2022-2023 Rt outputs |
| Figure S6 | Busan heatmap | `04_rt_heatmap_scenarios.ipynb` |
| Figure S7 | Daegu heatmap | `04_rt_heatmap_scenarios.ipynb` |
| Figure S8 | Daejeon heatmap | `04_rt_heatmap_scenarios.ipynb` |
| Figure S9 | Gwangju heatmap | `04_rt_heatmap_scenarios.ipynb` |
| Tables S1-S4 | Scenario summary tables for Busan, Daegu, Daejeon, and Gwangju | `05_scenario_summary_tables.ipynb` and `results/tables/scenario_summary_reference.csv` |

## Required release checks

Before final release, confirm that:

- The five uploaded notebooks are stored under `notebooks/` with the file names listed in `notebooks/README.md`.
- `CITATION.cff` exists at the repository root.
- `paper/Manuscript.pdf` and `paper/MBE_suppliments.pdf` are included if redistribution is allowed.
- The repository documentation states that code column `gamma` corresponds to manuscript \(\xi(t)\).
- No `theta` parameter is documented as part of the manuscript workflow.
- `scripts/patch_notebook_paths.py` has been run after moving the uploaded notebooks.
- `scripts/check_repository.py` passes before release.
- The \(R(t)\) CSV files for 2017-2018, 2018-2019, and 2022-2023 are included if full supplementary reproduction is required.
