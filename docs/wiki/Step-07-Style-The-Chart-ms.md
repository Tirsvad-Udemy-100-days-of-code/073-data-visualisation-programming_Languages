[English](Step-07-Style-The-Chart) · [Dansk](Step-07-Style-The-Chart-da) · **Bahasa Malaysia**

# Langkah 7: gayakan carta

## Apa yang kami lakukan

Kami membesarkan carta, membesarkan label tanda, menambah label paksi dan menetapkan paksi-y bermula pada sifar.

## Kod

```python
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
```

## Tangkapan skrin

![Langkah 7: gayakan carta](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/073-data-visualisation-programming_Languages/raw/branch/main/docs/images/step-07-style-chart.png)

## Apa yang kami peroleh

- `figure(figsize=...)` mengubah saiz carta; carta yang lebih besar memerlukan fon yang lebih besar.
- `xlabel()`, `ylabel()`, `xticks()` dan `yticks()` menjadikan paksi mudah dibaca.
- `ylim(0, 35000)` menetapkan had bawah 0, kerana tidak pernah ada kurang daripada 0 catatan.

[Sebelumnya](Step-06-Plot-One-Language-ms) · [Utama](Home-ms) · [Seterusnya](Step-08-Java-And-Python-ms)
