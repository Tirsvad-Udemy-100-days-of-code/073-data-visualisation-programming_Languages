"""Smoke test: the package can be imported."""

import programming_languages


def test_version_is_defined() -> None:
    assert programming_languages.__version__ == "0.1.0"
