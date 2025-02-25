import mysql.connector as connector
from datetime import date

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)

cursor = db.cursor()

sql = "INSERT INTO ogrenciler (ad,soyad,bolum,dogum_tarihi) VALUES (%s,%s,%s,%s)"

# tek bir kayıt için
#value = ("ali","ali","yazılım",date(2000, 5, 15)) # YYYY, MM, DD
#cursor.execute(sql,values)  

# Çoklu kayıt için
values = [
    ("ahmet","ahmet","bilgisayar",date(2000, 5, 15)),
    ("zeynep","zeynep","mimarlık",date(2000,1,1)),
    ("özkan","yıldız","yazılım",date(2000,1,1)),
    ("esra","zeynep","mimarlık",date(2000,1,1)),
] # YYYY MM, DD
cursor.executemany(sql,values) # birden fazla kayıt için

try:
    db.commit()
    print(cursor.rowcount, " kayıt edildi")
    print("son kayıt id: ",cursor._last_insert_id)
except connector.Error as a :
    print("hata: ", a)
finally:
    cursor.close()
    db.close()
    print("bağlantı kapatıldı")

