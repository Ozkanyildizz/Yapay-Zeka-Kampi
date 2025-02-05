import math 

class HesapMakinesi:
    def __init__(self, sayılar, isaret="+"):
        self.sayilar = sayılar
        self.isaret = isaret

    def dort_islem(self):
        if self.isaret == "+":
            sonuc = sum(self.sayilar)
            return sonuc
        elif self.isaret == "-":
            sonuc = self.sayilar[0]
            for sayi in self.sayilar[1:]:
                sonuc -= sayi
            return sonuc
        elif self.isaret == "*":
            sonuc = self.sayilar[0]
            for sayi in self.sayilar[1:]:
                sonuc *= sayi
            return sonuc
        elif self.isaret == "/":
            sonuc = self.sayilar[0]
            for sayi in self.sayilar[1:]:
                sonuc /= sayi
            return sonuc
        elif self.isaret == "**":
            sonuc = self.sayilar[0]
            for sayi in self.sayilar[1:]:
                sonuc = math.pow(sonuc, sayi)
            return sonuc
        
    def trigonmetri(self): # radian türünden değer alır
            if self.isaret == "sin":
                return math.sin(math.radians(self.sayilar[0]))
            elif self.isaret == "cos":
                return math.cos(math.radians(self.sayilar[0]))
            elif self.isaret == "tan":
                return math.tan(math.radians(self.sayilar[0]))
            elif self.isaret == "asin":
                return math.degrees(math.asin(self.sayilar[0]))
            elif self.isaret == "acos":
                return math.degrees(math.acos(self.sayilar[0]))
            elif self.isaret == "atan":
                return math.degrees(math.atan(self.sayilar[0]))