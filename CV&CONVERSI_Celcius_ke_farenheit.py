soal1="/---------/biodata diri-------"
print("Nama: Hilman")
print("Nim: 0110223303")
print("kelas: TI05")
print("No telp:082339333542")
print("Alamat:jagakarsa_srengsengsawah")
print("Asal; NTB")
print("menggambar")

print("====================================")

soal2="/---------Biodata diri-------------/"
print("Nama: Adikurniawan")
print("nim:0110223168")
print("kelas;TI05")
print("no.telepon:085333635854")
print("alamat: jagakarsa")
print("asal:NTB")
print("sepakbola")





soal3="/--------------/berat badan ideal--------"

def calc_BMI(berat, tinggi):

    # Rumus BMI
    BMI = berat / (tinggi * tinggi)
    print("Nilai BMI anda:",BMI)

    if BMI > 22.9:
        return "Overweight"
    elif BMI < 18.5:
        return "Underweight"
    else:
        return "Normal"
    


soal4="/-----------------nilai konversi dari celcius ke fahreinheit -------------------"
print('##  Program Python Konversi Suhu  ##')
print('====================================')
print()
 
celc = float(input('Input suhu celsius: '))
 
hilma = (9/5 * celc) + 32
hilmy = celc + 273.15
adi = celc * (4/5)
 
print(celc,'derajat Celsius =',hilma,'derajat hilma')
print(celc,'derajat Celsius =',hilmy,'derajat hilmy')
print(celc,'derajat Celsius =',adi,'derajat adi')

print ("--- Program Menghitung Volume dan Luas tabung motubablog ---\n")

tinggi=int(input("Masukan Tinggi : "))
jari=int(input("Masukan Jari-jari Lingkaran : "))

phi=22/7

luas=int(2*phi*jari*(tinggi+jari))
volume=int((phi*(jari*jari))*tinggi)

print ("Luas tabung = ", luas)
print ("Volume tabung=",volume)

