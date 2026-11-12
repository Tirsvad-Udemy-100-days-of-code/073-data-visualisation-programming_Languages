**English** · [Dansk](Step-02-Group-By-Language-da) · [Bahasa Malaysia](Step-02-Group-By-Language-ms)

# Step 2: group by language

## What we did

The TAG column holds the language, so grouping by it answers two questions: how many posts each language has had since 2008 and in how many months it has data.

## Code

```python
df.groupby('TAG').sum()
df.groupby('TAG').count()
```

## Screenshot

![Step 2: group by language](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-02-group-by-language.png)

## What we gained

- `groupby()` on a category column splits the rows into one group per language.
- `sum()` gives the total posts: JavaScript leads with 2,056,510, then Java with 1,696,403 and Python with 1,496,210.
- `count()` gives the months of data: C# has 145, Go only 129 and Swift 135, because those languages are newer.

[Previous](Step-01-Explore-Data) · [Home](Home) · [Next](Step-03-Timestamps)
