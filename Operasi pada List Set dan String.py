#len -> untuk menghitung panjang atau banyaknya elemen dari list, set, dan string
#       khusus string program akan menghitung jumlah karakternya

#list
list = [1,3,3,5,5,7,7,9]
print(list)
print(len(list))
"""
Output:
[1, 3, 3, 5, 5, 5, 7, 7, 9]
9
"""

#set
set = set([1,3,3,5,5,7,7,9])
print(set)
print(len(set))
"""
Output:
{1, 3, 5, 7, 9}
5
"""

#string
string = "Belajar Python"
print(string)
print(len(string))
"""
Output:
Belajar Python
14
"""

#min dan max -> mengetahui berapa nilai minimum dan maksimum dari suatu list
angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(min(angka))
print(max(angka))
"""
Output:
5
96
"""

#count -> untuk mengetahui berapa kali suatu objek muncul dalam list
genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(genap.count(6))
"""
Output:
3
"""

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(string.count(substring))
"""
Output:
6
"""

#in dan not in -> operator yang diperuntukkan untuk mengetahui nilai yang ada dalam list
#                 dan mengembalikan nilai boolean
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('Belajar' in kalimat)

#Memberikan Nilai untuk Multiple Variable
#contoh
data = ['shirt', 'white', 'L']
apparel = data[0]
color = data[1]
size = data[2]
print(apparel, color, size)
"""
Output:
shirt apparel L
"""
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)
"""
Output:
['shirt', 'white', 'L']
shirt 
white
L
"""

#sort -> untuk mengurutkan angka atau urutan huruf
vehicle = ['motor', 'mobil', 'sepeda', 'pesawat']
vehicle.sort()
print(vehicle)
"""
Output:
['mobil', 'motor', 'pesawat', 'sepeda'] -> diurutkan sesuai alphabet
"""

#beberapa hal yang diketahui mengenai sort
#1. membalikan urutan
vehicle = ['motor', 'mobil', 'sepeda', 'pesawat']
vehicle.sort(reverse = True)
print(vehicle)
"""Output:
['sepeda', 'pesawat', 'motor', 'mobil']
"""

#2. tidak dapat mengurutkan list yang memiliki string dan angka sekaligus didalamnya
#urutan = ['Dicoding', 1, 2, 'Indonesia', 3]
#urutan.sort()
#print(urutan)
"""
Output:
TypeError: '<' not supported between instances of 'int' and 'str'
"""

#3. menggunakan urutan ASCII sehingga nilai huruf UPPERCASE akan didahulukan dibandingkan
#   huruf lowercase
vehicle = ['Motor', 'mobil', 'helikopter', 'Pesawat']
vehicle.sort()
print(vehicle)