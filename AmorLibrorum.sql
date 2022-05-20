CREATE TABLE `Books` (
  `ISBN` varchar(13) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `publisher` varchar(20) NOT NULL,
  `year_published` int NOT NULL,
  `pages` int NOT NULL,
  `language` varchar(30) NOT NULL,
  `edition` int,
  `book_type` ENUM("paperback","hardcover"),
  `location` int NOT NULL,
  `section` int NOT NULL,
  `Genre` varchar(30),
  PRIMARY KEY (`ISBN`)
);

CREATE TABLE `Book_entries` (
  `Book_ID` int NOT NULL AUTO_INCREMENT,
  `ISBN` varchar(17) NOT NULL,
  `status/comment` varchar(100),
  PRIMARY KEY (`Book_ID`),
  FOREIGN KEY (`ISBN`) REFERENCES `Books`(`ISBN`)
);

CREATE TABLE `Price_exceptions` (
  `Book_ID` int NOT NULL,
  `new_price_in_cents` int,
  `comment` varchar(30),
  FOREIGN KEY (`Book_ID`) REFERENCES `Book_entries`(`Book_ID`)
);

CREATE TABLE `if_translated` (
  `ISBN` varchar(13) NOT NULL,
  `translator` varchar(50) NOT NULL,
  `Title_untranslated` varchar(50),
  `translated_from` varchar(20) NOT NULL,
  FOREIGN KEY (`ISBN`) REFERENCES `Books`(`ISBN`)
);

CREATE TABLE `Authors` (
  `ISBN` int NOT NULL,
  `author_name` varchar(50),
  `author_surname` varchar(50)
);

CREATE TABLE `Employees` (
  `Employee_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `position` ENUM("Staff","Manager") NOT NULL,
  `Password` varchar(50) NOT NULL,
  `email` varchar(100),
  PRIMARY KEY (`Employee_ID`)
);

CREATE TABLE `Transactions` (
  `Transaction_ID` int NOT NULL AUTO_INCREMENT,
  `Book_ID(local)` int NOT NULL,
  `Employee_ID` int NOT NULL,
  `Date` DATE NOT NULL,
  `price_in_cents` int NOT NULL,
  PRIMARY KEY (`Transaction_ID`),
  FOREIGN KEY (`Employee_ID`) REFERENCES `Employees`(`Employee_ID`),
  FOREIGN KEY (`Book_ID(local)`) REFERENCES `Book_entries`(`Book_ID`)
);

CREATE TABLE `variables` (
  `margin` int
);

