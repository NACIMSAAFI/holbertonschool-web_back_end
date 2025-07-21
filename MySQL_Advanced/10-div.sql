-- 10-div.sql
-- Create a function SafeDiv that returns a / b or 0 if b = 0

DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    RETURN IF(b = 0, 0, a / b);
END$$

DELIMITER ;
