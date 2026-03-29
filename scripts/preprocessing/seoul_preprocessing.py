from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw/seoul")
OUTPUT_DIR = Path("data/processed")

STATION_INFO_PATH = RAW_DIR / "seoul-metro-station-info.csv"

FILE_2016 = RAW_DIR / "seoul-metro-2016.logs.csv"
FILE_2017 = RAW_DIR / "seoul-metro-2017.csv"
FILE_2018 = RAW_DIR / "seoul-metro-2018.logs.csv"
FILE_2019 = RAW_DIR / "seoul-metro-2019.logs.csv"
FILE_2020 = RAW_DIR / "seoul-metro-2020.logs.csv"
FILE_2021 = RAW_DIR / "seoul-metro-2021.logs.csv"
FILE_2022 = RAW_DIR / "seoul-metro-2022.csv"
FILE_2023 = RAW_DIR / "seoul-metro-2023.logs.csv"
FILE_2024 = RAW_DIR / "seoul-metro-2024.logs.csv"

OUTPUT_PATH = OUTPUT_DIR / "seoul_metro_daily.csv"

def main():


station_info = pd.read_csv(STATION_INFO_PATH)

df_2016 = pd.read_csv(FILE_2016)
df_2017 = pd.read_csv(FILE_2017)
df_2018 = pd.read_csv(FILE_2018)
df_2019 = pd.read_csv(FILE_2019)
df_2020 = pd.read_csv(FILE_2020)
df_2021 = pd.read_csv(FILE_2021)
df_2022 = pd.read_csv(FILE_2022)
df_2023 = pd.read_csv(FILE_2023)
df_2024 = pd.read_csv(FILE_2024)


df_2022['station_code'] = pd.to_numeric(df_2022['station_code'], errors='coerce').fillna(0).astype(int)
df_2022['people_in'] = pd.to_numeric(df_2022['people_in'], errors='coerce').fillna(0).astype(int)
df_2022['people_out'] = pd.to_numeric(df_2022['people_out'], errors='coerce').fillna(0).astype(int)

df = pd.concat([
    df_2016, df_2017, df_2018, df_2019,
    df_2020, df_2021, df_2022, df_2023, df_2024
], ignore_index=True)


df = pd.merge(
    df,
    station_info,
    left_on='station_code',
    right_on='station.code',
    how='inner'
)


df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df['date'] = (df['timestamp'] - pd.Timedelta(hours=4)).dt.normalize()

daily = (
    df.groupby('date')[['people_in', 'people_out']]
    .sum()
    .reset_index()
    .sort_values('date')
)

daily['city'] = 'seoul'
daily = daily[['date', 'city', 'people_in', 'people_out']]

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
daily.to_csv(OUTPUT_PATH, index=False, encoding='utf-8')

print("Saved:", OUTPUT_PATH)
print(daily.head())

if **name** == "**main**":
main()
