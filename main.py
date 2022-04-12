import mysql.connector

our_servers_password = "root"
#change this to your server password

try:


    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=our_servers_password,
        database="testdatabase")

    mycursor = db.cursor()

    mycursor.execute("show databases;")

    for x in mycursor:
        print(x)
except:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=our_servers_password)

    mycursor = db.cursor()
    mycursor.execute("create database testdatabase")



