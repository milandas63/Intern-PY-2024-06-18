import mysql.connector
from stretcher import Table

# Step 3: Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="your_host",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

# Step 4: Define the query
query = """
SELECT id, name, mobile_no, relation_desc, locationname 
FROM your_table_name
"""

cursor.execute(query)

# Fetch all rows
rows = cursor.fetchall()

# Step 5: Format the output using stretcher
table = Table(columns=["ID", "Name", "Mobile No", "Relation Desc", "Location Name"])

for row in rows:
    table.add_row(row)

# Print the formatted table
print(table)

# Close the cursor and connection
cursor.close()
conn.close()
