"""
https://app.patika.dev/egitimler/veri-bilimi-patikasi/python-temel/proje
Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listtlerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir. Örnek olarak:
input: [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
output: [1,'a','cat',2,3,'dog',4,5]
"""

def flattenList(x):
    if x == []:
        return x
    elif isinstance(x[0],list):
        return flattenList(x[0]) + flattenList(s[1:])
    return x[:1] + flattenList(x[1:])

input([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(flattenList)