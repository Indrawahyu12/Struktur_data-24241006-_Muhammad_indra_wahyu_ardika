def input_data_mahasiswa():
    data_mahasiswa = {}

    try:
        jumlah = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input harus berupa angka.")
        return data_mahasiswa

    for i in range(jumlah):
        print(f"\nMahasiswa ke-{i + 1}")
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")

        mata_kuliah = []
        while True:
            matkul = input("Masukkan nama mata kuliah (atau ketik 'selesai' untuk lanjut): ")
            if matkul.lower() == 'selesai':
                break
            try:
                nilai = float(input(f"Masukkan nilai untuk {matkul}: "))
                mata_kuliah.append((matkul, nilai))
            except ValueError:
                print("Nilai harus berupa angka.")

        data_mahasiswa[nim] = (nama, mata_kuliah)

    return data_mahasiswa

def hitung_rata_rata(nilai_mk):
    if not nilai_mk:
        return 0.0
    total = sum(nilai for _, nilai in nilai_mk)
    return total / len(nilai_mk)

def tampilkan_rekap(data_mahasiswa):
    print("\n=== Daftar Rekapitulasi Mahasiswa ===")
    for nim, (nama, mata_kuliah) in data_mahasiswa.items():
        print(f"\nNIM: {nim}")
        print(f"Nama: {nama}")
        print("Mata Kuliah dan Nilai:")
        for matkul, nilai in mata_kuliah:
            print(f"  - {matkul}: {nilai}")
        rata2 = hitung_rata_rata(mata_kuliah)
        print(f"Rata-rata Nilai: {rata2:.2f}")

def main():
    print("=== Program Rekapitulasi Nilai Mahasiswa ===")
    data = input_data_mahasiswa()
    if data:
        tampilkan_rekap(data)
    else:
        print("Tidak ada data untuk ditampilkan.")

if __name__ == "__main__":
    main()
