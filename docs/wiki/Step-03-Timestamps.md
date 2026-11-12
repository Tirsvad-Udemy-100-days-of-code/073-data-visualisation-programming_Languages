**English** · [Dansk](Step-03-Timestamps-da) · [Bahasa Malaysia](Step-03-Timestamps-ms)

# Step 3: work with timestamps

## What we did

The dates were read as text. We checked the type of one cell and converted the whole column to timestamps.

## Code

```python
type(df['DATE'][1])           # str
df['DATE'] = pd.to_datetime(df['DATE'])
```

## Screenshot

![Step 3: work with timestamps](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-03-timestamps.png)

## What we gained

- A string is not a date: it cannot be sorted or plotted as time.
- `pd.to_datetime()` turns text into `Timestamp` objects that know how to handle dates and times.
- Converting the whole column once makes every later step (pivot, plot) work on real time data.

[Previous](Step-02-Group-By-Language) · [Home](Home) · [Next](Step-04-Pivot)
