[English](Step-02-Group-By-Language) · [Dansk](Step-02-Group-By-Language-da) · **Bahasa Malaysia**

# Langkah 2: kumpulkan mengikut bahasa

## Apa yang kami lakukan

Lajur TAG mengandungi bahasa, jadi pengumpulan mengikutnya menjawab dua soalan: berapa banyak catatan setiap bahasa sejak 2008 dan dalam berapa bulan ada data.

## Kod

```python
df.groupby('TAG').sum()
df.groupby('TAG').count()
```

## Tangkapan skrin

![Langkah 2: kumpulkan mengikut bahasa](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-02-group-by-language.png)

## Apa yang kami peroleh

- `groupby()` pada lajur kategori membahagikan baris kepada satu kumpulan bagi setiap bahasa.
- `sum()` memberi jumlah catatan: JavaScript mendahului dengan 2,056,510, kemudian Java dengan 1,696,403 dan Python dengan 1,496,210.
- `count()` memberi bilangan bulan data: C# ada 145, Go hanya 129 dan Swift 135, kerana bahasa itu lebih baharu.

[Sebelumnya](Step-01-Explore-Data-ms) · [Utama](Home-ms) · [Seterusnya](Step-03-Timestamps-ms)
