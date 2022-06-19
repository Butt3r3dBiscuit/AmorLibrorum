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

    def search(self, search=""):
        conditions = ""
        cor_sub = "BE.BOOK_ID IN (SELECT BOEN.BOOK_ID " \
                              "FROM BOOK_ENTRIES BOEN, TRANSACTIONS TRA " \
                              "WHERE TRA.BOOK_ID=BOEN.BOOK_ID " \
                              "AND TRA.PRICE_IN_CENTS=(SELECT MIN(TR.PRICE_IN_CENTS) " \
                                                      "FROM TRANSACTIONS TR, BOOK_ENTRIES BEN, BOOKS BO " \
                                                      "WHERE TR.BOOK_ID=BEN.BOOK_ID " \
                                                      "AND BEN.ISBN=BO.ISBN " \
                                                      "AND BO.ISBN=B.ISBN "
        if search == "":
            conditions = f"WHERE {cor_sub})) "
        else:
            cor_sub = f"{cor_sub}" \
                      "AND ((BO.ISBN IN (SELECT ISBN FROM BOOKS " \
                      f"WHERE TITLE LIKE '%{search}%') " \
                      "OR BO.ISBN IN (SELECT ISBN FROM IF_TRANSLATED " \
                      f"WHERE TITLE_UNTRANSLATED LIKE '%{search}%'))) " \
                      "OR (BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                      f"WHERE AUTHOR_NAME LIKE '%{search}%')) " \
                      "OR (BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                      f"WHERE AUTHOR_SURNAME LIKE '%{search}%')) "
            conditions = f"WHERE B.TITLE LIKE '%{search}%' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '%{search}%' " \
                         f"OR A.AUTHOR_NAME LIKE '%{search}%' " \
                         f"OR A.AUTHOR_SURNAME LIKE '%{search}%' " \
                         f"AND {cor_sub})) "

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
                       "GROUP BY B.ISBN, PRICE_DETERMINATION(BE.BOOK_ID)")
        result = cursor.fetchall()
        return result
