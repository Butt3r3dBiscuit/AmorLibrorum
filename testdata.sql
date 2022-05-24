start transaction;

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (9781501110368, "It Ends with Us", "Atria", "2016", "384", "English", null, "paperback", "78", "58", "College Romance, Fiction");
INSERT INTO `books` VALUES (9780679805274, "Oh, the Places You'll Go!","Random House Books for Young Readers","1990", "56", "English", null, null, "77", "78", "Children Classics");
INSERT INTO `books` VALUES (9781476797090, "Phil: The Rip-Roaring \(and Unauthorized!\) Biography of Golf's Most Colorful Superstar","Avid Reader Press / Simon & Schuster","2022", "256", "English", null, "hardcover", "747", "178", "Biographies");
INSERT INTO `books` VALUES (9780735211292, "Atomic Habits: An Easy & Proven Way to Build Good Habits & Break Bad Ones","Avery","2018", "320", "English", null, "hardcover", "11", "7", "Psychology");
INSERT INTO `books` VALUES (9781538724731, "Verity","Grand Central Publishing","2021", "336", "English", null, "paperback", "74", "578", "Suspense, Thriller");
INSERT INTO `books` VALUES (9781501161938, "The Seven Husbands of Evelyn Hugo: A Novel","Washington Square Press","2018", "400", "English", null, "paperback", "2", "718", "Holiday Romance");
INSERT INTO `books` VALUES (9780593334833, "Book Lovers","Berkley","2022", "400", "English", null, "paperback", "17", "18", "Sisters Fiction, Romantic Comedy");
INSERT INTO `books` VALUES (9780735219109, "Where the Crawdads Sing","Penguin Publishing Group","2021", "400", "English", null, "paperback", "7", "7", "Fiction");
INSERT INTO `books` VALUES (9786094872082, "Priesaikos laužytojas", "BALTO leidybos namai", "2021", "320", "Lithuanian", 1, "hardcover", "2", "2", "Thriller, Suspense, Romantic");

/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;



LOCK TABLES `book_entries` WRITE;
/*!40000 ALTER TABLE `book_entries` DISABLE KEYS */;
INSERT INTO `book_entries` VALUES (1, 9781501110368, null);
INSERT INTO `book_entries` VALUES (2, 9781501110368, null);
INSERT INTO `book_entries` VALUES (3, 9781501110368, null);
INSERT INTO `book_entries` VALUES (4, 9781501110368, null);
INSERT INTO `book_entries` VALUES (5, 9781501110368, null);
INSERT INTO `book_entries` VALUES (6, 9781501110368, null);
INSERT INTO `book_entries` VALUES (7, 9781501110368, null);
INSERT INTO `book_entries` VALUES (8, 9781501110368, null);
INSERT INTO `book_entries` VALUES (9, 9781501110368, null);
INSERT INTO `book_entries` VALUES (10, 9780679805274, null);
INSERT INTO `book_entries` VALUES (11, 9781476797090, null);
INSERT INTO `book_entries` VALUES (12, 9780735211292, null);
INSERT INTO `book_entries` VALUES (13, 9781538724731, null);
INSERT INTO `book_entries` VALUES (14, 9781501161938, null);
INSERT INTO `book_entries` VALUES (15, 9780593334833, null);
INSERT INTO `book_entries` VALUES (16, 9780735219109, null);
INSERT INTO `book_entries` VALUES (17, 9780735219109, null);
INSERT INTO `book_entries` VALUES (18, 9780735219109, null);
INSERT INTO `book_entries` VALUES (19, 9781476797090, null);
INSERT INTO `book_entries` VALUES (20, 9781476797090, null);
INSERT INTO `book_entries` VALUES (21, 9786094872082, null);

/*!40000 ALTER TABLE `book_entries` ENABLE KEYS */;
UNLOCK TABLES;



