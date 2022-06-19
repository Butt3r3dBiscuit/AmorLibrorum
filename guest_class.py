import mysql.connector
db = mysql.connector.connect(
            host="localhost",
            user="guest",
            passwd="TheGu3stP4ssw0rd!*",
            database="AmorLibrorum")
cursor = db.cursor()

class Guest:
    def __init__(self):
        pass

    def search(self, search, type):
        conditions = ""
        or_isbn = ""
        if type != 0:
            or_isbn = f"OR B.ISBN LIKE '%{search}%'"
        if search != "":
            conditions = f"WHERE B.TITLE LIKE '%{search}%' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '%{search}%' " \
                         f"OR A.AUTHOR_NAME LIKE '%{search}%' " \
                         f"OR A.AUTHOR_SURNAME LIKE '%{search}%' " \
                         f"{or_isbn}"
        cursor.execute("SET sql_mode = ''")

        cursor.execute("SELECT B.ISBN, B.TITLE, IT.TITLE_UNTRANSLATED, A.AUTHOR_NAME, A.AUTHOR_SURNAME, IT.TRANSLATOR, B.EDITION, B.LANGUAGE, IT.TRANSLATED_FROM, B.GENRE, B.PUBLISHER, B.BOOK_TYPE, B.YEAR_PUBLISHED, B.PAGES, B.LOCATION, B.SECTION, PRICE_DETERMINATION(BE.BOOK_ID), COUNT(BE.BOOK_ID) "
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
        result = cursor.fetchall()
        return result
