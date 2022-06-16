import mysql.connector
db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="MyN3wP4ssw0rd!*",
            database="AmorLibrorum")
cursor = db.cursor()

class Guest:
    def __init__(self):
        pass

    def search(self, search=""):
        conditions = ""
        cor_sub = "T.PRICE_IN_CENTS=(SELECT MIN(TR.PRICE_IN_CENTS) " \
                           "FROM TRANSACTIONS TR, BOOK_ENTRIES BEN, BOOKS BO " \
                           "WHERE TR.BOOK_ID=BEN.BOOK_ID " \
                           "AND BEN.ISBN=BO.ISBN " \
                           "AND BO.ISBN=B.ISBN "
        if search == "":
            conditions = f"WHERE {cor_sub}) "
        else:
            cor_sub = f"{cor_sub}" \
                      "AND ((BO.ISBN IN (SELECT ISBN FROM BOOKS " \
                      f"WHERE TITLE LIKE '%{search}' " \
                      f"OR TITLE LIKE '{search}%') " \
                      "OR BO.ISBN IN (SELECT ISBN FROM IF_TRANSLATED " \
                      f"WHERE TITLE_UNTRANSLATED LIKE '%{search}' " \
                      f"OR TITLE_UNTRANSLATED LIKE '{search}%'))) " \
                      "OR (BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                      f"WHERE AUTHOR_NAME LIKE '%{search}' " \
                      f"OR AUTHOR_NAME LIKE '{search}%')) " \
                      "OR (BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                      f"WHERE AUTHOR_SURNAME LIKE '%{search}' " \
                      f"OR AUTHOR_SURNAME LIKE '{search}%')) "
            conditions = f"WHERE (B.TITLE LIKE '%{search}' " \
                         f"OR B.TITLE LIKE '{search}%' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '%{search}' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '{search}%') " \
                         f"OR (A.AUTHOR_NAME LIKE '%{search}' " \
                         f"OR A.AUTHOR_NAME LIKE '{search}%') " \
                         f"OR (A.AUTHOR_SURNAME LIKE '%{search}' " \
                         f"OR A.AUTHOR_SURNAME LIKE '{search}%') " \
                         f"AND {cor_sub}) "

        cursor.execute("SELECT B.TITLE, A.AUTHOR_NAME, A.AUTHOR_SURNAME, B.LANGUAGE, B.GENRE, B.LOCATION, B.EDITION, B.BOOK_TYPE, T.PRICE_IN_CENTS, COUNT(BE.BOOK_ID) " \
                       "FROM BOOKS B LEFT JOIN AUTHORS A " 
                       "ON B.ISBN=A.ISBN " 
                       "LEFT JOIN BOOK_ENTRIES BE " 
                       "ON B.ISBN=BE.ISBN " 
                       "LEFT JOIN TRANSACTIONS T "
                       "ON BE.BOOK_ID=T.BOOK_ID " 
                       "LEFT JOIN IF_TRANSLATED IT " 
                       "ON IT.ISBN=B.ISBN " 
                       f"{conditions}" 
                       "GROUP BY B.ISBN")
        result = cursor.fetchall()
        return result
