-- 9-index_name_score.sql
-- Create index on first letter of name and score
CREATE INDEX idx_name_score ON names (name(1), score);
