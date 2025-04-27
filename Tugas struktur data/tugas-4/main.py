# Variabel global untuk menyimpan data mahasiswa
mahasiswa = []

# Fungsi CREATE
def create():
    nama = input("Masukkan nama mahasiswa: ")
    mahasiswa.append(nama)
    print("Data berhasil ditambahkan.")

# Fungsi READ
def read():
    print("Daftar Mahasiswa:")
    for i, nama in enumerate(mahasiswa):
        print(f"{i}. {nama}")

# Fungsi UPDATE
def update():
    read()
    index = int(input("Masukkan indeks yang ingin diubah: "))
    if 0 <= index < len(mahasiswa):
        nama_baru = input("Masukkan nama baru: ")
        mahasiswa[index] = nama_baru
        print("Data berhasil diubah.")
    else:
        print("Indeks tidak valid.")

# Fungsi DELETE
def delete():
    read()
    index = int(input("Masukkan indeks yang ingin dihapus: "))
    if 0 <= index < len(mahasiswa):
        mahasiswa.pop(index)
        print("Data berhasil dihapus.")
    else:
        print("Indeks tidak valid.")

# Fungsi menu
def show_menu():
    print("\n=== Menu ===")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Mahasiswa")
    print("3. Ubah Mahasiswa")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

# Main loop
while True:
    show_menu()
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == '1':
        create()
    elif pilihan == '2':
        read()
    elif pilihan == '3':
        update()
    elif pilihan == '4':
        delete()
    elif pilihan == '5':
        print("Program selesai.")
        exit()
    else:
        print("Pilihan tidak valid.")