#konsep dari prosedur adalah kita tidak menggunakan return dalam mengembalikan value
"""
contoh:
def greeting(name):
    print("Halo " + name + ", Selamat Datang!") 

Perhatikan bahwa kita tidak mendefinisikan return dan membuat return value. 
Konsep ini disebut sebagai prosedur, yakni fungsi Python yang kita buat tidak mengeluarkan nilai dari fungsi tersebut.

Lantas bagaimana cara memanggil nya?
"""
print("=== memanggil dan mendefinisikan prosedur ===")
"""
untuk memanggil suatu fungsi kita hanya cukup mendefinisikan
satu baris instruksi seperti "greeting()"
"""
def greeting(name):
    print("Halo "+ name +" , Selamat Datang!")

greeting(input("Masukkan nama : "))
"""
Output: 
Halo Dicoding Indonesia, Selamat Datang!
"""

"""
contoh di atas kita tetap dapat menggunakan fungsi print() dalam prosedur
tanpa harus membuat return value, dan tetap mendapatkan outputnya.
"""