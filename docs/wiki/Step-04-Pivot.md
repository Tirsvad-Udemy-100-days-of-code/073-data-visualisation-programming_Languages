**English** · [Dansk](Step-04-Pivot-da) · [Bahasa Malaysia](Step-04-Pivot-ms)

# Step 4: pivot the DataFrame

## What we did

We reshaped the data so that each row is a month and each language has its own column.

## Code

```python
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')
reshaped_df.shape   # (145, 14)
```

## Screenshot

![Step 4: pivot the DataFrame](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-04-pivot.png)

## What we gained

- `pivot()` takes the row labels (`index`), the new columns (`columns`) and the cell values (`values`).
- The result has 145 rows and 14 columns: one per month and one per language.
- Months without posts become `NaN`, for example Swift in July 2008; `count()` now differs per column.

[Previous](Step-03-Timestamps) · [Home](Home) · [Next](Step-05-Fill-NaN)
