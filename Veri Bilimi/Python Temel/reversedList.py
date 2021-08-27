"""
https://app.patika.dev/egitimler/veri-bilimi-patikasi/python-temel/proje
Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. Örnek olarak:
input: [[1, 2], [3, 4], [5, 6, 7]]
output: [[[7, 6, 5], [4, 3], [2, 1]]
"""

def reversedList(x):
  x=x[::-1]
  for i in range(len(x)):
    if type(x[i])==list:
      x[i]=x[i][::-1]
  return x