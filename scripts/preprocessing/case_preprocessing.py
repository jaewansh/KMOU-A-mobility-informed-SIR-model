from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

RAW_DIR = Path("data/raw/nhis")
PROCESSED_DIR = Path("data/processed/cases")

INPUT_PATH = RAW_DIR / "국민건강보험공단_감염성질환(인플루엔자) 의료이용정보_20241231.xlsx"

def save_case_series(filtered_df, city_codes, output_name, title):
case_data = filtered_df[filtered_df["city"].isin(city_codes)]
case_df = case_data.groupby("date")["cases"].sum().reset_index()


full_date_range = pd.date_range(start="2016-09-01", end="2017-08-31")
case_df = case_df.set_index("date").reindex(full_date_range)
case_df["cases"] = case_df["cases"].fillna(0)
case_df = case_df.reset_index().rename(columns={"index": "date"})
case_df["cases"] = case_df["cases"].astype(int)

print(case_df.tail(10))
case_df.to_csv(PROCESSED_DIR / output_name, index=False)


return case_df


def main():
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
FIGURE_DIR.mkdir(parents=True, exist_ok=True)


df = pd.read_excel(INPUT_PATH)
print(df.info())

df = df.rename(columns={"요양개시일자": "date"})
df = df.rename(columns={"주소(시도)": "city"})
df = df.rename(columns={"진료에피소드 건수": "cases"})
print(df.head(10))

df["date"] = pd.to_datetime(df["date"], errors="coerce")

data = df.groupby(["date", "city"])["cases"].sum().reset_index()
print(data.head())

start_date = "2016-09-01"
end_date = "2017-08-31"
filtered_df = data[data["date"].between(start_date, end_date)]

print(filtered_df.head())
print(filtered_df["city"].unique())

# Korea cases
korea = [11, 26, 27, 28, 29, 30, 36, 41, 43, 44, 45, 46, 47, 48, 51, 31, 50]
korea_cases = filtered_df[filtered_df["city"].isin(korea)].groupby("date")["cases"].sum().reset_index()
print(korea_cases.tail(10))
korea_cases.to_csv(PROCESSED_DIR / "Korea_cases.csv", index=False)

korea_df = pd.read_csv(PROCESSED_DIR / "Korea_cases.csv")


# Seoul cases
save_case_series(filtered_df, [11, 41], "Seoul_cases.csv", "Seoul cases")

# Busan cases
save_case_series(filtered_df, [26], "Busan_cases.csv", "Busan cases")

# Daejeon cases
save_case_series(filtered_df, [30], "Daejeon_cases.csv", "Daejeon cases")

# Daegu cases
save_case_series(filtered_df, [27], "Daegu_cases.csv", "Daegu cases")

# Gwangju cases
save_case_series(filtered_df, [29], "Gwangju_cases.csv", "Gwangju cases")

seoul_df = pd.read_csv(PROCESSED_DIR / "Seoul_cases.csv")
busan_df = pd.read_csv(PROCESSED_DIR / "Busan_cases.csv")
daejeon_df = pd.read_csv(PROCESSED_DIR / "Daejeon_cases.csv")
daegu_df = pd.read_csv(PROCESSED_DIR / "Daegu_cases.csv")
gwangju_df = pd.read_csv(PROCESSED_DIR / "Gwangju_cases.csv")


if **name** == "**main**":
main()
