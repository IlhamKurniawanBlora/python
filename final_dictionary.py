
# Program Kamus Indonesia-inggris sederhana
# fungsi mengupdate atau mengedit data kamus
def update_data():
    kata = input("Masukan kata yang ingin diperbaharui: ").lower()
    if kata in kamus:
        print(f"Value sebelumnya: {kamus[kata]}")
        new_value_arti = input("Masukan definisi baru: ")
        kamus[kata] = new_value_arti
        print(f"berhasil update kata: {kata} dengan definisi: {new_value_arti}")
        cari_data()
    else:
        print(f"kata: {kata} tidak ditemukan")
        cari_data()


# fungsi menghapus data kamus
def delete_data():
    kata = input("Masukan kata yang ingin dihapus: ").lower()
    if kata in kamus:
        del kamus[kata]
        print(f"Berhasil Menghapus kata: {kata}")
        cari_data()
    else:
        print(f"Kata: {kata} tidak ditemukan")
        cari_data()

# fungsi menambah data kamus
def tambah_data():
    kata = input("Masukkan kata baru : ").lower()
    arti = input("Masukkan definisi: ")
    kamus.update({kata: arti})
    print(f"berhasil Menambahkan data kata: {kata} dengan definisi: {arti}")

# fungsi mencari dan menampilkan data kamus
def cari_data():
    kata = input("Masukan kata yang ingin dicari: ").lower()
    if kata in kamus:
        print(f"Kata {kata} memiliki definisi: {kamus[kata]}")
        print("apakah anda ingin menghapus atau mengupdate data")
        pilihan = (input("ketik 'update'/'delete'/'cari' : ")).lower()
        if pilihan == "update":
            update_data()
        elif pilihan == "delete":
            delete_data()
        elif pilihan == "cari":
            cari_data()
        else:
            print("perintah tidak ditemukan")
            cari_data()
    else:
        print("Kata tidak ditemukan dalam kamus. Cobalah untuk menambahkan data kata.")
        pilihan = int(input("ketik '1' untuk melanjutkan: "))
        if pilihan == 1:
            tambah_data()
            cari_data()
        else:
            print("Terima kasih telah menggunakan Kamus definisi Sederhana!")
            cari_data()

# fungsi utama // main fungsi
def main(kamus):
    print("Selamat datang di Kamus bahasa inggris Sederhana!")
    cari_data()

kamus = {
"message" : "pesanan, berita, warta",
"protein" : "protein",
"sale" : "penjualan, lelang",
"texture anyaman" : "susunan, tenunan",
"unbox" : "mengeluarkan dari peti",
"vagabondage" : "pengembaraan",
"withdraw" : "menarik kembali",
"limit" : "membatasi",
"horrific" : "mengerikan",
"grandeur" : "kemuliaan",
}
# menjalankan fungsi main
main(kamus)

