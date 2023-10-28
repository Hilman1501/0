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

print("Luas Persegi:", hitung_luas("persegi", 7))
print("Luas Lingkaran:", hitung_luas("lingkaran", 8))
print("Luas Segitiga:", hitung_luas("segitiga",8,4))#





pilihan=int(input('menghitung luas bangun datar; '))
match pilihan:
    case "persegi":
        sisi = int(input('Input panjang sisi persegi: '))
        luas_p= sisi* sisi
        print('Luas persegi', luas_p)

    case "lingkaran":
        jari2 = float(input('Input jari-jari lingkaran: '))
        luas_L= 3.14 * jari2 * jari2
        print('Luas lingkaran', int(luas_L))
    
    case "segitiga":
        print(" menghitung segitiga")
        alas = int(input("Alas  : "))
        tinggi = int(input("Tinggi: "))
        luas_S= alas*tinggi/2
        print('Luas Segitiga ', int(luas_S))





