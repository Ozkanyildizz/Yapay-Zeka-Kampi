import mysql.connector as connector

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)
cursor = db.cursor()

sql = "SELECT COUNT(*) FROM dersler" #sayısı
sql = "SELECT AVG(kredi) FROM dersler" #ortalama
sql = "SELECT SUM(kredi) FROM dersler" # toplamı
sql = "SELECT MIN(kredi) FROM dersler" # MİNİMUNU
sql = "SELECT MAX(kredi) FROM dersler" # MAXİMUM
sql = "SELECT bolum, ders_adi FROM dersler WHERE kredi = (SELECT MAX(kredi) FROM dersler)" 

cursor.execute(sql)
result = cursor.fetchall()
for i in result:
    print(i)

