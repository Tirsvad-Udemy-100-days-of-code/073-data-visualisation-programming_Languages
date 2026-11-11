"""Read the Stack Overflow query results from a CSV file."""

from pathlib import Path

import pandas as pd
from pandas import DataFrame

from programming_languages.domain.language_stats import (
    DATE_COLUMN,
    POSTS_COLUMN,
    TAG_COLUMN,
)

DEFAULT_DATA_PATH = Path(__file__).resolve().parents[3] / "data" / "QueryResults.csv"


def load_data(path: Path | str) -> DataFrame:
    """Load the CSV at ``path`` with the domain column names."""
    return pd.read_csv(path, names=[DATE_COLUMN, TAG_COLUMN, POSTS_COLUMN], header=0)
