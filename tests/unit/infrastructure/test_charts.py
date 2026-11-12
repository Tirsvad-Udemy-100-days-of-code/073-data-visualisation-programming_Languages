"""Unit tests for the chart functions, inspecting the returned figures."""

from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from pandas import DataFrame

from programming_languages.infrastructure.charts import (
    plot_language,
    plot_languages,
    save_figure,
)

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


@pytest.fixture
def frame() -> DataFrame:
    index = pd.date_range("2020-01-01", periods=4, freq="MS", name="DATE")
    return DataFrame(
        {
            "java": [100.0, 200.0, 300.0, 400.0],
            "python": [50.0, 150.0, 250.0, 350.0],
            "c": [10.0, 20.0, 30.0, 40.0],
        },
        index=index,
    )


def test_plot_language_draws_one_line_of_the_language(frame: DataFrame) -> None:
    axes = plot_language(frame, "java").axes[0]
    assert len(axes.lines) == 1
    assert np.asarray(axes.lines[0].get_ydata()).tolist() == [
        100.0,
        200.0,
        300.0,
        400.0,
    ]


def test_plot_language_styled_sets_size_labels_and_limits(frame: DataFrame) -> None:
    figure = plot_language(frame, "java")
    axes = figure.axes[0]
    assert tuple(figure.get_size_inches()) == (16.0, 10.0)
    assert axes.get_xlabel() == "Date"
    assert axes.get_ylabel() == "Number of Posts"
    assert axes.get_xlabel() and axes.xaxis.label.get_fontsize() == 14
    assert axes.get_ylim() == (0, 35000)


def test_plot_language_unstyled_is_the_bare_line(frame: DataFrame) -> None:
    figure = plot_language(frame, "java", styled=False)
    axes = figure.axes[0]
    assert len(axes.lines) == 1
    assert axes.get_xlabel() == ""
    assert axes.get_ylabel() == ""
    assert tuple(figure.get_size_inches()) != (16.0, 10.0)
    assert axes.get_ylim() != (0, 35000)


def test_plot_languages_defaults_to_all_columns(frame: DataFrame) -> None:
    axes = plot_languages(frame).axes[0]
    _, labels = axes.get_legend_handles_labels()
    assert labels == ["java", "python", "c"]


def test_plot_languages_draws_only_requested_languages(frame: DataFrame) -> None:
    axes = plot_languages(frame, ["java", "python"]).axes[0]
    _, labels = axes.get_legend_handles_labels()
    assert labels == ["java", "python"]
    assert [line.get_label() for line in axes.lines] == ["java", "python"]


def test_plot_languages_styles_lines_legend_and_axes(frame: DataFrame) -> None:
    figure = plot_languages(frame, title="Posts")
    axes = figure.axes[0]
    assert all(line.get_linewidth() == 3 for line in axes.lines)
    assert len({line.get_color() for line in axes.lines}) == 3
    legend = axes.get_legend()
    assert legend is not None
    assert legend.get_texts()[0].get_fontsize() == 16
    assert tuple(figure.get_size_inches()) == (16.0, 10.0)
    assert axes.get_ylim() == (0, 35000)
    assert axes.get_title() == "Posts"
    assert axes.get_ylabel() == "Number of Posts"


def test_plot_languages_gives_fourteen_lines_distinct_colours() -> None:
    names = [f"lang{n}" for n in range(14)]
    df = DataFrame({name: [1.0, 2.0] for name in names})
    axes = plot_languages(df).axes[0]
    assert len({line.get_color() for line in axes.lines}) == 14


def test_plot_languages_without_title_has_no_title(frame: DataFrame) -> None:
    assert plot_languages(frame).axes[0].get_title() == ""


def test_save_figure_writes_png_and_creates_parent_folders(
    frame: DataFrame, tmp_path: Path
) -> None:
    target = tmp_path / "nested" / "chart.png"
    result = save_figure(plot_languages(frame), target)
    assert result == target
    content = target.read_bytes()
    assert content.startswith(PNG_SIGNATURE)
    assert len(content) > 1000
