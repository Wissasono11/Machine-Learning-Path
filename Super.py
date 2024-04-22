"""
ketika kita ingin menggunakan method atau atribut dari kelas induk
tapi kita malas untuk menuliskan ulang kode. Tujuan adanya super inilah dalam konsep OOP
kita dapat memanfaatkan konsep ini untuk menghindari penulisan kode berulang dan memanfaatkan
fungsi yang sudah ada pada kelas induk (super class)
"""
class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        self.kecepatan += 10
    
class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 10
    
    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("Kecepatan anda meningkat! Hati-Hati!")

# Kelas mobil sport
mobilsport1 = MobilSport("Hitam", "DicodingSportCar", 160)
mobilsport1.tambah_kecepatan() # memanggil method baru
print(mobilsport1.kecepatan)
"""
Output:
Kecepatan Anda meningkat! Hati-hati!
170
"""
"""
pada method ini kita menggunakan super() untuk mengambil method tambah_kecepatan 
yang berasal dari super class atau induknya, yaitu kelas mobil. Dengan begitu program akan
menjalankan metode tersebut dan dibawahnya kita menambahkan teks baru sesuai kebutuhan pada kelas turunan
berupa "Kecepatan anda meningkat! Hati-Hati!"
"""