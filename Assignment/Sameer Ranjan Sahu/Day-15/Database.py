import mysql.connector as Myconn

mydb=Myconn.connect(host="localhost",user="root",password="root")
db_cursor=mydb.cursor()

db_cursor.execute("create database LearnMysql")
print("Database Created !!")