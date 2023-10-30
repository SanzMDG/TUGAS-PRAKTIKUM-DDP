kendaraan1 =["avansa", "mobil", "toyota", 1500]
print(kendaraan1)

kendaraan1 = kendaraan1 + ["hitam", 4, 250_000_000]
kendaraan1.remove("mobil")
print(kendaraan1)


pesan = """
menu :
1. menghitung luas persegi
2. menghitung luas lingkaran
3. menghitung lua segitiga
pilih menu
"""
pilihan =input (pesan)

match pilihan:
    case "1":
        print ("anda memasukan angka 1 untuk menghitung luas persegi")
        sisi = int(input ("masukan sisi:"))
        luas = sisi * sisi
        print("luas persegi dengan sisi",sisi, "adalah", luas)

    case "2":
        print ("anda memasukan angka 2 untuk menghitung luas lingkaran")
        jari =int(input("masukan jari jari: "))
        luas = 22/7 *jari* jari
        print("luas lingkaran dengan jari jari", jari, "adalah",luas)

    case "3":
        print ("anda memasukan angka 3 untuk menghitung luas segitiga")
        alas = int(input("masukkan alas : "))
        tinggi = int (input ("masukkan tinggi :"))
        luas = 1/2 * (alas * tinggi) 
        print("luas segitiga dengan alas dan tinggi", alas,tinggi, "adalah", luas)
        


