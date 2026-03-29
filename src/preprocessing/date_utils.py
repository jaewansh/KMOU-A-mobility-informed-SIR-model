import pandas as pd


def to_datetime_column(series: pd.Series, fmt: str | None = None) -> pd.Series:
    """Convert a pandas Series to datetime."""
    return pd.to_datetime(series, format=fmt, errors="coerce")


def add_date_parts(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """Add year, month, day, and weekday columns based on a datetime column."""
    df = df.copy()
    df["year"] = df[date_col].dt.year
    df["month"] = df[date_col].dt.month
    df["day"] = df[date_col].dt.day
    df["weekday"] = df[date_col].dt.day_name()
    return df
