from pathlib import Path
from scipy.stats import nbinom
import numpy as np
import matplotlib.pyplot as pt
import time
import pandas as pd


CASE_DIR = Path("data/processed/cases")
GAMMA_DIR = Path("results/mobility/2016_2017/0.01")
BETA_OUT_DIR = Path("results/model/2016_2017/0.01/beta")
FIG_OUT_DIR = Path("results/figures/model/2016_2017/0.01")


def moving_average(x, w):
    x = np.asarray(x, dtype=float)
    kernel = np.ones(w)

    num = np.convolve(x, kernel, mode="same")
    den = np.convolve(np.ones(len(x)), kernel, mode="same")

    return num / den


def transform_datetype(df):
    df["date"] = pd.to_datetime(df["date"])
    return df


def main():
    BETA_OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_OUT_DIR.mkdir(parents=True, exist_ok=True)
    print("Regional Rt model start")


if __name__ == "__main__":
    main()
