import sqlite3, csv

# Connects to a db called "?????"" - here it is in a directory called data
db = sqlite3.connect('data/mydbNEW.db')

# create/get a cursor object
cursor = db.cursor()

# parse and load csv into sqlite db
csvreader = csv.reader(open('data/newemps2.csv', 'rb'), delimiter=',', quotechar='|')

for item in csvreader:
    cursor.execute('''
    INSERT INTO users(name, phone, email, password)
    VALUES(?,?,?,?)''',(item[0],item[1],item[2],item[3]))
    print ("User Inserted")
    
cursor.execute('''SELECT name, email, phone FROM users''')

print ("Data Inserted for:")
rows = cursor.fetchall()
for row in rows:
    print (row[0])
    


# commits changes to db
db.commit()

# closes db
db.close()