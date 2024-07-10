import mysql.connector

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="aryan",
            password="your_password",
            database="SMS"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_data():
    conn = connect_to_database()
    if conn is None:
        return

    cursor = conn.cursor()

    # Fetch and print data from student table
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()
    print("Students:")
    for student in students:
        print(student)

    # Fetch and print data from class table
    cursor.execute("SELECT * FROM class")
    classes = cursor.fetchall()
    print("\nClasses:")
    for cls in classes:
        print(cls)

    # Fetch and print data from house table
    cursor.execute("SELECT * FROM house")
    houses = cursor.fetchall()
    print("\nHouses:")
    for house in houses:
        print(house)

    # Fetch and print data from optional_subject table
    cursor.execute("SELECT * FROM optional_subject")
    subjects = cursor.fetchall()
    print("\nOptional Subjects:")
    for subject in subjects:
        print(subject)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    fetch_data()
