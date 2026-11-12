[English](Step-03-Timestamps) · **Dansk** · [Bahasa Malaysia](Step-03-Timestamps-ms)

# Trin 3: arbejd med tidsstempler

## Hvad vi gjorde

Datoerne blev læst som tekst. Vi kontrollerede typen af en celle og konverterede hele kolonnen til tidsstempler.

## Kode

```python
type(df['DATE'][1])           # str
df['DATE'] = pd.to_datetime(df['DATE'])
```

## Skærmbillede

![Trin 3: arbejd med tidsstempler](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-03-timestamps.png)

## Hvad vi lærte

- En streng er ikke en dato: den kan ikke sorteres eller plottes som tid.
- `pd.to_datetime()` gør tekst til `Timestamp`-objekter, der kan håndtere datoer og tidspunkter.
- Når hele kolonnen konverteres én gang, arbejder alle senere trin (pivot, plot) på rigtige tidsdata.

[Forrige](Step-02-Group-By-Language-da) · [Hjem](Home-da) · [Næste](Step-04-Pivot-da)
