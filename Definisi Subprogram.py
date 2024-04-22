# subprogram -> serangkaian instruksi dirancang melakukan operasi
#               yang sering digunakan dalam suatu program.
#Luas Pertama
"""panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

#Luas Kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)"""
"""
Output:
50
60
"""
# kode seperti diatas tidak efisien dan 
# mengakibatkan perulangan kode yang perlu diketik berulang
def luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang1 = luas_persegi_panjang(5, 10)
print(persegi_panjang1)

persegi_panjang2 = luas_persegi_panjang(4, 15)
print(persegi_panjang2)
"""
Output:
50
60
"""
