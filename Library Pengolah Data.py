"""
bertujuan untuk membantu dalam memanipulasi,analisis, dan pemrosesan data.
menyediakan berbagai fungsi dan metode yang memudahkan pengguna untuk melakukan operasi pengeolahan data dengan lebih efesien dan cepat
"""

"""
1. pandass -> menyediakan struktur data dan alat untuk membantu pengguna dalam melakukan manipulasi
              pembersihan transformasi dan analisis data dengan mudah
"""
print("=== 1. Pandas ===")
import pandas as pd

# membuat dataframe dari dictionary
data = {
    'Nama':['Bayu', 'Rizki', 'Rizal', 'Zaki', 'Angga'],
    'Usia':[18,19,19,18,20],
    'Pekerjaan':['Consultant IT', 'HRD', 'Juragan Sawit', 'Boss Tambang', 'Ahli Kehutanan']
}

df = pd.DataFrame(data)

# menampilkan data frame
print(df)

"""
2. Numpy -> sering digunakan untuk scientific computing python dan menyediakan
            objek array multidimensi, seperti array dan matrix
"""
print("=== 2. Numpy ===")
import numpy 

matriks = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(matriks)

"""
3. Matplotlib -> library untuk visualisasi data. 
"""
print("=== 3. Matplotlib ===")
import matplotlib.pyplot as plt

# data
x = [1,2,3,4,5]
y = [2,4,6,8,10]

# membuat plot garis
plt.plot(x, y)

# menambahkan judul dan label sumbu
plt.title("Garis Lurus")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

# menampilkan plot
plt.show()

"""
4. Seaborn -> untuk visualisasi data sama seperti matplotlib namun lebih bagus
"""
import seaborn as sns
import matplotlib.pyplot as plt

# contoh data
tips = sns.load_dataset('tips') # membuat dataset tips dari seaborn

# contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()
