"""
Program: Hitung Rata-rata Nilai Huruf (Versi Interaktif)
Deskripsi:
    Program ini menerima input nilai huruf satu per satu,
    menampilkan hasil konversinya ke angka,
    lalu menghitung rata-rata di akhir.
Author  : [Nama Anda]
Version : 1.1
"""

def konversi_nilai(huruf: str) -> float:
    """
    Mengonversi nilai huruf menjadi angka.
    """
    konversi = {
        "A": 4.00,
        "A-": 3.75,
        "B+": 3.50,
        "B": 3.00,
        "B-": 2.75,
        "C+": 2.50,
        "C": 2.00,
        "C-": 1.75,
        "D": 1.50,
        "E": 1.25
    }
    return konversi.get(huruf.upper(), None)


def main():
    """
    Fungsi utama untuk menjalankan program.
    """
    print("=" * 50)
    print("     PROGRAM HITUNG RATA-RATA NILAI HURUF")
    print("=" * 50)

    total = 0
    count = 0

    while True:
        huruf = input("masukkan nilai: ").strip().upper()
        if huruf == "":
            break  # tekan Enter kosong untuk berhenti

        nilai = konversi_nilai(huruf)
        if nilai is not None:
            print(f"nilai = {nilai}")
            total += nilai
            count += 1
        else:
            print("Nilai huruf tidak valid! Coba lagi.")
            continue

    if count > 0:
        rata = total / count
        print(f"\nrata - rata nya adalah: {rata}")
    else:
        print("\nTidak ada nilai yang dimasukkan.")


if __name__ == "__main__":
    main()
