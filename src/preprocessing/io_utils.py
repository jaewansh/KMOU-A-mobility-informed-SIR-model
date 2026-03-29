from pathlib import Path
import pandas as pd


def ensure_directory(path: str) -> None:
    """Create directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def read_csv_file(path: str, **kwargs) -> pd.DataFrame:
    """Read a CSV file and return a pandas DataFrame."""
    return pd.read_csv(path, **kwargs)


def save_csv_file(df: pd.DataFrame, path: str, index: bool = False) -> None:
    """Save a DataFrame to CSV, creating parent directories if needed."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=index)
