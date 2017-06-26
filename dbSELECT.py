# reader

import sqlite3, csv

# Connects to a db called "?????"" - here it is in a directory called data
db = sqlite3.connect('data/mydbNEW.db')

# create/get a cursor object
cursor = db.cursor()

cursor.execute('''SELECT name, email, phone FROM users''')

print ("Current Database Contents: ")

rows = cursor.fetchall()
for row in rows:
    print ("Name:  " + row[0])
    print ("Email: " + row[1])
    print ("Phone: " + row[2])
    print ( " ")
