# 1.1 __str__ Metodu

class Ogrenci:
    def __init__(self, isim, yas, numara):
        self.isim = isim
        self.yas = yas
        self.numara = numara
    
    def __str__(self): # __str__ metodu nesnenin açıklamasını almak için kullanılır kullanıcılar için uygundur
        return f"Öğrenci Adı: {self.isim}, Yaşı: {self.yas} yaşında , Numarası: {self.numara}"
    
    # def __repr__(self): # __str__ ile aynı şeyi yapar fakat genelde geliştiriciler içindir 
    #     return f"Kisi(ad='{self.isim}', yas={self.yas}, numara={self.numara})"

# iki şekilde __str__ metodunu kullanarak nesnenin açıklamasını alabiliriz
ogrenci1 = Ogrenci("Ali", 20, 2525)
print(ogrenci1.__str__()) 
print(ogrenci1)  
# print(ogrenci1.__repr__())

# 1.2 __add__ Metodu

class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, diger):
        return Vektor(self.x + diger.x, self.y + diger.y)

    def __str__(self): 
        return f"Vektor({self.x}, {self.y})"
    
    

# Vektor sınıfından iki nesne oluşturma
vektor1 = Vektor(2, 3)
vektor2 = Vektor(4, 5)
vektor3 = vektor1 + vektor2 # __add__ metodunu kullanarak iki vektörü toplama
print(vektor1) # Vektor(2, 3)
print(vektor2) # Vektor(4, 5)
print(vektor3)  # Vektor(6, 8)
