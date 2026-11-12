[English](Home) · **Dansk** · [Bahasa Malaysia](Home-ms)

# Programmeringssprog: dag 73

Hvilket programmeringssprog er mest populært? Denne wiki følger dag 73 af Udemys 100 Days of Code trin for trin: hver side viser koden, et skærmbillede og hvad vi lærte i det trin.

| Side | Læs den, når du vil |
| --- | --- |
| [Kom i gang](Getting-Started-da) | Opsætning og kørsel |
| [Trin 1: udforsk data](Step-01-Explore-Data-da) | Vi læste Stack Overflow-eksporten ind i en DataFrame, gav kolonnerne egne navne og så på de første og sidste fem rækker, formen og antallet af værdier i hver kolonne |
| [Trin 2: gruppér efter sprog](Step-02-Group-By-Language-da) | Kolonnen TAG indeholder sproget, så en gruppering efter den besvarer to spørgsmål: hvor mange indlæg hvert sprog har haft siden 2008, og i hvor mange måneder der er data |
| [Trin 3: arbejd med tidsstempler](Step-03-Timestamps-da) | Datoerne blev læst som tekst |
| [Trin 4: pivotér DataFrame](Step-04-Pivot-da) | Vi omformede data, så hver række er en måned, og hvert sprog har sin egen kolonne |
| [Trin 5: erstat NaN-værdier](Step-05-Fill-NaN-da) | En måned uden indlæg betyder nul indlæg, så vi erstattede alle NaN med 0 og kontrollerede, at ingen var tilbage |
| [Trin 6: plot ét sprog](Step-06-Plot-One-Language-da) | Én kodelinje tegner Javas popularitet over tid: datoer på x-aksen, indlæg på y-aksen |
| [Trin 7: stil diagrammet](Step-07-Style-The-Chart-da) | Vi gjorde diagrammet større, forstørrede aksemærkerne, tilføjede aksetekster og lod y-aksen starte ved nul |
| [Trin 8: to linjer i ét diagram](Step-08-Java-And-Python-da) | Når `plot()` kaldes to gange, tegnes Java og Python ved siden af hinanden |
| [Trin 9: alle sprog med forklaring](Step-09-All-Languages-da) | En for-løkke tegner alle sprog med en tykkere linje og en etiket, og en forklaring skelner farverne |
| [Trin 10: udglat med glidende gennemsnit](Step-10-Rolling-Mean-da) | Vi tog gennemsnittet af hver 6 måneder med `rolling(window=6).mean()` og plottede de udglattede serier for at se tendenserne |

![Skærmbillede](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-09-all-languages.png)
