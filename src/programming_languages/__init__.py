"""Analyse the popularity of programming languages from Stack Overflow tags."""

from programming_languages.application.use_cases import explore_data, prepare_data
from programming_languages.domain.language_stats import (
    convert_dates,
    fill_missing,
    months_per_language,
    posts_per_language,
    reshape_data,
    rolling_mean,
)
from programming_languages.infrastructure.charts import (
    plot_language,
    plot_languages,
    save_figure,
)
from programming_languages.infrastructure.csv_dataset import load_data

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "convert_dates",
    "explore_data",
    "fill_missing",
    "load_data",
    "months_per_language",
    "plot_language",
    "plot_languages",
    "posts_per_language",
    "prepare_data",
    "reshape_data",
    "rolling_mean",
    "save_figure",
]
