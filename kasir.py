import pandas as pd,os


class kasir:
    def __init__(self):
        self.data = {}
        self.total_penghasilan = 0
    def banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("\tAplikasi Kasir Untuk Penjualan")
    def menu(self):
        print("""
1. Tambah Data Penjualan
2. Melihat Hasil Penjualan
3. Keluar
        """)
    def tambah_data(self,nama,harga):
        nama_ = []
        harga_ = []
        nama_.append(nama)
        harga_.append(harga)
        self.data["Nama Barang"] = nama_
        self.data["Harga Barang"] = harga_
        self.total_penghasilan += harga
    def lihat_hasil(self):
        if len(self.data) == 0:
            print("\nTidak Ada Transaksi Hari Ini !")
        else:
            hasil = pd.DataFrame(self.data)
            print(hasil)
            print("\nTotal Hasil Penjualan Hari Ini :",self.total_penghasilan)

aplikasi = kasir()
while True:
        aplikasi.banner()
        aplikasi.menu()
        pilihan = int(input("masukan nomor menu : "))
        if pilihan == 1:
            nama = input("masukkan nama barang : ")
            harga = int(input("masukkan harga barang : "))
            aplikasi.tambah_data(nama,harga)
            input("data berhasil ditambahkan\n\ntekan enter untuk kembali ke menu !")
        elif pilihan == 2:
            aplikasi.lihat_hasil()
            input("\ntekan enter untuk kembali ke menu !")
        elif pilihan == 3:
            exit("keluar dari aplikasi kasir")
        else:print("masukkan nomor menu !");continue