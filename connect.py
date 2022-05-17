import mysql.connector

def connect_user():
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="user",
            passwd="Password123_",
            database="AmorLibrorum")

        print("database has already been installed")
        return db
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
        return e

def connect_employee(email, password_from_log_in):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user=f"{email}",
            passwd=f"{password_from_log_in}",
            database="AmorLibrorum")

        print("database has already been installed")
        return db
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
        return e

def connect_admin(password_from_log_in):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=f"{password_from_log_in}",
            database="AmorLibrorum")

        print("database has already been installed")
        return db
    except mysql.connector.errors.ProgrammingError as e:
        print(e)
        return e

if __name__== "__main__":
    mycursor= connect_user()
    connect_admin("MyN3wP4ssw0rd!*")
