**English** · [Dansk](Step-08-Java-And-Python-da) · [Bahasa Malaysia](Step-08-Java-And-Python-ms)

# Step 8: two lines in one chart

## What we did

Calling `plot()` twice draws Java and Python next to each other.

## Code

```python
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)
```

## Screenshot

![Step 8: two lines in one chart](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-08-java-and-python.png)

## What we gained

- Every `plot()` call adds a line to the same chart.
- Comparing two series on the same axes shows how Python overtakes Java in the later years.
- Without a legend we cannot tell the lines apart yet: that is the next step.

[Previous](Step-07-Style-The-Chart) · [Home](Home) · [Next](Step-09-All-Languages)
