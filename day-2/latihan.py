# #latihan if function

# nilai = input("Masukkan nilai anda : ")

# if int (nilai) >= 80 and int(nilai) <=100 :
#     print("A")
# elif int(nilai) >= 70  and int(nilai) <=80:
#     print("B")
# elif int (nilai) >= 60 and int(nilai) <=70:
#     print("C")
# elif int(nilai) >= 50 and int(nilai) <= 60 :
#     print ("D")
# elif int (nilai) > 100 or int(nilai) < 0:
#     print("tidak valid")
# else :
#     print("E")

nilai = int(input("Masukkan nilai anda : "))


#konversi
if nilai > 100 or nilai < 0:
    print("Nilai Tidak valid")
elif nilai >= 80:
    print("Nilai Anda Adalah " + str (nilai) + "Predikat Nilai Anda : A")
elif nilai >= 70 and nilai < 80 :
    print("Nilai Anda Adalah " + str (nilai) + "Predikat Nilai Anda : B")
elif nilai >= 60 and nilai < 70 :
    print("Nilai Anda Adalah " + str (nilai) + "Predikat Nilai Anda : C")
elif nilai >= 50 and nilai < 60:
    print("Nilai Anda Adalah " + str (nilai) + "Predikat Nilai Anda : D")
else :
    print("Nilai Anda Adalah " + str (nilai) + "Predikat Nilai Anda : E")