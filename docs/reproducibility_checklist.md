# Reproducibility checklist

This checklist links repository outputs to the manuscript and supplementary material.

## Main manuscript

| Output | Description | Repository requirement |
|---|---|---|
| Figure 1 | Conceptual mobility-informed SIR model diagram | Conceptual figure or manuscript figure |
| Figure 2 | Mobility-factor construction pipeline | Mobility construction documentation and script |
| Figure 3 | Particle filtering and particle smoothing validation | Synthetic validation workflow |
| Figure 4 | Seoul subway-based mobility factor \(\xi(t)\) | Mobility output and plotting workflow |
| Figure 5 | Observed and simulated incidence, 2016-2017 season | 2016-2017 model output |
| Figure 6 | Estimated \(R(t)\) and \(\beta(t)\), 2016-2017 season | 2016-2017 model output |
| Figure 7 | Seoul heatmaps under mobility-reduction scenarios | Heatmap workflow and scenario outputs |
| Table 2 | Seoul scenario summary metrics | Scenario summary table |

## Supplementary material

| Output | Description | Repository requirement |
|---|---|---|
| Figure S1 | Time-resolved RMSE comparison between particle filtering and particle smoothing | Synthetic validation workflow |
| Figure S2 | Gwangju 2016-2017 model fitting result | 2016-2017 model output |
| Figure S3 | 2017-2018 model fitting and transmission dynamics | 2017-2018 model output |
| Figure S4 | 2018-2019 model fitting and transmission dynamics | 2018-2019 model output |
| Figure S5 | 2022-2023 model fitting and transmission dynamics | 2022-2023 model output |
| Figure S6 | Busan heatmap under mobility-reduction scenarios | Scenario heatmap output |
| Figure S7 | Daegu heatmap under mobility-reduction scenarios | Scenario heatmap output |
| Figure S8 | Daejeon heatmap under mobility-reduction scenarios | Scenario heatmap output |
| Figure S9 | Gwangju heatmap under mobility-reduction scenarios | Scenario heatmap output |
| Tables S1-S4 | Scenario summary metrics for Busan, Daegu, Daejeon, and Gwangju | Scenario summary table |

## Complete reproduction target

A complete release should include processed inputs or generated outputs for:

```text
Cities:
Seoul, Busan, Daegu, Daejeon, Gwangju

Seasons:
2016_2017, 2017_2018, 2018_2019, 2022_2023
```

## Release checks

Before creating a public release, confirm that:

- `README.md` contains the final manuscript title and author list.
- `CITATION.cff` exists at the repository root.
- Legacy mobility output names using `gamma` are either renamed to `xi` or clearly documented.
- Raw data redistribution rules have been checked.
- Processed data or reconstruction instructions are available.
- The repository can be cloned and the documented commands can be run without local absolute paths.
