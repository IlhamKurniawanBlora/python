# Program Kamus Indonesia-Rusia sederhana
def update_data():
    kata = input("Masukan kata yang ingin diperbaharui: ").lower()
    if kata in kamus:
        print(f"Value sebelumnya: {kamus[kata]}")
        new_value_arti = input("Masukan definisi baru: ")
        kamus[kata] = new_value_arti
        print(f"berhasil update kata: {kata} dengan definisi: {new_value_arti}")
    else:
        print(f"kata: {kata} tidak ditemukan")

def delete_data():
    kata = input("Masukan kata yang ingin dihapus: ").lower()
    if kata in kamus:
        del kamus[kata]
        print(f"Berhasil Menghapus kata: {kata}")
    else:
        print(f"Kata: {kata} tidak ditemukan")

def tambah_data():
    kata = input("Masukkan kata baru : ").lower()
    arti = input("Masukkan definisi: ")
    kamus.update({kata: arti})
    print(f"berhasil Menambahkan data kata: {kata} dengan definisi: {arti}")

def cari_data():
    kata = input("Masukan kata yang ingin dicari: ").lower()
    if kata in kamus:
        print(f"Kata {kata} memiliki definisi: {kamus[kata]}")
        cari_data()
    else:
        print("Kata tidak ditemukan dalam kamus. Cobalah untuk menambahkan data kata.")
        pilihan = int(input("ketik '1' untuk melanjutkan: "))
        if pilihan == 1:
            cari_data()
        else:
            print("Terima kasih telah menggunakan Kamus definisi Sederhana!")
            exit

def main(kamus):
    print("Selamat datang di Kamus definisi Sederhana!")
    print("Pilihan:")
    print("1. Search")
    print("2. Update")
    print("3. Delete")
    print("4. Add")
    print("5. exit")
    choice = int(input("Masukan Pilihanmu (1/2/3/4/5): "))
    if choice == 1:
        cari_data()
        main(kamus)
    elif choice == 2:
        update_data()
        main(kamus)
    elif choice == 3:
        delete_data()
        main(kamus)
    elif choice == 4:
        tambah_data()
        main(kamus)
    elif choice == 5:
        print("Terima kasih telah menggunakan Kamus definisi Sederhana!")
        exit      
    else:
        print("Pilihan tidak ditemukan. Pastikan pilihan sesuai dengan list")
        main(kamus)


kamus = {
   "rumah": "gedung untuk tempat tinggal manusia",
    "makan": "makan",
    "minum": "minum",
    "kucing": "binatang kecil yang ditemani, carnivora dengan bulu lembut, hidung pendek, dan kaki belakang yang dapat ditarik kembali",
    "mobil": "kendaraan bermotor dengan empat roda; biasanya dipropelkan oleh mesin pembakaran internal",
    "buku": "serangkaian kertas cetak, gambar, atau kosong, yang dibuat dari tinta, kertas, pergamen, atau bahan lainnya, biasanya disatukan bersama untuk hingga di satu sisi",
    "tas": "tas atau kantong dengan tangan atau tali pinggang, digunakan untuk mengangkut barang-barang pribadi",
    "komputer": "mesin elektronik yang digunakan untuk melakukan perhitungan secara otomatis",
    "telepon": "bertukar ucapan dengan seseorang melalui telepon",
    "televisi": "perangkat elektronik yang menerima dan menampilkan pancaran televisi, biasanya di layar"
}
main(kamus)