# import sqlite3 module
import sqlite3

# creates or connects to a db called mydb - here it is in a directory called data
db = sqlite3.connect('data/mydb')

db.close()