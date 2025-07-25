-- 11-need_meeting.sql
-- Create a view need_meeting listing students with score < 80 and no recent meeting

CREATE OR REPLACE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
