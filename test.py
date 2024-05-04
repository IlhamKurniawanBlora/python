def tambah_data(kamus):
    kata = input("Masukkan kata baru dalam bahasa Indonesia: ").lower()
    arti = input("Masukkan arti kata dalam bahasa Rusia: ").lower()
    kamus.update({kata: arti})

def cari_arti(kata):
    if kata in kamus:
        return kamus[kata]
    else:
        return "Kata tidak ditemukan dalam kamus. Untuk menambahkan, ketik 'tambah' dan ikuti petunjuknya."

kamus = {
    "rumah": "дом",
    "makan": "есть",
    "minum": "пить",
    "kucing": "кошка",
    "mobil": "машина"
}

tambah_data(kamus)

print(kamus)
