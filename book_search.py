import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MyN3wP4ssw0rd!*",
    database="AmorLibrorum")
mycursor = db.cursor()
#

def book_search(book_id, db):
    try:
        mycursor.execute("SET sql_mode = ''")
        mycursor.execute(
            "SELECT B.ISBN, PE.COMMENT, B.TITLE, IT.TITLE_UNTRANSLATED, A.AUTHOR_NAME, A.AUTHOR_SURNAME, IT.TRANSLATOR, B.EDITION, B.LANGUAGE, IT.TRANSLATED_FROM, B.GENRE, B.PUBLISHER, B.BOOK_TYPE, B.YEAR_PUBLISHED, B.PAGES, B.LOCATION, B.SECTION, PRICE_DETERMINATION(BE.BOOK_ID), COUNT(BE.BOOK_ID) "
            "FROM BOOKS B LEFT JOIN AUTHORS A "
            "ON B.ISBN=A.ISBN "
            "LEFT JOIN BOOK_ENTRIES BE "
            "ON B.ISBN=BE.ISBN "
            "LEFT JOIN TRANSACTIONS T "
            "ON BE.BOOK_ID=T.BOOK_ID "
            "LEFT JOIN IF_TRANSLATED IT "
            "ON IT.ISBN=B.ISBN "
            "LEFT JOIN PRICE_EXCEPTIONS PE "
            "ON PE.BOOK_ID=BE.BOOK_ID "
            f"WHERE BE.BOOK_ID={book_id} "
            "AND PRICE_DETERMINATION(BE.BOOK_ID)>0 "
            "GROUP BY B.ISBN, PRICE_DETERMINATION(BE.BOOK_ID) "
            "ORDER BY B.ISBN, PRICE_DETERMINATION(BE.BOOK_ID)")
        result = mycursor.fetchall()
        return result
    except Exception as e:
        return e.errno
