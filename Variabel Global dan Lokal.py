# ada konsep "scope" dalam  Python yang mengatur jangkauan variabel dan fungsi dalam suatu program
# ada 2 jenis scopre yang umum dijumpai

print("=== Variabel Global ===")
a = 10

def add(b):
    result = a+b
    return result
bilanganPertama = add(20)
print(bilanganPertama)
"""
Output:
30
"""
# variable a merupakan variabel global dan dapat digunakan pada seluruh bagian program yang dibuat

print("=== Variable Lokal ===")
def add(a,b):
    lokal_var = 5
    result = a + b - lokal_var
    return result

bilanganPertama = add(10, 20)
print(bilanganPertama)
"""
Output:
25
"""
# kita mendefinisikan fungsi penjumlahan bernama "add" dengan dua parameter, yakni
# a dan b, dalam fungsi tersebut kita mengoperasikan penjumlahan antara a dan b dikurangi 
# variabel lokal bernama "lokal_var" dengan nilai 5