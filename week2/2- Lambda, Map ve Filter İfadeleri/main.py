# 2.1 Bir liste içindeki tek sayıların karesini alan bir map fonksiyonu
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kare = list(map(lambda x: x**2, filter(lambda x: x % 2 != 0, liste)))
print(kare)

# 2.2  0-50 arasında yer alan çift sayıları filtrelemek
sayılar = list(range(0, 51)) # 0'dan 50'ye kadar sayılar
cift = list(filter(lambda x : x % 2 == 0, sayılar))
print(cift)

# 2.3 Lambda ile verilen iki sayı arasındaki tüm tam sayıların toplamı
toplam = lambda x, y: sum(range(x, y+1))
print(toplam(1, 10))  # 55