CREATE TABLE `Book` (
  `ISBN` varchar(17),
  `Original title` varchar(50),
  `Title` varchar(50),
  `Author(s)` varchar(50),
  `publisher` varchar(20),
  `publisher(year)` int(4),
  `pages` int(5),
  `language` varchar(30),
  `translator` varchar(30),
  `edition` int(2),
  `dimensions, type` ENUM("paperback","hardcover"),
  `location` char(2),
  `section` int(2),
  PRIMARY KEY (`ISBN`)
);

CREATE TABLE `Book_entry` (
  `Book ID (local)` int(11) NOT NULL AUTO_INCREMENT,
  `copy of (ISBNM)` varchar(17),
  `status` ENUM("used","just like new","new"),
  PRIMARY KEY (`Book ID (local)`),
  FOREIGN KEY (`copy of (ISBNM)`) REFERENCES `Book`(`ISBN`),
  KEY `PK_FK` (`copy of (ISBNM)`)
);

