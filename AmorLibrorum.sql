CREATE TABLE `Books` (
  `ISBN` varchar(13) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `year_published` int NOT NULL,
  `pages` int NOT NULL,
  `language` varchar(30) NOT NULL,
  `edition` int,
  `book_type` ENUM("Paperback","Hardcover"),
  `location` varchar(2) NOT NULL,
  `section` int NOT NULL,
  `Genre` varchar(50),
  PRIMARY KEY (`ISBN`)
);

CREATE TABLE `Book_entries` (
  `Book_ID` int NOT NULL AUTO_INCREMENT,
  `ISBN` varchar(13) NOT NULL,
  `status_comment` varchar(100),
  PRIMARY KEY (`Book_ID`),
  FOREIGN KEY (`ISBN`) REFERENCES `Books`(`ISBN`)
);

CREATE TABLE `Price_exceptions` (
  `Book_ID` int NOT NULL,
  `new_price_in_cents` int,
  `Comment` varchar(100),
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
  `ISBN` varchar(13) NOT NULL,
  `author_name` varchar(50),
  `author_surname` varchar(50)
);

CREATE TABLE `Employees` (
  `Employee_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `position` ENUM("Staff","Manager") NOT NULL,
  `email` varchar(100) NOT NULL,
  PRIMARY KEY (`Employee_ID`)
);

CREATE TABLE `Transactions` (
  `Transaction_ID` int NOT NULL AUTO_INCREMENT,
  `Book_ID` int NOT NULL,
  `Employee_ID` int NOT NULL,
  `Trans_Date` DATE NOT NULL,
  `Price_in_cents` int NOT NULL,
  PRIMARY KEY (`Transaction_ID`),
  FOREIGN KEY (`Employee_ID`) REFERENCES `Employees`(`Employee_ID`),
  FOREIGN KEY (`Book_ID`) REFERENCES `Book_entries`(`Book_ID`)
);

CREATE TABLE `variables` (
  `margin` float(4,3)
);

