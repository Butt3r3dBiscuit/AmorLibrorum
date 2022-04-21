import os
import mysql.connector

try:


    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*",
        database="testdatabase")

    mycursor = db.cursor()

    mycursor.execute("show databases;")

    for x in mycursor:
        print(x)
except:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*")

    mycursor = db.cursor()
    mycursor.execute("create database testdatabase")



