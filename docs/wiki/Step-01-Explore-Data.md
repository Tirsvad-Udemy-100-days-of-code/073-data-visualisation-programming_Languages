**English** · [Dansk](Step-01-Explore-Data-da) · [Bahasa Malaysia](Step-01-Explore-Data-ms)

# Step 1: explore the data

## What we did

We read the Stack Overflow export into a DataFrame, gave the columns our own names and looked at the first and last five rows, the shape and the number of entries per column.

## Code

```python
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.head()
df.tail()
df.shape
df.count()
```

## Screenshot

![Step 1: explore the data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-01-explore-data.png)

## What we gained

- `read_csv` with `names` and `header=0` replaces the column names of the file.
- `head()` and `tail()` verify that the loading worked before any analysis starts.
- `shape` shows 1991 rows and 3 columns; `count()` counts the non-NaN values per column.

[Home](Home) · [Next](Step-02-Group-By-Language)
