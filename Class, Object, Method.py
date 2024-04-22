"""
mobil adalah jenis kendaraan roda 4 yang memiliki kemampuan untuk bergerak maju, mundur, berbelok, 
dan berhenti. mobil dapat melaju dalam kecepatan dari 0 hingga sekian km/jam, mobil juga memiliki variasi 
warna yang beragam warna, merah, hitam, dan warna lainnya

mobil -> class 
perilaku mobil -> method (maju, mundur, belok, berhenti)
karakteristik mobil -> atribut (warna, kecepatan)

class diibaratkan sebagai blueprint atau cetakan. Ketika class sudah terbuat maka
kita dapat membuat sebuah objek baru berdasarkan class tersebut. 
"""
"""
Object-Oriented Programming -> paradigma pemrograman berorientasi pada pengorganisasian kode menjadi objek-objek yang memiliki
                               atribut dan perilaku (method)
Objek -> perwujudan dari class dengan menganggap kelas adalah cetakan yang memungkinkan kita membuat banyak objek berdasarkan cetakan
Method -> perilaku atau tindakan yang dapat dilakukan objek atau kelas.
Atribut -> variabel yang menjadi identitas dari objek atau kelas
"""
print("=== class ===")
class Mobil:
    warna = "Merah"
print("Tidak ada keluaran")
# jika dijalan tidak akan mengeluarkan output apapun karena kita belum memanggil kelas
# tersebut dan mendefinisikan kembali nilai (return)

print("=== object ===")
class Mobil:
    warna = 'Merah'

mobil1 =Mobil() #membuat sebuah objek dan menyimpannya dalam variabel mobil1
print(mobil1.warna) #print(nama_objek.nama_atribut)

# kita juga dapat mengubah atribut yang sudah ada
class Mobil:
    warna = 'Merah'

mobil1 = Mobil()
mobil1.warna = "Biru" #bagian yang mengubah atribut kelas
print(mobil1.warna)

print("=== atribut ===")
"""
perlu diperhatikan jika nilai atribut kelas diubah, perubahan tersebut akan
memengaruhi semua objek yang dibuat berdasarkan kelas
"""
class Mobil:
    warna ="Merah"

mobil1 = Mobil()
print(mobil1.warna)

mobil2 = Mobil()
print(mobil2.warna)

#mengubah atribut kelas 
Mobil.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)
"""
Output:
Merah
Merah
Hitam
Hitam
"""
"""
hasilnya  akan berubah semula merah menjadi hitam
"""

print("=== class constructor ===")
# sebuah fungsi khusus dalam python yang digunakan untuk menentukan nial awal atau kondisi awal
# dari suatu kelas. 
class Mobil:
    def __init__(self):
        self.warna = 'Merah'
"""
kita membuat fungsi bernama "__init__" sebagai fungsi khusus yang menjadi
constructor. Kita menggunakan parameter self, yakni sebuah kata kunci untuk merujuk
objek yang sedang diproses saat ini.

artinya ketika membuat instance "mobil1", constructor akan dipanggil pertama kali dan self
akan merujuk pada instance "mobil1". Hal ini memungkinkan setiap objek baru memiliki atribut masing-masing.
Jika kita dapat mengubah atribut suatu objek tanpa memengaruhi objek lainnya.

self.warna -> jenis dari atribut instance, yakni atribut yang terkait dengan instance itu sendiri
"""
class Mobil:
    def __init__(self):
        self.warna = 'Merah'

mobil1 = Mobil()
mobil2 = Mobil()

print(mobil1.warna)
print(mobil2.warna)

mobil1.warna = "Hitam"

print(mobil1.warna)
print(mobil2.warna)
"""
Output:
Merah
Merah
Hitam
Merah
"""
print("=== menambahkan parameter ===")
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

mobil1 = Mobil('Hitam', 'Pajero', '180')

print(mobil1.warna)
print(mobil1.merek)
print(mobil1.kecepatan)

print("=== Method ===")
# method terbagi menjadi 3 jenis
"""
1. Method Object
2. Method Static
3. Metode Class

Dekorator -> fungsi dalam python yang mengembalikan fungsi lain,
             biasanya di awali dengan sintaks "@" diawal
"""
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Memanggil fungsi yang sudah didekorasi
say_hello()
"""
Output:
Sebelum fungsi dieksekusi.
Hello, world!
Setelah fungsi dieksekusi.
"""

print("=== Method Object ===")
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil1 = Mobil("Merah", "Dicoding", 160)
print("Sebelum ditambahkan: ") 
print(mobil1.kecepatan)

mobil1.tambah_kecepatan() # memanggil metode tambah_kecepatan.

print("Setelah ditambahkan: ") 
print(mobil1.kecepatan)

print("=== Method Static ===")
"""
static method fungsi atau method pada sebuah kelas yang bersifat statis.
Artinya, metode atau fungsi bersifat independen dan tidak terikat pada instance kelas.
Metode ini dianggap seperti membuat fungsi seperti biasa.
"""
class Mobil:
    def __init__(self, merek):
        self.merek = merek
    
    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""

print("=== Method Class ===")
"""
termasuk jenis metode yang sangat spesial dalam python"""
class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas mobil")

    Mobil.intro_mobil()
    mobil1 = Mobil("Dicodingcar")
    mobil1.intro_mobil()

"""
Output:
Ini adalah metode dari kelas Mobil
Ini adalah metode dari kelas Mobil
"""