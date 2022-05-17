#insert functions

def add_to_books(ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre):
    query = f"insert into books values ({ISBN}, {Title}, {publisher}, {published_year}, {pages}, {language}, {edition}, {book_type}, {location}, {section}, {genre})"
    return query

def add_to_authors():
    query = f"insert into Authors values ({ISBN}, {author_name}, {author_surname})"
    return query

def add_to_if_translated():
    query = f"insert into if_translated values ({ISBN}, {translator}, {Title_translated}, {translated_from})"
    return query

def add_to_Book_entries():
    query = f"insert into book_entries(ISBN, status/comment) values ({ISBN}, {status_comment})"
    return query

def add_to_Price_exceptions():
    query = f"insert into Price_exceptions values ({book_id}, {newprice}, {comment})"
    return query

def add_to_Transactions():
    query = f"insert into transactions(book_ID, Employee_ID, date, Price(in_cents)) values ({book_id}, {employee_id}, {date}, {Price})"
    return query

def add_to_employees():
    query = f"insert into employees(Name, Surname, position, Password, email) values({Name}, {Surname}, {position}, {Password}, {email})"
    return query

def add_to_variables(margin):
    query = f"insert into variables(margin) values ({margin})"
    return query

#Admin class query
class Admin:
    def add_book(self, ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre):
        return add_to_books(ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre)

class Employee:
    pass

Frank = Admin()

qurry = Frank.add_book(ISBN=54, Title="Lord of the Rings", publisher="IDK", published_year="2012", pages=500, language="English", edition="NULL", book_type="NULL", location="IDK", section="Diemen zuid", genre="NULL")

print(qurry)