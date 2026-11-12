[English](Step-07-Style-The-Chart) · **Dansk** · [Bahasa Malaysia](Step-07-Style-The-Chart-ms)

# Trin 7: stil diagrammet

## Hvad vi gjorde

Vi gjorde diagrammet større, forstørrede aksemærkerne, tilføjede aksetekster og lod y-aksen starte ved nul.

## Kode

```python
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```

## Skærmbillede

![Trin 7: stil diagrammet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-07-style-chart.png)

## Hvad vi lærte

- `figure(figsize=...)` ændrer diagrammets størrelse; større diagrammer kræver større skrift.
- `xlabel()`, `ylabel()`, `xticks()` og `yticks()` gør akserne læsbare.
- `ylim(0, 35000)` sætter en nedre grænse på 0, fordi der aldrig er færre end 0 indlæg.

[Forrige](Step-06-Plot-One-Language-da) · [Hjem](Home-da) · [Næste](Step-08-Java-And-Python-da)
