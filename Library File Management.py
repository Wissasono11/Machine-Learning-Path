"""
kumpulan library yang dirancang untuk membantu pengguna dalam mengelola dan berinteraksi
dengan berkas dan direktori pada sistem file. 
"""
"""
1. OS -> Untuk fungsi-fungsi yang berkaitan dengan sistem operasi, misal open(), path()
         getcwd(), dll.
"""
print("1. OS")
import os
print(os.getcwd)

"""
2. JSON -> JavaScript Object Nation
"""
print("2. JSON")
import json
 
# contoh JSON:
x = '{ "nama":"Buchori", "umur":22, "Kota":"New York"}'
 
# parse  x:
y = json.loads(x)
 
print(y["umur"])
"""
3. Pickle -> jika kita memiliki sebuah list yang ingin disimpan atau ditransmisikan
            fungsi dari library pickle dapat dimanfaatkan           
"""
print("4. Pickle")
import pickle
contoh_dictionary = {1:"6", 2:"2", 3:"f"}
pickle_keluar =open("dict.pickle","wb")
pickle.dump(contoh_dictionary, pickle_keluar)
pickle_keluar.close()

# jika ingin mengekstrak berkas pickle dan menaruh nya pada sebuah variabel
import pickle
pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()
 
print(contohDictionary)