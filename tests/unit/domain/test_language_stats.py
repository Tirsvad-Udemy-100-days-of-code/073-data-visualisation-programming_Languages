"""Unit tests for the language statistics rules."""

import pandas as pd
from pandas import DataFrame

from programming_languages.domain.language_stats import (
    convert_dates,
    fill_missing,
    months_per_language,
    posts_per_language,
    reshape_data,
    rolling_mean,
)

FIRST_DATE = "2008-07-01 00:00:00"
SECOND_DATE = "2008-08-01 00:00:00"


def _frame() -> DataFrame:
    return DataFrame(
        {
            "DATE": [FIRST_DATE, SECOND_DATE, SECOND_DATE],
            "TAG": ["c#", "c#", "java"],
            "POSTS": [3, 5, 7],
        }
    )


def test_convert_dates_returns_datetimes_without_mutating_input() -> None:
    original = _frame()
    result = convert_dates(original)
    assert pd.api.types.is_datetime64_any_dtype(result["DATE"])
    assert original["DATE"].iloc[0] == FIRST_DATE


def test_posts_per_language_sums_posts() -> None:
    result = posts_per_language(_frame())
    assert result.loc["c#", "POSTS"] == 8
    assert result.loc["java", "POSTS"] == 7


def test_months_per_language_counts_rows() -> None:
    result = months_per_language(_frame())
    assert result.loc["c#", "POSTS"] == 2
    assert result.loc["java", "POSTS"] == 1


def test_reshape_data_leaves_nan_for_missing_months() -> None:
    result = reshape_data(convert_dates(_frame()))
    assert result.shape == (2, 2)
    assert list(result.columns) == ["c#", "java"]
    assert result["java"].isna().sum() == 1


def test_fill_missing_replaces_nan_without_mutating_input() -> None:
    pivoted = reshape_data(convert_dates(_frame()))
    filled = fill_missing(pivoted)
    assert not filled.isna().values.any()
    assert pivoted.isna().values.any()


def test_rolling_mean_uses_default_window() -> None:
    df = DataFrame({"a": [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]})
    result = rolling_mean(df)
    assert result["a"].iloc[:5].isna().all()
    assert result["a"].iloc[5] == 3.5


def test_rolling_mean_uses_custom_window() -> None:
    df = DataFrame({"a": [1.0, 2.0, 3.0]})
    result = rolling_mean(df, window=2)
    assert pd.isna(result["a"].iloc[0])
    assert result["a"].iloc[1] == 1.5
