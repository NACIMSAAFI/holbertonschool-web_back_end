-- 8-index_my_names.sql
-- Create an index on the first letter of the name column in the names table

CREATE INDEX idx_name_first ON names (name(1));
