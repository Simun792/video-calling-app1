import mysql.connector

def get_connection():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456"
    )
    return mydb