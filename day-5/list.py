#mendefenisikan list = bisa diubah atau di manipulasi
nama_buah = ["apel","mangga","anggur","jeruk"]

#tuple = array yang tidak bisa dimodifikasi
nama_siswa = ("lengga","ely","nabila","encik","rahman")

#1. menampilkan isi dari list dan tuple (keseluruhan)
print(nama_buah)
print(nama_siswa)

#2, tampilkan sebagian isi dari list
print(nama_buah[1])

#menampilkan sebagian 
print(nama_siswa[1:3])

#3, menampilkan element list dan tople dengan perulangan (looping)
#list
for buah in nama_buah:
    print(buah)
#topl
for siswa in nama_siswa:
    print (siswa)
    
#Menampilkan list DENGAN MEMODIFIKASINYA ATAU MEMANIPULASI LIST
# #1. menghitung jumlah elemen
# jumlah_elemen = len(nama_buah)
# print(jumlah_elemen)

# #2. Mengurutkan elemen dalam list
# #sebelum di urutkan
# print(nama_buah)

# #sesudah diurutkan
# #proses
# nama_buah.sort()
# #hasil
# print(nama_buah)

# #Descanding (terbalik) =menampilkan dari belakang
# #sebelum diurutkan
# print(nama_buah)
# #urutkan elemet
#nama_buah.sort(reverse=True)
#print(nama_buah)

# #3. MENAMBAHKAN ELEMEN BARU
#nama_buah.append("Pisang")
#print(nama_buah)

#4. MENGGANTI ISI ELEMEN pada list
#sebeelum dirubah
# print(nama_buah)
# #setelah diubah
# nama_buah[2] ="Melon"
# print(nama_buah)

#5. MENGHAPUS ISI ELEMENT PADA LIST
#sebeelum dihapus
print(nama_buah)
#setelah dihapuus (menghapus yang terakhir)
#nama_buah.pop()
print(nama_buah)
#untuk menghapus pilihan 
nama_buah.remove("jeruk")
print(nama_buah)