"""
string -> upper() mengubah setiap huruf dalam string menjadi huruf kapital
          lower() mengubah setiap huruf dalam string menjadi huruf kecil
          split() memisahkan teks berdasarkan delimiter(karakter pemisah)
          title() jadikan setiap awal kata kapital
          zfill() tambahkan nol diawal string sebanyak nilai yang ada pada parameter
"""
tesString = "dicoding"
print(tesString.upper())
print(tesString.lower())
print(tesString.split("i"))
print(tesString.title())
print(tesString.zfill(20))

"""
regex (regular expression) -> sebuah cara untuk mencari teks berdasarkan pola tertentu.
                              contoh dari regex adalah email kita menggunakan regex untuk mengecek
                              bahwa karakter @ ada pada email atau tidak
"""
import re # import modul regex

pola = '^a...s$'
stringTes = 'abyss'
hasil = re.match(pola, stringTes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal")