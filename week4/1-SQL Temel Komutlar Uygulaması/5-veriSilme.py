import mysql.connector as connector

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)
cursor = db.cursor()

sql = "DELETE FROM ogrenciler WHERE id=1"
sql = "DELETE FROM ogrenciler WHERE ad LIKE 'ahmet%'"
cursor.execute(sql)

cursor.execute("DROP DATABASE IF EXISTS exampledb") # database silme

try:
    db.commit()
    print(f"{cursor.rowcount} tane kayıt silindi")
except connector.Error as a:
    print("hata",a)
finally:
    cursor.close()
    db.close()