LOCK TABLES `authors` WRITE;
/*!40000 ALTER TABLE `authors` DISABLE KEYS */;
INSERT INTO `authors` VALUES (9781501110368, "Colleen", "Hoover");
INSERT INTO `authors` VALUES (9780679805274, "Theodor", "Seuss Geisel");
INSERT INTO `authors` VALUES (9781476797090, "Alan", "Shipnuck");
INSERT INTO `authors` VALUES (9780735211292, "James", "Clear");
INSERT INTO `authors` VALUES (9781538724731, "Colleen", "Hoover");
INSERT INTO `authors` VALUES (9781501161938, "Taylor", "Jenkins Reid");
INSERT INTO `authors` VALUES (9780593334833, "Emily", "Henry");
INSERT INTO `authors` VALUES (9780735219109, "Delia", "Owens");
INSERT INTO `authors` VALUES (9786094872082, "Leena", "Lehtolainen");

/*!40000 ALTER TABLE `authors` ENABLE KEYS */;
UNLOCK TABLES;



LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1, "Margje", "Penning", "Manager", "NotAn0therqwertypassword", "margje@amorlibrorum.boek");
INSERT INTO `employees` VALUES (2, "Frank", "Brandse", "Manager", "An0therqwertyp4ssword", "frank@amorlibrorum.boek");
INSERT INTO `employees` VALUES (3, "Casual", "Employee", "Staff", "YetAn0therqwertyp4ssword", "casual@amorlibrorum.boek");

/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;



LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
INSERT INTO `transactions` VALUES (1, 1, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (2, 2, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (3, 3, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (4, 4, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (5, 5, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (6, 6, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (7, 7, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (8, 8, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (9, 9, 1, "2017-06-15", -1081);
INSERT INTO `transactions` VALUES (10, 10, 1, "2017-06-15", -898);
INSERT INTO `transactions` VALUES (11, 11, 2, "2017-06-16", -2499);
INSERT INTO `transactions` VALUES (12, 12, 2, "2017-06-16", -1198);
INSERT INTO `transactions` VALUES (13, 13, 2, "2017-06-16", -1126);
INSERT INTO `transactions` VALUES (14, 14, 2, "2017-06-16", -942);
INSERT INTO `transactions` VALUES (15, 15, 2, "2017-06-16", -1222);
INSERT INTO `transactions` VALUES (16, 16, 2, "2017-06-16", -998);
INSERT INTO `transactions` VALUES (17, 17, 2, "2017-06-16", -998);
INSERT INTO `transactions` VALUES (18, 18, 2, "2017-06-16", -998);
INSERT INTO `transactions` VALUES (19, 19, 2, "2017-06-16", -2499);
INSERT INTO `transactions` VALUES (20, 20, 2, "2017-06-16", -2499);
INSERT INTO `transactions` VALUES (21, 21, 2, "2021-05-05", -739);
INSERT INTO `transactions` VALUES (22, 20, 1, "2021-05-06", 2499);

/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;



LOCK TABLES `if_translated` WRITE;
/*!40000 ALTER TABLE `if_translated` DISABLE KEYS */;
INSERT INTO `if_translated` VALUES (9786094872082, "Aida Krilavičienė", "Valapatto", "Finnish");
INSERT INTO `if_translated` VALUES (9786094872082, "LT: 11ąčęėįšųūž Krilavičienė", "VRL: ðøåælöæøåþ", "intl: áóòe~eã~uõíC");

/*!40000 ALTER TABLE `if_translated` ENABLE KEYS */;
UNLOCK TABLES;




LOCK TABLES `Price_exceptions` WRITE;
/*!40000 ALTER TABLE `Price_exceptions` DISABLE KEYS */;
INSERT INTO `Price_exceptions` VALUES (21, 850, "Book was damaged by a customer");
-- INSERT INTO `Price_exceptions` VALUES (20, 900, "test");

/*!40000 ALTER TABLE `Price_exceptions` ENABLE KEYS */;
UNLOCK TABLES;

LOCK TABLES `variables` WRITE;
/*!40000 ALTER TABLE `variables` DISABLE KEYS */;
INSERT INTO `variables` VALUES (1.21);

/*!40000 ALTER TABLE `variables` ENABLE KEYS */;
UNLOCK TABLES;
