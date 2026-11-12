[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Mula di sini

Keperluan: Python 3.13 atau lebih baharu. Kebergantungan masa jalan: `pandas` dan `matplotlib`; JupyterLab, pytest, ruff dan mypy ialah tambahan pembangunan.

## Windows (PowerShell)

Cipta dan gunakan `.venv` setempat:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Linux dan macOS

Cipta dan gunakan `.venv` setempat:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Jalankan

Jalankan buku nota dan jana semula sepuluh tangkapan skrin dalam `docs/images/`:

```bash
python -m jupyter lab notebooks/programming_languages.ipynb
python -m programming_languages.presentation.screenshots --output docs/images
```

## Ujian

```bash
python -m pytest
```

Ujian berjalan luar talian dan tidak memerlukan paparan: carta dilukis dengan backend Agg.

Apa yang anda peroleh: persediaan yang boleh diulang (satu persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh disunting dan ujian yang membuktikan setiap langkah.

[Utama](Home-ms)
