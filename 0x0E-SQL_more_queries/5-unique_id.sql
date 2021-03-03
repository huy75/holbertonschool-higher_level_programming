-- creates the table unique_id on the MySQL server.
-- unique_id description
--    id INT with default value 1 and unique
--    name VARCHAR(256)
-- Script should not fail if table exists
CREATE TABLE IF NOT EXISTS `unique_id` (
       `id` INT UNIQUE DEFAULT 1,
       `name` VARCHAR(256)
);
