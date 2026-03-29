from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/processed")

def main():

    print("=== Merging city-level metro data ===")

    df_seoul = pd.read_csv(DATA_DIR / "seoul_metro_daily.csv")
    df_busan = pd.read_csv(DATA_DIR / "busan_metro.csv")
    df_daegu = pd.read_csv(DATA_DIR / "daegu_metro.csv")
    df_gwangju = pd.read_csv(DATA_DIR / "gwangju_metro.csv")
    df_daejeon = pd.read_csv(DATA_DIR / "daejeon_metro.csv")

    df = pd.concat(
        [df_seoul, df_busan, df_daegu, df_gwangju, df_daejeon],
        ignore_index=True
    )

    df["date"] = pd.to_datetime(df["date"])

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "all_city_metro.csv"

    df.to_csv(output_path, index=False)

    print("Saved:", output_path)
    print(df.head())

if __name__ == "__main__":
    main()
