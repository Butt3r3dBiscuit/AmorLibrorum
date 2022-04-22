import sys
#https://stackoverflow.com/questions/36574621/running-a-entire-sql-script-via-python
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MyN3wP4ssw0rd!*")

mycursor = db.cursor()
mycursor.execute("drop database testdatabase;")
mycursor.execute("create database testdatabase;")

db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="MyN3wP4ssw0rd!*",
            database="testdatabase")
mycursor = db.cursor()
f = open("test.sql")
full_sql = f.read()
sql_commands = full_sql.replace('\n', '').split(';')[:-1]
for sql_command in sql_commands:
    mycursor.execute(sql_command)

