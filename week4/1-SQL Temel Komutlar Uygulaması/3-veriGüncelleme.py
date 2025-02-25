import mysql.connector as connector

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)

cursor = db.cursor()

def updateProduct(id,bolum):
    sql = "UPDATE ogrenciler SET bolum = %s WHERE id=%s "
    params = (bolum,id)
    cursor.execute(sql,params)

    try:
        db.commit()
        print(cursor.rowcount," tane kayıt güncellendi")
    except connector.Error as a:
        print(a)
    finally:
        cursor.close()
        db.close()



updateProduct(3,"mimarlık")
   