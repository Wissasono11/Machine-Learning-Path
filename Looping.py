#for -> bersifat definite iteration
# definite iteration -> sebuah proses iterasi atau perulangan 
#                       ketika jumlah pengulangannya ditentukan
#                       secara eksplisit sebelumnya
print("====== for =======")
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in  var_list:
    print(i)
"""
Output:
1
2
3
4
5
6
7
8
9
10
"""
#versi simpel 
print("================")
for i in range(10):
    print(i)
"""
Output:
1
2
3
4
5
6
7
8
9
"""
print("================")
for i in range(1,10,2):
    print(i)
"""
Output:
1
3
5
7
9
"""

#while -> bersifat indefinite iteration
"""
indefinite iteration -> sebuah proses iterasi yang
                        akan berhenti ketika memenuhi kondisi tertentu.
"""
print("====== while ========")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1 # increment
"""
Output:
1
2
3
4
5
"""
print("====== for-nested ========")
for i in range(1,3):
    for j in range(1,3):
        print(i,j)
"""
Output:
                            1,1 -> hasil perulangan for dalam
hasil perulangan for luar <-1,2
                            2,1
                            2,2
"""
print("====== Break ========")
"""
break -> pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis
keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok
perulangan selanjutnya.
"""
for i in range(2): # perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10): # perulangan tingkat kedua
        print("Perulangan dalam: ", j)
        if j == 1:
            break # menghentikan perulangan dalam jika j = 1
"""
Output:
Perulangan luar: 0
Perulangan dalam: 0
Perulangan dalam: 1
Perulangan luar: 1
Perulangan dalam: 0
Perulangan dalam: 1
"""
print("====== Break-2 ========")
for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))
"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
"""
print("====== Continue ========")
for huruf in 'Dico ding':
    if huruf == ' ':
        continue
    print('Huruf saat ini: {}'.format(huruf))
"""
Output:
Huruf saat ini: D
Huruf saat ini: i
Huruf saat ini: c
Huruf saat ini: o
Huruf saat ini: d   # Perhatikan bahwa harusnya sebelum ini ada spasi, namun dilewati.
Huruf saat ini: i
Huruf saat ini: n
Huruf saat ini: g
"""
print("====== else after for ========")
numbers = [1,2,3,4,5]

for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti")
        break
else:
    print("Angka tidak ditemukan")
"""
Output:
Angka tidak ditemukan.
"""
print("====== else after while ========")
count = 0

while count < 3:
    print("Dicoding Indonesia")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")
"""
Output:
Dicoding Indonesia
Dicoding Indonesia
Dicoding Indonesia
Blok else dieksekusi karena kondisi pada while salah (3<3 == False).
"""
print("====== else after while-2 ========")
n = 10
while n > 0:
    n -= 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
"""
Output:
9
8
"""
print("====== pass ========")
"""pass -> pernyataan yang digunakan jika anda menginginkan sebuah pertanyaan atau blok pertanyaan
           tetapi tidak ada tindakan atau program tidak melakukan apapun"""
x = 10

if x > 5:
    pass
else:
    print("Nilai x tidak memenuhi kondisi")
"""
Output:


"""
print("====== list-comprehension ========")
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
"""
Output:
[1, 4, 9, 16]

"""
print("====== list-comprehension-2 ========")
angka = [1,2,3,4]
pangkat = [n**2 for n in angka]
print(pangkat)
"""
Output:
[1, 4, 9, 16]
"""
