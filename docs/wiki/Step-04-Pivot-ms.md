[English](Step-04-Pivot) · [Dansk](Step-04-Pivot-da) · **Bahasa Malaysia**

# Langkah 4: pivot DataFrame

## Apa yang kami lakukan

Kami membentuk semula data supaya setiap baris ialah satu bulan dan setiap bahasa mempunyai lajurnya sendiri.

## Kod

```python
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.shape   # (145, 14)
```

## Tangkapan skrin

![Langkah 4: pivot DataFrame](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-04-pivot.png)

## Apa yang kami peroleh

- `pivot()` mengambil label baris (`index`), lajur baharu (`columns`) dan nilai sel (`values`).
- Hasilnya ada 145 baris dan 14 lajur: satu bagi setiap bulan dan satu bagi setiap bahasa.
- Bulan tanpa catatan menjadi `NaN`, contohnya Swift pada Julai 2008; `count()` kini berbeza bagi setiap lajur.

[Sebelumnya](Step-03-Timestamps-ms) · [Utama](Home-ms) · [Seterusnya](Step-05-Fill-NaN-ms)
