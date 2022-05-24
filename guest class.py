class Guest:
    def __init__(self):
        a = 0
        
    def search(self, author_name="", author_surname="", title=""):
        conditions = ""
        cor_sub = "T.PRICE_IN_CENTS=(SELECT MAX(TR.PRICE_IN_CENTS) " \
                           "FROM TRANSACTIONS TR, BOOK_ENTRIES BEN, BOOKS BO " \
                           "WHERE TR.BOOK_ID=BEN.BOOK_ID " \
                           "AND BEN.ISBN=BO.ISBN " \
                           "AND BO.ISBN=B.ISBN "
        if title == "" and author_name == "" and author_surname == "":
            conditions = "WHERE " + cor_sub + ") "
        if title != "":
            cor_sub = cor_sub + \
                      "AND (BO.ISBN IN (SELECT ISBN FROM BOOKS " \
                                       "WHERE TITLE LIKE '%" + title + "' " \
                                       "OR TITLE LIKE '" + title + "%') " \
                      "OR BO.ISBN IN (SELECT ISBN FROM IF_TRANSLATED " \
                                     "WHERE TITLE_UNTRANSLATED LIKE '% " + title + "' " \
                                     "OR TITLE_UNTRANSLATED LIKE ' " + title + "%')) "
            conditions = "WHERE B.TITLE LIKE '%" + title + "' " \
                         "OR B.TITLE LIKE '" + title + "%' " \
                         "OR IT.TITLE_UNTRANSLATED LIKE '%" + title + "' " \
                         "OR IT.TITLE_UNTRANSLATED LIKE '" + title + "%' " \
                         "AND " + cor_sub + ") "
        if author_name != "" and author_surname == "":
            cor_sub = cor_sub + \
                      "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                                      "WHERE AUTHOR_NAME LIKE '%" + author_name + "' " \
                                      "OR AUTHOR_NAME LIKE '" + author_name + "%') "
            conditions = "WHERE A.AUTHOR_NAME LIKE '%" + author_name + "' " \
                         "OR A.AUTHOR_NAME LIKE '" + author_name + "%' " \
                         "AND " + cor_sub + ") "
        if author_surname != "" and author_name == "":
            cor_sub = cor_sub + \
                      "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                                      "WHERE AUTHOR_SURNAME LIKE '%" + author_surname + "' " \
                                      "OR AUTHOR_SURNAME LIKE '" + author_surname + "%') "
            conditions = "WHERE A.AUTHOR_SURNAME LIKE '%" + author_surname + "' " \
                         "OR A.AUTHOR_SURNAME LIKE '" + author_surname + "%' " \
                         "AND " + cor_sub + ") "
        if author_name != "" and author_surname != "":
            cor_sub = cor_sub + \
                      "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                                      "WHERE (AUTHOR_NAME LIKE '%" + author_surname + "' " \
                                      "OR AUTHOR_NAME LIKE '" + author_surname + "%') " \
                                      "AND (AUTHOR_SURNAME LIKE '%" + author_surname + "' " \
                                      "OR AUTHOR_SURNAME LIKE '" + author_surname + "%')) "
            conditions = "WHERE (A.AUTHOR_NAME LIKE '%" + author_name + "' " \
                                "OR A.AUTHOR_NAME LIKE '" + author_name + "%') " \
                         "AND (A.AUTHOR_SURNAME LIKE '%" + author_surname + "' " \
                              "OR A.AUTHOR_SURNAME LIKE '" + author_surname + "%') " \
                         "AND " + cor_sub + ") "
        query = "SELECT B.TITLE, A.AUTHOR_NAME, A.AUTHOR_SURNAME, B.LANGUAGE, B.GENRE, B.LOCATION, B.EDITION, B.BOOK_TYPE, T.PRICE_IN_CENTS, COUNT(BE.BOOK_ID) " \
                "FROM BOOKS B LEFT JOIN AUTHORS A " \
                "ON B.ISBN=A.ISBN " \
                "LEFT JOIN BOOK_ENTRIES BE " \
                "ON B.ISBN=BE.ISBN " \
                "LEFT JOIN TRANSACTIONS T " \
                "ON BE.BOOK_ID=T.BOOK_ID " \
                "LEFT JOIN IF_TRANSLATED IT " \
                "ON IT.ISBN=B.ISBN " \
                + conditions + \
                "GROUP BY B.ISBN"
        return query

Test = Guest()
print(Test.search("", "", "It Ends"))
