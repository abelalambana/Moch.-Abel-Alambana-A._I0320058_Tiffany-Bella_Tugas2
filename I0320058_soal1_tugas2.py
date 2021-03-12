from math import pi

print ("======================================")
print ("Tugas 2 Praktikum Programa Komputer")
print ("======================================")
print ("Aplikasi Hitung Cepat")
print ("======================================")


print ("Apakah yang ingin anda hitung?")
print ("1. Persegi Panjang")
print ("2. Lingkaran")
print ("3. Luas Permukaan Kubus")
print ("4. Celcius ke Fahrenheit")
print ("5. Reamur ke Celcius")

cetak = 0
choice = input("Masukkan pilihan anda (1/2/3/4/5): ")

if choice == "1": 
    p = float(input("Masukkan panjangnya : "))
    l = float(input("Masukkan lebarnya : "))
    Luas = p*l

    print ("persegi panjang tersebut memiliki luas sebesar {}" .format(Luas))
    cetak = 1

elif choice == "2":
    r = float(input("Masukkan jari-jarinya : "))
    Luas = pi*r*r

    print ("lingkaran tersebut memiliki luas sebesar {}" .format(Luas))
    cetak = 1

elif choice == "3":
    rusuk = float(input("Masukkan rusuk kubus : "))
    Luas = 6*rusuk**2

    print ("kubus tersebut memiliki luas permukaan sebesar {}" .format(Luas))
    cetak = 1

elif choice == "4":
    celcius = float(input("Masukkan suhunya : "))
    ckef = (9/5 * celcius) + 32

    print ("suhu {} celcius samadengan {} fahrenheit".format(celcius,ckef))
    cetak = 1

elif choice == "5":
    reamur = float(input("Masukkan suhunya : "))
    rkec = 5/4 * reamur 

    print ("suhu {} reamur samadengan {} celcius".format(reamur,rkec))
    cetak = 1

else :
    print("Input tidak ditemukan")
