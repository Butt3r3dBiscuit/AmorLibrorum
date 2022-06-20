import connect

def admin_user_addition(db, username, password):
    my_cursor = db.cursor()
    try:
        my_cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")

        my_cursor.execute("FLUSH PRIVILEGES;")

        my_cursor.execute(f"grant all privileges on AmorLibrorum.* to '{username}'@'localhost';")

    except Exception as e:
        # this error catches if passsword doesn't satisfy the policy requirements
        if e.errno == 1819:
            return e

        # this error cathes if user already exists
        if e.errno == 1396:
            my_cursor.execute(f"DROP USER '{username}'@'localhost';")
            return admin_user_addition(db, username, password)

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

        my_cursor.execute(f"GRANT EXECUTE ON PROCEDURE `Amorlibrorum`.`sell` to '{username}'@'localhost'")


    except Exception as e:
        # this error cathes if passsword doesn't satisfy the policy requirements
        if e.errno==1819:
            return e

        # this error catches if user already exists
        if e.errno==1396:
            my_cursor.execute(f"DROP USER '{username}'@'localhost';")
            return employee_user_addition(db,username,password)

