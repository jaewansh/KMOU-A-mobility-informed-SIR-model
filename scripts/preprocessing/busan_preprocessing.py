from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw/busan")
OUTPUT_DIR = Path("data/processed")


def process_2016():
    df_raw = pd.read_csv(
        RAW_DIR / "부산교통공사 시간대별 승하차인원(2016년).csv",
        encoding="euc-kr"
    )

    df = df_raw.iloc[:, :5].copy()
    df.columns = ["station_id", "station_name", "date", "type", "total"]

    df_pivoted = df.pivot_table(
        index=["date", "station_id", "station_name"],
        columns="type",
        values="total",
        aggfunc="sum"
    ).reset_index()

    df_pivoted.rename(columns={"승차": "people_in", "하차": "people_out"}, inplace=True)
    df_pivoted.columns.name = None

    df_pivoted["date"] = pd.to_numeric(df_pivoted["date"], errors="coerce")
    df_pivoted = df_pivoted.dropna(subset=["date"])
    df_pivoted["date"] = pd.to_datetime(
        df_pivoted["date"].astype(int).astype(str),
        format="%Y%m%d"
    )

    total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
    total_df.to_csv(OUTPUT_DIR / "busan_metro(2016).csv")


def process_2017_2018():
    df_raw_1 = pd.read_csv(
        RAW_DIR / "부산교통공사 시간대별 승하차인원(2017년).csv",
        encoding="euc-kr"
    )
    df_raw_2 = pd.read_csv(
        RAW_DIR / "부산교통공사 시간대별 승하차인원(2018년).csv",
        encoding="euc-kr"
    )

    df_raw = pd.concat([df_raw_1, df_raw_2], ignore_index=True)
    df = df_raw.iloc[:, :5].dropna().copy()
    df.columns = ["station_id", "station_name", "date", "type", "total"]

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
    total_df.to_csv(OUTPUT_DIR / "busan_metro(2017-2018).csv")


def process_2019_2020():
    df_raw_1 = pd.read_csv(
        RAW_DIR / "부산교통공사 시간대별 승하차인원(2019년).csv",
        encoding="euc-kr"
    )
    df_raw_2 = pd.read_csv(
        RAW_DIR / "부산교통공사 시간대별 승하차인원(2020년).csv",
        encoding="euc-kr"
    )

    df_raw = pd.concat([df_raw_1, df_raw_2], ignore_index=True)
    df = df_raw.iloc[:, :5].copy()
    df.columns = ["station_id", "station_name", "date", "type", "total"]

    df_pivoted = df.pivot_table(
        index=["date", "station_id", "station_name"],
        columns="type",
        values="total",
        aggfunc="sum"
    ).reset_index()

    df_pivoted.rename(columns={"승차": "people_in", "하차": "people_out"}, inplace=True)
    df_pivoted.columns.name = None

    df_pivoted["date"] = pd.to_numeric(df_pivoted["date"], errors="coerce")
    df_pivoted = df_pivoted.dropna(subset=["date"])
    df_pivoted["date"] = pd.to_datetime(
        df_pivoted["date"].astype(int).astype(str),
        format="%Y%m%d"
    )

    total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
    total_df.to_csv(OUTPUT_DIR / "busan_metro(2019-2020).csv")


def process_2021():
    df_raw = pd.read_csv(
        RAW_DIR / "부산교통공사 시간대별 승하차인원(2021년).csv",
        encoding="euc-kr"
    )

    df = df_raw.iloc[:, :5].copy()
    df.columns = ["station_id", "station_name", "date", "type", "total"]

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
    total_df.to_csv(OUTPUT_DIR / "busan_metro(2021).csv")


def process_2022_2024():
    df_raw_1 = pd.read_csv(
        RAW_DIR / "일별 역별 시간대별 승하차(2023년 12월).csv",
        encoding="euc-kr"
    )
    df_raw_2 = pd.read_csv(
        RAW_DIR / "일별 역별 시간대별 승하차인원(2024년 12월).csv",
        encoding="euc-kr"
    )
    df_raw_3 = pd.read_csv(
        RAW_DIR / "일별역별시간대별승하차(2022년 12월).csv",
        encoding="euc-kr"
    )

    df_raw = pd.concat([df_raw_1, df_raw_2, df_raw_3], ignore_index=True)
    df = df_raw.iloc[:, :6].copy()
    df.columns = ["station_id", "station_name", "date", "day_of_week", "type", "total"]

    df["type"] = df["type"].replace({"승차": "people_in", "하차": "people_out"})

    df_pivoted = df.pivot_table(
        index=["date", "day_of_week", "station_id", "station_name"],
        columns="type",
        values="total",
        aggfunc="sum"
    ).reset_index()

    df_pivoted = df_pivoted.fillna(0)
    df_pivoted["people_in"] = df_pivoted["people_in"].astype(int)
    df_pivoted["people_out"] = df_pivoted["people_out"].astype(int)

    total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
    total_df.to_csv(OUTPUT_DIR / "busan_metro(2022-2024).csv")


def merge_all():
    df_1 = pd.read_csv(OUTPUT_DIR / "busan_metro(2016).csv", index_col=0)
    df_2 = pd.read_csv(OUTPUT_DIR / "busan_metro(2017-2018).csv", index_col=0)
    df_3 = pd.read_csv(OUTPUT_DIR / "busan_metro(2019-2020).csv", index_col=0)
    df_4 = pd.read_csv(OUTPUT_DIR / "busan_metro(2021).csv", index_col=0)
    df_5 = pd.read_csv(OUTPUT_DIR / "busan_metro(2022-2024).csv", index_col=0)

    df = pd.concat([df_1, df_2, df_3, df_4, df_5], ignore_index=True)
    df["city"] = "busan"
    df = df[["date", "city", "people_in", "people_out"]]

    df.to_csv(OUTPUT_DIR / "busan_metro.csv")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    process_2016()
    process_2017_2018()
    process_2019_2020()
    process_2021()
    process_2022_2024()
    merge_all()

    print("Saved: data/processed/busan_metro.csv")


if __name__ == "__main__":
    main()
