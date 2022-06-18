DELIMITER &&

CREATE PROCEDURE return_book(ID varchar(13), emp_id INT)
BEGIN
	DECLARE t_date date;
	DECLARE Price int;
	SET Price = -(select price_determination(ID));
	SET t_date = (select current_date);
	INSERT INTO transactions(Book_ID, Employee_ID, Trans_Date, Price_in_cents) values (ID, emp_id, t_date, Price);
END &&

DELIMITER ;