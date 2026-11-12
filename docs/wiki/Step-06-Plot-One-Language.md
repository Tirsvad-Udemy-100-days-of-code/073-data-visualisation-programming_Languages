**English** · [Dansk](Step-06-Plot-One-Language-da) · [Bahasa Malaysia](Step-06-Plot-One-Language-ms)

# Step 6: plot one language

## What we did

One line of code draws the popularity of Java over time: dates on the x-axis, posts on the y-axis.

## Code

```python
plt.plot(reshaped_df.index, reshaped_df.java)
```

## Screenshot

![Step 6: plot one language](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-06-plot-java.png)

## What we gained

- `plt.plot(x, y)` needs the x-values (the index) and the y-values (a column).
- The index of the pivoted DataFrame is the date, so a time series plots directly.
- The bare chart already shows the rise and fall of Java, but it is hard to read.

[Previous](Step-05-Fill-NaN) · [Home](Home) · [Next](Step-07-Style-The-Chart)
