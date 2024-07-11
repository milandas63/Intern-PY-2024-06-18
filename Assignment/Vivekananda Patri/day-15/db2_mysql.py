import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='PATRI',
    password='PATRI',
    database='StudentManagementSystem'
)

cursor = conn.cursor()


cursor.execute('SELECT * FROM student')
students = cursor.fetchall()

cursor.execute('SELECT * FROM class')
classes = cursor.fetchall()

cursor.execute('SELECT * FROM house')
houses = cursor.fetchall()

cursor.execute('SELECT * FROM optional')
optionals = cursor.fetchall()


print("Students:")
for student in students:
    print(student)

print("\nClasses:")
for cls in classes:
    print(cls)

print("\nHouses:")
for house in houses:
    print(house)

print("\nOptionals:")
for optional in optionals:
    print(optional)


cursor.close()
conn.close()
