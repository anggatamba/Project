# Data mobil rental
mobil_rental = [
    {"plat": "B1234XYZ", "jenis": "SUV", "merk": "Toyota", "tahun": 2020, "harga": 500000, "status": "Tersedia"},
    {"plat": "B5678ABC", "jenis": "Sedan", "merk": "Honda", "tahun": 2021, "harga": 400000, "status": "Tersedia"},
    {"plat": "B9876LMN", "jenis": "Minibus", "merk": "Suzuki", "tahun": 2019, "harga": 600000, "status": "Tersedia"},
    {"plat": "B8765QWE", "jenis": "SUV", "merk": "Mitsubishi", "tahun": 2020, "harga": 550000, "status": "Tersedia"}
]

# Data pelanggan
pelanggan = []

# Fungsi untuk menampilkan data dalam bentuk tabel secara manual
def tampilkan_tabel(data, headers):
    col_widths = [max(len(str(item[key])) for item in data + [dict(zip(headers, headers))]) for key in headers]

    header_row = " | ".join(f"{headers[i].ljust(col_widths[i])}" for i in range(len(headers)))
    print(header_row)

    print("-" * len(header_row))

    # Print rows
    for item in data:
        row = " | ".join(f"{str(item[key]).ljust(col_widths[i])}" for i, key in enumerate(headers))
        print(row)
    

def lihat_semua_mobil():
    print("\nDaftar Mobil:")
    headers = ["plat", "jenis", "merk", "tahun", "harga", "status"]
    tampilkan_tabel(mobil_rental, headers)

# Fungsi untuk menambahkan mobil baru
def tambah_mobil():
    plat = input("Masukkan plat mobil: ")
    jenis = input("Masukkan jenis mobil: ")
    merk = input("Masukkan merk mobil: ")
    tahun = int(input("Masukkan tahun mobil: "))
    harga = int(input("Masukkan harga rental mobil: "))
    
    mobil_rental.append({"plat": plat, "jenis": jenis, "merk": merk, "tahun": tahun, "harga": harga, "status": "Tersedia"})
    print(f"Mobil dengan plat {plat} berhasil ditambahkan.")

# Fungsi untuk mengedit data mobil
def edit_mobil(plat_mobil):
    for mobil in mobil_rental:
        if mobil["plat"] == plat_mobil:
            mobil["jenis"] = input(f"Masukkan jenis mobil baru (sebelumnya: {mobil['jenis']}): ")
            mobil["merk"] = input(f"Masukkan merk mobil baru (sebelumnya: {mobil['merk']}): ")
            mobil["tahun"] = int(input(f"Masukkan tahun mobil baru (sebelumnya: {mobil['tahun']}): "))
            mobil["harga"] = int(input(f"Masukkan harga rental mobil baru (sebelumnya: {mobil['harga']}): "))
            print(f"Data mobil dengan plat {plat_mobil} berhasil diupdate.")
            return
    print(f"Mobil dengan plat {plat_mobil} tidak ditemukan.")

# Fungsi untuk menghapus mobil
def hapus_mobil(plat_mobil):
    for mobil in mobil_rental:
        if mobil["plat"] == plat_mobil:
            mobil_rental.remove(mobil)
            print(f"Mobil dengan plat {plat_mobil} berhasil dihapus.")
            return
    print(f"Mobil dengan plat {plat_mobil} tidak ditemukan.")

# Fungsi untuk mencari mobil berdasarkan plat
def cari_mobil(plat_mobil):
    for mobil in mobil_rental:
        if mobil["plat"] == plat_mobil:
            headers = ["plat", "jenis", "merk", "tahun", "harga", "status"]
            tampilkan_tabel([mobil], headers)
            return mobil
    print(f"Mobil dengan plat {plat_mobil} tidak ditemukan.")
    return None

