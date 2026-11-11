"""Use cases that prepare the language data for analysis."""

from dataclasses import dataclass

from pandas import DataFrame, Series

from programming_languages.domain.language_stats import (
    convert_dates,
    fill_missing,
    reshape_data,
)


@dataclass(frozen=True)
class DataSummary:
    """A first look at a data frame: its ends, its shape and its counts."""

    head: DataFrame
    tail: DataFrame
    shape: tuple[int, int]
    counts: "Series[int]"


def explore_data(df: DataFrame) -> DataSummary:
    """Summarise ``df`` with head, tail, shape and non-null counts."""
    return DataSummary(
        head=df.head(),
        tail=df.tail(),
        shape=df.shape,
        counts=df.count(),
    )


def prepare_data(df: DataFrame) -> DataFrame:
    """Convert dates, pivot to one column per language and fill gaps with zero."""
    return fill_missing(reshape_data(convert_dates(df)))
