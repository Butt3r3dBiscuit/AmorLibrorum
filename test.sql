CREATE TABLE `Book` (
  `ISBN` varchar(17) NOT NULL,
  `Original_title` varchar(50) NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Author(s)` varchar(50) NOT NULL,
  `publisher` varchar(20) NOT NULL,
  `publisher(year)` int(4) NOT NULL,
  `pages` int(5) NOT NULL,
  `language` varchar(30) NOT NULL,
  `translator` varchar(30) NOT NULL,
  `edition` int(2) NOT NULL,
  `dimensions/type` ENUM("paperback","hardcover") NOT NULL,
  `location` char(2) NOT NULL,
  `section` int(2) NOT NULL,
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

CREATE TABLE `Transactions` (
  `Transaction_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Book_ID(local)` int(11) NOT NULL,
  `Employee_ID` int(4) NOT NULL,
  `Date` DATE NOT NULL,
  `Price` int(4) NOT NULL,
  `Type` ENUM("Buy","Sell") NOT NULL,
  PRIMARY KEY (`Transaction_ID`),
  FOREIGN KEY (`Employee_ID`) REFERENCES `Employees`(`Employee_ID`),
  KEY `PK_FK` (`Book_ID(local)`, `Employee_ID`)
);

CREATE TABLE `Book_entry` (
  `Book_ID(local)` int(11) NOT NULL AUTO_INCREMENT,
  `copy_of(ISBNM)` varchar(17) NOT NULL,
  `status` ENUM("used","just like new","new") NOT NULL,
  PRIMARY KEY (`Book_ID(local)`),
  FOREIGN KEY (`copy_of(ISBNM)`) REFERENCES `Book`(`ISBN`),
  FOREIGN KEY (`Book_ID(local)`) REFERENCES `Transactions`(`Book_ID(local)`),
  KEY `PK_FK` (`copy_of(ISBNM)`)
);
