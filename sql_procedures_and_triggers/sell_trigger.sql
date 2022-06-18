DELIMITER $$

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

END $$

DELIMITER ;