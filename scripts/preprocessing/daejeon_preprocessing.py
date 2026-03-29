from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw/daejeon")
OUTPUT_DIR = Path("data/processed")

def process_2017_2024():
df_raw_1 = pd.read_csv(
RAW_DIR / "대전광역시도시철도공사_시간대별 승하차인원_2017년01월~12월.csv",
encoding="euc-kr"
)
df_raw_2 = pd.read_csv(
RAW_DIR / "대전광역시도시철도공사_시간대별 승하차인원_2018년01월~12월.csv",
encoding="euc-kr"
)
df_raw_3 = pd.read_csv(
RAW_DIR / "대전광역시도시철도공사_시간대별 승하차인원_2019년01월~12월.csv",
encoding="euc-kr"
)
df_raw_4 = pd.read_csv(
RAW_DIR / "시간대별 승차 인원_2020년_2021년01_12월.csv",
encoding="euc-kr"
)
df_raw_5 = pd.read_csv(
RAW_DIR / "시간대별승하차인원_2022년 01_12월.csv",
encoding="euc-kr"
)
df_raw_6 = pd.read_csv(
RAW_DIR / "시간대별승하차인원_2023년 01_12월.csv",
encoding="euc-kr"
)
df_raw_7 = pd.read_csv(
RAW_DIR / "역별일별시간대별통행량_20240101~20241231.csv",
encoding="euc-kr"
)


df_raw = pd.concat(
    [df_raw_1, df_raw_2, df_raw_3, df_raw_4, df_raw_5, df_raw_6, df_raw_7],
    ignore_index=True
)

df_raw["total"] = df_raw.iloc[:, 4:].sum(axis=1)

df = df_raw[["날짜", "역번호", "역명", "구분", "total"]].copy()
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
df_pivoted.columns.name = None

total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
total_df.to_csv(OUTPUT_DIR / "daejeon_metro(2017~2024).csv")


def merge_all():
df_1 = pd.read_csv(OUTPUT_DIR / "daejeon_metro(2016).csv")
df_2 = pd.read_csv(OUTPUT_DIR / "daejeon_metro(2017~2024).csv", index_col=0)


df = pd.concat([df_1, df_2], ignore_index=True)

df["city"] = "daejeon"
df = df[["date", "city", "people_in", "people_out"]]
df.info()

df.to_csv(OUTPUT_DIR / "daejeon_metro.csv")


def main():
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


process_2017_2024()
merge_all()

print("Saved:", OUTPUT_DIR / "daejeon_metro.csv")


if __name__ == "__main__":
main()
