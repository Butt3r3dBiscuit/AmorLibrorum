import connect.py

class Admin:
    def __init__(self, password):
        connection = connect.connect_admin(password)
    def search(ISBN):


class Employee:
    def __init__(self):
        connection = connect.connect_user()
    def search(book_id):
        return f"select a.title, b.author, a.edition, a.location, a.section, a.language, d.sellprice from book a, author b, book_entry c, Price_exceptions d where a.ISBN=b.ISBN and a.ISBN=c.ISBN and book_id='{book_id}'"

Niels = Employee

query = Niels.search(1234)

print(query)