# Fungsi untuk melihat stok mobil
def lihat_stok_mobil():
    print("\nMobil Tersedia:")
    headers = ["plat", "jenis", "merk", "tahun", "harga", "status"]
    stok_tersedia = [mobil for mobil in mobil_rental if mobil["status"] == "Tersedia"]
    tampilkan_tabel(stok_tersedia, headers)

# Fungsi untuk menyewa mobil
def sewa_mobil(plat_mobil, identitas_pelanggan):
    mobil = cari_mobil(plat_mobil)
    if mobil and mobil["status"] == "Tersedia":
        mobil["status"] = "Disewa"
        pelanggan.append({"plat": plat_mobil, "identitas": identitas_pelanggan})
        print(f"Mobil dengan plat {plat_mobil} berhasil disewa oleh pelanggan {identitas_pelanggan}.")
    else:
        print(f"Mobil dengan plat {plat_mobil} tidak tersedia untuk disewa.")

# Fungsi untuk mengembalikan mobil
def kembalikan_mobil(plat_mobil, identitas_pelanggan):
    for rental in pelanggan:
        if rental["plat"] == plat_mobil and rental["identitas"] == identitas_pelanggan:
            for mobil in mobil_rental:
                if mobil["plat"] == plat_mobil:
                    mobil["status"] = "Tersedia"
                    pelanggan.remove(rental)
                    print(f"Mobil dengan plat {plat_mobil} telah dikembalikan oleh pelanggan {identitas_pelanggan}.")
                    return
    print(f"Mobil dengan plat {plat_mobil} tidak ditemukan dalam sewaan untuk pelanggan {identitas_pelanggan}.")

# Fungsi untuk mencari pelanggan berdasarkan identitas
def cari_pelanggan(identitas_pelanggan):
    for rental in pelanggan:
        if rental["identitas"] == identitas_pelanggan:
            headers = ["identitas", "plat"]
            tampilkan_tabel([rental], headers)
            return rental
    print(f"Pelanggan dengan identitas {identitas_pelanggan} tidak ditemukan.")
    return None

# Menu utama
def menu():
    while True:
        print("\n===== Sistem Rental Mobil =====")
        print("1. Lihat semua mobil")
        print("2. Tambah mobil")
        print("3. Edit data mobil")
        print("4. Hapus mobil")
        print("5. Cari mobil")
        print("6. Lihat stok mobil")
        print("7. Sewa mobil")
        print("8. Kembalikan mobil")
        print("9. Cari pelanggan")
        print("10. Keluar")
        
        pilihan = input("Pilih menu (1-10): ")

        if pilihan == "1":
            lihat_semua_mobil()
        elif pilihan == "2":
            tambah_mobil()
        elif pilihan == "3":
            plat_mobil = input("Masukkan plat mobil yang ingin diubah: ")
            edit_mobil(plat_mobil)
        elif pilihan == "4":
            plat_mobil = input("Masukkan plat mobil yang ingin dihapus: ")
            hapus_mobil(plat_mobil)
        elif pilihan == "5":
            plat_mobil = input("Masukkan plat mobil yang ingin dicari: ")
            cari_mobil(plat_mobil)
        elif pilihan == "6":
            lihat_stok_mobil()
        elif pilihan == "7":
            plat_mobil = input("Masukkan plat mobil yang ingin disewa: ")
            identitas_pelanggan = input("Masukkan identitas pelanggan (misalnya nomor KTP): ")
            sewa_mobil(plat_mobil, identitas_pelanggan)
        elif pilihan == "8":
            plat_mobil = input("Masukkan plat mobil yang ingin dikembalikan: ")
            identitas_pelanggan = input("Masukkan identitas pelanggan: ")
            kembalikan_mobil(plat_mobil, identitas_pelanggan)
        elif pilihan == "9":
            identitas_pelanggan = input("Masukkan identitas pelanggan: ")
            cari_pelanggan(identitas_pelanggan)
        elif pilihan == "10":
            print("Terima kasih telah menggunakan sistem rental mobil.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

# Menjalankan menu utama
menu()
