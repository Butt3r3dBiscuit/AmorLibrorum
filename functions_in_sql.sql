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
            
            drop table if exists temp_table;
            create table temp_table
            as select Transaction_ID, price_in_cents as temp_table from transactions where book_id=book_id_given;
            select price_in_cents into buying_price from temp_table where transaction_id=(select min(transaction_id) from temp_table);
            drop table temp_table;

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
