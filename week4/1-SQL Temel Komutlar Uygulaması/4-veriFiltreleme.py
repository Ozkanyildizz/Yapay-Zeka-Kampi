import mysql.connector as connector

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)
cursor = db.cursor()

sql = "SELECT * FROM ogrenciler"
sql = "SELECT * FROM ogrenciler WHERE id >= 1"
sql = "SELECT * FROM ogrenciler WHERE bolum = 'bilgisayar'"
sql = "SELECT * FROM ogrenciler WHERE bolum = 'bilgisayar' or bolum = 'yazılım'"
sql = "SELECT * FROM ogrenciler WHERE bolum = 'yazılım' and ad = 'özkan'"
sql = "SELECT * FROM ogrenciler WHERE bolum LIKE '%yazılım%'" # bolum içinde yazılım kelimesi geçenleri al 
sql = "SELECT * FROM ogrenciler WHERE bolum LIKE 'yazılım%'" # bolum içinde yazılım kelimesi ile başlaanları al 
sql = "SELECT * FROM ogrenciler WHERE bolum LIKE '%yazılım'" # bolum içinde yazılım kelimesi ile bitenleri al 
sql = "SELECT * FROM ogrenciler WHERE bolum LIKE 'bilgisayar%' or ad LIKE '%öz%'" 


cursor.execute(sql)

sonuc = cursor.fetchall() # hepsini getirir
for i in sonuc:
    print(i)

# sonuc = cursor.fetchone() # bir tane getiri
# print(sonuc)

def getById(id):
    sql = "SELECT * FROM ogrenciler WHERE id = %s"
    params = (id,)

    cursor.execute(sql,params)
    sonuc = cursor.fetchall()
    print(sonuc)

# getById(2)
# getById(3)

# doğum tarihine göre sıralama
def yasaGoreListele():
    """ASC= oldest to youngest 
    DESC= youngest to oldest """
    sql = "SELECT * FROM ogrenciler ORDER BY dogum_tarihi ASC" 
    sql = "SELECT * FROM ogrenciler ORDER BY dogum_tarihi DESC LIMIT 1" # limit1 ilkini alır
    cursor.execute(sql)
    sonuc = cursor.fetchall()
    for i in sonuc:
        print(i)

yasaGoreListele()