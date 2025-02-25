import mysql.connector as connector

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE ogrencilerdb") # Database oluşturma

# TABLO OLUŞTURMA

cursor.execute("""CREATE TABLE ogrenciler ( 
    id INT AUTO_INCREMENT PRIMARY KEY,
    ad VARCHAR(255),
    soyad VARCHAR(255),
    bolum VARCHAR(255),
    dogum_tarihi DATETIME NULL)"""
)

cursor.execute("SHOW TABLES") 

for i in cursor:
    print(i)


# cursor.execute("DROP TABLE IF EXISTS ogrenciler;") # TABLO SİLME
