# tugas 1

baris = 3                        # Penjelasan:Menentukan jumlah baris segitiga. Karena total 9 bintang, dan kita tahu 1 + 3 + 5 = 9, maka cukup 3 baris.
for i in range(baris): # ini adalah awal dari loop for, yang akan mengulang sebanyak baris kali (dalam hal ini, sebanyak 3 kali). Fungsi range(baris) menghasilkan urutan angka mulai dari 0 hingga baris-1. Jadi, i akan memiliki nilai
    spasi = ' ' * (baris - i - 1) # spasi di gunakan agar bintang terlihat lebih simetris 
    bintang = '*' * (2 * i + 1)   # menghitung jumlah bintang untuk tiap baris,selalu bilangan ganjil
    print(spasi + bintang)        # mencetak hasil dari spasi + bintang
