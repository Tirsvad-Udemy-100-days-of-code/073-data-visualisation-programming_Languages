"""Draw the language popularity charts with matplotlib, without a display."""

import logging
from collections.abc import Sequence
from pathlib import Path

from matplotlib import colormaps
from matplotlib.axes import Axes
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
from pandas import DataFrame

logger = logging.getLogger(__name__)

FIGURE_SIZE = (16.0, 10.0)
CHART_DPI = 100
TICK_LABEL_SIZE = 14
AXIS_LABEL_SIZE = 14
TITLE_SIZE = 18
LEGEND_SIZE = 16
LINE_WIDTH = 3
X_LABEL = "Date"
Y_LABEL = "Number of Posts"
Y_LIMITS = (0, 35000)
# tab20 gives 20 distinct colours, enough for the 14 language lines.
LINE_COLORS = [colormaps["tab20"](index) for index in range(20)]


def _new_axes(*, styled: bool) -> tuple[Figure, Axes]:
    figure = Figure(figsize=FIGURE_SIZE if styled else None, dpi=CHART_DPI)
    FigureCanvasAgg(figure)
    return figure, figure.add_subplot()


def _style_axes(axes: Axes) -> None:
    axes.tick_params(axis="both", labelsize=TICK_LABEL_SIZE)
    axes.set_xlabel(X_LABEL, fontsize=AXIS_LABEL_SIZE)
    axes.set_ylabel(Y_LABEL, fontsize=AXIS_LABEL_SIZE)
    axes.set_ylim(*Y_LIMITS)


def plot_language(df: DataFrame, language: str, *, styled: bool = True) -> Figure:
    """Draw the posts of one language over time; ``styled=False`` is the bare line."""
    figure, axes = _new_axes(styled=styled)
    axes.plot(df.index, df[language])
    if styled:
        _style_axes(axes)
    return figure


def plot_languages(
    df: DataFrame,
    languages: Sequence[str] | None = None,
    *,
    title: str | None = None,
) -> Figure:
    """Draw one line per language (all columns by default) with a legend."""
    columns = list(df.columns) if languages is None else list(languages)
    figure, axes = _new_axes(styled=True)
    for column, color in zip(columns, LINE_COLORS, strict=False):
        axes.plot(df.index, df[column], linewidth=LINE_WIDTH, label=column, color=color)
    _style_axes(axes)
    if title is not None:
        axes.set_title(title, fontsize=TITLE_SIZE)
    axes.legend(fontsize=LEGEND_SIZE, ncols=2 if len(columns) > 7 else 1)
    return figure


def save_figure(figure: Figure, path: Path) -> Path:
    """Write ``figure`` as an image to ``path``, creating parent folders."""
    path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(path, dpi=CHART_DPI)
    logger.info("Wrote %s", path)
    return path
