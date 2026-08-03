"""
Design a relational database for a small application and populate the database. Using
SQL do the CRUD (create, read, update and delete) operations.
"""
import mysql.connector

def fetch(query):
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
def insert(query):
    cursor.execute(query)
    connection.commit()
    print("Data inserted successfully")
def update(query):
    cursor.execute(query)
    connection.commit()
    print("Data updated successfully")
def delete(query):
    cursor.execute(query)
    connection.commit()
    print("Data deleted successfully")


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1903@kp",
    database="users"
)
cursor = connection.cursor()

if connection.is_connected():
    print("Connected to the database")
    fetch("SELECT * FROM login")
    insert("INSERT INTO login (username, password) VALUES ('Anshu', 'password123')")
    fetch("SELECT * FROM login")
    update("UPDATE login SET password = 'JavaIsBooring' WHERE username = 'Anshu'")
    fetch("SELECT * FROM login")
    delete("DELETE FROM login WHERE username = 'Anshu'")
    fetch("SELECT * FROM login")

else:
    print("Failed to connect to the database")

