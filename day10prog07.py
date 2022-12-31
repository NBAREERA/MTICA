import sqlite3
con=sqlite3.connect('mtica.db')

cur=con.cursor()
cur.execute("SELECT*FROM Cars")
rows=cur.fetchall()
for row in rows:
    print(row)

