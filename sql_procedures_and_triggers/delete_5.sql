DELIMITER &&

CREATE PROCEDURE cleann()
BEGIN
	DECLARE t_date date;
	DECLARE d_date date;
	SET t_date = (select current_date);
	SET d_date = DATEADD(t_date, -5);
    DELETE FROM TRANSACTIONS WHERE Trans_Date<=t_date AND sold(book_id)=1;
END &&

DELIMITER ;