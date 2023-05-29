def bubble_sort(daftarnilai):
    n = len(daftarnilai)
    for i in range(n-1):
        for j in range(n-i-1):
            if daftarnilai[j] > daftarnilai[j+1]:
                daftarnilai[j], daftarnilai[j+1] = daftarnilai[j+1], daftarnilai[j]

daftarnilai = [78,65,90,82,70]
bubble_sort(daftarnilai)
print("hasil pengurutan daftar nilai siswa:",daftarnilai)
