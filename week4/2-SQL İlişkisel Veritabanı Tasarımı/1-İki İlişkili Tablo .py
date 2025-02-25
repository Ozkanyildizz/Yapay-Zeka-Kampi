import mysql.connector as connector

# database bağlanma 
db = connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
    database = "ogrencilerdb"
)
cursor = db.cursor()


# dersler tablosunu oluşturma
create_dersler_table = """
CREATE TABLE IF NOT EXISTS dersler (
    ders_id INT AUTO_INCREMENT PRIMARY KEY,
    ders_adi VARCHAR(255),
    kredi INT,
    bolum VARCHAR(255)
)
"""
# cursor.execute(create_dersler_table)

# Ders bilgileri girme
sql = "INSERT INTO dersler (ders_adi,kredi,bolum) VALUES (%s,%s,%s)"

values = [
    ("mat","5","bilgisayar"),
    ("fizik","4","mimarlık"),
    ("mat","5","yazılım"),
    ("fizik","5","mimarlık"),
    ("biyo","5","mimarlık"),
    ("mat","5","mimarlık"),
    ("biyo","4","mimarlık"),
] 

# cursor.executemany(sql,values) 

# ogrenci_ders tablosunu oluşturma (ilişki tablosu)
create_ogrenci_ders_table = """
CREATE TABLE IF NOT EXISTS ogrenci_ders (
    ogrenci_id INT,
    ders_id INT,
    FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(id),
    FOREIGN KEY (ders_id) REFERENCES dersler(ders_id),
    PRIMARY KEY (ogrenci_id, ders_id)
)
"""
cursor.execute(create_ogrenci_ders_table)



# ogrenci_ders tablosuna veri ekleme
insert_ogrenci_ders = """
INSERT INTO ogrenci_ders (ogrenci_id, ders_id)
VALUES (%s, %s);
"""

# Öğrencilerin derslerle ilişkilendirilmesi
# (ogrenci_id, ders_id)
ogrenci_ders_data = [
    (1, 2),
    (1, 5),
    (3, 3), 
    (4, 4),  
    (5, 5),
    (7, 7),
]
# Verileri ekleme
# cursor.executemany(insert_ogrenci_ders, ogrenci_ders_data)


# Değişiklikleri kaydetme
db.commit()





