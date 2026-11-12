[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom i gang

## Opsætning og kørsel

Opret et lokalt virtuelt miljø, installér projektet og kør testene:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
```

Notebooken `notebooks/programming_languages.ipynb` følger de ti trin. Åbn den med `jupyter lab`.

[Hjem](Home-da)
