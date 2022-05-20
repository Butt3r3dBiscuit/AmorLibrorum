DELIMITER $$

CREATE function price_determination(book_id_given int)
    returns int
    Deterministic
    begin
        declare price int;
        declare margin_var int;
        declare buying_price int;
        select new_price_in_cents into price from Price_exceptions where Book_ID=book_id_given;
        if price IS NULL THEN
            select margin into margin_var from variables;
            select Price_in_cents into buying_price from Transactions where Book_ID=book_id_given;
            SET price = - buying_price * margin_var;
        end if;
    RETURN price;
END$$

DELIMITER ;