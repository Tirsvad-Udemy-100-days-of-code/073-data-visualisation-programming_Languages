[English](Step-05-Fill-NaN) · [Dansk](Step-05-Fill-NaN-da) · **Bahasa Malaysia**

# Langkah 5: gantikan nilai NaN

## Apa yang kami lakukan

Bulan tanpa catatan bermaksud sifar catatan, jadi kami menggantikan setiap NaN dengan 0 dan menyemak bahawa tiada yang tinggal.

## Kod

```python
reshaped_df.fillna(0, inplace=True)
reshaped_df.isna().values.any()   # False
```

## Tangkapan skrin

![Langkah 5: gantikan nilai NaN](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-05-fill-nan.png)

## Apa yang kami peroleh

- `fillna(0)` menggantikan nilai yang hilang; di sini 0 ialah pilihan yang betul, bukan membuang baris.
- `inplace=True` mengemas kini DataFrame itu sendiri; tanpanya kita perlu menetapkan semula hasilnya.
- `isna().values.any()` ialah semakan pantas seluruh DataFrame untuk nilai NaN yang tinggal.

[Sebelumnya](Step-04-Pivot-ms) · [Utama](Home-ms) · [Seterusnya](Step-06-Plot-One-Language-ms)
