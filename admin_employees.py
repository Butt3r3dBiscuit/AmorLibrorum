def employee_account_addition(my_cursor,username,password):
    try:
        my_cursor.execute(f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{password}'")
        my_cursor.execute("FLUSH PRIVILEGES;")
        my_cursor.execute("GRANT SELECT ON AmorLibrorum.book TO 'user'@'localhost'")
        ##Give more power eventually
    except mysql.connector.errors.DatabaseError:
        mycursor.execute(f"DROP USER '{username}'@'localhost';")
        return user_intergration(my_cursor)
    mycursor.execute("show tables;")
    for i in mycursor:
        print(i[0])