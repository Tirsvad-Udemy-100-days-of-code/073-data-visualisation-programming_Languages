**English** · [Dansk](Home-da) · [Bahasa Malaysia](Home-ms)

# Programming Languages: Day 73

Which programming language is the most popular? This wiki follows Day 73 of Udemy's 100 Days of Code step by step: each page shows the code, a screenshot and what we gained in that step.

| Page | Read it when you want to |
| --- | --- |
| [Getting started](Getting-Started) | Set up and run |
| [Step 1: explore the data](Step-01-Explore-Data) | We read the Stack Overflow export into a DataFrame, gave the columns our own names and looked at the first and last five rows, the shape and the number of entries per column |
| [Step 2: group by language](Step-02-Group-By-Language) | The TAG column holds the language, so grouping by it answers two questions: how many posts each language has had since 2008 and in how many months it has data |
| [Step 3: work with timestamps](Step-03-Timestamps) | The dates were read as text |
| [Step 4: pivot the DataFrame](Step-04-Pivot) | We reshaped the data so that each row is a month and each language has its own column |
| [Step 5: replace NaN values](Step-05-Fill-NaN) | A month without posts means zero posts, so we replaced every NaN with 0 and checked that none were left |
| [Step 6: plot one language](Step-06-Plot-One-Language) | One line of code draws the popularity of Java over time: dates on the x-axis, posts on the y-axis |
| [Step 7: style the chart](Step-07-Style-The-Chart) | We made the chart larger, enlarged the tick labels, added axis labels and fixed the y-axis to start at zero |
| [Step 8: two lines in one chart](Step-08-Java-And-Python) | Calling `plot()` twice draws Java and Python next to each other |
| [Step 9: all languages with a legend](Step-09-All-Languages) | A for-loop draws every language, with a thicker line and a label, and a legend tells the colours apart |
| [Step 10: smooth with a rolling mean](Step-10-Rolling-Mean) | We averaged every 6 months with `rolling(window=6).mean()` and plotted the smoothed series to see the trends |

![Screenshot](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-09-all-languages.png)
