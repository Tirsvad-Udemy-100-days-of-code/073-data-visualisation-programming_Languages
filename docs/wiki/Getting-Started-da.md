[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

Du skal bruge Python 3.13 eller nyere. De eneste runtime-afhængigheder er pandas og Matplotlib; JupyterLab, pytest, ruff og mypy er udviklingstilvalg.

## Opret miljøet

På Windows, i PowerShell, fra projektmappen:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

På Linux og macOS bruges `source .venv/bin/activate` i stedet for aktiveringslinjen; i Git Bash på Windows bruges `source .venv/Scripts/activate`.

## Kør

```bash
python -m jupyter lab notebooks/programming_languages.ipynb
python -m programming_languages.presentation.screenshots --output docs/images
```

Den første kommando åbner notebooken, der følger de ti trin i lektionen. Den anden genskaber de ti skærmbilleder i `docs/images/`.

## Test

```bash
python -m pytest
```

Testene kører offline og kræver ingen skærm: diagrammerne tegnes med Agg-backend.

[Hjem](Home-da)
