-- 4-store.sql
-- SQL script to create a trigger that decreases the quantity of an item after a new order is inserted

DELIMITER $$

CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END$$

DELIMITER ;
