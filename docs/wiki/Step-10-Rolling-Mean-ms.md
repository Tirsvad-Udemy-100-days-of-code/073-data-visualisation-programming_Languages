[English](Step-10-Rolling-Mean) · [Dansk](Step-10-Rolling-Mean-da) · **Bahasa Malaysia**

# Langkah 10: licinkan dengan purata bergerak

## Apa yang kami lakukan

Kami memurnikan setiap 6 bulan dengan `rolling(window=6).mean()` dan memplot siri yang dilicinkan untuk melihat trend.

## Kod

```python
roll_df = reshaped_df.rolling(window=6).mean()
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=column)
```

## Tangkapan skrin

![Langkah 10: licinkan dengan purata bergerak](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-10-rolling-mean.png)

## Apa yang kami peroleh

- Siri masa penuh gangguan; purata bergerak mengira purata satu tetingkap cerapan dan menggerakkannya satu langkah demi satu langkah.
- `rolling(window=n).mean()` ialah cara terbina dalam pandas; `n-1` nilai pertama ialah NaN.
- Tetingkap lebih besar (12) melicinkan lebih banyak, yang lebih kecil (3) mengikut data lebih rapat: cuba kedua-duanya.

[Sebelumnya](Step-09-All-Languages-ms) · [Utama](Home-ms)
