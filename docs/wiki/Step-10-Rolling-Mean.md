**English** · [Dansk](Step-10-Rolling-Mean-da) · [Bahasa Malaysia](Step-10-Rolling-Mean-ms)

# Step 10: smooth with a rolling mean

## What we did

We averaged every 6 months with `rolling(window=6).mean()` and plotted the smoothed series to see the trends.

## Code

```python
roll_df = reshaped_df.rolling(window=6).mean()
for column in roll_df.columns:
    plt.plot(roll_df.index, roll_df[column], linewidth=3, label=column)
```

## Screenshot

![Step 10: smooth with a rolling mean](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-10-rolling-mean.png)

## What we gained

- Time series are noisy; a rolling mean averages a window of observations and moves it one step at a time.
- `rolling(window=n).mean()` is the built-in pandas way; the first `n-1` values are NaN.
- A bigger window (12) smooths more, a smaller one (3) follows the data closer: try both.

[Previous](Step-09-All-Languages) · [Home](Home)
