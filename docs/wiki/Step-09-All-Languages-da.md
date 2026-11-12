[English](Step-09-All-Languages) · **Dansk** · [Bahasa Malaysia](Step-09-All-Languages-ms)

# Trin 9: alle sprog med forklaring

## Hvad vi gjorde

En for-løkke tegner alle sprog med en tykkere linje og en etiket, og en forklaring skelner farverne.

## Kode

```python
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)
plt.legend(fontsize=16)
```

## Skærmbillede

![Trin 9: alle sprog med forklaring](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-09-all-languages.png)

## Hvad vi lærte

- En for-løkke over `columns` sparer os for at skrive `plot()` én gang pr. sprog.
- `label=` og `plt.legend()` forbinder hver farve med et sprog; `linewidth` gør linjerne lettere at se.
- Python har flest indlæg i dataens sidste måneder, mens JavaScript fører i totalen siden 2008.

[Forrige](Step-08-Java-And-Python-da) · [Hjem](Home-da) · [Næste](Step-10-Rolling-Mean-da)
