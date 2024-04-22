"""
One-liner -> gaya penulisan pada Python yang memungkinkan
             anda untuk membuat sebuah kode hanya dalam satu baris
             One-liner adalah salah satu keunggulan dalam Python yang
             susah untuk diimplementasikan bagi beberapa bahasa pemrograman
             lainnya. Tujuan one-liner untuk membuat satu baris kode yang singkat dan jelas.
"""
x = 1
y = 2

temp = x 
x = y
y = temp
print("Setelah pertukaran: ")
print("x = ", x)
print("y = ", y)
"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""

x = 1 
y = 2
x, y = y, x #One-liner
print("Setelah pertukaran: ")
print("x = ", x)
print("y = ", y)
"""
Output:
Setelah pertukaran: 
x = 2
y = 1
"""