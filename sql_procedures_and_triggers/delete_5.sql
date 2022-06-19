DELIMITER &&

CREATE PROCEDURE clean()
BEGIN
	DECLARE t_date date;
	SET t_date = (select current_date);
    DELETE FROM TRANSACTIONS WHERE Trans_Date<=t_date AND sold(book_id)=1;
END &&

DELIMITER ;