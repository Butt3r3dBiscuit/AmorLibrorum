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

#Admin class query
class Admin:
    def add_book(self, ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre, author_name, author_surname, status_comment, translator, Title_translated, translated_from, book_id, employee_id, date, Price):
        add_to_books = add_to_books(ISBN, Title, publisher, published_year, pages, language, edition, book_type, location, section, genre)
        add_to_authors = add_to_authors(ISBN, author_name, author_surname)
        add_to_Book_entries = add_to_Book_entries(ISBN, status_comment)
        add_to_Transactions(book_id, employee_id, date, Price)
        add_to_if_translated = add_to_if_translated(ISBN, translator, Title_translated, translated_from)
        return add_to_books, add_to_authors, add_to_Book_entries, add_to_Transactions, add_to_if_translated

class Employee:
    pass

Frank = Admin()

qurry = Frank.add_book

print(qurry)