**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer. Runtime dependencies: `pandas` and `matplotlib`; JupyterLab, pytest, ruff and mypy are development extras.

## Windows (PowerShell)

Create and use a local `.venv`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux and macOS

Create and use a local `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Run

Run the notebook and regenerate the ten screenshots in `docs/images/`:

```bash
python -m jupyter lab notebooks/programming_languages.ipynb
python -m programming_languages.presentation.screenshots --output docs/images
```

## Test

```bash
python -m pytest
```

The tests run offline and need no display: the charts are drawn with the Agg backend.

What you gain: a repeatable set-up (a virtual environment per project), a package installed in editable mode, and tests that prove each step.

[Home](Home)
