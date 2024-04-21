import sqlite3 

#connect to SQLlite
connection = sqlite3.connect("student.db")

#create a cursor object to insert record and create table
cursor = connection.cursor()

#create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#insert records

cursor.execute(''' INSERT Into STUDENT values('Darsh','AI','A',90)''')
cursor.execute(''' INSERT Into STUDENT values('Aseem','ML','A',95)''')
cursor.execute(''' INSERT Into STUDENT values('Devam','AI','B',85)''')
cursor.execute(''' INSERT Into STUDENT values('Siddhant','ML','C',75)''')

#Display records
print("The inserted records:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

connection.commit()
connection.close()