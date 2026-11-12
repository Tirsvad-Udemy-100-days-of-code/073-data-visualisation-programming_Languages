[English](Step-10-Rolling-Mean) · **Dansk** · [Bahasa Malaysia](Step-10-Rolling-Mean-ms)

# Trin 10: udglat med glidende gennemsnit

## Hvad vi gjorde

Vi tog gennemsnittet af hver 6 måneder med `rolling(window=6).mean()` og plottede de udglattede serier for at se tendenserne.

## Kode

```python
roll_df = reshaped_df.rolling(window=6).mean()
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=column)
```

## Skærmbillede

![Trin 10: udglat med glidende gennemsnit](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-10-rolling-mean.png)

## Hvad vi lærte

- Tidsserier er støjende; et glidende gennemsnit tager gennemsnittet af et vindue af observationer og flytter det ét trin ad gangen.
- `rolling(window=n).mean()` er pandas' indbyggede måde; de første `n-1` værdier er NaN.
- Et større vindue (12) udglatter mere, et mindre (3) følger data tættere: prøv begge.

[Forrige](Step-09-All-Languages-da) · [Hjem](Home-da)
