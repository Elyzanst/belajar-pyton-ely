#array mempunyai nilai key (kunci) dan value (nilai)
#dictionary = OBJEK =array assosiatif
#1. MENDEFENISIKAN DICTIONARY
biodata = {"nama":"Elyza", "umur":22,"alamat":"sumut"}
#menampilkan
print(biodata)
#memanggil elemen pada dictopnary
print(biodata["umur"])

#2. Menambahkan elemen baru
biodata["jurusan"]="S2 Teknik Informatika"
print(biodata)

#3. MERUBAH DATA
biodata["alamat"]="PADANG"
print(biodata)

#MENGHAPPUS ELEMEN
del biodata["umur"]
print(biodata)