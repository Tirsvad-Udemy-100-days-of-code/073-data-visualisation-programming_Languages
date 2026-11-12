**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

## Set up and run

Create a local virtual environment, install the project and run the tests:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m pytest
```

The notebook `notebooks/programming_languages.ipynb` follows the ten steps. Open it with `jupyter lab`.

[Home](Home)
