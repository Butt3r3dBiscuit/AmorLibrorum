CREATE TABLE `Book` (
  `ISBN` varchar(17) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Title_untranslated` varchar(50),
  `Author(s)` varchar(100) NOT NULL,
  `publisher` varchar(20) NOT NULL,
  `published(year)` int(4) NOT NULL,
  `pages` int(5) NOT NULL,
  `language` varchar(30) NOT NULL,
  `translator` varchar(30),
  `edition` int(2) ,
  `book_type` ENUM("paperback","hardcover"),
  `location` int(3) NOT NULL,
  `section` int(3) NOT NULL,
  PRIMARY KEY (`ISBN`)
);

CREATE TABLE `Employees` (
  `Employee_ID` int(4) NOT NULL AUTO_INCREMENT,
  `Name` varchar(50) NOT NULL,
  `Surname` varchar(50) NOT NULL,
  `position` ENUM("Staff","Manager") NOT NULL,
  `Password` varchar(50) NOT NULL,
  PRIMARY KEY (`Employee_ID`)
);

CREATE TABLE `Book_entry` (
  `Book_ID` int(11) NOT NULL AUTO_INCREMENT,
  `copy_of(ISBN)` varchar(17) NOT NULL,
  `status` ENUM("used","just like new","new") DEFAULT "new",
  PRIMARY KEY (`Book_ID`),
  FOREIGN KEY (`copy_of(ISBN)`) REFERENCES `Book`(`ISBN`)
);

CREATE TABLE `Transactions` (
  `Transaction_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Book_ID(local)` int(11) NOT NULL,
  `Employee_ID` int(4) NOT NULL,
  `Date` DATE NOT NULL,
  `Price` int(4) NOT NULL,
  PRIMARY KEY (`Transaction_ID`),
  FOREIGN KEY (`Book_ID(local)`) REFERENCES `Employees`(`Employee_ID`),
  FOREIGN KEY (`Transaction_ID`) REFERENCES `Book_entry`(`Book_ID`)
);

insert into book (ISBN, Title, Author(s), publisher, published(year), pages, language, location, section) values ()