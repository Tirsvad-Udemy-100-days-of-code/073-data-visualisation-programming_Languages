"""Integration tests for reading the CSV data."""

from pathlib import Path

from programming_languages.application.use_cases import prepare_data
from programming_languages.infrastructure.csv_dataset import (
    DEFAULT_DATA_PATH,
    load_data,
)

CSV_TEXT = 'm,TagName,\n"2008-07-01 00:00:00","c#","3"\n'


def test_load_data_reads_columns_from_tmp_csv(tmp_path: Path) -> None:
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(CSV_TEXT, encoding="utf-8", newline="\n")
    result = load_data(csv_file)
    assert list(result.columns) == ["DATE", "TAG", "POSTS"]
    assert result.shape == (1, 3)
    assert result["POSTS"].iloc[0] == 3


def test_load_data_accepts_string_path(tmp_path: Path) -> None:
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(CSV_TEXT, encoding="utf-8", newline="\n")
    assert load_data(str(csv_file)).shape == (1, 3)


def test_real_data_has_expected_shape() -> None:
    assert load_data(DEFAULT_DATA_PATH).shape == (1991, 3)


def test_real_data_prepares_to_145_by_14_without_nan() -> None:
    result = prepare_data(load_data(DEFAULT_DATA_PATH))
    assert result.shape == (145, 14)
    assert not result.isna().values.any()
