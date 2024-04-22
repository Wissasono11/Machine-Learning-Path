#if-else
print("Jawab dengan Ya atau Tidak")
ketersediaan = input("Apakah ketersediaan ayam di rumah masih ada: ")
if ketersediaan == "Ya":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

"""
Output:
Ibu membeli dan memasak ayam
"""   

print("===== if =====")
#if -> tatement python yang akan mengecek nilai variabel didalamnya memenuhi kriteria suatu kondisi atau tidak.
score = 100
if score == 100:
    print("Nilai anda sempurna!")

x = ""
if x:
    print("Ini true")
"""output tidak menghasilkan apapun karena python akan menggangap setiap nilai kosong dan null sebagai false
sebaliknya, nilai yang tidak kosong dan tidak null akan bernilai True."""

score = 100 
if score == 100: print("Nilai anda sempurna!") #-> percabangan juga dapat ditulis dengan one-liner atau single statement

print("===== else =====")
#else -> statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi if
#        statement bernilai false. 

tinggi_badan = int(input("berapa tinggi anda: "))

if tinggi_badan >= 160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")
"""
Output:
Anda tidak diperbolehkan menaiki roller coaster
"""

print("===== elif =====")
#elif -> alternatif untuk if bertingkat atau switch case.
#        elif berada setelah if dan dapat ditambahkan lebih dari satu
#        karena tidak dibatasi dan opsinal

nilai = int(input("berapa nilai ujian anda: "))

if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmm. Anda mendapat nilai C")
    print("Ayo semangat!")
else:
    print("Waduh! bodoh banget dapat nilai D")
    print("Belajar tod jangan mabar mulu!")

nilai = 81
perilaku = 'tidak baik'

if nilai >= 80 and perilaku == 'baik':
    print("Selamat! Anda mendapatkan nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != 'baik':
    print("Kamu mendapatkan nilai A, tetapi perilaku anda kurang baik")
    print("Perbaiki lagi ya!")
else :
    print("Belajar lagi tod")