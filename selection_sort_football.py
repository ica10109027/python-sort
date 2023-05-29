def selection_sort_players(players):
    n = len(players)
    
    # Iterasi untuk setiap elemen dalam daftar
    for i in range(n):
        
        # Temukan pemain dengan jumlah gol terbanyak dalam sisa daftar yang belum diurutkan
        max_idx = i
        for j in range(i+1, n):
            if players[j]["jumlah_gol"] > players[max_idx]["jumlah_gol"]:
                max_idx = j
        
        # Tukar pemain dengan jumlah gol terbanyak dengan pemain pertama dalam sisa daftar yang belum diurutkan
        players[i], players[max_idx] = players[max_idx], players[i]

# Daftar pemain yang perlu diurutkan berdasarkan jumlah gol
daftar_pemain = [
    {"nama": "Kylian Mbappe", "klub": "Paris Saint-Germain", "jumlah_gol": 40},
    {"nama": "Victor Osimhen", "klub": "Napoli", "jumlah_gol": 28},
    {"nama": "Robert Lewandowski", "klub": "Barcelona", "jumlah_gol": 33},
    {"nama": "Erling Haaland", "klub": "Manchester City", "jumlah_gol": 52},
    {"nama": "Christopher Nkunku", "klub": "RB Leipzig", "jumlah_gol": 22}
]

# Memanggil fungsi selection_sort_players untuk mengurutkan daftar pemain berdasarkan jumlah gol
selection_sort_players(daftar_pemain)

# Menampilkan daftar pemain yang telah diurutkan berdasarkan jumlah gol secara descending
print("Daftar pemain yang diurutkan berdasarkan jumlah gol secara descending:")
for pemain in daftar_pemain:
    print("Nama Pemain:", pemain["nama"])
    print("Klub Pemain:", pemain["klub"])
    print("Jumlah Gol:", pemain["jumlah_gol"])
    print()