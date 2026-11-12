[English](Step-03-Timestamps) · [Dansk](Step-03-Timestamps-da) · **Bahasa Malaysia**

# Langkah 3: bekerja dengan cap masa

## Apa yang kami lakukan

Tarikh dibaca sebagai teks. Kami menyemak jenis satu sel dan menukar seluruh lajur kepada cap masa.

## Kod

```python
type(df['DATE'][1])           # str
df['DATE'] = pd.to_datetime(df['DATE'])
```

## Tangkapan skrin

![Langkah 3: bekerja dengan cap masa](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-03-timestamps.png)

## Apa yang kami peroleh

- Rentetan bukan tarikh: ia tidak boleh diisih atau diplot sebagai masa.
- `pd.to_datetime()` menukar teks kepada objek `Timestamp` yang tahu mengendalikan tarikh dan masa.
- Menukar seluruh lajur sekali menjadikan setiap langkah seterusnya (pivot, plot) berfungsi pada data masa sebenar.

[Sebelumnya](Step-02-Group-By-Language-ms) · [Utama](Home-ms) · [Seterusnya](Step-04-Pivot-ms)
