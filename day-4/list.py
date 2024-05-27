#mendefenisikan list
nama_buah = ["apel","mangga","anggur","jeruk"]

#tuple = array yang tidak bisa dimodifikasi
nama_siswa = ("lengga","ely","nabila","encik","rahman")

#menampilkan isi dari list dan tuple
print(nama_buah)
print(nama_siswa)

#tampilkan sebagian isi dari list
print(nama_buah[1])

#menampilkan sebagian 
print(nama_siswa[1:3])

#menampilkan element list dan tople dengan perulangan
#list
for buah in nama_buah:
    print(buah)
#topl
for siswa in nama_siswa:
    print (siswa)