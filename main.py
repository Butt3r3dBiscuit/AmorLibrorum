import os
import mysql.connector

our_servers_password = "root"
try:


    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("DBPassword"),
        database="testdatabase")

    mycursor = db.cursor()

    mycursor.execute("show databases;")

    for x in mycursor:
        print(x)
except:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=os.environ.get("DBPassword"))

    mycursor = db.cursor()
    mycursor.execute("create database testdatabase")



