import sqlite3

db = sqlite3.connect("contacts.sqlite")  # connection to sqlite
db.execute("CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)")  # creating table and checking
# if not exist already
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6556678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'brian@myemail.com')")


cursor = db.cursor()
cursor.execute("SELECT * FROM CONTACTS")

# print(cursor.fetchall())  # will print a list of all the entries and can move backwards and forwards for iter useful
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())  # will print next row and 3 rd fetchone is none as no other entry to fetch


for row in cursor:
    print(row)

# for row in cursor:  # no print anything as cursor don't remember previous row for data efficiency without fetchall
#     print(row)

cursor.close()
db.commit()
db.close()
