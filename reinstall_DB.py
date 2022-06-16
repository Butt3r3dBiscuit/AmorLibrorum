# https://stackoverflow.com/questions/36574621/running-a-entire-sql-script-via-python
import mysql.connector
import os


# pip install mysql-connector-python

# import pandas as pd

def reinstall(database_name="AmorLibrorum", sql_script="AmorLibrorum.sql"):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*")

    mycursor = db.cursor()
    mycursor.execute(f"drop database if exists {database_name};")
    mycursor.execute(f"create database {database_name};")

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*",
        database=database_name)
    mycursor = db.cursor()
    try:
        f = open(f"{sql_script}", encoding="utf8")
        full_sql = f.read()
        sql_commands = full_sql.replace('\n', '').split(';')[:-1]
        for sql_command in sql_commands:
            mycursor.execute(sql_command)
    except FileNotFoundError:
        print("Here will be a pop_up that such directory doesn't exist or sth")
    mycursor.close()
    db.close()


def importing_data(sql_script):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*",
        database="Amorlibrorum")
    mycursor = db.cursor()
    try:
        f = open(f"{sql_script}")
        full_sql = f.read()
        sql_commands = full_sql.replace('\n', '').split(';')[:-1]
        for sql_command in sql_commands:
            mycursor.execute(sql_command)
    except FileNotFoundError:
        print("Here will be a pop_up that such directory doesn't exist or sth")
    mycursor.close()
    db.close()


def importing_functions(sql_script):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*",
        database="Amorlibrorum")
    mycursor = db.cursor()
    with open(sql_script, 'r') as sql_file:
        result_iterator = mycursor.execute(sql_file.read(), multi=True)
        for res in result_iterator:
            print(res)

    mycursor.close()
    db.close()


# def filling_up(excel_file):
#     df = pd.read_excel(excel_file)

#     print(df["title"][0])

if __name__ == "__main__":
    reinstall()
    importing_data("testdata.sql")
    importing_functions("functions_in_sql.sql")
    # filling_up("Amor_librorum.xlsx")