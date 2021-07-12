import sqlite3

conn = sqlite3.connect("contacts.sqlite")

name = input("Enter Name= ")
for row in conn.execute("select * from contacts where name LIKE ?", (name,)):
    print(row)

conn.close()
