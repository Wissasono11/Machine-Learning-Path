# mempelajari cara membuat fungsi tanpa mendeklarasikan def, ini dikenal dengan 
# ekspresi lambda yang digunakan untuk membuat fungsi tanpa perlu menyebutkan def ketika membuatnya.
# kita dapat mengamsumsikan fungsi anonim ini sebagai fungsi one-liner

# jika menggunakan def
# >>>def func(args):
#     return ret_val

#jika menggunakan ekspresi lambda
# >>>func = lambda args: ret_val
# fungsi = func setara dengan nama variabel yang digunakan untuk menyimpan lambda
# args = argumen yang dibutuhkan untuk dioperasikan
# ret_val = nilai yang kita kembalikan (return)

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5, 10))
"""
Output:
50
"""