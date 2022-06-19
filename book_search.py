import mysql.connector

def book_search(book_id, db):
    mycursor = db.cursor()
    mycursor.execute("SELECT PE.NEW_PRICE_IN_CENTS "
                     "FROM BOOK_ENTRIES BE "
                     "INNER JOIN "
                     "PRICE_EXCEPTIONS AS PE "
                     "ON BE.BOOK_ID=PE.BOOK_ID "
                     f"AND BE.BOOK_ID={book_id}")
    price_exc = mycursor.fetchall()
    if len(price_exc) == 0:
        book_search = f"SELECT B.TITLE, A.AUTHOR_NAME, A.AUTHOR_SURNAME, B.EDITION, B.BOOK_TYPE, B.LOCATION," \
                      f" B.SECTION, B.LANGUAGE, PRICE_DETERMINATION({book_id}) " \
                      "FROM BOOKS AS B " \
                      "LEFT JOIN " \
                      "AUTHORS A " \
                      "ON B.ISBN=A.ISBN " \
                      "LEFT JOIN " \
                      "BOOK_ENTRIES BE " \
                      "ON B.ISBN=BE.ISBN " \
                      "LEFT JOIN " \
                      "TRANSACTIONS T " \
                      "ON BE.BOOK_ID=T.BOOK_ID " \
                      f"WHERE BE.BOOK_ID={book_id}"

    else:
        book_search = "SELECT B.TITLE, A.AUTHOR_NAME, A.AUTHOR_SURNAME, B.EDITION, B.BOOK_TYPE, B.LOCATION," \
                      " B.SECTION, B.LANGUAGE, PE.NEW_PRICE_IN_CENTS " \
                      "FROM BOOKS B " \
                      "LEFT JOIN " \
                      "AUTHORS A " \
                      "ON B.ISBN=A.ISBN " \
                      "LEFT JOIN " \
                      "BOOK_ENTRIES BE " \
                      "ON B.ISBN=BE.ISBN " \
                      "LEFT JOIN " \
                      "PRICE_EXCEPTIONS PE " \
                      "ON PE.BOOK_ID=BE.BOOK_ID " \
                      f"WHERE BE.BOOK_ID={book_id}"
    return book_search
