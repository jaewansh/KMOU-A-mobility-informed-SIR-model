from pathlib import Path
import pandas as pd

RAW_DIR = Path("data/raw/daegu")
OUTPUT_DIR = Path("data/processed")

def process_2016():
    df_raw = pd.read_csv(
    RAW_DIR / "대구교통공사_2016년 역별일별시간별승하차현황.csv",
    encoding="euc-kr",
    skiprows=2
    )


    target_year = 2016

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2016).csv")


def process_2017():
    df_raw = pd.read_csv(
    RAW_DIR / "대구교통공사_역별일별시간별 승하차인원_20171231.csv",
    encoding="euc-kr"
    )


    target_year = 2017

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2017).csv")


def process_2018():
    df_raw = pd.read_csv(
    RAW_DIR / "대구도시철도공사_일별시간별승하차인원_20181231.csv",
    encoding="euc-kr"
    )


    target_year = 2018

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하차", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2018).csv")


def process_2019():
    df_raw = pd.read_csv(
    RAW_DIR / "대구도시철도공사_역별일별시간별승하차인원현황_20191231.csv",
    encoding="euc-kr"
    )


    target_year = 2019

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2019).csv")


def process_2020():
    df_raw = pd.read_csv(
    RAW_DIR / "대구도시철도공사_역별일별시간별승하차인원현황_20201231.csv",
    encoding="euc-kr"
    )


    target_year = 2020

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하", "일계"]].copy()
    df.columns = ["date", "station_id", "station_name", "type", "total"]

    df["type"] = df["type"].replace({"승차": "people_in", "하차": "people_out"})

    df_pivoted = df.pivot_table(
        index=["date", "station_id", "station_name"],
        columns="type",
        values="total",
        aggfunc="sum"
    ).reset_index()

    df_pivoted = df_pivoted.fillna(0)

    if "2020-02-29" not in df_pivoted["date"].values:
        print("2월 29일 데이터 누락 생성 시작")

        d28 = df_pivoted[df_pivoted["date"] == "2020-02-28"].copy()
        d01 = df_pivoted[df_pivoted["date"] == "2020-03-01"].copy()

        leap_day = pd.merge(
            d28, d01,
            on=["station_id", "station_name"],
            suffixes=("_28", "_01")
        )

        leap_day["date"] = "2020-02-29"
        leap_day["people_in"] = ((leap_day["people_in_28"] + leap_day["people_in_01"]) / 2).astype(int)
        leap_day["people_out"] = ((leap_day["people_out_28"] + leap_day["people_out_01"]) / 2).astype(int)

        leap_day_final = leap_day[["date", "station_id", "station_name", "people_in", "people_out"]]

        df_pivoted = pd.concat([df_pivoted, leap_day_final], ignore_index=True)
        df_pivoted = df_pivoted.sort_values(["date", "station_id"]).reset_index(drop=True)

        print("2월 29일 데이터 생성 완료")

    else:
        print("2월 29일 데이터 존재")

    df_pivoted["people_in"] = df_pivoted["people_in"].astype(int)
    df_pivoted["people_out"] = df_pivoted["people_out"].astype(int)
    df_pivoted.columns.name = None

    total_df = df_pivoted.groupby("date")[["people_in", "people_out"]].sum().reset_index()
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2020).csv")


def process_2021():
    df_raw = pd.read_csv(
    RAW_DIR / "대구도시철도공사_역별일별시간별승하차인원현황_20211231.csv",
    encoding="euc-kr"
    )


    target_year = 2021

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2021).csv")


def process_2022():
    df_raw = pd.read_csv(
    RAW_DIR / "역별일별시간별승하차인원현황_20221231.csv",
    encoding="euc-kr"
    )


    target_year = 2022

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하차", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2022).csv")


def process_2023():
    df_raw = pd.read_csv(
    RAW_DIR / "역별일별시간별승하차인원현황_20231231.csv",
    encoding="euc-kr"
    )


    target_year = 2023

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하차", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2023).csv")


def process_2024():
    df_raw = pd.read_csv(
    RAW_DIR / "역별일별시간별승하차인원현황_20241231.csv",
    encoding="euc-kr"
    )


    target_year = 2024

    df_raw["date"] = (
        str(target_year) + "-" +
        df_raw["월"].astype(str).str.zfill(2) + "-" +
        df_raw["일"].astype(str).str.zfill(2)
    )

    df = df_raw[["date", "역번호", "역명", "승하차", "일계"]].copy()
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
    total_df.to_csv(OUTPUT_DIR / "daegu_metro(2024).csv")


def merge_all():
    df_1 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2016).csv", index_col=0)
    df_2 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2017).csv", index_col=0)
    df_3 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2018).csv", index_col=0)
    df_4 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2019).csv", index_col=0)
    df_5 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2020).csv", index_col=0)
    df_6 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2021).csv", index_col=0)
    df_7 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2022).csv", index_col=0)
    df_8 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2023).csv", index_col=0)
    df_9 = pd.read_csv(OUTPUT_DIR / "daegu_metro(2024).csv", index_col=0)


    df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7, df_8, df_9], ignore_index=True)
    df["city"] = "daegu"
    df = df[["date", "city", "people_in", "people_out"]]

    df.info()
    df.to_csv(OUTPUT_DIR / "daegu_metro.csv")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


    process_2016()
    process_2017()
    process_2018()
    process_2019()
    process_2020()
    process_2021()
    process_2022()
    process_2023()
    process_2024()
    merge_all()

    print("Saved:", OUTPUT_DIR / "daegu_metro.csv")


if __name__ == "__main__":
    main()
