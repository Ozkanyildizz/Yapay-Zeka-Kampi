#1.1 Hesap Makinesi

class HesapMakinesi:
    def __init__(self,sayi1, sayi2):
        self.sonuc = 0
        self.sayi1 = sayi1
        self.sayi2 = sayi2

    def topla(self, ):
        self.sonuc = self.sayi1 + self.sayi2
        return f"Toplamları: {self.sonuc}"

    def cikar(self):
        self.sonuc = self.sayi1 - self.sayi2
        return f"Farkları : {self.sonuc}"

    def carp(self):
        self.sonuc =  self.sayi1 * self.sayi2
        return f"Carpımları: {self.sonuc}"
        
    def bol(self):
        self.sonuc = self.sayi1 / self.sayi2
        return f"Bölümleri: {self.sonuc}"
    
islem = HesapMakinesi(20, 5)

print(islem.topla())
print(islem.cikar())
print(islem.carp())
print(islem.bol())

#1.2 Öğrenci Sınıfı

class Ogrenci:
    def __init__(self, ad, not1, not2 , sinif):
        self.ad = ad
        self.not1 = not1 
        self.not2 = not2
        self.sinif = sinif

    def bilgileriGoster(self):
        print(f"Adı: {self.ad}, Notu: {self.not1}, {self.not2}, Sınıfı: {self.sinif}")

    def ortalamayiHesapla(self):
        print(f"{self.ad} ortalaması: ",(self.not1 + self.not2)/ 2) 

ogrenci1 = Ogrenci("Ali", 90, 80, "9/A")
ogrenci1.bilgileriGoster()
ogrenci1.ortalamayiHesapla()

ogrenci2 = Ogrenci("Özkan", 70, 60, "9/B")
ogrenci2.bilgileriGoster()
ogrenci2.ortalamayiHesapla()
