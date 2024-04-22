#fungsi -> pemetaan antara 2 himpunan nilai, yaitu domain dan range
#          input(domain) dan output(range). Output tersebut pasti terkait dengan input
#          bagaimana pun kondisinya.
# notasi fungsi -> f(x) = 2x -> f = nama fungsi, x = input, 2x = apa yang harus dikeluarkan

#fungsi dalam pemrograman -> mengubah suatu bentuk menjadi bentuk lain dengan aturan yang sama
"""
Dalam Python fungsi terbagi 2 jenis:
1. Built-in Functions -> fungsi bawaan adalah kumpulan fungsi yang sudah terintegrasi dengan bahsa pemrograman
                         Python sehingga tidak perlu mengimpor modul atau library tambahan. Contoh fungsi bawaan 
                         adalah print(), len(), type(), range(), dan sebagainya.
2. User-defined Functions -> jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. contoh dari fungsi ini adalah
                             luas persegi panjang
"""
print("=== user-defined functions ===")
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

"""
Output:
50
60
"""
print("=== kegunaan fungsi ===")
"""
1. program dapat dipecah menjadi bagian yang menjadi kecil (sub)
2. penggunaan ulang kode alih-alih menulis ulang kode
3. setiap fungsi bersifat indenpenden dan dapat diuji secara terpisah
"""
print("=== mendefinisikan fungsi dalam python ===")
#def mencari_luas_persegi_panjang(panjang, lebar): -> function header
#    luas_persegi_panjang = panjang*lebar -> function body 
#    return luas_persegi_panjang
#       ^
#    function return
"""
1. function header -> mendefinisikan suatu fungsi
2. function body -> blok kode yang diindentasikan setelah header fungsi
3. functiomn return -> pernyataan yang digunakan dalam fungsi untuk mengembalikan nilai atau hasil eksekusi dari fungsi tersebut.
"""
def rectangle(long, width):
    luas = long * width 
    return luas
luas1 = rectangle(10, 5) # ini adalah pemanggilan fungsi
print(luas1)
"""
Output:
50
"""
print("=== docstring ===")
#docstring -> akronim dari documentation string, bertujuan utnuk membuat dokumentasi terhadap 
#             fungsi yang dibuat. umumnya berupa argumen, returun, deskripsi fungsi, dan sebaliknya
def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang

    Args:
        panjang(int) : panjang persegi panjang
        lebar(int) : lebar persegi panjang
    
    Returns:
        int: Luas persegi panjang hasil perhitungan
    """
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

"""
Output:
50
"""