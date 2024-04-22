class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50
    
    def tambah_kecepatan(self):     # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobilsport1 = MobilSport("Hitam", "DicodingSportCar", 160)
print(mobilsport1.kecepatan)
mobilsport1.tambah_kecepatan()     # Memanggil metode baru tambah kecepatan()
print(mobilsport1.kecepatan)

# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "DicodingCar", 160)
print(mobil_1.kecepatan)
mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)
"""
Output:
160
180
"""
"""
yang perlu dipahami bahwa menimpa bukan berarti mengubah metode dari kelas induk
Hall ini karena metode dari kelas baru merupakan hasil dari inheritance sehingga tidak 
akan mengubah metode dari kelas induk.
"""