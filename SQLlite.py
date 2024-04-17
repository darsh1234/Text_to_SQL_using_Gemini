import sqlite3 

#connect to SQLlite
connection = sqlite3.connect("student.db")

#create a cursor object to insert record and create table
cursor = connection.cursor()

#create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""

cursor.execute(table_info)

#insert records

cursor.execute(''' INSERT Into STUDENT values('Darsh','AI','A')''')
cursor.execute(''' INSERT Into STUDENT values('Aseem','ML','A')''')
cursor.execute(''' INSERT Into STUDENT values('Devam','AI','A')''')
cursor.execute(''' INSERT Into STUDENT values('Siddhant','ML','A')''')

#Display records
print("The inserted records:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)