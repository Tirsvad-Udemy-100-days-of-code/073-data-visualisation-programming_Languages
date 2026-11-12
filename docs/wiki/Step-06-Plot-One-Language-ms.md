[English](Step-06-Plot-One-Language) · [Dansk](Step-06-Plot-One-Language-da) · **Bahasa Malaysia**

# Langkah 6: plot satu bahasa

## Apa yang kami lakukan

Satu baris kod melukis populariti Java dari semasa ke semasa: tarikh pada paksi-x, catatan pada paksi-y.

## Kod

```python
plt.plot(reshaped_df.index, reshaped_df.java)
```

## Tangkapan skrin

![Langkah 6: plot satu bahasa](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-06-plot-java.png)

## Apa yang kami peroleh

- `plt.plot(x, y)` memerlukan nilai-x (indeks) dan nilai-y (satu lajur).
- Indeks DataFrame yang dipivot ialah tarikh, jadi siri masa boleh diplot terus.
- Carta kosong ini sudah menunjukkan naik turun Java, tetapi sukar dibaca.

[Sebelumnya](Step-05-Fill-NaN-ms) · [Utama](Home-ms) · [Seterusnya](Step-07-Style-The-Chart-ms)
