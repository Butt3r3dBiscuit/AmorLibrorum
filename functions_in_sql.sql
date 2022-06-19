DROP USER if exists 'margje@amorlibrorum.boek'@'localhost';
DROP USER if exists 'frank@amorlibrorum.boek'@'localhost';
DROP USER if exists 'guest'@'localhost';

CREATE USER 'margje@amorlibrorum.boek'@'localhost' IDENTIFIED BY 'NotAn0therqwer!ypassword';
FLUSH PRIVILEGES;
CREATE USER 'frank@amorlibrorum.boek'@'localhost' IDENTIFIED BY 'An0!herqwertyp4ssword';
FLUSH PRIVILEGES;

CREATE USER 'guest'@'localhost' IDENTIFIED BY 'TheGu3stP4ssw0rd!*';
FLUSH PRIVILEGES;

grant all privileges on AmorLibrorum.* to 'margje@amorlibrorum.boek'@'localhost';
grant all privileges on AmorLibrorum.* to 'frank@amorlibrorum.boek'@'localhost';

grant create user on *.* to 'margje@amorlibrorum.boek'@'localhost' with grant option;
grant create user on *.* to 'frank@amorlibrorum.boek'@'localhost' with grant option;

grant reload on *.* to 'frank@amorlibrorum.boek'@'localhost' with grant option;
grant reload on *.* to 'margje@amorlibrorum.boek'@'localhost' with grant option;


GRANT SELECT ON AmorLibrorum.Books TO 'guest'@'localhost';
GRANT SELECT ON AmorLibrorum.Book_entries TO 'guest'@'localhost';
GRANT SELECT ON AmorLibrorum.Transactions TO 'guest'@'localhost';
GRANT SELECT ON AmorLibrorum.Authors TO 'guest'@'localhost';
GRANT SELECT ON AmorLibrorum.if_translated TO 'guest'@'localhost';




drop function if exists price_determination;

CREATE function price_determination(book_id_given int)
    returns VARCHAR(20)
    Deterministic
    begin
        declare price int;
        declare margin_var float;
        declare buying_price int;
        declare return_string varchar(20);
        select new_price_in_cents into price from Price_exceptions where Book_ID=book_id_given;
        if price IS NULL THEN
            select margin into margin_var from variables;

            select price_in_cents into buying_price from transactions where book_id=book_id_given 
            and transaction_id=(select min(transaction_id) from transactions where book_id=book_id_given);
            
            set price = -buying_price * margin_var;
        end if;
        set return_string = concat(price);
    RETURN return_string;
END;

GRANT EXECUTE on FUNCTION `Amorlibrorum`.`price_determination` to 'guest'@'localhost';
-- drop trigger if exists ISBN_cz;
-- create handler that checks while adding boook to book_entries if the ISBN exists already in the books
-- create trigger ISBN_cz before insert on Book_entries
--    for each row

-- Transaction procedures and trigger
DROP TRIGGER IF EXISTS before_sold;
CREATE TRIGGER before_sold
BEFORE INSERT
ON transactions FOR EACH ROW
BEGIN
    DECLARE boughtcount INT;
    DEClARE soldcount INT;
    DECLARE message_text varchar(255);

    SELECT COUNT(*) 
    INTO boughtcount
    FROM transactions WHERE Price_in_cents<0 and book_id=NEW.book_id;
    
    SELECT COUNT(*) 
    INTO soldcount
    FROM transactions WHERE Price_in_cents>=0 and book_id=NEW.book_id;

    IF (boughtcount<=soldcount) AND (NEW.Price_in_cents>0) THEN
        signal sqlstate '45000' SET message_text = 'Book cannot be sold more times than it is bought >:(';
    END IF; 
END;

DROP PROCEDURE IF EXISTS sell;
CREATE PROCEDURE sell(ID varchar(13), emp_id INT)
BEGIN
	DECLARE t_date date;
	DECLARE Price int;
	SET Price = (select price_determination(ID));
	SET t_date = (select current_date);
	INSERT INTO transactions(Book_ID, Employee_ID, Trans_Date, Price_in_cents) values (ID, emp_id, t_date, Price);
END;

DROP PROCEDURE IF EXISTS return_booK;
CREATE PROCEDURE return_book(ID varchar(13), emp_id INT)
BEGIN
	DECLARE t_date date;
	DECLARE Price int;
	SET Price = -1*(select price_in_cents from transactions where transaction_id=(select max(transaction_id) from transactions where book_id=ID));
	SET t_date = (select current_date);
	INSERT INTO transactions(Book_ID, Employee_ID, Trans_Date, Price_in_cents) values (ID, emp_id, t_date, Price);
END;

-- determines wether a book has been sold
CREATE FUNCTION sold(ID varchar(13))
RETURNS smallint
DETERMINISTIC
BEGIN
    DECLARE boughtcount INT;
    DEClARE soldcount INT;
    DECLARE bool smallint;

    SELECT COUNT(*) 
    INTO boughtcount
    FROM transactions WHERE Price_in_cents<0 and book_id=ID;

    SELECT COUNT(*) 
    INTO soldcount
    FROM transactions WHERE Price_in_cents>=0 and book_id=ID;

    SET bool = 1;
    IF boughtcount>soldcount THEN
        SET bool = 0;
    END IF;
RETURN bool;
END;

-- deletes sold book records in transactions older than 5 years
CREATE PROCEDURE clean()
BEGIN
	DECLARE t_date date;
	SET t_date = (select current_date);
    DELETE FROM TRANSACTIONS WHERE Trans_Date<=t_date AND sold(book_id)=1;
END;