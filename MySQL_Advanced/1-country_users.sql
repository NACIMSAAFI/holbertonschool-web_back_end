-- 1-country_users.sql
-- SQL script to create a users table with unique email and country

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country EnUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
