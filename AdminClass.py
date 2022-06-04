import connect
from user_creation import employee_user_addition

# insert queries
def add_to_books(ISBN, Title, publisher, published_year, pages, language, location, section, edition, genre, book_type):
    query = f"insert into books(ISBN, Title, publisher, published_year, pages, language," \
            f" location, section, book_type, edition, genre) values ({ISBN}, '{Title}', '{publisher}', {published_year}, {pages}, '{language}'," \
            f" {location}, {section}, '{book_type}', '{edition}', '{genre}')"
    return query

def add_to_authors(ISBN, author_name, author_surname):
    query = f"insert into Authors values ({ISBN}, '{author_name}', '{author_surname}')"
    return query

def add_to_if_translated(ISBN, translator, Title_untranslated, translated_from):
    query = f"insert into if_translated values ({ISBN}, {translator}, {Title_untranslated}, {translated_from})"
    return query

def add_to_Book_entries(ISBN, status_comment):
    query = f"insert into book_entries(ISBN, status_comment) values ({ISBN}, '{status_comment}')"
    return query

def add_to_Price_exceptions(book_id, newprice, comment):
    query = f"insert into Price_exceptions values ({book_id}, {newprice}, {comment})"
    return query

def add_to_Transactions(book_id, employee_id, date, Price):
    query = f"insert into transactions(Book_ID, Employee_ID, Date, Price_in_cents) values ({book_id}," \
            f" {employee_id}, '{date}', {Price})"
    return query

def add_to_employees(Name, Surname, position, Password, email):
    query = f"insert into employees(Name, Surname, position, Password, email) values({Name}, {Surname}," \
            f" {position}, {Password}, {email})"
    return query

def add_to_variables(margin):
    query = f"insert into variables(margin) values ({margin})"
    return query


# Admin class query
class Admin:
    # inventory search
    def inventory_search_authors_books(self, ISBN=9780593334833):  #
        #returns ISBN, title, author_name, author_surname, publisher, year_published,
        #pages, language, edition, book_type, location, section and Genre
        query = f"select a.ISBN, a.title, b.author_name, b.author_surname, a.publisher, a.year_published, a.pages," \
                f" a.language, a.edition, a.book_type, a.location, a.section, a.Genre from books a," \
                f" authors b where a.ISBN={ISBN} and b.ISBN={ISBN}"
        return query

    def inventory_search_num_books(self, ISBN=9780593334833):
        #returns the number of books
        query = f"select count(book_id) from book_entries where ISBN={ISBN}"
        return query

    def inventory_search_exceptionsprice(self, ISBN=9780593334833):
        #returns list of book_ids
        query = f"select a.book_id from book_entries a, price_exceptions b where a.book_id=b.book_id and a.ISBN={ISBN}"
        return query

    # transaction search
    def search_records(self, ISBN=None, Employee_id=None, Book_id=None):
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

    def num_of_sales(self, start_date=None, end_date=None, Employee_id=None, ISBN=None):
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

    def profits(self, ISBN=None, employee_id=None, start_date=None, end_date=None):
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
    def employee_search(self, name, surname):
        #returns employee_id, name, surname,  email, position
        query = f"select a.employee_id, a.name, a.surname, a.email, a.position from employees a where a.Name='{name}' and a.Surname='{surname}'"
        return query
    
    # procedures
    def add_user(self, mycursor, email, password):
        employee_user_addition(mycursor, email, password)

    def add_book(self, mycursor, ISBN, Title, author_name, author_surname, publisher, published_year, pages, language, book_type, location, section, genre, employee_id, date, Price, status_comment="NULL", translator="NULL", Title_untranslated="NULL", translated_from="NULL", edition="NULL", number_of_copies=1):
        #queries
        Book_entries = add_to_Book_entries(ISBN=ISBN, status_comment=status_comment)
        print(Book_entries)
        books = add_to_books(ISBN=ISBN, Title=Title, publisher=publisher, published_year=published_year, pages=pages, language=language, edition=edition, book_type=book_type, location=location, section=section, genre=genre)
        print(books)
        authors = add_to_authors(ISBN=ISBN, author_name=author_name, author_surname=author_surname)
        print(authors)
        if_translated = add_to_if_translated(ISBN=ISBN, translator=translator, Title_untranslated=Title_untranslated, translated_from=translated_from)
        print(if_translated)
        
        Transactions = add_to_Transactions(book_id, employee_id, date, Price)
        print(Transactions)

        #adds to book_entries
        for i in range(number_of_copies):
            mycursor.execute(Book_entries)
        #adds to transactions
        book_id_list = mycursor.execute(f"select book_id from book_entries where ISBN={ISBN}")
        for x in book_id_list:
            for book_id in x:
                mycursor.execute(Transactions)
        #if book not yet in database adds to books, auhtors, if_translated
        ISBN_list = mycursor.execute("select ISBN from books")
        for i in ISBN_list:
            if ISBN not in i:
                #adds to books
                mycursor.execute(books)
                #adds to authors
                mycursor.execute(authors)
                #adds to translated if translated
                if translator!=None or Title_untranslated!=None or translated_from!=None:
                    mycursor.execute(if_translated)





admin = Admin()
db = connect.connect_admin("MyN3wP4ssw0rd!*")
mycursor= db.cursor()

mycursor.execute("start transaction;")
admin.add_book(mycursor=mycursor, ISBN=9780590353403, Title="Harry Potter and the Sorcerer's Stone", author_name="Joanne", author_surname="Rowling", publisher="Scholastic Inc", published_year='2003', pages="309", language="English (USA)", book_type="Hardcover", location="7", section="7", genre="Fiction", employee_id=2, date="2022-06-02", Price=1000, translator="Harry potter", Title_untranslated="Harry Potter and the Philosopher's Stone", translated_from="English", edition="Library Edition", number_of_copies=1)


class Employee:
    pass


# try:
#     db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd="MyN3wP4ssw0rd!*",
#         database="amorlibrorum")
# except:
#     print("Something went wrong which sucks for u bud :3")

db = connect.connect_admin("MyN3wP4ssw0rd!*") #temporal solution

# def query_to_values(db, query):  # returns a list of values
#     mycursor = db.cursor()
#     mycursor.execute(query)
#     for (x) in mycursor:
#         return x


# test = (query_to_values(db, curry))
# print(test)
