from re import L
import mysql.connector
import connect
from user_creation import employee_user_addition


# insert queries
def add_to_books(ISBN, Title, publisher, published_year, pages, language, location, section, edition, genre, book_type):
    query = f"insert into books(ISBN, Title, publisher, year_published, pages, language," \
            f" location, section, book_type, edition, genre) values ({ISBN}, '{Title}', '{publisher}', " \
            f"{published_year}, {pages}, '{language}'," \
            f" {location}, {section}, '{book_type}', '{edition}', '{genre}')"
    return query


def add_to_authors(ISBN, author_name, author_surname):
    query = f"insert into Authors values ({ISBN}, '{author_name}', '{author_surname}')"
    return query


def add_to_if_translated(ISBN, translator, Title_untranslated, translated_from):
    query = f"insert into if_translated values ({ISBN}, '{translator}', '{Title_untranslated}', '{translated_from}')"
    return query


def add_to_Book_entries(ISBN, status_comment):
    query = f"insert into book_entries(ISBN, status_comment) values ({ISBN}, '{status_comment}')"
    return query


def add_to_Price_exceptions(newprice=None, book_id=None, comment="NULL"):
    if newprice==None:
        newprice="Null"
    query = f"insert into Price_exceptions values ({book_id}, {newprice}, '{comment}')"
    return query


def add_to_Transactions(book_id, employee_id, date, Price):
    query = f"insert into transactions(Book_ID, Employee_ID, Trans_Date, Price_in_cents) values ({book_id}," \
            f" {employee_id}, '{date}', {Price})"
    return query


def add_to_employees(Name, Surname, position, email):
    query = f"insert into employees(Name, Surname, position, email) values('{Name}', '{Surname}'," \
            f" '{position}', '{email}')"
    return query


def add_to_variables(margin):
    query = f"insert into variables(margin) values ({margin})"
    return query

# transaction search
def func_search_records(ISBN=None, Employee_id=None, Book_id=None):
    #returns book_id, ISBN, title, author_name, author_surname, edition, book_type, name, surname, price_in_cents
    query = f"select c.book_id, a.ISBN, a.title, b.author_name, b.author_surname, a.edition," \
            f" a.book_type, e.name, e.surname, c.price_in_cents from books a, authors b, transactions c, book_entries d," \
            f" employees e where a.ISBN=d.ISBN and c.book_id=d.book_id and d.ISBN=b.ISBN and" \
            f" e.employee_id=c.employee_id"
    if ISBN!=None:
        query+= f" and a.ISBN={ISBN}"
    if Employee_id!=None:
        query+= f" and e.Employee_id={Employee_id}"
    if Book_id!=None:
        query+= f" and c.book_id={Book_id}"
    return query

def num_of_sales(start_date=None, end_date=None, Employee_id=None, ISBN=None):
    #returns number of sales
    query = f"select count(a.book_id) from transactions a, book_entries b" \
            f" where a.book_id=b.book_id and a.price_in_cents>0"
    if ISBN is not None:
        query = query + f" and b.ISBN={ISBN}"
    if Employee_id is not None:
        query += f" and a.Employee_id={Employee_id}"
    if start_date is not None:
        query += f" and a.date>={start_date}"
    if end_date is not None:
        query += f" and a.date<{end_date}"
    return query

def profits(ISBN=None, employee_id=None, start_date=None, end_date=None):
    #returns profit in cents
    query = f"select sum(a.price_in_cents) from transactions a, book_entries b"
    if ISBN is not None:
        if "=" not in query:
            query += f" where a.book_id=b.book_id and b.ISBN={ISBN}"
        else:
            query += f" and a.book_id=b.book_id and b.ISBN={ISBN}"
    if employee_id is not None:
        if "=" not in query:
            query += f" where a.employee_id={employee_id}"
        else:
            query += f" and a.employee_id={employee_id}"
    if start_date is not None:
        if ("=" or ">=") not in query:
            query += f" where a.date>='{start_date}'"
        else:
            query += f" and a.date>='{start_date}'"
    if end_date is not None:
        if ("=" or "<") not in query:
            query += f" where a.date<'{end_date}'"
        else:
            query += f" and a.date<'{end_date}'"
    return query
    
# employee search
def employee_search(name, surname):
    #returns employee_id, name, surname,  email, position
    query = f"select a.employee_id, a.name, a.surname, a.email, a.position from employees a where a.Name='{name}' and a.Surname='{surname}'"
    return query
    
