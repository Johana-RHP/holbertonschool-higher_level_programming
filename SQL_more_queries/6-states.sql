-- create a database hbtn_0d_usa and the table states
-- id INT unique, auto generated, can’t be null and is a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states
(id INT AUTO_INCREMENT NOT NULL,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id));
