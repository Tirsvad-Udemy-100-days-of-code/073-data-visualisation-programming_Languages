[English](Step-02-Group-By-Language) · **Dansk** · [Bahasa Malaysia](Step-02-Group-By-Language-ms)

# Trin 2: gruppér efter sprog

## Hvad vi gjorde

Kolonnen TAG indeholder sproget, så en gruppering efter den besvarer to spørgsmål: hvor mange indlæg hvert sprog har haft siden 2008, og i hvor mange måneder der er data.

## Kode

```python
df.groupby('TAG').sum()
df.groupby('TAG').count()
```

## Skærmbillede

![Trin 2: gruppér efter sprog](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-02-group-by-language.png)

## Hvad vi lærte

- `groupby()` på en kategorikolonne deler rækkerne i én gruppe pr. sprog.
- `sum()` giver det samlede antal indlæg: JavaScript fører med 2.056.510, derefter Java med 1.696.403 og Python med 1.496.210.
- `count()` giver antal måneder med data: C# har 145, Go kun 129 og Swift 135, fordi disse sprog er nyere.

[Forrige](Step-01-Explore-Data-da) · [Hjem](Home-da) · [Næste](Step-03-Timestamps-da)
