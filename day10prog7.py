import sqlite3
carData=[
    (1,'Audi',52642),
    (2,'Mercedes',57127),
    (3,'Skoda',9999),
    (4,'Volvo',29000),
    (5,'Bently',350000),
    (6,'Hummer',414000),
    (7,'Volkswagen',21600)
    ]
con=sqlite3.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
cur.executemany("INSERT INTO Cars VALUES(?,?,?)",carData)
con.commit()
con.close()
print("values inserted.")
