#insert functions

def add_to_books(ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre):
    query = f"insert into books values ({ISBN}, {Title}, {publisher}, {published_year}, {pages}, {language}, {edition}, {book_type}, {location}, {section}, {genre})"
    return query

def add_to_authors(ISBN, author_name, author_surname):
    query = f"insert into Authors values ({ISBN}, {author_name}, {author_surname})"
    return query

def add_to_if_translated(ISBN, translator, Title_translated, translated_from):
    query = f"insert into if_translated values ({ISBN}, {translator}, {Title_translated}, {translated_from})"
    return query

def add_to_Book_entries(ISBN, status_comment):
    query = f"insert into book_entries(ISBN, status/comment) values ({ISBN}, {status_comment})"
    return query

def add_to_Price_exceptions(book_id, newprice, comment):
    query = f"insert into Price_exceptions values ({book_id}, {newprice}, {comment})"
    return query

def add_to_Transactions(book_id, employee_id, date, Price):
    query = f"insert into transactions(book_ID, Employee_ID, date, Price(in_cents)) values ({book_id}, {employee_id}, {date}, {Price})"
    return query

def add_to_employees(Name, Surname, position, Password, email):
    query = f"insert into employees(Name, Surname, position, Password, email) values({Name}, {Surname}, {position}, {Password}, {email})"
    return query

def add_to_variables(margin):
    query = f"insert into variables(margin) values ({margin})"
    return query

#admin search
def inventory_search(ISBN):
    ISBN = 9780593334833
    query = f"select a.ISBN, a.title, b.author_name, b.author_surname, a.publisher, a.year_published, a.pages, a.language, a.edition, a.book_type, a.location, a.section, a.Genre from books a, authors b where a.ISBN={ISBN} and b.ISBN={ISBN};"

#Admin class query
class Admin:
    #insert queries
    def add_to_books(self, ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre):
        query = f"insert into books values ({ISBN}, {Title}, {publisher}, {published_year}, {pages}, {language}, {edition}, {book_type}, {location}, {section}, {genre})"
        return query

    def add_to_authors(self, ISBN, author_name, author_surname):
        query = f"insert into Authors values ({ISBN}, {author_name}, {author_surname})"
        return query

    def add_to_if_translated(self, ISBN, translator, Title_translated, translated_from):
        query = f"insert into if_translated values ({ISBN}, {translator}, {Title_translated}, {translated_from})"
        return query

    def add_to_Book_entries(self, ISBN, status_comment):
        query = f"insert into book_entries(ISBN, status/comment) values ({ISBN}, {status_comment})"
        return query

    def add_to_Price_exceptions(self, book_id, newprice, comment):
        query = f"insert into Price_exceptions values ({book_id}, {newprice}, {comment})"
        return query

    def add_to_Transactions(self, book_id, employee_id, date, Price):
        query = f"insert into transactions(Book_ID, Employee_ID, Date, Price_in_cents) values ({book_id}, {employee_id}, {date}, {Price})"
        return query

    def add_to_employees(self, Name, Surname, position, Password, email):
        query = f"insert into employees(Name, Surname, position, Password, email) values({Name}, {Surname}, {position}, {Password}, {email})"
        return query

    def add_to_variables(self, margin):
        query = f"insert into variables(margin) values ({margin})"
        return query

    #inventory search
    def inventory_search_authors_books(self, ISBN=9780593334833): #returns ISBN, title, author_name, author_surname, publisher, year_published, pages, language, edition, book_type, location, section and Genre
        query = f"select a.ISBN, a.title, b.author_name, b.author_surname, a.publisher, a.year_published, a.pages, a.language, a.edition, a.book_type, a.location, a.section, a.Genre from books a, authors b where a.ISBN={ISBN} and b.ISBN={ISBN}"
        return query

    def inventory_search_num_books(self, ISBN=9780593334833): #returns the number of books
        query = f"select count(book_id) from book_entries where ISBN={ISBN}"
        return query

    def inventory_search_exceptionsprice(self, ISBN=9780593334833): #returns book_ids
        query = f"select a.book_id from book_entries a, price_exceptions b where a.book_id=b.book_id and a.ISBN={ISBN}"
        return query
    #transaction search
    def search_records_Book_id(self, Book_id=15):#search records by book_id
        query = f"select e.name, e.surname, a.ISBN, a.title, b.author_name, b.author_surname, a.edition, a.book_type, c.price_in_cents from books a, authors b, transactions c, book_entries d, employees e where a.ISBN=d.ISBN and c.book_id=d.book_id and d.ISBN=b.ISBN and e.employee_id=c.employee_id and c.book_id={Book_id}"
    
    def search_records_ISBN(self, ISBN=9780593334833):#search by ISBN
        query = f"select e.name, e.surname, a.ISBN, a.title, b.author_name, b.author_surname, a.edition, a.book_type, c.price_in_cents from books a, authors b, transactions c, book_entries d, employees e where a.ISBN=d.ISBN and c.book_id=d.book_id and d.ISBN=b.ISBN and e.employee_id=c.employee_id and a.ISBN={ISBN}"
        return query
    
    def search_records_Employee_id(self, Employee_id=2):#search by employee_id
        query = f""
        return query
    
    def num_of_sales(self, date=None, Employee_id=None, ISBN=None):#number of sales per employee and/or ISBN and/or date
        query = f"select count(a.book_id) from transactions a, book_entries b where a.book_id=b.book_id and a.price_in_cents>0"
        if ISBN!=None:
            query = query + f" and b.ISBN={ISBN}"
        if Employee_id!=None:
            query = query + f" and a.Employee_id={Employee_id}"
        if date!=None:
            query = query + f" and a.date={date}"
        return query

admin = Admin()
curry = admin.inventory_search_authors_books()
print(curry)

class Employee:
    pass

import mysql.connector
import os

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="MyN3wP4ssw0rd!*",
        database="amorlibrorum")
except:
    print("Something went wrong sucks for u bud :3")

def query_to_value(db, query):
    mycursor = db.cursor()
    mycursor.execute(query)
    for x in mycursor:
        return x

print(query_to_value(db, curry))