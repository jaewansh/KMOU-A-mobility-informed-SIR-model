from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw/seoul")
PROCESSED_DIR = Path("data/processed")
STATION_INFO_PATH = RAW_DIR / "seoul-metro-station-info.csv"
OUTPUT_PATH = PROCESSED_DIR / "seoul_metro_daily.csv"

YEARLY_FILES = {
    2016: "seoul-metro-2016.logs.csv",
    2017: "seoul-metro-2017.csv",
    2018: "seoul-metro-2018.logs.csv",
    2019: "seoul-metro-2019.logs.csv",
    2020: "seoul-metro-2020.logs.csv",
    2021: "seoul-metro-2021.logs.csv",
    2022: "seoul-metro-2022.csv",
    2023: "seoul-metro-2023.logs.csv",
    2024: "seoul-metro-2024.logs.csv",
}


def load_station_info() -> pd.DataFrame:
    """Load station metadata."""
    return pd.read_csv(STATION_INFO_PATH)


def load_yearly_data(file_path: Path) -> pd.DataFrame:
    """Load one yearly subway file."""
    return pd.read_csv(file_path)


def standardize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Convert numeric columns to integer where needed."""
    df = df.copy()
    cols_to_convert = ["station_code", "people_in", "people_out"]

    for col in cols_to_convert:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0).astype(int)

    return df


def load_all_years() -> pd.DataFrame:
    """Load and concatenate all yearly subway files."""
    frames = []

    for year, filename in YEARLY_FILES.items():
        file_path = RAW_DIR / filename
        df = load_yearly_data(file_path)
        df = standardize_numeric_columns(df)
        df["source_year"] = year
        frames.append(df)

    return pd.concat(frames, ignore_index=True)


def merge_with_station_info(df: pd.DataFrame, station_info: pd.DataFrame) -> pd.DataFrame:
    """Merge mobility logs with station metadata."""
    merged = pd.merge(
        df,
        station_info,
        left_on="station_code",
        right_on="station.code",
        how="inner",
    )
    return merged


def create_analysis_date(df: pd.DataFrame) -> pd.DataFrame:
    """Create analysis date by shifting timestamp back by 4 hours."""
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["date"] = (df["timestamp"] - pd.Timedelta(hours=4)).dt.normalize()
    df["day_of_week"] = df["date"].dt.dayofweek
    return df


def aggregate_daily_city_level(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate daily inflow/outflow totals at the city level."""
    daily = (
        df.groupby("date")[["people_in", "people_out"]]
        .sum()
        .reset_index()
        .sort_values("date")
    )
    daily["city"] = "seoul"
    daily = daily[["date", "city", "people_in", "people_out"]]
    return daily


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    station_info = load_station_info()
    df_all = load_all_years()
    df_merged = merge_with_station_info(df_all, station_info)
    df_merged = create_analysis_date(df_merged)

    daily = aggregate_daily_city_level(df_merged)
    daily.to_csv(OUTPUT_PATH, index=False, encoding="utf-8")

    print(f"Saved processed Seoul daily mobility data to: {OUTPUT_PATH}")
    print(daily.head())


if __name__ == "__main__":
    main()