# Admin class query
class Admin:
    def __init__(self, db):
        self.mycursor = db.cursor()
    # inventory search
    def inventory_search_authors_books(self, ISBN=9780593334833):  #
        # returns ISBN, title, author_name, author_surname, publisher, year_published,
        # pages, language, edition, book_type, location, section and Genre
        query = f"select a.ISBN, a.title, b.author_name, b.author_surname, a.publisher, a.year_published, a.pages," \
                f" a.language, a.edition, a.book_type, a.location, a.section, a.Genre from books a," \
                f" authors b where a.ISBN={ISBN} and b.ISBN={ISBN}"
        return query

    def inventory_search_num_books(self, ISBN=9780593334833):
        # returns the number of books
        query = f"select count(book_id) from book_entries where ISBN={ISBN}"
        return query

    def inventory_search_exceptionsprice(self, ISBN=9780593334833):
        # returns list of book_ids
        query = f"select a.book_id from book_entries a, price_exceptions b where a.book_id=b.book_id and a.ISBN={ISBN}"
        return query
    
    #procedures
    def add_user(self, email, password):
        employee_user_addition(mycursor, email, password)

    def add_book(self, ISBN, Title, author_name, author_surname, publisher,
    published_year, pages, language, book_type, location, section, genre, employee_id, date, 
    Price, status_comment="NULL", translator="NULL", Title_untranslated="NULL", translated_from="NULL", 
    edition="NULL", number_of_copies=1):
        #queries
        print()
        print("Queries executed add book")
        add_book_entries = add_to_Book_entries(ISBN=ISBN, status_comment=status_comment)
        print(add_book_entries)

        add_book = add_to_books(ISBN=ISBN, Title=Title, publisher=publisher, 
        published_year=published_year, pages=pages, language=language, edition=edition, 
        book_type=book_type, location=location, section=section, genre=genre)
        print(add_book)

        add_authors = add_to_authors(ISBN=ISBN, author_name=author_name, author_surname=author_surname)
        print(add_authors)

        add_if_translated = add_to_if_translated(ISBN, translator, Title_untranslated, translated_from)
        print(add_if_translated)

        #checks if price is negative
        if Price<0:
            Price*=-1
        #if book not yet in database adds to books, auhtors, if_translated
        self.mycursor.execute("select ISBN from books")
        ISBN_list_fetch = self.mycursor.fetchall()
        ISBN_list = []
        for i in ISBN_list_fetch:
            for j in i:
                ISBN_list.append(j)
        print(ISBN_list)
        print(ISBN)
        if str(ISBN) not in ISBN_list:
            #adds to books
            self.mycursor.execute(add_book)
            # adds to authors
            self.mycursor.execute(add_authors)
            # adds to translated if translated
            if translator is not None or Title_untranslated is not None or translated_from is not None:
                self.mycursor.execute(add_if_translated)
        #adds to book_entries
        for i in range(number_of_copies):
            print(add_book_entries)
            self.mycursor.execute(add_book_entries)
        #adds to transactions
        self.mycursor.execute(f"select a.book_id from book_entries a order by book_id desc limit {number_of_copies}")
        book_id_list_fetch = self.mycursor.fetchall()
        book_id_list = []
        for i in book_id_list_fetch:
            for j in i:
                book_id_list.append(j)
        print()
        print("book_id list: " + str(book_id_list)) 
        for i in book_id_list:
            print(add_to_Transactions(book_id=i, employee_id=employee_id, date=date, Price=Price))
            self.mycursor.execute(add_to_Transactions(book_id=i, employee_id=employee_id, date=date, Price=Price))
        print()
    
    #space searchbook

    def search_records(self, ISBN=None, Employee_id=None, Book_id=None):
        #retrieves records
        search = func_search_records(ISBN=ISBN, Employee_id=Employee_id, Book_id=Book_id)
        self.mycursor.execute(search)
        result_fetch = self.mycursor.fetchall()
        return result_fetch
    
    def add_price_exception(self, newprice=None, ISBN=None, book_id=None, comment=None):#update by ISBN!
        #list of book_ids in excpetions
        self.mycursor.execute(f"select book_id from price_exceptions")
        book_id_list_exceptions = []
        book_id_list_exceptions_fetch = self.mycursor.fetchall()
        for i in book_id_list_exceptions_fetch:
            for j in i:
                book_id_list_exceptions.append(j)
        #adds book_id to excpetions if book not in price_exceptions list
        try:
            if book_id!=None and ISBN==None:
                book_id_list_fetch = self.mycursor.fetchall()
                if book_id not in book_id_list_exceptions:
                    self.mycursor.execute(add_to_Price_exceptions(newprice=newprice, book_id=book_id, comment=comment))
                else:
                    self.mycursor.execute(f"update price_exceptions set new_price_in_cents={newprice}, Comment='{comment}' where book_id={book_id}")
            #adds book_ids according to ISBN to book excpetions if book_id not in book id exception list
            if book_id==None and ISBN!=None:
                self.mycursor.execute(f"select book_id from book_entries where ISBN={ISBN}")
                book_id_list_fetch = self.mycursor.fetchall()
                book_id_list = []
                for i in book_id_list_fetch:
                    for j in i:
                        book_id_list.append(j)
                for ID in book_id_list:
                    if ID not in book_id_list_exceptions:
                        self.mycursor.execute(add_to_Price_exceptions(newprice=newprice, book_id=ID, comment=comment))
        except mysql.connector.errors.IntegrityError:
            print("Book id does not exist in database >:(")

    def add_employee(self, name, surname, position, passwd, email):
        #checks if employee in database
        self.mycursor.execute(employee_search(name, surname))
        employee_list = []
        for i in self.mycursor.fetchall():
            for j in i:
                employee_list.append(j)
        #adds employee if it not record doesnt already exist
        if (name or surname) not in employee_list:
            print(add_to_employees(Name=name, Surname=surname, position=position, Password=passwd, email=email))
            self.mycursor.execute(add_to_employees(Name=name, Surname=surname, position=position, Password=passwd, email=email))
        #if employee not in employee_list adds employee
        else:
            print("Employee is already in employees >:(")
    
    def search_employee(self, name, surname):
        #retrieves employee datab
        self.mycursor.execute(employee_search(name=name, surname=surname))
        return self.mycursor.fetchall()
    
    def set_margin(self, margin):
        #deltes all variables (margin)
        self.mycursor.execute('delete from variables')
        #adds new margin
        self.mycursor.execute(add_to_variables(margin=margin))
    def emp_search(self, search):
        self.mycursor.execute("SET sql_mode = ''")
        self.mycursor.execute("SELECT EMPLOYEE_ID, NAME, SURNAME, EMAIL "
                              "FROM EMPLOYEES "
                             f"WHERE EMPLOYEE_ID LIKE '%{search}%' "
                             f"OR NAME LIKE '%{search}%' "
                             f"OR SURNAME LIKE '%{search}%' "
                             f"OR EMAIL LIKE '%{search}%' ")
        result = self.mycursor.fetchall()
        return result
    def clean(self):
        self.mycursor.callproc("clean")

    def search(self, search):
        conditions = ""
        conditions = f"WHERE B.TITLE LIKE '%{search}%' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '%{search}%' " \
                         f"OR A.AUTHOR_NAME LIKE '%{search}%' " \
                         f"OR A.AUTHOR_SURNAME LIKE '%{search}%' " \
                         f"OR B.ISBN LIKE '%{search}%'"
        self.mycursor.execute("SET sql_mode = ''")

        self.mycursor.execute(
            "SELECT B.ISBN, B.TITLE, IT.TITLE_UNTRANSLATED, A.AUTHOR_NAME, A.AUTHOR_SURNAME, IT.TRANSLATOR, B.EDITION, B.LANGUAGE, IT.TRANSLATED_FROM, B.GENRE, B.PUBLISHER, B.BOOK_TYPE, B.YEAR_PUBLISHED, B.PAGES, B.LOCATION, B.SECTION, PRICE_DETERMINATION(BE.BOOK_ID), COUNT(BE.BOOK_ID) "
            "FROM BOOKS B LEFT JOIN AUTHORS A "
            "ON B.ISBN=A.ISBN "
            "LEFT JOIN BOOK_ENTRIES BE "
            "ON B.ISBN=BE.ISBN "
            "LEFT JOIN TRANSACTIONS T "
            "ON BE.BOOK_ID=T.BOOK_ID "
            "LEFT JOIN IF_TRANSLATED IT "
            "ON IT.ISBN=B.ISBN "
            f"{conditions} "
            "AND PRICE_DETERMINATION(BE.BOOK_ID)>0 "
            "GROUP BY B.ISBN, PRICE_DETERMINATION(BE.BOOK_ID) "
            "ORDER BY B.ISBN, PRICE_DETERMINATION(BE.BOOK_ID)")
        result = self.mycursor.fetchall()
        return result
