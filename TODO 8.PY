"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.
def minimal(a,b):
    if a <= b:
        return a
    else:
        return b
num1 = 8
num2 = 2
hasil = minimal(8, 2)
print(f"nilai terkecil antara {num1} dan {num2} adalah {hasil}")
