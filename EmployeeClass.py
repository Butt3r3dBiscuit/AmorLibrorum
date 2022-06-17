from re import L
import mysql.connector
import connect
from user_creation import employee_user_addition

class Employee:
    #database cursor
    def __init__(self, db):
        self.db = db
        self.mycursor = db.cursor()
    #sell procedure
    def sell(self, book_id, employee_id):
        arg=(book_id, employee_id)
        self.mycursor.callproc("sell", arg)
    def return_book(self, book_id, employee_id):
        arg=(book_id, employee_id)
        self.mycursor.callproc("return_book", arg)

if __name__ == "__main__":
    db = connect.connect_admin("MyN3wP4ssw0rd!*")
    emp = Employee(db)
    mycursor= db.cursor()

    emp.sell(21, 2)
    db.commit()
    db.close()