if __name__ == "__main__":
    db = connect.connect_admin("MyN3wP4ssw0rd!*")
    admin = Admin(db)
    mycursor= db.cursor()

    # # #call add employee to employees procedure
    # admin.add_employee(name="Albus", surname="Dumbledore", position="Manager", passwd="EldenWandIsOPAF123:3", email="dumbiegamer@hogwarts.com")

    # #call add_book procedure
    #admin.add_book(ISBN=9780590353403, Title="Harry Potter and the Sorcerers Stone", author_name="Joanne", author_surname="Rowling", publisher="Scholastic Inc", published_year=2003, pages="309", language="English (USA)", book_type="Hardcover", location="7", section="7", genre="Fiction", employee_id=1, date="2022-06-02", Price=1000, translator="Joanne Rowling", Title_untranslated="Harry Potter and the Philosophers Stone", translated_from="English", edition=1, number_of_copies=3)
    # #mycursor.execute(f"select * from transactions order by Transaction_ID desc limit 1")

    #print(mycursor.fetchall())

    #call add_price_exception
    #admin.add_price_exception(newprice=10, ISBN=None, book_id=2, comment="Malfidus broke it >:(")

    # #call set margin procedure
    # admin.set_margin(margin=1.210)

    # #call search employee procedure
    # print(admin.search_employee(name="Albus", surname="Dumbledore"))

    # #call search records procedure
    # print(admin.search_records(ISBN=9780593334833, Employee_id=None, Book_id=None))

    #call clean
    admin.clean()

    db.commit()
