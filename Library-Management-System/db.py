import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MONSTER_X_YT1",
    database="library_db"
)

cursor = connection.cursor()