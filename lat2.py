nama_bulan = [
    "", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

while True:
    try:
        tahun = int(input("Masukkan tahun (contoh: 2024): "))
        bulan = int(input("Masukkan bulan (1-12): "))

        if bulan < 1 or bulan > 12:
            print("Input tidak valid. Harap masukkan angka bulan antara 1 dan 12.\n")
            continue

    except ValueError:
        print("Input tidak valid. Harap masukkan angka numerik untuk tahun dan bulan.\n")
        continue

    jumlah_hari = 0
    while True:
        if bulan in [1, 3, 5, 7, 8, 10, 12]:
            jumlah_hari = 31
            break

        if bulan in [4, 6, 9, 11]:
            jumlah_hari = 30
            break

        if bulan == 2:
            if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
                jumlah_hari = 29
            else:
                jumlah_hari = 28
            break

    print(f"-> Jumlah hari di bulan {nama_bulan[bulan]} tahun {tahun} adalah {jumlah_hari} hari.")
    print("-" * 30)

    ulangi = input("Apakah Anda ingin mengecek bulan lain? (y/n): ")
    if ulangi.lower() != 'y':
        print("Terima kasih telah menggunakan program ini.")
        break
    print()