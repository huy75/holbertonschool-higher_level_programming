-- Creates the MySQL server user user_0d_1
-- Password should be user_0d_1_pwd
-- If user already exists, script should not fail
DROP USER IF EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
--  grant all privileges on your MySQL server
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
