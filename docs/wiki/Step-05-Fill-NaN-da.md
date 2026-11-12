[English](Step-05-Fill-NaN) · **Dansk** · [Bahasa Malaysia](Step-05-Fill-NaN-ms)

# Trin 5: erstat NaN-værdier

## Hvad vi gjorde

En måned uden indlæg betyder nul indlæg, så vi erstattede alle NaN med 0 og kontrollerede, at ingen var tilbage.

## Kode

```python
reshaped_df.fillna(0, inplace=True)
reshaped_df.isna().values.any()   # False
```

## Skærmbillede

![Trin 5: erstat NaN-værdier](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-05-fill-nan.png)

## Hvad vi lærte

- `fillna(0)` erstatter manglende værdier; her er 0 det rigtige valg i stedet for at fjerne rækkerne.
- `inplace=True` opdaterer selve DataFrame; uden det skulle vi gentildele resultatet.
- `isna().values.any()` er en hurtig kontrol af hele DataFrame for resterende NaN-værdier.

[Forrige](Step-04-Pivot-da) · [Hjem](Home-da) · [Næste](Step-06-Plot-One-Language-da)
