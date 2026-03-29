from pathlib import Path
import os
import requests
import pandas as pd
import xml.etree.ElementTree as ET
from urllib.parse import unquote

raw_key = os.getenv("DAEJEON_API_KEY")
service_key = unquote(raw_key)

url = "http://www.djtc.kr/OpenAPI/service/StationPassengerSVC/getStationPassenger"

params = {
"serviceKey": service_key,
"startDate": "20160101",
"endDate": "20161231",
"numOfRows": "20000"
}

try:
    print("데이터 수집 중...")
    response = requests.get(url, params=params)
    response.encoding = "utf-8"


    root = ET.fromstring(response.content)
    items = root.findall(".//item")

    data_list = []
    for item in items:
        data_list.append({
            "date": item.findtext("businessDay"),
            "station_id": item.findtext("stationNo"),
            "type": item.findtext("entryFlag"),
            "total": item.findtext("sumCnt")
        })

    df = pd.DataFrame(data_list)

    df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")
    df["type"] = df["type"].replace({"1": "people_in", "2": "people_out"})
    df["total"] = pd.to_numeric(df["total"]).fillna(0).astype(int)

    df_daily = df.groupby(["date", "type"])["total"].sum().unstack().reset_index()

    df_daily.columns.name = None
    df_daily = df_daily[["date", "people_in", "people_out"]]

    print("--- 대전 데이터 전처리 완료 ---")
    print(df_daily.head())

    output_path = Path("data/processed/daejeon_metro(2016).csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df_daily.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"파일 저장 완료: {output_path}")


except Exception as e:
    print(f"오류 발생: {e}")
