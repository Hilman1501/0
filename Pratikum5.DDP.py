#buat variabel list dengan value :[nama kendaraan, jenis kendaran, cckendaraan, warna kendaraan,roda kendaraan]
#tambahkan dari list tersebut dibalakang dengan value:[harga kendaraan,tibe kendaran]
#tambahakan setelah jenis kendaraan dengan value [merk kendaraan]


kendaraan=["yamaha", "motor", "6000", "Hitam manis"]

print(kendaraan)

kendaraan.append("Rp.15juta",)
kendaraan.append("Roda 2")
kendaraan.insert(2,"Honda")
kendaraan.insert(1,"Matic")

print(kendaraan)

#buat program python dengan match case untuk menghitung luas bangun datar:
##jika pilih1, maka menghitung persegi
##jika pilih2, maka menghitung lingkaran
#jika pilih3 maka menghitung luas segitiga


import math

def hitung_luas(bentuk, *args):
    match bentuk:
        case "persegi":
            sisi = args[0]
            luas_persegi = sisi ** 2
            return luas_persegi
        case "lingkaran":
            jari_jari = args[0]
            luas_lingkaran = math.pi * jari_jari ** 2
            return luas_lingkaran
        case "segitiga":
            alas, tinggi = args[0], args[1]
            luas_segitiga = 0.5 * alas * tinggi
            return luas_segitiga
        case _:
            return " Salah masukkan pilihan"

print("Luas Persegi:", hitung_luas("persegi", 20))
print("Luas Lingkaran:", hitung_luas("lingkaran", 38))
print("Luas Segitiga:", hitung_luas("segitiga",8,4))#


