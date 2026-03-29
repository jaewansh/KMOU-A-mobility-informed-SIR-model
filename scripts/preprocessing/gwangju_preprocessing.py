from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw/gwangju")
OUTPUT_DIR = Path("data/processed")

def process_2016():
df = pd.read_csv(
RAW_DIR / "광주교통공사_일별승하차인원_20161231.csv",
encoding="euc-kr"
)


df.columns = ["date", "people_in", "people_out"]

df["people_in"] = df["people_in"].astype(int)
df["people_out"] = df["people_out"].astype(int)

df.to_csv(OUTPUT_DIR / "gwangju_metro(2016).csv")


def process_2017():
df_raw = pd.read_csv(
RAW_DIR / "광주광역시도시철도공사_2017년도_역,일,시간대별 승하차량.csv",
encoding="euc-kr"
)


time_cols = df_raw.columns[4:]
for col in time_cols:
    df_raw[col] = pd.to_numeric(df_raw[col], errors="coerce").fillna(0)

df_raw["total"] = df_raw[time_cols].sum(axis=1)

df = df_raw[["날짜", "역번호", "역명", "승하차구분", "total"]].copy()
df.columns = ["date", "station_id", "station_name", "type", "total"]

df["type"] = df["type"].replace({"승차": "people_in", "하차": "people_out"})

df_pivoted = df.pivot_table(
    index=["date", "station_id", "station_name"],
    columns="type",
    values="total",
    aggfunc="sum"
).reset_index()

df_pivoted = df_pivoted.fillna(0)
df_pivoted["people_in"] = df_pivoted["people_in"].astype(int)
df_pivoted["people_out"] = df_pivoted["people_out"].astype(int)

total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
total_df.to_csv(OUTPUT_DIR / "gwangju_metro(2017).csv")


def process_2018_2022():
df_raw_1 = pd.read_csv(
RAW_DIR / "광주광역시도시철도공사_2018년도_역,일,시간대별 승하차량.csv",
encoding="euc-kr"
)
df_raw_2 = pd.read_csv(
RAW_DIR / "광주광역시도시철도공사_2019년도_역,일,시간대별 승하차량.csv",
encoding="euc-kr"
)
df_raw_3 = pd.read_csv(
RAW_DIR / "광주광역시도시철도공사_2020년도_역,일,시간대별 승하차량 .csv",
encoding="euc-kr"
)
df_raw_4 = pd.read_csv(
RAW_DIR / "광주광역시도시철도공사_2021년도_역,일,시간대별 승하차량.csv",
encoding="euc-kr"
)
df_raw_5 = pd.read_csv(
RAW_DIR / "광주광역시도시철도공사_2022년도_역,일,시간대별 승하차량.csv",
encoding="utf-8"
)


df_raw = pd.concat([df_raw_1, df_raw_2, df_raw_3, df_raw_4, df_raw_5], ignore_index=True)

time_cols = df_raw.columns[4:]
for col in time_cols:
    df_raw[col] = pd.to_numeric(df_raw[col], errors="coerce").fillna(0)

df_raw["total"] = df_raw[time_cols].sum(axis=1)

df = df_raw[["일자", "역번호", "역명", "구분", "total"]].copy()
df.columns = ["date", "station_id", "station_name", "type", "total"]

df["type"] = df["type"].str.strip()
df["type"] = df["type"].replace({
    "승차": "people_in",
    "하차": "people_out",
    "하자": "people_out"
})

df_pivoted = df.pivot_table(
    index=["date", "station_id", "station_name"],
    columns="type",
    values="total",
    aggfunc="sum"
).reset_index()

df_pivoted = df_pivoted.fillna(0)
df_pivoted["people_in"] = df_pivoted["people_in"].astype(int)
df_pivoted["people_out"] = df_pivoted["people_out"].astype(int)

total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
total_df.to_csv(OUTPUT_DIR / "gwangju_metro(2018~2022).csv")


def process_2023_2024():
df_raw_1 = pd.read_csv(
RAW_DIR / "광주교통공사_2023년도_역,일,시간대별 승하차량.csv",
encoding="euc-kr"
)
df_raw_2 = pd.read_csv(
RAW_DIR / "광주교통공사_2024년도_역,일,시간대별 승하차량.csv",
encoding="euc-kr"
)


df_raw = pd.concat([df_raw_1, df_raw_2], ignore_index=True)

time_cols = df_raw.columns[4:]
for col in time_cols:
    df_raw[col] = pd.to_numeric(df_raw[col], errors="coerce").fillna(0)

df_raw["total"] = df_raw[time_cols].sum(axis=1)

df = df_raw[["일자", "역번호", "역명", "구분", "total"]].copy()
df.columns = ["date", "station_id", "station_name", "type", "total"]

df["type"] = df["type"].str.strip()
df["type"] = df["type"].replace({
    "승차": "people_in",
    "하차": "people_out",
    "하자": "people_out"
})

df_pivoted = df.pivot_table(
    index=["date", "station_id", "station_name"],
    columns="type",
    values="total",
    aggfunc="sum"
).reset_index()

df_pivoted = df_pivoted.fillna(0)
df_pivoted["people_in"] = df_pivoted["people_in"].astype(int)
df_pivoted["people_out"] = df_pivoted["people_out"].astype(int)

total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
total_df.to_csv(OUTPUT_DIR / "gwangju_metro(2023~2024).csv")


def merge_all():
df_1 = pd.read_csv(OUTPUT_DIR / "gwangju_metro(2016).csv", index_col=0)
df_2 = pd.read_csv(OUTPUT_DIR / "gwangju_metro(2017).csv", index_col=0)
df_3 = pd.read_csv(OUTPUT_DIR / "gwangju_metro(2018~2022).csv", index_col=0)
df_4 = pd.read_csv(OUTPUT_DIR / "gwangju_metro(2023~2024).csv", index_col=0)


df = pd.concat([df_1, df_2, df_3, df_4], ignore_index=True)
df["city"] = "gwangju"
df = df[["date", "city", "people_in", "people_out"]]
df.info()

df.to_csv(OUTPUT_DIR / "gwangju_metro.csv")


def main():
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


process_2016()
process_2017()
process_2018_2022()
process_2023_2024()
merge_all()

print("Saved:", OUTPUT_DIR / "gwangju_metro.csv")


if __name__ == "__main__":
main()
