# KMOU-A-mobility-informed-SIR-model

## Overview

This repository provides reproducible code for a mobility-informed SIR model that incorporates subway-based mobility to analyze regional influenza transmission dynamics.

## Study Description

This study integrates mobility data derived from subway boarding records into an SIR framework to capture spatial heterogeneity in influenza transmission. The model aims to improve estimation of transmission dynamics by accounting for region-specific mobility patterns.

## Repository Structure

* `data/` : Processed mobility and epidemiological data
* `src/` : Core model implementation (SIR + mobility)
* `scripts/` : Data preprocessing, model fitting, and simulation scripts
* `results/` : Generated figures and tables for the manuscript

## Reproducibility

To reproduce the results:

1. Prepare the data in the `data/` directory
2. Run preprocessing scripts
3. Execute model fitting
4. Generate figures and tables

## Data Availability

Due to data usage restrictions (e.g., NHIS data), raw data may not be publicly available. Processed or synthetic data may be provided where possible.

## Code Availability

All code used for analysis and figure generation is available in this repository.

## Citation

If you use this code, please cite the associated paper:

> (Your paper citation will be added here after publication)

## License

MIT License
