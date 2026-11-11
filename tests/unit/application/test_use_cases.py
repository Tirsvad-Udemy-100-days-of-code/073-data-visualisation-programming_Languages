"""Unit tests for the data preparation use cases."""

import pandas as pd
from pandas import DataFrame

from programming_languages.application.use_cases import explore_data, prepare_data


def _frame() -> DataFrame:
    return DataFrame(
        {
            "DATE": ["2008-07-01 00:00:00", "2008-08-01 00:00:00"],
            "TAG": ["c#", "java"],
            "POSTS": [3, 7],
        }
    )


def test_explore_data_reports_shape_and_counts() -> None:
    summary = explore_data(_frame())
    assert summary.shape == (2, 3)
    assert summary.counts["POSTS"] == 2
    assert len(summary.head) == 2
    assert len(summary.tail) == 2


def test_prepare_data_pivots_and_fills_gaps() -> None:
    result = prepare_data(_frame())
    assert result.shape == (2, 2)
    assert not result.isna().values.any()
    assert pd.api.types.is_datetime64_any_dtype(result.index)
