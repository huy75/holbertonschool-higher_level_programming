-- Creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- creates a table called states.
-- states description
--     id INT unique, auto generated, can't be null and is primary key
--     name VARCHAR(256) can't be null
-- Should not fail if database or states exists
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
       name VARCHAR(256) NOT NULL
);
