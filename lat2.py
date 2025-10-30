"""
Program: Hitung Tiket Masuk Kebun Binatang
Deskripsi:
    Program ini menghitung total biaya tiket masuk berdasarkan umur pengunjung.
    - Umur ≤ 2 tahun      → Gratis
    - Umur 3–12 tahun     → $14
    - Umur ≥ 65 tahun     → $18
    - Umur lainnya        → $23

    Program berjalan berulang hingga pengguna menekan Enter tanpa input umur.
    Setelah itu, pengguna diminta memasukkan jumlah uang,
    dan program menghitung kembalian.
Author  : [Nama Anda]
Version : 1.0
"""

def hitung_harga(umur: int) -> float:
    """
    Mengembalikan harga tiket berdasarkan umur.
    """
    if umur <= 2:
        return 0.0
    elif 3 <= umur <= 12:
        return 14.0
    elif umur >= 65:
        return 18.0
    else:
        return 23.0


def main() -> None:
    """
    Fungsi utama program.
    """
    print("=" * 50)
    print("     PROGRAM HITUNG TIKET MASUK KEBUN BINATANG")
    print("=" * 50)

    total = 0.0

    while True:
        umur_input = input("masukkan umur: ").strip()
        if umur_input == "":
            break

        try:
            umur = int(umur_input)
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            continue

        harga = hitung_harga(umur)

        if harga == 0:
            print("Gratis")
        else:
            print(f"Harga ${harga:.2f}")

        total += harga
        print(f"Running total: {total:.2f}\n")

    if total == 0:
        print("Tidak ada tiket yang dibeli.")
        return

    try:
        uang = float(input("masukkan jumlah uang: "))
        kembalian = uang - total
        print(f"Running kembalian: {kembalian:.2f}")
    except ValueError:
        print("Input uang tidak valid!")


if __name__ == "__main__":
    main()
