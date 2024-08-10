import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="root")

print(mydb,"Connection Establisted")