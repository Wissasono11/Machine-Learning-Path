#ternary operators -> bentuk ekspresi  yang bertujuan
#                     untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya.

lulus = True
print("Selamat") if lulus else print("Perbaiki")
"""
Output:
selamat
"""
#opsi lain dari ternary operators -> melibatkan tuple
lulus = True
kelulusan = ("Perbaiki, anda belum lulus.","Selamat, anda lulus!")[lulus]
print(kelulusan)
"""
Output:
Selamat, Anda lulus!
"""