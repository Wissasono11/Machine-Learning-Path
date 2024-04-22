#python interpreter

print("===block code===")
for i in range(10):
    print(i)
"""
kode perulangan diatas juga melakukan aksi sekunsial
yakni setiap kode akan dijalankan lalu diulangi hingga kondisi
akhir terpenuhi. Kode blok yang baik dan benar akan memudahkan interpreter
atau compiler untuk berjalan dengan baik dan tidak menghasilkan error.
"""
#contoh
#for i in range(10):
#print(i)
"""
Output:
IndentationError: expected an indented block
"""

print("===case-sensitive===")
"""
artinya python memperlakukan huruf besar dan kecil
sebagai karakter yang berbda dalam penamaan variabel, nama fungsi, atau
penulisan kode secara umum
"""
teks = "Dicoding"
Teks = "Indonesia"
print(teks)
print(Teks)

"""
teks = "Dicoding"
Teks = "Indonesia"

print(teks)
print(Teks)
print(TEks)

Output:
Dicoding
Indonesia
NameError: name 'TEks' is not defined
"""