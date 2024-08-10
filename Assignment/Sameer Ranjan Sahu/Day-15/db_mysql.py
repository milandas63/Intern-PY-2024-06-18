import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'mca_python'
)

curs = conn.cursor()
curs.execute('SELECT c.con_id,c.con_name,c.mobile_1,rel_desc,loc_name FROM contact AS c LEFT JOIN relation AS r ON c.rel_id=r.rel_id LEFT JOIN location AS l ON c.loc_id=l.loc_id')

for row in curs:
    for col in row:
        print(col, end='  ')
    print() 