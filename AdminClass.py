import connect


# insert functions

def add_to_books(ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre):
    query = f"insert into books values ({ISBN}, {Title}, {publisher}, {published_year}, {pages}, {language}, " \
            f"{edition}, {book_type}, {location}, {section}, {genre})"
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
    query = f"insert into transactions(book_ID, Employee_ID, date, Price_in_cents) values ({book_id}, {employee_id}," \
            f" {date}, {Price})"
    return query


def add_to_employees(Name, Surname, position, Password, email):
    query = f"insert into employees(Name, Surname, position, Password, email) values({Name}, {Surname}, {position}," \
            f" {Password}, {email})"
    return query


def add_to_variables(margin):
    query = f"insert into variables(margin) values ({margin})"
    return query


# admin search
def inventory_search(ISBN):
    ISBN = 9780593334833
    query = f"select a.ISBN, a.title, b.author_name, b.author_surname, a.publisher, a.year_published, a.pages," \
            f" a.language, a.edition, a.book_type, a.location, a.section, a.Genre from books a," \
            f" authors b where a.ISBN={ISBN} and b.ISBN={ISBN};"
    return query


# Admin class query
class Admin:
    # insert queries
    def add_to_books(self, ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre):
        query = f"insert into books values ({ISBN}, {Title}, {publisher}, {published_year}, {pages}, {language}," \
                f" {edition}, {book_type}, {location}, {section}, {genre})"
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
        query = f"insert into transactions(Book_ID, Employee_ID, Date, Price_in_cents) values ({book_id}," \
                f" {employee_id}, {date}, {Price})"
        return query

    def add_to_employees(self, Name, Surname, position, Password, email):
        query = f"insert into employees(Name, Surname, position, Password, email) values({Name}, {Surname}," \
                f" {position}, {Password}, {email})"
        return query

    def add_to_variables(self, margin):
        query = f"insert into variables(margin) values ({margin})"
        return query

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

    def num_of_sales(self, start_date=None, end_date=None, Employee_id=None, ISBN=None):  # number of sales per employee and/or ISBN and/or date
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

    def profits(self, employee_id=None, start_date=None, end_date=None):
        query = f"select sum(price_in_cents) from transactions"
        if employee_id is not None:
            if "=" not in query:
                query += f" where employee_id={employee_id}"
            else:
                query += f" and employee_id={employee_id}"
        if start_date is not None:
            if ("=" or ">=") not in query:
                query += f" where date>='{start_date}'"
            else:
                query += f" and date>='{start_date}'"
        if end_date is not None:
            if ("=" or "<") not in query:
                query += f" where date<'{end_date}'"
            else:
                query += f" and date<'{end_date}'"
        return query


admin = Admin()
curry = admin.search_records(ISBN=9780593334833)
print(curry)


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

def query_to_values(db, query):  # returns a list of values
    mycursor = db.cursor()
    mycursor.execute(query)
    for (x) in mycursor:
        return x


test = (query_to_values(db, curry))
print(test)
