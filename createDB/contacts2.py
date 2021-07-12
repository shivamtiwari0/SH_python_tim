import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "new2email@update.com"
phone = input("Please enter phone no. ")

update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))  # executescript = multiple script
print("{} rows updated".format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute("select * from contacts"):  # using connection without using cursor
    print(row)

db.close()

# use placeholders  if input has to come from user
