"""Pure pandas rules for the Stack Overflow programming language data."""

import pandas as pd
from pandas import DataFrame

DATE_COLUMN = "DATE"
TAG_COLUMN = "TAG"
POSTS_COLUMN = "POSTS"


def convert_dates(df: DataFrame) -> DataFrame:
    """Return a copy of ``df`` whose DATE column holds datetimes."""
    converted = df.copy()
    converted[DATE_COLUMN] = pd.to_datetime(converted[DATE_COLUMN])
    return converted


def posts_per_language(df: DataFrame) -> DataFrame:
    """Return the total number of posts for each language tag."""
    return df.groupby(TAG_COLUMN)[[POSTS_COLUMN]].sum()


def months_per_language(df: DataFrame) -> DataFrame:
    """Return the number of monthly entries for each language tag."""
    return df.groupby(TAG_COLUMN).count()


def reshape_data(df: DataFrame) -> DataFrame:
    """Pivot to one row per date and one column per language tag."""
    return df.pivot(index=DATE_COLUMN, columns=TAG_COLUMN, values=POSTS_COLUMN)


def fill_missing(df: DataFrame) -> DataFrame:
    """Return a copy of ``df`` with missing values replaced by zero."""
    return df.fillna(0)


def rolling_mean(df: DataFrame, window: int = 6) -> DataFrame:
    """Return the rolling mean of ``df`` over ``window`` rows."""
    return df.rolling(window=window).mean()
