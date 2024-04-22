print("===ekspresi menurut arity dari operator===")
# biner -> (x + y), (x - y), (x * y), (x / y), (x ** y), (x < y), (x <= y), (x > y), (x >= y), 
#          (x % y), (x == y), (x != y).
# uner ->  (x += 1), (x-=1), (not x).
"""
Ekspresi biner merupakan jenis yang memiliki dua operan. Operatornya meliputi penjumlahan (+), pengurangan (-), 
perkalian (*), pembagian (/), perpangkatan (**), lebih kecil dari (<), 
lebih kecil dari sama dengan (<=), 
lebih besar dari (>), lebih besar dari sama dengan (>=), modulus (%), 
sama dengan (==), dan tidak sama dengan (!=).
Namun, ekspresi uner adalah jenis ekspresi yang memiliki 
bentuk dasar operasi dengan satu operan. Contohnya adalah increment (x+=1), 
decrement (x-=1), dan negasi (not x).
"""
a = True
a = not a
print(a)

b = 6
b -= 1 #-> decrement
print(b)

c = 6 
c += 1 #-> increment
print(c)

d = 10
print(-d)
"""
Output:
False
5
7
-10
"""

print("===ekspresi menurut tipe data yang dihasilkan===")
# aritmatika  = <numerik> <operator> <numerik> = <numerik>
# relasional = <numerik> <operator> <numerik> = <boolean>
# logika = <boolean> <operator> <boolean> = <boolean>

print (2+2)
print(3<10)
print(True or False)
"""
Output:
4
True
True
"""

print("===operator aritmatika===")
# penjumlahan (+), pengurangan (-), perkalian (*)
# pembagian bulat(//), pembagian riil(/), modulo(%)
# pangkat(**)

x = 11
y = 5
print(x + y)
print(x - y)
print(x * y)
print(x // y)
print(x / y)
print(x % y)
print(x ** y)

print("===operator relasional===")
# sama dengan (==), tidak sama dengan (!=), lebih besar dari (>)
# kurang dari (<), lebih besar dari sama dengan (>=), kurang dari sama dengan (<=)

x = 5
y = 10

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print("===penggunaaan dalam string=== ")
x = "Dicoding"
y ="Indonesia"

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

print("===operator logika===")
# "AND" atau "&", "OR" atau "|", NOT
# operator AND akan bernilai True jika keduanya bernilai benar
# operator OR akan bernilai False jika keduanya bernilai salah
# NOT bertujuan untuk membalikkan nilai logika dari operannya.

print("==AND==")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
"""
Output:
True
False
False
False
"""

print("==OR==")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
"""
Output:
True
True
True
False
"""

print("==NOT==")
print(not True)
print(not False)
"""
Output:
False
True
"""

print("===Operator Assignment===")
x = 11
x += 5 # -> x = x + 5
print(x)

x = 11
x -= 5 # -> x = x - 5
print(x)

x = 11
x *= 5 # -> x = x * 5
print(x)

x = 11
x /= 5 # -> x = x / 5
print(x)

x = 11
x %= 5 # -> x = x % 5
print(x)
"""
Output:
16
6
55
2.2
1
"""