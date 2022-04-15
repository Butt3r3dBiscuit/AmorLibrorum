import os
import mysql.connector

def log_in(database_name="testdatabase"): #log into the database
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=os.environ.get("DBPassword"),
            database=database_name)

        print("database has already been installed")
        return db
    except:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=os.environ.get("DBPassword"))

        mycursor = db.cursor()
        mycursor.execute(f"create database {database_name}")
        log_in()

def initialization(my_cursor):
    #here we are going to build the database's core
    my_cursor.execute("CREATE USER 'user'@'localhost' IDENTIFIED BY 'Password123_'")
    my_cursor.execute("FLUSH PRIVILEGES;")



if __name__ == "__main__":
    db = log_in()
    mycursor = db.cursor()

    initialization(mycursor)

    #here we could reference the starting app Ig

    # mycursor.execute("DROP USER 'user'@'localhost';")







