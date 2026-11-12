[English](Step-09-All-Languages) · [Dansk](Step-09-All-Languages-da) · **Bahasa Malaysia**

# Langkah 9: semua bahasa dengan legenda

## Apa yang kami lakukan

Gelung for melukis setiap bahasa dengan garisan lebih tebal dan label, dan legenda membezakan warna.

## Kod

```python
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)
plt.legend(fontsize=16)
```

## Tangkapan skrin

![Langkah 9: semua bahasa dengan legenda](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-09-all-languages.png)

## Apa yang kami peroleh

- Gelung for pada `columns` mengelakkan menaip `plot()` sekali bagi setiap bahasa.
- `label=` dan `plt.legend()` mengaitkan setiap warna dengan bahasa; `linewidth` menjadikan garisan lebih mudah dilihat.
- Python ialah bahasa dengan catatan terbanyak pada bulan-bulan terakhir data, manakala JavaScript mendahului dalam jumlah sejak 2008.

[Sebelumnya](Step-08-Java-And-Python-ms) · [Utama](Home-ms) · [Seterusnya](Step-10-Rolling-Mean-ms)
