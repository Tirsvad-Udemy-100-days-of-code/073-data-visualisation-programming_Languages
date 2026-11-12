[English](Step-08-Java-And-Python) · [Dansk](Step-08-Java-And-Python-da) · **Bahasa Malaysia**

# Langkah 8: dua garisan dalam satu carta

## Apa yang kami lakukan

Memanggil `plot()` dua kali melukis Java dan Python bersebelahan.

## Kod

```python
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python)
```

## Tangkapan skrin

![Langkah 8: dua garisan dalam satu carta](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-08-java-and-python.png)

## Apa yang kami peroleh

- Setiap panggilan `plot()` menambah satu garisan pada carta yang sama.
- Membandingkan dua siri pada paksi yang sama menunjukkan Python mengatasi Java pada tahun-tahun kemudian.
- Tanpa legenda kita belum dapat membezakan garisan: itu langkah seterusnya.

[Sebelumnya](Step-07-Style-The-Chart-ms) · [Utama](Home-ms) · [Seterusnya](Step-09-All-Languages-ms)
