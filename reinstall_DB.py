# https://stackoverflow.com/questions/36574621/running-a-entire-sql-script-via-python
import mysql.connector

# pip install mysql-connector-python

# import pandas as pd

def reinstall(database_name="AmorLibrorum",sql_script="AmorLibrorum.sql"):
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
        f = open(f"{sql_script}")
        full_sql = f.read()
        sql_commands = full_sql.replace('\n', '').split(';')[:-1]
        for sql_command in sql_commands:
            mycursor.execute(sql_command)
    except FileNotFoundError:
        print("Here will be a pop_up that such directory doesn't exist or sth")
    mycursor.close()
    db.close()

# def filling_up(excel_file):
#     df = pd.read_excel(excel_file)

#     print(df["title"][0])

if __name__=="__main__":
    reinstall()
    # filling_up("Amor_librorum.xlsx")


'''
next we will add there the insertion of values from excel sheet
which would probably be defined in another function idk yet
'''