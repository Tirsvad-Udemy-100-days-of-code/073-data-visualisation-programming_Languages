**English** · [Dansk](Step-05-Fill-NaN-da) · [Bahasa Malaysia](Step-05-Fill-NaN-ms)

# Step 5: replace NaN values

## What we did

A month without posts means zero posts, so we replaced every NaN with 0 and checked that none were left.

## Code

```python
reshaped_df.fillna(0, inplace=True)
reshaped_df.isna().values.any()   # False
```

## Screenshot

![Step 5: replace NaN values](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-05-fill-nan.png)

## What we gained

- `fillna(0)` replaces missing values; here the right choice is 0, not dropping the rows.
- `inplace=True` updates the DataFrame itself; without it we would reassign the result.
- `isna().values.any()` is a quick check of the whole DataFrame for remaining NaN values.

[Previous](Step-04-Pivot) · [Home](Home) · [Next](Step-06-Plot-One-Language)
