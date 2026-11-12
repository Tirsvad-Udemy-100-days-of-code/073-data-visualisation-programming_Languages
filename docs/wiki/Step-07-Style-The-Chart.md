**English** · [Dansk](Step-07-Style-The-Chart-da) · [Bahasa Malaysia](Step-07-Style-The-Chart-ms)

# Step 7: style the chart

## What we did

We made the chart larger, enlarged the tick labels, added axis labels and fixed the y-axis to start at zero.

## Code

```python
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```

## Screenshot

![Step 7: style the chart](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-07-style-chart.png)

## What we gained

- `figure(figsize=...)` resizes the chart; larger charts need larger fonts.
- `xlabel()`, `ylabel()`, `xticks()` and `yticks()` make the axes readable.
- `ylim(0, 35000)` sets a lower bound of 0, because there are never fewer than 0 posts.

[Previous](Step-06-Plot-One-Language) · [Home](Home) · [Next](Step-08-Java-And-Python)
