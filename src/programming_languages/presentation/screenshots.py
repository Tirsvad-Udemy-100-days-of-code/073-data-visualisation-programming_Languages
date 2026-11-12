"""Render each lecture step as a PNG of monospace text, without a display."""

import argparse
import logging
from collections.abc import Callable
from pathlib import Path

import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from pandas import DataFrame

from programming_languages.application.use_cases import explore_data, prepare_data
from programming_languages.domain.language_stats import (
    DATE_COLUMN,
    convert_dates,
    fill_missing,
    months_per_language,
    posts_per_language,
    reshape_data,
    rolling_mean,
)
from programming_languages.infrastructure.charts import plot_language, plot_languages
from programming_languages.infrastructure.csv_dataset import (
    DEFAULT_DATA_PATH,
    load_data,
)

logger = logging.getLogger(__name__)

DPI = 120
FIGURE_WIDTH_INCHES = 12.0
LINE_HEIGHT_INCHES = 0.19
MARGIN_INCHES = 0.9
BACKGROUND = "#f7f7f5"
TEXT_COLOR = "#222222"
FONT_SIZE = 9
TITLE_FONT_SIZE = 13
DISPLAY_WIDTH = 120

# A text step takes the raw data and returns a title and the body text.
TextStep = Callable[[DataFrame], tuple[str, str]]
# A step renderer takes the raw data and returns the figure to save.
StepRenderer = Callable[[DataFrame], Figure]

CHART_TITLE = "Stack Overflow posts per programming language"
ROLLING_WINDOW = 6


def _section(heading: str, body: object) -> str:
    return f"{heading}\n{body}\n"


def _explore(df: DataFrame) -> tuple[str, str]:
    summary = explore_data(df)
    body = "\n".join(
        [
            _section("df.head()", summary.head.to_string()),
            _section("df.tail()", summary.tail.to_string()),
            _section("df.shape", summary.shape),
            _section("df.count()", summary.counts.to_string()),
        ]
    )
    return "Step 1: explore the data", body


def _group_by_language(df: DataFrame) -> tuple[str, str]:
    posts = posts_per_language(df).to_string()
    months = months_per_language(df).to_string()
    body = "\n".join(
        [
            _section("Posts per language (groupby TAG, sum)", posts),
            _section("Months per language (groupby TAG, count)", months),
        ]
    )
    return "Step 2: group by language", body


def _timestamps(df: DataFrame) -> tuple[str, str]:
    converted = convert_dates(df)
    body = "\n".join(
        [
            _section("Type of first DATE before", type(df[DATE_COLUMN].iloc[0])),
            _section("Type of first DATE after", type(converted[DATE_COLUMN].iloc[0])),
            _section("Converted head", converted.head().to_string()),
        ]
    )
    return "Step 3: convert the dates to timestamps", body


def _pivot(df: DataFrame) -> tuple[str, str]:
    reshaped = reshape_data(convert_dates(df))
    body = "\n".join(
        [
            _section("Reshaped head", reshaped.head().to_string()),
            _section("Reshaped tail", reshaped.tail().to_string()),
            _section("Shape", reshaped.shape),
            _section("Columns", list(reshaped.columns)),
            _section(
                "Counts per column (NaN rows are not counted)",
                reshaped.count().to_string(),
            ),
        ]
    )
    return "Step 4: pivot to one column per language", body


def _fill_nan(df: DataFrame) -> tuple[str, str]:
    reshaped = reshape_data(convert_dates(df))
    filled = fill_missing(reshaped)
    body = "\n".join(
        [
            _section("Any NaN before", reshaped.isna().values.any()),
            _section("Any NaN after fill_missing", filled.isna().values.any()),
            _section("Filled head", prepare_data(df).head().to_string()),
        ]
    )
    return "Step 5: replace NaN with zero", body


def _text_figure(title: str, body: str) -> Figure:
    lines = body.count("\n") + 1
    height = lines * LINE_HEIGHT_INCHES + MARGIN_INCHES
    figure = Figure(figsize=(FIGURE_WIDTH_INCHES, height), dpi=DPI)
    figure.set_facecolor(BACKGROUND)
    FigureCanvasAgg(figure)
    top = 1 - 0.25 / height
    figure.text(
        0.02,
        top,
        title,
        fontsize=TITLE_FONT_SIZE,
        weight="bold",
        color=TEXT_COLOR,
        va="top",
    )
    figure.text(
        0.02,
        top - 0.5 / height,
        body,
        family="monospace",
        fontsize=FONT_SIZE,
        color=TEXT_COLOR,
        va="top",
    )
    return figure


def _as_figure(step: TextStep) -> StepRenderer:
    def render(df: DataFrame) -> Figure:
        return _text_figure(*step(df))

    return render


def _plot_java(df: DataFrame) -> Figure:
    return plot_language(prepare_data(df), "java", styled=False)


def _style_chart(df: DataFrame) -> Figure:
    return plot_language(prepare_data(df), "java")


def _java_and_python(df: DataFrame) -> Figure:
    return plot_languages(prepare_data(df), ["java", "python"], title="Java and Python")


def _all_languages(df: DataFrame) -> Figure:
    return plot_languages(prepare_data(df), title=CHART_TITLE)


def _rolling_mean(df: DataFrame) -> Figure:
    smoothed = rolling_mean(prepare_data(df), window=ROLLING_WINDOW)
    return plot_languages(
        smoothed, title=f"{CHART_TITLE} ({ROLLING_WINDOW}-month rolling mean)"
    )


# Step file stems with their renderers; append further steps here.
STEPS: list[tuple[str, StepRenderer]] = [
    ("step-01-explore-data", _as_figure(_explore)),
    ("step-02-group-by-language", _as_figure(_group_by_language)),
    ("step-03-timestamps", _as_figure(_timestamps)),
    ("step-04-pivot", _as_figure(_pivot)),
    ("step-05-fill-nan", _as_figure(_fill_nan)),
    ("step-06-plot-java", _plot_java),
    ("step-07-style-chart", _style_chart),
    ("step-08-java-and-python", _java_and_python),
    ("step-09-all-languages", _all_languages),
    ("step-10-rolling-mean", _rolling_mean),
]


def generate_screenshots(
    output_dir: Path, data_path: Path = DEFAULT_DATA_PATH
) -> list[Path]:
    """Render every step to a PNG in ``output_dir`` and return the file paths."""
    output_dir.mkdir(parents=True, exist_ok=True)
    data = load_data(data_path)
    written: list[Path] = []
    with pd.option_context("display.width", DISPLAY_WIDTH):
        for stem, renderer in STEPS:
            path = output_dir / f"{stem}.png"
            renderer(data).savefig(path)
            logger.info("Wrote %s", path)
            written.append(path)
    return written


def main() -> None:
    """Generate the screenshots from the command line."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("docs/images"))
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA_PATH)
    args = parser.parse_args()
    generate_screenshots(args.output, args.data)


if __name__ == "__main__":
    main()
