"""
jenis library untuk membantu pengguna mengumpulkan data dari halaman web.
"""
print("1. Beautifulsoup")
from urllib.request import urlopen
from bs4 import BeautifulSoup

# pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# membuat objek beautifulsoup
soup = BeautifulSoup(html, "html.parser")

# mencetak judul halaman
print(soup.title)
"""
2. urllib -> scraping konten dari sebuah website. urllib sedikit lebih kompleks dibandingkan
             beautifulsoup
"""
print("2. urllib")
from urllib.request import urlopen

# pengambilan konten
url = "http://python.org"
page = urlopen(url)
html = page.read().decode("utf-8")

# mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# mengekstrak dan mencetak judul halaman 
title = html[start_index:end_index]
print(title)