import mysql.connector as connector

# Veritabanına bağlanma
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)
cursor = db.cursor()

# SQL sorgusunu yaz

sql = """
SELECT ogrenciler.ad AS ogrenci_adi, dersler.ders_adi
FROM ogrenci_ders
JOIN ogrenciler ON ogrenci_ders.ogrenci_id = ogrenciler.id
JOIN dersler ON ogrenci_ders.ders_id = dersler.ders_id
"""

# cursor.execute(sql)

# Öğrenci adına göre sorgu yazma (Örneğin 'özkan')
ogrenci_adi = "özkan"  # İstediğiniz öğrenci adını buraya yazabilirsiniz
sql = """
SELECT ogrenciler.ad AS ogrenci_adi, dersler.ders_adi
FROM ogrenci_ders
JOIN ogrenciler ON ogrenci_ders.ogrenci_id = ogrenciler.id
JOIN dersler ON ogrenci_ders.ders_id = dersler.ders_id
WHERE ogrenciler.ad = %s
"""

cursor.execute(sql,(ogrenci_adi,))

# Sonuçları al
result = cursor.fetchall()

# Sonuçları yazdır
for ogrenci_adi, ders_adi in result:
    print(f"Öğrenci Adı: {ogrenci_adi}, Ders Adı: {ders_adi}")
