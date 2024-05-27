print("PROGRAM MENGHITUNG LUAS DAN KELILING BANGUN DATAR")
print("By: ELY NURHALIZAH NST")



#rumus
def hitung_persegi():
    print("MENGHITUNG NILAI PERSEGI")
    sisi = float(input("\nMasukkan panjang sisi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi: " + str (luas))
    print("Keliling Persegi: " + str (keliling))

def hitung_persegi_panjang():
    print("MENGHITUNG NILAI PERSEGI PANJANG")
    panjang = float(input("\nMasukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang: "+ str (luas))
    print("Keliling Persegi Panjang:" + str (keliling))
    
def hitung_segitiga():
    print("MENGHITUNG NILAI SEGITIGA")
    alas = float(input("\nMasukkan panjang alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi1 = float(input("Masukkan panjang sisi 1: "))
    sisi2 = float(input("Masukkan panjang sisi 2: "))
    sisi3 = float(input("Masukkan panjang sisi 3: "))
    luas = 0.5 * alas * tinggi
    keliling = sisi1 + sisi2 + sisi3
    print(f"Luas Segitiga: {luas}")
    print(f"Keliling Segitiga: {keliling}")

def hitung_lingkaran():
    print("MENGHITUNG NILAI LINGKARAN")
    jari_jari = float(input("\nMasukkan panjang jari-jari: "))
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    print(f"Luas Lingkaran: {luas}")
    print(f"Keliling Lingkaran: {keliling}")

def hitung_belah_ketupat():
    print("MENGHITUNG NILAI BELAH KETUPAT")
    diagonal1 = float(input("\nMasukkan panjang diagonal 1: "))
    diagonal2 = float(input("Masukkan panjang diagonal 2: "))
    sisi = float(input("Masukkan panjang sisi: "))
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print(f"Luas Belah Ketupat: {luas}")
    print(f"Keliling Belah Ketupat: {keliling}")
    
def main():
    while True:
        print("\nPilih bentuk geometri yang ingin dihitung:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Belah Ketupat")
        
        #MASUKKAN INPUT
        pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

        if pilihan == str (1):
            hitung_persegi()
        elif pilihan == '2':
            hitung_persegi_panjang()
        elif pilihan == '3':
            hitung_segitiga()
        elif pilihan == '4':
            hitung_lingkaran()
        elif pilihan == '5':
            hitung_belah_ketupat()
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

        lagi = input("Apakah Anda ingin mengulangi perhitungan? (ya/tidak): ").lower()
        if lagi != 'y':
            break

if __name__ == "__main__":
    main()

