import pandas as pd


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names by lowercasing and replacing spaces."""
    df = df.copy()
    df.columns = [
        col.strip().lower().replace(" ", "_").replace("-", "_")
        for col in df.columns
    ]
    return df


def drop_empty_rows(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows that are entirely empty."""
    return df.dropna(how="all").copy()
