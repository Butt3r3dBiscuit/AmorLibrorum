import connect

def admin_user_addition(db, username, password):
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")

        my_cursor.execute("FLUSH PRIVILEGES;")

        my_cursor.execute(f"grant all privileges on AmorLibrorum.* to '{username}'@'localhost';")

    except Exception as e:
        if e.errno == 1819:
            # this error catches if passsword doesn't satisfy the policy requirements
            print("make a pop up out of this:")
            print("Your password does not satisfy the current policy requirements")
            return e

        if e.errno == 1396:
            # this error cathes if user already exists
            print('here')
            my_cursor.execute(f"DROP USER '{username}'@'localhost';")
            return admin_user_addition(my_cursor, username, password)
        print(e)

def employee_user_addition(db,username,password):
    my_cursor = db.cursor()

    try:
        my_cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")

        my_cursor.execute("FLUSH PRIVILEGES;")

        my_cursor.execute(f"GRANT SELECT ON AmorLibrorum.authors TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT ON AmorLibrorum.Book_entries TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT ON AmorLibrorum.Books TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT ON AmorLibrorum.if_translated TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT ON AmorLibrorum.Price_exceptions TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT, INSERT ON AmorLibrorum.Transactions TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT ON AmorLibrorum.variables TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT SELECT (position, email, Employee_ID) ON AmorLibrorum.Employees TO '{username}'@'localhost'")

        my_cursor.execute(f"GRANT EXECUTE on FUNCTION `Amorlibrorum`.`price_determination` to '{username}'@'localhost'")


        print("user has been added")

    except Exception as e:
        if e.errno==1819:
            #this error cathes if passsword doesn't satisfy the policy requirements
            print("make a pop up out of this:")
            print("Your password does not satisfy the current policy requirements")
            return e

        if e.errno==1396:
            #this error cathes if user already exists
            print('here')
            my_cursor.execute(f"DROP USER '{username}'@'localhost';")
            return employee_user_addition(my_cursor,username,password)
        print(e)

if __name__=="__main__":
    db = connect.connect_admin("MyN3wP4ssw0rd!*")
    my_cursor = db.cursor()
    ## test add user
    employee_user_addition(my_cursor,"casual@amorlibrorum.boek","YetAn0!herqwertyp4ssword")
    admin_user_addition(my_cursor, "mytestADmin", "YetAn0!herqwertyp4ssword")

#for dropping