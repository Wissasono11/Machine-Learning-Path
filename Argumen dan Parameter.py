#argumen dan parameter adalah dua hal yang berbeda 
# def fungsi(a,b,c)                      
    #function body
# a, b, c merupakan parameter namun saat dipanggil dengan nilai 1, b=50, c='Dicoding'menjadi argumen
# def fungsi (nilai 1, b = 50, c = "Dicoding")
print("=== Argumen ===")
# argumen ada 2 jenis :
# 1. keyword argument -> jenis argumen yang disertai dengan nama parameter(identifier) dan secara eksplisit disebutkan.
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

print(persegi_panjang_pertama)

"""
Output:
50
"""
# contoh penulisan keyword argument "panjang=5" dan "lebar=10" diberikan saat pemanggilan fungsi
# 2. Positional Argument -> positional artinya kita tidak menyebutkan nama parameter secara eksplisit ketika memanggil fungsi 
#                           Ketika memanggil fungsi, Anda hanya harus memasukkan nilai yang ingin diberikan. 
#                           Namun, Anda harus mengikuti urutan dari parameter fungsi tersebut.
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

print(persegi_panjang_pertama)
"""
Output:
50
"""
# contoh di atas kita memanggil fungsi "mencari_luas_persegi_panjang" dengan argumen 5 dan 10
# masing-masing merupakan paramater panjang dan lebar, walaupun kita menukar urutan nilainya, program akan menganggap
# panjangnya 10 dan lebarnya 5
print("=== Positional-Keyword ===")
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))
"""
Output:
Halo, Dicoding! Selamat pagi!
Halo, Dicoding! Selamat sore!
"""
print("=== Positional-Only ===")
def penjumlahan (a, b, /):
    return a + b

print(penjumlahan(8, 50))
"""
Output:
58
"""
print("=== Keyword-Only ===")
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan
print(greeting(pesan="Selamat sore!",nama="Dicoding"))
"""
Output:
Halo, Dicoding! Selamat sore!
"""
print("=== Var-Postional(Variadic Postional Parameter ===")
def hitung(*args): # *args mengumpulkan semua argumen posisi yang diberikan saat pemanggilan fungsi dan membungkusnya menjadi tuple "args"
    print(type(args))
    total = sum(args)
    return total
print(hitung(1,2,3))
"""
Output:
<class 'tuple'>
6
"""
print("=== Var-Keyword ===")
# **kwargs berperan sebagai dictionary(seperti tipe datanya)
def cetak(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
