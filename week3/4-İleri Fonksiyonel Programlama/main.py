# map filter 
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kare = list(map(lambda x: x**2, liste))
print(kare)

# reduce()
from functools import reduce

# Bir listenin çarpımını hesaplamak için reduce() kullanımı
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, numbers)
print("Listenin çarpımı:", result)

# Bir listeyi toplamak için reduce() kullanımı
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print("Listenin toplamı:", result)

"""
map redduce farkı 
map() fonksiyonu, bir dizinin her öğesine bir işlev uygular ve sonuçları içeren yeni bir dizi döndürür.
reduce() fonksiyonu, bir diziyi tek bir değere indirgemek için kullanılır ve tek bir değer döndürür.
map() fonksiyonu, her öğeyi bağımsız olarak işlerken, 
reduce() fonksiyonu, bir önceki işlemin sonucunu bir sonraki öğe ile birlikte kullanır.
"""

# sorted()

karısık_dizi = [5,9,6,5,3,1,4]
kare_alma = list(map(lambda x: x**2,sorted(karısık_dizi,reverse=False)))
print("sorted listenin karesi: ",kare_alma)