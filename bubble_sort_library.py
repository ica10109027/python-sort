def bubble_sort(daftar_buku):
    n = len(daftar_buku)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if daftar_buku[j]['Jumlah Halaman'] > daftar_buku[j+1]['Jumlah Halaman']:
                daftar_buku[j], daftar_buku[j+1] = daftar_buku[j+1], daftar_buku[j]

# Daftar buku yang perlu diurutkan berdasarkan jumlah halaman
daftar_buku = [
    {'No.': 1, 'Judul Buku': "Harry Potter and the Sorcerer's Stone", 'Penulis': "J.K. Rowling", 'Jumlah Halaman': 320},
    {'No.': 2, 'Judul Buku': "To Kill a Mockingbird", 'Penulis': "Harper Lee", 'Jumlah Halaman': 281},
    {'No.': 3, 'Judul Buku': "The Great Gatsby", 'Penulis': "F. Scott Fitzgerald", 'Jumlah Halaman': 180},
    {'No.': 4, 'Judul Buku': "Pride and Prejudice", 'Penulis': "Jane Austen", 'Jumlah Halaman': 432},
    {'No.': 5, 'Judul Buku': "1984", 'Penulis': "George Orwell", 'Jumlah Halaman': 328}
]

# Panggil fungsi bubble_sort untuk mengurutkan daftar buku
bubble_sort(daftar_buku)

# Tampilkan daftar buku yang sudah diurutkan berdasarkan jumlah halaman
print("Daftar buku setelah diurutkan berdasarkan jumlah halaman secara ascending:")
for buku in daftar_buku:
    print(f"No. {buku['No.']}: {buku['Judul Buku']} - Jumlah Halaman: {buku['Jumlah Halaman']}")