import stretcher as s
import mysql.connector;

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    database = 'mca_python'
)
curs = conn.cursor()
curs.execute('SELECT c.con_id,c.con_name,c.mobile_1,rel_desc,loc_name FROM contact AS c LEFT JOIN relation AS r ON c.rel_id=r.rel_id LEFT JOIN location AS l ON c.loc_id=l.loc_id')
list = ( (4,"ID"), (20,"NAME"), (12,"MOBILE"), (20,"RELATION"), (20,"LOCATION") )

print("+",end='')
for index, item in enumerate(list):
    print(s.replicate("-",item[0]), end='+')
print()

print("|",end='')
for index, item in enumerate(list):
    print(s.justC(item[1], item[0]), end='|')
print()

print("+",end='')
for index, item in enumerate(list):
    print(s.replicate("-",item[0]), end='+')
print()

i = 0;
for row in curs:
	print('|',end='')
	position = list[i]
	for index, col in enumerate(row):
		list_index = list[index]
		width = list_index[0]
		print(s.justL(col,width), end='|')

	print()
	i = i+1

print("+",end='')
for index, item in enumerate(list):
    print(s.replicate("-",item[0]), end='+')
print()



