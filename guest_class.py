class Guest:
    def __init__(self):
        a = 0
        
    def search(self, author_name="", author_surname="", title=""):
        conditions = ""
        cor_sub = "T.PRICE_IN_CENTS=(SELECT MIN(TR.PRICE_IN_CENTS) " \
                           "FROM TRANSACTIONS TR, BOOK_ENTRIES BEN, BOOKS BO " \
                           "WHERE TR.BOOK_ID=BEN.BOOK_ID " \
                           "AND BEN.ISBN=BO.ISBN " \
                           "AND BO.ISBN=B.ISBN "
        if title == "" and author_name == "" and author_surname == "":
            conditions = f"WHERE {cor_sub}) "
        if title != "":
            cor_sub = f"{cor_sub}" \
                      "AND (BO.ISBN IN (SELECT ISBN FROM BOOKS " \
                                      f"WHERE TITLE LIKE '%{title}' " \
                                      f"OR TITLE LIKE '{title}%') " \
                      "OR BO.ISBN IN (SELECT ISBN FROM IF_TRANSLATED " \
                                    f"WHERE TITLE_UNTRANSLATED LIKE '%{title}' " \
                                    f"OR TITLE_UNTRANSLATED LIKE '{title}%')) "
            conditions = f"WHERE B.TITLE LIKE '%{title}' " \
                         f"OR B.TITLE LIKE '{title}%' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '%{title}' " \
                         f"OR IT.TITLE_UNTRANSLATED LIKE '{title}%' " \
                         f"AND {cor_sub}) "
        if author_name != "" and author_surname == "":
            cor_sub = f"{cor_sub}" \
                      "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                                     f"WHERE AUTHOR_NAME LIKE '%{author_name}' " \
                                     f"OR AUTHOR_NAME LIKE '{author_name}%') "
            conditions = f"WHERE A.AUTHOR_NAME LIKE '%{author_name}' " \
                         f"OR A.AUTHOR_NAME LIKE '{author_name}%' " \
                         f"AND {cor_sub}) "
        if author_surname != "" and author_name == "":
            cor_sub = f"{cor_sub}" \
                      "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                                     f"WHERE AUTHOR_SURNAME LIKE '%{author_surname}' " \
                                     f"OR AUTHOR_SURNAME LIKE '{author_surname}%') "
            conditions = f"WHERE A.AUTHOR_SURNAME LIKE '%{author_surname}' " \
                         f"OR A.AUTHOR_SURNAME LIKE '{author_surname}%' " \
                         f"AND {cor_sub}) "
        if author_name != "" and author_surname != "":
            cor_sub = f"{cor_sub}" \
                      "AND BO.ISBN IN (SELECT ISBN FROM AUTHORS " \
                                     f"WHERE (AUTHOR_NAME LIKE '%{author_name}' " \
                                     f"OR AUTHOR_NAME LIKE '{author_name}%') " \
                                     f"AND (AUTHOR_SURNAME LIKE '%{author_surname}' " \
                                     f"OR AUTHOR_SURNAME LIKE '{author_surname}%')) "
            conditions = f"WHERE (A.AUTHOR_NAME LIKE '%{author_name}' " \
                                f"OR A.AUTHOR_NAME LIKE '{author_name}%') " \
                         f"AND (A.AUTHOR_SURNAME LIKE '%{author_surname}' " \
                              f"OR A.AUTHOR_SURNAME LIKE '{author_surname}%') " \
                         f"AND {cor_sub}) "
        query = "SELECT B.TITLE, A.AUTHOR_NAME, A.AUTHOR_SURNAME, B.LANGUAGE, B.GENRE, B.LOCATION, B.EDITION, B.BOOK_TYPE, T.PRICE_IN_CENTS, COUNT(BE.BOOK_ID) " \
                "FROM BOOKS B LEFT JOIN AUTHORS A " \
                "ON B.ISBN=A.ISBN " \
                "LEFT JOIN BOOK_ENTRIES BE " \
                "ON B.ISBN=BE.ISBN " \
                "LEFT JOIN TRANSACTIONS T " \
                "ON BE.BOOK_ID=T.BOOK_ID " \
                "LEFT JOIN IF_TRANSLATED IT " \
                "ON IT.ISBN=B.ISBN " \
                f"{conditions}" \
                "GROUP BY B.ISBN"
        return query

Test = Guest()
print(Test.search("", "", "It Ends"))
