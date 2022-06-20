from re import L
import mysql.connector
import connect
from user_creation import employee_user_addition
from AdminClass import func_search_records

class Employee:
    # database cursor
    def __init__(self, db):
        self.db = db
        self.mycursor = db.cursor()
    # sell procedure
    def sell(self, book_id, employee_id):
        arg=(book_id, employee_id)
        self.mycursor.callproc("sell", arg)
    # return  book procedure
    def return_book(self, book_id, employee_id):
        arg=(book_id, employee_id)
        self.mycursor.callproc("return_book", arg)
    # search records
    def search_records(self, ISBN=None, Employee_id=None, Book_id=None):
        # retrieves records
        search = func_search_records(ISBN=ISBN, Employee_id=Employee_id, Book_id=Book_id)
        self.mycursor.execute(search)
        result_fetch = self.mycursor.fetchall()
        return result_fetch

if __name__ == "__main__":
    db = connect.connect_admin("MyN3wP4ssw0rd!*")
    emp = Employee(db)
    mycursor= db.cursor()

    emp.sell(21, 2)
    emp.return_book(21, 1)
    emp.sell(21, 2)
    emp.return_book(21, 1)
    db.commit()
    db.close()