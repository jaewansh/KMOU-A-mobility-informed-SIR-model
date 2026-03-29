from pathlib import Path
import pandas as pd
import numpy as np

DATA_DIR = Path("data/processed")
OUTPUT_DIR = Path("results/mobility/2016_2017")

def save_gamma_by_city(target_daily, theta, output_dir):
target_daily["gamma"] = ((target_daily["L_i"] / target_daily["L_ref"]) ** theta) * target_daily["b"]

```
seoul_data = target_daily[target_daily["city"] == "seoul"]
busan_data = target_daily[target_daily["city"] == "busan"]
daegu_data = target_daily[target_daily["city"] == "daegu"]
daejeon_data = target_daily[target_daily["city"] == "daejeon"]
gwangju_data = target_daily[target_daily["city"] == "gwangju"]

theta_dir = output_dir / str(theta)
theta_dir.mkdir(parents=True, exist_ok=True)

seoul_data.to_csv(theta_dir / "Seoul_gamma.csv", index=False)
busan_data.to_csv(theta_dir / "Busan_gamma.csv", index=False)
daegu_data.to_csv(theta_dir / "Daegu_gamma.csv", index=False)
daejeon_data.to_csv(theta_dir / "Daejeon_gamma.csv", index=False)
gwangju_data.to_csv(theta_dir / "Gwangju_gamma.csv", index=False)
```

def main():
df = pd.read_csv(DATA_DIR / "all_city_metro.csv")

```
df["date"] = pd.to_datetime(df["date"])
df.sort_values(["date"], inplace=True)

daily = df[df["date"].between("2016-09-01", "2017-08-31")]
daily.info()

pop_map = {
    "seoul": 22_689_358.5,
    "busan": 3_484_591,
    "daejeon": 1_508_298.5,
    "daegu": 2_479_894,
    "gwangju": 1_466_492
}

target_gus = list(pop_map.keys())

target_daily = (
    daily[daily["city"].isin(target_gus)]
    .groupby(["city", "date"], as_index=False)["people_in"]
    .sum()
    .sort_values(["city", "date"])
)

target_daily["pop"] = target_daily["city"].map(pop_map)

target_daily["m"] = target_daily["people_in"] / target_daily["pop"]

target_daily["m_7"] = (
    target_daily
    .groupby(["city"])["m"]
    .transform(lambda s: s.rolling(window=7, center=True, min_periods=1).mean())
)

L = target_daily.groupby("city")["m_7"].mean()
L_ref = L.mean()

target_daily["L"] = (
    target_daily
    .groupby(["city"])["m_7"]
    .transform("mean")
)

target_daily["b"] = target_daily["m_7"] / target_daily["L"]

print("L_i (지역별 레벨, 기간 평균 m):")
print(L)
print("\nL_ref (광역시 L_i 평균):", L_ref)

target_daily["L_i"] = target_daily["city"].map(L)
target_daily["L_ref"] = L_ref

save_gamma_by_city(target_daily.copy(), 1, OUTPUT_DIR)
save_gamma_by_city(target_daily.copy(), 0.5, OUTPUT_DIR)
save_gamma_by_city(target_daily.copy(), 0.4, OUTPUT_DIR)
save_gamma_by_city(target_daily.copy(), 0.2, OUTPUT_DIR)
save_gamma_by_city(target_daily.copy(), 0.1, OUTPUT_DIR)
save_gamma_by_city(target_daily.copy(), 0.01, OUTPUT_DIR)

print("Saved gamma files to:", OUTPUT_DIR)
```

if **name** == "**main**":
main()
