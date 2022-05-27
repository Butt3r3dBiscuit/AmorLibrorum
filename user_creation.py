import connect

def employee_user_addition(my_cursor,username,password):
    #here we are going to build the database's core
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




        print("user has been added")

    except Exception as e:
        if e.errno==1819:
            #this error cathes if passsword doesn't satisfy the policy requirements
            print("make a pop up out of this:")
            print("Your password does not satisfy the current policy requirements")

        if e.errno==1396:
            #this error cathes if user already exists
            print('here')
            my_cursor.execute(f"DROP USER '{username}'@'localhost';")
            return employee_user_addition(my_cursor,username,password)
        print(e)

db = connect.connect_admin("MyN3wP4ssw0rd!*")
my_cursor = db.cursor()
## test add user
employee_user_addition(my_cursor,"Jan@mail.com","MyCoolPassword123!")