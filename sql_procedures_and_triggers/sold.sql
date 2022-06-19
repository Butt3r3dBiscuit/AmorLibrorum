DELIMITER &&

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
END &&

DELIMITER ;