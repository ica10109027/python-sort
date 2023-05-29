def selection_sort(daftar_angka):
    n = len(daftar_angka)
    for i in range(n-1):
        indeks_terkecil = i
        for j in range(i+1, n):
            if daftar_angka[j] < daftar_angka[indeks_terkecil]:
                indeks_terkecil = j

        daftar_angka[i], daftar_angka[indeks_terkecil] = daftar_angka[indeks_terkecil], daftar_angka[i]

# Daftar angka yang dimiliki Andi
daftar_angka = [9, 5, 3, 8, 2]

# Panggil fungsi selection_sort untuk mengurutkan daftar angka
selection_sort(daftar_angka)

# Tampilkan daftar angka yang sudah diurutkan
print("Daftar angka setelah diurutkan: ", daftar_angka)