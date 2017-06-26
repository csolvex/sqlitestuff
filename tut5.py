# import sqlite3 module
import sqlite3

# creates or connects to a db called mydb - here it is in a directory called data
db = sqlite3.connect('data/mydbNEW')
# define a cursor
cursor = db.cursor()

cursor.execute('''SELECT name, email, phone FROM users''')
user1 = cursor.fetchone() #retrieve the first row
user2 = cursor.fetchone() #retrieve the second row

print(user1[0]) #Print the first column retrieved(user's name)
print(user2[0]) #Print the first column retrieved(user's name)

all_rows = cursor.fetchall()

#for row in all_rows:
    # row[0] returns the first column in the query (name), row[1] returns email column.
    #print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))

db.close()