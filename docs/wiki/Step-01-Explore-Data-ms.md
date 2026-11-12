[English](Step-01-Explore-Data) · [Dansk](Step-01-Explore-Data-da) · **Bahasa Malaysia**

# Langkah 1: teroka data

## Apa yang kami lakukan

Kami membaca eksport Stack Overflow ke dalam DataFrame, memberi nama sendiri kepada lajur dan melihat lima baris pertama dan terakhir, bentuk data serta bilangan nilai bagi setiap lajur.

## Kod

```python
df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)
df.head()
df.tail()
df.shape
df.count()
```

## Tangkapan skrin

![Langkah 1: teroka data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-01-explore-data.png)

## Apa yang kami peroleh

- `read_csv` dengan `names` dan `header=0` menggantikan nama lajur dalam fail.
- `head()` dan `tail()` mengesahkan bahawa pemuatan berjaya sebelum analisis bermula.
- `shape` menunjukkan 1991 baris dan 3 lajur; `count()` mengira nilai bukan NaN bagi setiap lajur.

[Utama](Home-ms) · [Seterusnya](Step-02-Group-By-Language-ms)
