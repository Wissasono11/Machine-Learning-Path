# konsep inheritance (pewarisan) 
"""
anggap kita mempunyai kelas mobil sebagai dasar atau induk, kemudian kita ingin membuat
kelas baru yaitu kelas sport sebagai turunan dari kelas mobil yang sudah ada, kita bisa
memiliki perilaku dan atribut yang sudah ada sebelumnya, selanjutnya kita dapat membuat kelas yang baru sama 
dengan sebelumnya, bahkan mungkin menambahkan fitur baru, seperti turbo pada kelas mobil sport

bagaimana implementasinya?
"""
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil1 =  Mobil("Merah", "Dicoding", 160)
print(mobil1.kecepatan)

# membuat klass terbaru dengan nama "MobilSport"
print("=== membuat kelas mobil biasa dan menambahkan kelas mobil sport ===")
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

# mobil biasa
mobil1 = Mobil("Merah", "Dicoding", 160)
print(mobil1.kecepatan)

# mobil sport
mobilsport1 = MobilSport("Hitam", "Dicoding", 160)
print("Sebelum dipasang turbo: ")
print(mobilsport1.kecepatan)
print("Setelah dipasang turbo: ")
mobilsport1.turbo()
print(mobilsport1.kecepatan)
"""
Output:
160
160
210
"""