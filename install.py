import os
import mysql.connector

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("DBPassword"),
        database="testdatabase")

    print("database has already been installed")
    exit()
except:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("DBPassword"))

    mycursor = db.cursor()
    mycursor.execute("create database testdatabase")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("DBPassword"),
        database="testdatabase")

    mycursor = db.cursor()
    mycursor.execute("CREATE USER 'test'@'localhost' IDENTIFIED BY 'MyGreatPW123_'")
    mycursor.execute("FLUSH PRIVILEGES;")
    #to drop a user use: DROP USER 'test'@'localhost';






