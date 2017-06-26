# pip install maya  --> module for working with datetime in human readable language
# imports modules
import csv
import sqlite3

# connects to the database
db = sqlite3.connect('data/mydb')

# creates a cursor object. 
cursor = db.cursor()

#load csv file and parse

csvreader = csv.reader(open('data/newemps.csv', 'rb'), delimiter =',',quotechar='|')

#
for row in csvreader:
    
    cursor.execute('''
    INSERT INTO users(name, phone, email, password)
    VALUES(?,?,?,?)''',(row[0],row[1],row[2],row[3]))
    print ("record inserted")


# Code below simply tells us which records are in the db now.     
cursor.execute('''SELECT name FROM users''')
print("Data inserted for: ")

# tells the cursor to get all records inserted
data = cursor.fetchall()
for item in data:
    print (item[0])

# commits changes to the db
db.commit()

# closes the connection to the db
db.close()

