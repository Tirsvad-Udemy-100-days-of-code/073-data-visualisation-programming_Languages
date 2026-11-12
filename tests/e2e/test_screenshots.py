"""End-to-end test: the screenshot generator writes real PNG files."""

from pathlib import Path

from programming_languages.presentation.screenshots import generate_screenshots

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_FILES = [
    "step-01-explore-data.png",
    "step-02-group-by-language.png",
    "step-03-timestamps.png",
    "step-04-pivot.png",
    "step-05-fill-nan.png",
    "step-06-plot-java.png",
    "step-07-style-chart.png",
    "step-08-java-and-python.png",
    "step-09-all-languages.png",
    "step-10-rolling-mean.png",
]


def test_generate_screenshots_writes_ten_png_files(tmp_path: Path) -> None:
    written = generate_screenshots(tmp_path)
    assert [path.name for path in written] == EXPECTED_FILES
    for path in written:
        content = path.read_bytes()
        assert content.startswith(PNG_SIGNATURE)
        assert len(content) > 1000
