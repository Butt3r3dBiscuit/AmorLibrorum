drop function if exists price_determination;

CREATE function price_determination(book_id_given int)
    returns VARCHAR(20)
    Deterministic
    begin
        declare price int;
        declare margin_var float;
        declare buying_price int;
        declare counting_rows int;
        declare return_string varchar(20);
        select count(Book_ID) into counting_rows from Transactions where Book_ID=book_id_given;
        if counting_rows=1 THEN
            if price IS NULL THEN
                select margin into margin_var from variables;
                select Price_in_cents into buying_price from Transactions where Book_ID=book_id_given;
                SET price = -buying_price * margin_var;
                set return_string = concat(price);
            elseif price is not NULL then
                select new_price_in_cents into price from Price_exceptions where Book_ID=book_id_given;
                set return_string = concat(price);
            end if;
        elseif counting_rows=2 THEN
            set return_string= 'already sold lol';
        end if;
    RETURN return_string;
END;

-- drop trigger if exists ISBN_cz;

-- create handler that checks while adding boook to book_entries if the ISBN exists already in the books
-- create trigger ISBN_cz before insert on Book_entries
--    for each row
