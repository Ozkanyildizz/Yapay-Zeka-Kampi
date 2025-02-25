# 1.1  Bir dizi içerisindeki sayıların ortalamasını hesaplayan bir fonksiyon yazınız.
def ortalama_hesapla(dizi):
    toplam = 0
    for i in dizi:
        toplam += i
    return toplam / len(dizi)
dizi = [1, 2, 3, 4, 5]
# print(ortalama_hesapla(dizi))

# 1.2 girilen iki sayı içerisindeki en büyük sayıyı bulan bir fonksiyon yazınız.
def en_buyuk_bul(sayı1,sayı2):
 return sayı1 if sayı1 > sayı2 else sayı2 

sayi1 = 4
sayi2 = 8
# print(f"En büyük sayı: {en_buyuk_bul(sayi1,sayi2)}")

# 1.3  Bir metin içindeki kelimeleri sayan bir fonksiyon yazın

def kelime_say(metin):
    ayrılmıs_metin = metin.split()
    print(ayrılmıs_metin)
    return len(ayrılmıs_metin)
metin = "Python programlama dili oldukça popüler bir dildir."
# print(kelime_say(metin))






