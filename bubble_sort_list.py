def bubble_sort(daftarangka):
    n = len(daftarangka)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftarangka[j] < daftarangka[j+1]:
                daftarangka[j], daftarangka[j+1] = daftarangka[j+1], daftarangka[j]
daftarangka = [42,19,33,8,55]
bubble_sort(daftarangka)
print("hasil pengurutan daftar nilai angka:",daftarangka)