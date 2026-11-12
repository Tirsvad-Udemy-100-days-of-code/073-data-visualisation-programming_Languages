[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Krav: Python 3.13 eller nyere. Runtime-afhængigheder: `pandas` og `matplotlib`; JupyterLab, pytest, ruff og mypy er udviklingstilvalg.

## Windows (PowerShell)

Opret og brug et lokalt `.venv`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux og macOS

Opret og brug et lokalt `.venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Kør

Kør notebooken og genskab de ti skærmbilleder i `docs/images/`:

```bash
python -m jupyter lab notebooks/programming_languages.ipynb
python -m programming_languages.presentation.screenshots --output docs/images
```

## Test

```bash
python -m pytest
```

Testene kører offline og kræver ingen skærm: diagrammerne tegnes med Agg-backend.

Det får du: en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke installeret i redigerbar tilstand og tests, der beviser hvert trin.

[Hjem](Home-da)
