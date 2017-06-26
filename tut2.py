# import sqlite3 module
import sqlite3

# creates or connects to a db called mydb - here it is in a directory called data
db = sqlite3.connect('data/mydb')

# get a cursor object
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')
db.commit()

db.close()