[English](Step-01-Explore-Data) · **Dansk** · [Bahasa Malaysia](Step-01-Explore-Data-ms)

# Trin 1: udforsk data

## Hvad vi gjorde

Vi læste Stack Overflow-eksporten ind i en DataFrame, gav kolonnerne egne navne og så på de første og sidste fem rækker, formen og antallet af værdier i hver kolonne.

## Kode

```python
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.head()
df.tail()
df.shape
df.count()
```

## Skærmbillede

![Trin 1: udforsk data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-01-explore-data.png)

## Hvad vi lærte

- `read_csv` med `names` og `header=0` erstatter filens kolonnenavne.
- `head()` og `tail()` kontrollerer, at indlæsningen virkede, før analysen starter.
- `shape` viser 1991 rækker og 3 kolonner; `count()` tæller værdier, der ikke er NaN, i hver kolonne.

[Hjem](Home-da) · [Næste](Step-02-Group-By-Language-da)
