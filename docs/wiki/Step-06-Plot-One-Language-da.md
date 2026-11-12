[English](Step-06-Plot-One-Language) · **Dansk** · [Bahasa Malaysia](Step-06-Plot-One-Language-ms)

# Trin 6: plot ét sprog

## Hvad vi gjorde

Én kodelinje tegner Javas popularitet over tid: datoer på x-aksen, indlæg på y-aksen.

## Kode

```python
plt.plot(reshaped_df.index, reshaped_df.java)
```

## Skærmbillede

![Trin 6: plot ét sprog](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-06-plot-java.png)

## Hvad vi lærte

- `plt.plot(x, y)` skal bruge x-værdierne (indekset) og y-værdierne (en kolonne).
- Indekset i den pivoterede DataFrame er datoen, så en tidsserie kan plottes direkte.
- Det nøgne diagram viser allerede Javas op- og nedgang, men er svært at læse.

[Forrige](Step-05-Fill-NaN-da) · [Hjem](Home-da) · [Næste](Step-07-Style-The-Chart-da)
