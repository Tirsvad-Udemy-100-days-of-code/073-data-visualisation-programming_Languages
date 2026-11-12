**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

You need Python 3.13 or newer. The only runtime dependencies are pandas and Matplotlib; JupyterLab, pytest, ruff and mypy are development extras.

## Create the environment

On Windows, in PowerShell, from the project folder:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Linux and macOS use `source .venv/bin/activate` instead of the activation line; in Git Bash on Windows use `source .venv/Scripts/activate`.

## Run

```bash
python -m jupyter lab notebooks/programming_languages.ipynb
python -m programming_languages.presentation.screenshots --output docs/images
```

The first command opens the notebook that follows the ten lecture steps. The second one regenerates the ten screenshots in `docs/images/`.

## Test

```bash
python -m pytest
```

The tests run offline and need no display: the charts are drawn with the Agg backend.

[Home](Home)
