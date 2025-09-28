list_semua = [
    ["Endometril", "Tablet", "Bebas Terbatas"],
    ["Gastran", "Tablet", "Bebas"],
    ["Salbutamol", "Cair", "Keras"],
    ["Morfin", "Analgesik", "Narkotika"]
]
list_obat = ("Endometril", "Gastran", "Salbutamol", "Morfin")
list_golongan = ("Bebas", "Bebas Terbatas", "Keras", "Narkotika")
list_bentuk = ("Tablet", "Cair", "Analgesik")
laporan_bulan = [
    ["Nama Obat: Endometril", "Stok Awal: 5", "Keluar: 2", "Masuk: 3", "Stok Akhir: 5"],
    ["Nama Obat: Gastran", "Stok Awal: 5", "Keluar: 4", "Masuk: 2", "Stok Akhir: 3"],
    ["Nama Obat: Salbutamol", "Stok Awal: 6", "Keluar: 2", "Masuk: 3", "Stok Akhir: 7"],
    ["Nama Obat: Morfin", "Stok Awal: 7", "Keluar: 5", "Masuk: 6", "Stok Akhir: 8"]
]
stok_obat = {
    "Endometril": "5",
    "Gastran": "3",
    "Salbutamol": "7",
    "Morfin": "8"
}

#program utama
def login():
    while True:
        try:
            print("[1] Apoteker")
            print("[2] Admin gudang")
            opsi=int(input("Pilih Opsi 1-2 : "))
            if opsi == 1:
                username = str(input("Masukkan nama anda: "))
                password = str(input("Masukkan password anda: "))
                if username == "Shoto" and password == "todorokisho":
                    print("------------------------------------------------------")
                    print("Login berhasil! Selamat datang, Apoteker Shoto!")
                    print("------------------------------------------------------")
                    print("Pendataan Obat di Rumah Sakit")
                    print("[1] Input Data Obat")
                    print("[2] Cari Obat")
                    print("[3] Keluar")
                    opsi=int(input("Pilih Opsi 1-3 : "))
                    if opsi == 1:
                        list_semua.append(input("Nama Obat, Bentuk sediaan, Golongan Obat: "))
                        for element in list_semua:
                            print(element)
                        break
                    elif opsi == 2:
                        search_filter = input("Search atau Filter? : ")
                        if search_filter == "Search":
                            cari_obat = input("Ingin mencari obat apa? : ")
                            if cari_obat in list_obat:
                                print(f"{cari_obat}: Obat Tersedia")
                                if cari_obat in ["Endometril"]:
                                    print("Bentuk sediaan: Obat Tablet")
                                    print("Golongan: Obat Bebas Terbatas")
                                    break
                                elif cari_obat in ["Gastran"]:
                                    print("Bentuk sediaan: Obat Tablet")
                                    print("Golongan: Obat Bebas")
                                    break
                                elif cari_obat in ["Salbutamol"]:
                                    print("Bentuk sediaan: Obat Cair")
                                    print("Golongan: Obat Keras")
                                    break
                                elif cari_obat in ["Morfin"]:
                                    print("Bentuk sediaan: Obat Analgesik")
                                    print("Golongan: Obat Narkotika")
                                    break
                            else:
                                print("Obat Tidak Tersedia")
                                break
                        elif search_filter == "Filter":
                            golongan_bentuk = input("Golongan atau Bentuk sediaan obat? : ")
                            if golongan_bentuk == "Golongan":
                                cari_golongan = input("Ingin mencari golongan obat apa? : ")
                                if cari_golongan in list_golongan:
                                    print(f"{cari_golongan}: Golongan Obat Tersedia")
                                    if cari_golongan in ["Bebas"]:
                                        print("Gastran")
                                        break
                                    elif cari_golongan in ["Bebas Terbatas"]:
                                        print("Endometril")
                                        break
                                    elif cari_golongan in ["Keras"]:
                                        print("Salbutamol")
                                        break
                                    elif cari_golongan in ["Narkotika"]:
                                        print("Morfin")
                                        break
                                else:
                                    print("Golongan Obat Tidak Tersedia")
                                    break
                            elif golongan_bentuk == "Bentuk":
                                cari_bentuk = input("Ingin mencari bentuk obat apa? : ")
                                if cari_bentuk in list_bentuk:
                                    print(f"{cari_bentuk}: Bentuk Obat Tersedia")
                                    if cari_bentuk in ["Tablet"]:
                                        print("Endometril", "Gastran", sep=", ")
                                        break
                                    if cari_bentuk in ["Cair"]:
                                        print("Sabutamol")
                                        break
                                    if cari_bentuk in ["Analgesik"]:
                                        print("Morfin")
                                        break
                                else:
                                    print("Bentuk Obat Tidak Tersedia")
                                    break
                            else:
                                print("Opsi Tidak Tersedia")
                                break
                        else: 
                            print("Opsi Tidak Tersedia")
                            break
                    elif opsi == 3:
                        break
                    else:
                        print("Opsi Tidak Tersedia")
                        break
                else:
                    print("Login gagal! Nama atau password anda salah.")
            elif opsi == 2:
                username = str(input("Masukkan nama anda: "))
                password = str(input("Masukkan password anda: "))
                if username == "Bakugo" and password == "bkgkatsu":
                    print("------------------------------------------------------")
                    print("Login berhasil! Selamat datang, Admin Gudang Bakugo!")
                    print("------------------------------------------------------")
                    print("[1] Cetak/Export Laporan Stok")
                    print("[2] Update Stok")
                    print("[3] Keluar")

                    opsi=int(input("Pilih Opsi 1-3 : "))
                    if opsi == 1:
                        export_laporan = input("Cetak/Export laporan masuk/keluar obat bulan ini? ( Ya / Tidak ) : ")
                        if export_laporan == "Ya":
                            for element in laporan_bulan:
                                print(element)
                            break
                        else:
                            break
                    elif opsi == 2:
                        tambah_stok = input("Apakah ingin mengupdate stok obat? ( Ya / Tidak ) : ")
                        if tambah_stok == "Ya":
                            print("Stok obat telah berhasil di update!")
                            stok_obat["Salbutamol"] = "9"
                            stok_obat["Gastran"] = "1"
                            stok_obat["Endometril"] = "7"
                            stok_obat["Morfin"] = "5"
                            print(stok_obat)
                            break
                        else:
                            break
                    elif opsi == 3:
                        break
                    else:
                        print("Opsi Tidak Tersedia")
                        break
                else:
                    print("Login gagal! Nama atau password anda salah.")
        except ValueError:
            print("Tolong masukkan angka.")
        except KeyboardInterrupt:
            print("Jangan tekan CTRL C ya")
        except EOFError:
            print("Jangan tekan CTRL Z ya")

login()