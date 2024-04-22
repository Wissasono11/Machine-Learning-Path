print("===Mengubah Huruf Besar/Kecil===")
#UPPERCASE
kata = 'dicoding'
kata = kata.upper()
print(kata)
"""
Output:
DICODING
"""

#lower
kata = 'DICODING'
kata = kata.lower()
print(kata)
"""
Output:
dicoding
"""

print("===Awalan dan Akhiran===")
#rstrip -> menghapus whitespaces pada sebelah kanan atau akhir string
print("Dicoding             ".rstrip())
"""
Output:
Dicoding
"""

#lstrip -> kebalikan dari rstrip, lstrip bertugas untuk menghapus whitespaces sebelah kiri atau awal string
print("             Dicoding".lstrip())
"""Output:
Dicoding
"""

#strip -> menghapus whitespaces pada bagian awal dan akhir string
print("     Dicoding        ".strip())
"""Output:
Dicoding
"""
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

#startswith -> untuk menemukan suatu kata pada awal string dan memberikan nilai boolean
print('Dicoding Indonesia'.startswith('Dicoding'))
"""
Output:
True
"""

#endswith -> untuk menemukan suatu kata pada akhir string dan memberikan nilai boolean
print('Dicoding Indonesia'.endswith('Dicoding'))
"""
Output:
False
"""

print("===Memisahkan dan Menggabungkan String===")
#join -> menggabungkan string
print(''.join(['Dicoding','Indonesia', '!']))
"""
Output:
Dicoding Indonesia!
"""
print('123'.join(['Dicoding','Indonesia', '!']))
"""
Output:
Dicoding Indonesia!
"""

#split -> memisahkan string
print('Dicoding Indonesia !'.split())
"""
Output:
['Dicoding','Indonesia','!']
"""
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))
"""
Output:
['Halo,', 'aku ikan,', 'aku suka sekali menyelam', 'aku tinggal di perairan.', 'Badanku licin dan renangku cepat.', 'Senang berkenalan denganmu.']
"""

print("===Mengganti Elemen String===")
#replace
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))
"""
Output:
Ayo belajar Pemrograman di Dicoding
"""


print("===Pengecekan String===")
#isupper -> mengembalikan nilai True jika semua huruf dalam string adalah UPPERCASE, jika tidak maka akan memberikan nilai False
kata = 'DICODING'
print(kata.isupper())
"""
Output:
True
"""

#islower -> mengembalikan nila True jika semua huruf adalah lowercase, jika tidak akan memberikan nilai False
kata = 'dicoding'
print(kata.islower())
"""
Output:
True
"""

#isalpha -> mengembalikan nilai True jika semua karakter dalam string adalah huruf alfabet, jika tidak maka akan memberikan nilai False
kata ='dicoding99'
print(kata.isalpha())
"""
Output:
False
"""

#isalnum -> mengembalikan nilai True jika karakter dalam string adalah alfanumerik, yaitu hanya huruf atau hanya angka atau keduanya, jika tidak akan memberikan nilai False
kata = 'dicoding123'
print(kata.isalnum())
"""
Output:
True
"""

#isdecimal -> mengembalikan nilai True jika karakter dalam string berisi hanya angka. Jika tidak akan memberikan False
print('123'.isdecimal())
"""
Output:
True
"""

#isspace -> mengembalikan nilai True jika string hanya berisi whitespace, seperti spasi, tab, newline dll
print('     '.isspace())
"""
Output:
True
"""

#istitle -> mengembalikan nilai True jika string berisi huruf kapital setiap kata pertamanya, Jika tidak bernilai False
print('Dicoding Indonesia'.istitle())
"""
Output:
True
"""

print("===Formatting pada String===")
"""zfill -> untuk menambahkan nilai 0 di depan sebuah string dengan panjang tertentu. Tujuannya untuk memastikan bahwa sebuah angka atau nilai memiliki panjang tetap 
            terutama ketika ingin menyimpan nilai dalam format yang konsisten"""
teks = 'Code'
tambah_number = teks.zfill(5)
print(tambah_number)
"""
Output:
0Code
"""

#rjust -> untuk merapikan pencatatan teks menjadi rata kanan sehingga tampilannya lebih rapi
print('Dicoding'.rjust(20))
"""
Output:
            Dicoding

"""

#ljust -> untuk membuat teks menjadi rata kiri
print('Dicoding'.ljust(20))
"""
Output:
Dicoding            '
"""

#center
print('Dicoding'.center(10, '-'))
"""
Output:
-Dicoding-
"""

print("===String Laterals===")
st1 = "Jum'at"
print(st1)

print("Halo!\nKapan terakhir kali kita bertemu?\nKita bertemu hari Jum\'at yang lalu.")
"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum'at yang lalu.
"""

print("===Raw String===")
print(r'Dicoding\tIndonesia')
"""
Output:
Dicoding\tIndonesia
"""

