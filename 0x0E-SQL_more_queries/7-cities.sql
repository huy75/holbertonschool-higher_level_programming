-- Creates the database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
-- cities description:
--     id INT unique, auto generated, cant be null and is a primary key
--     state_id INT, not null and must be a FOREIGN KEY that references id of states
--     name VARCHAR(256) cant be null
-- Should not fail if database or table exists
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` (
       `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
       `state_id` INT NOT NULL,
       `name` VARCHAR(256) NOT NULL,
       FOREIGN KEY (`state_id`) REFERENCES `states`(`id`)
);
