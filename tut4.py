# INSERT data

# import sqlite3 module
import sqlite3

# creates or connects to a db called mydb - here it is in a directory called data
db = sqlite3.connect('data/mydb')

# get a cursor object
cursor = db.cursor()

# OUR DATA
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password ;)
password1 = '12345'
 
name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# insert user 1

cursor.execute('''
    INSERT INTO users(name, phone, email, password)
    VALUES(?,?,?,?)''',(name1, phone1, email1, password1))
print('First user inserted')

# insert user 2

cursor.execute('''
    INSERT INTO users(name, phone, email, password)
    VALUES(?,?,?,?)''',(name2, phone2, email2, password2))
print('Second user inserted')

db.commit()

db.close()