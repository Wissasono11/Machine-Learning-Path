"""
menyediakan fasilitas untuk menguraikan kode python menjadi struktur data 
yang dapat diproses dan dianalisis
"""
import argparse
 
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
args = parser.parse_args()
 
if args.output:
   print("Halo, ini merupakan sebuah output dari panggildicoding.py")