-- Creates AddBonus procedure that inserts a correction.
-- If the project does not exist, it is created.

DELIMITER $$

CREATE PROCEDURE AddBonus (
    IN in_user_id INT,
    IN in_project_name VARCHAR(255),
    IN in_score INT
)
BEGIN
    DECLARE project_id INT;

    SELECT id INTO project_id
    FROM projects
    WHERE name = in_project_name
    LIMIT 1;

    IF project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (in_project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (in_user_id, project_id, in_score);
END$$

DELIMITER ;
