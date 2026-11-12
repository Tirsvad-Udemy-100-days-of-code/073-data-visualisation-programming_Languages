**English** · [Dansk](Step-09-All-Languages-da) · [Bahasa Malaysia](Step-09-All-Languages-ms)

# Step 9: all languages with a legend

## What we did

A for-loop draws every language, with a thicker line and a label, and a legend tells the colours apart.

## Code

```python
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3, label=reshaped_df[column].name)
plt.legend(fontsize=16)
```

## Screenshot

![Step 9: all languages with a legend](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-09-all-languages.png)

## What we gained

- A for-loop over `columns` avoids typing `plot()` once per language.
- `label=` and `plt.legend()` connect each colour to a language; `linewidth` makes the lines easier to see.
- Python is the most posted language in the last months of the data, while JavaScript leads in the total since 2008.

[Previous](Step-08-Java-And-Python) · [Home](Home) · [Next](Step-10-Rolling-Mean)
