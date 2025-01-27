# Global ve yerel değişkenler 

sayı_global = 10 # Global değişken her yerden erişilebilir

def yerel():
    sayı_global = 20 # global değişken fonksiyon içerisinde değiştirilebilir
    print("Yeni global değer: ", sayı_global)
    sayı_yerel = 5 # Yerel değişken sadece tanımlandığı fonksiyon içerisinde erişilebilir
    print("yerel değişken: ", sayı_yerel)

# sayı_yerel = 15 # Yerel değişken fonksiyon dışında erişilemez 
yerel()
def fonksiyon_global_degisken():
    global sayı # yerel değişkene dışardan ulaşmak için global anahtar kelimesi kullanılır
    sayı = 30
fonksiyon_global_degisken() #  sayı değişkenini kullanmak için fonksiyon çağrılmalı
print("Fonksiyon içerisindeki global değişken: ",sayı) # 30

def fonksiyon_global_degisken_2(): # fonksiyon içerisinde başka bir fonksiyonun global değişkenini kullanmak
    print("Önceki fonksiyonun global değişkeni: ", sayı)
fonksiyon_global_degisken_2() # 30 

# Global değişkeninin fonksiyon ile artırılması 

sayac = 0

def sayaci_artir():
    global sayac  # Global sayaç değişkenini kullan
    sayac += 1  # Sayaç değişkenini artır
    print("Sayaç değeri: ", sayac)

sayaci_artir() # 1
sayaci_artir() # 2
sayaci_artir() # 3
