import mysql.connector
db = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="MyN3wP4ssw0rd!*")
mycursor = db.cursor()
class Guest:
    def __init__(self):
        a=0
    def search(self, author_name="", author_surname="", title=""):
        conditions = ""
        cor_sub = "T.PRICE=(SELECT MAX(TR.PRICE)" \
                  "         FROM TRANSACTIONS TR, BOOK_ENTRY BEN, BOOK BO" \
                  "         WHERE TR.BOOK_ID=BEN.BOOK_ID" \
                   "         AND BEN.ISBN=BO.ISBN" \
                   "         AND BO.ISBN=B.ISBN"
         if title == "" and author_name == "" and author_surname == "":
             conditions = "WHERE", cor_sub, ")"
         if title != "":
             cor_sub = cor_sub, \
                       "AND (BO.ISBN IN (SELECT ISBN FROM BOOKS" \
                       "                WHERE TITLE LIKE '%", title, "'" \
                       "                OR TITLE LIKE '", title, "%')" \
                       "OR BO.ISBN IN (SELECT ISBN FROM IF_TRANSLATED" \
                       "               WHERE UNTRANSLATED_TITLE LIKE '%", title, "'" \
                       "               OR UNTRANSLATED_TITLE LIKE '", title, "%'))"
             conditions = "WHERE B.TITLE LIKE '%", title, "'" \
                          "OR B.TITLE LIKE '", title, "%'" \
                          "OR IT.TITLE_UNTRANSLATED LIKE '%", title, "'" \
                          "OR IT.TITLE_UNTRANSLATED LIKE '", title, "%'" \
                          "AND", cor_sub, ")"
         if author_name != "" and author_surname == "":
             cor_sub = cor_sub, \
                       "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS" \
                       "                WHERE AUTHOR_NAME LIKE '%", author_name, "'" \
                       "                OR AUTHOR_NAME LIKE '", author_name, "%')"
             conditions = "WHERE A.AUTHOR_NAME LIKE '%", author_name, "'" \
                          "OR A.AUTHOR_NAME LIKE '", author_name, "%'" \
                          "AND", cor_sub, ")"
         if author_surname != "" and author_name == "":
             cor_sub = cor_sub, \
                       "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS" \
                       "                WHERE AUTHOR_SURNAME LIKE '%", author_surname, "'" \
                       "                OR AUTHOR_SURNAME LIKE '", author_surname, "%')"
             conditions = "WHERE A.AUTHOR_SURNAME LIKE '%", author_surname, "'" \
                          "OR A.AUTHOR_SURNAME LIKE '", author_surname, "%'" \
                          "AND", cor_sub, ")"
         if author_name != "" and author_surname != "":
             cor_sub = cor_sub, \
                       "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS" \
                       "                WHERE (AUTHOR_NAME LIKE '%", author_name, "'" \
                       "                OR AUTHOR_NAME LIKE '", author_name, "%')" \
                       "                AND (AUTHOR_SURNAME LIKE '%", author_surname, "'" \
                       "                OR AUTHOR_SURNAME LIKE '", author_surname, "%'))"
             conditions = "WHERE (A.AUTHOR_NAME LIKE '%", author_name, "'" \
                          "OR A.AUTHOR_NAME LIKE '", author_name, "%')" \
                          "AND (A.AUTHOR_SURNAME LIKE '%", author_surname, "'" \
                          "OR A.AUTHOR_SURNAME LIKE '", author_surname, "%')" \
                          "AND", cor_sub, ")"
         mycursor.execute("SELECT B.TITLE, A.AUTHOR_NAME, A.AUTHOR_SURNAME, B.LANGUAGE, B.GENRE, B.LOCATION, B.EDITION, B.BOOK_TYPE, T.PRICE, COUNT(BE.BOOK_ID)"
                          "FROM BOOK AS B"
                          "INNER JOIN"
                          "AUTHORS AS A"
                          "ON B.ISBN=A.ISBN"
                          "INNER JOIN"
                          "BOOK_ENTRY AS BE"
                          "ON B.ISBN=BE.ISBN"
                          "INNER JOIN"
                          "TRANSACTIONS AS T"
                          "ON BE.BOOK_ID=T.BOOK_ID"
                          "INNER JOIN"
                          "IF_TRANSLATED AS IT"
                          "ON IT.ISBN=B.ISBN",
                          conditions,
                          "GROUP BY B.ISBN")