[English](Step-04-Pivot) · **Dansk** · [Bahasa Malaysia](Step-04-Pivot-ms)

# Trin 4: pivotér DataFrame

## Hvad vi gjorde

Vi omformede data, så hver række er en måned, og hvert sprog har sin egen kolonne.

## Kode

```python
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.shape   # (145, 14)
```

## Skærmbillede

![Trin 4: pivotér DataFrame](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-04-pivot.png)

## Hvad vi lærte

- `pivot()` tager rækkenavne (`index`), de nye kolonner (`columns`) og cellernes værdier (`values`).
- Resultatet har 145 rækker og 14 kolonner: én pr. måned og én pr. sprog.
- Måneder uden indlæg bliver til `NaN`, for eksempel Swift i juli 2008; `count()` er nu forskellig pr. kolonne.

[Forrige](Step-03-Timestamps-da) · [Hjem](Home-da) · [Næste](Step-05-Fill-NaN-da)
