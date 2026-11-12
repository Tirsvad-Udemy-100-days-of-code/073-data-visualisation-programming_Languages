[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Mula di sini

Anda memerlukan Python 3.13 atau lebih baharu. Satu-satunya kebergantungan masa jalan ialah pandas dan Matplotlib; JupyterLab, pytest, ruff dan mypy ialah tambahan pembangunan.

## Cipta persekitaran

Pada Windows, dalam PowerShell, dari folder projek:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Pada Linux dan macOS gunakan `source .venv/bin/activate` sebagai ganti baris pengaktifan; dalam Git Bash pada Windows gunakan `source .venv/Scripts/activate`.

## Jalankan

```bash
python -m jupyter lab notebooks/programming_languages.ipynb
python -m programming_languages.presentation.screenshots --output docs/images
```

Arahan pertama membuka buku nota yang mengikuti sepuluh langkah kuliah. Arahan kedua menjana semula sepuluh tangkapan skrin dalam `docs/images/`.

## Ujian

```bash
python -m pytest
```

Ujian berjalan luar talian dan tidak memerlukan paparan: carta dilukis dengan backend Agg.

[Utama](Home-ms)
