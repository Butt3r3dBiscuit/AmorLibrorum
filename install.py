import mysql.connector
import reinstall_DB


def log_in(database_name="AmorLibrorum"):  # log into the database
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="MyN3wP4ssw0rd!*",
            database=database_name)

        print("database has already been installed")
        return db
    except:
        reinstall_DB.reinstall(database_name)
        log_in()
        '''
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="MyN3wP4ssw0rd!*")

        mycursor = db.cursor()
        mycursor.execute(f"create database {database_name}")
        log_in()
        '''


def user_intergration(my_cursor):
    # here we are going to build the database's core
    try:
        my_cursor.execute("CREATE USER 'user'@'localhost' IDENTIFIED BY 'Password123_'")
        my_cursor.execute("FLUSH PRIVILEGES;")
        my_cursor.execute("GRANT SELECT ON AmorLibrorum.book TO 'user'@'localhost'")
    except mysql.connector.errors.DatabaseError:
        mycursor.execute("DROP USER 'user'@'localhost';")
        return user_intergration(my_cursor)
    mycursor.execute("show tables;")
    for i in mycursor:
        print(i[0])


if __name__ == "__main__":
    db = log_in()
    mycursor = db.cursor()

    # mycursor.execute("show tables;")
    # for i in mycursor:
    #     print(i[0])

    user_intergration(mycursor)

    # here we could reference the starting app ig

    # mycursor.execute("DROP USER 'user'@'localhost';")
    # test
