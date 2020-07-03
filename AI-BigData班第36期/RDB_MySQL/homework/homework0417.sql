CREATE DATABASE homework;
CREATE TABLE food (
	id char(5) PRIMARY KEY,
	w_name varchar(30),
	expiredate datetime,
	placeid char(2),
	price int unsigned,
	catalog varchar(20));
DESC food;
CREATE TABLE place (
	id char(2) PRIMARY KEY,
    name VARCHAR(20));
DESC place;
DESC food1;
CREATE TABLE food1 LIKE food;
ALTER TABLE food1 ADD price2 INT FIRST;
ALTER TABLE food1 MODIFY price2 CHAR(20) AFTER price;
ALTER TABLE food1 CHANGE price2 price3 INT AFTER id;
ALTER TABLE food1 DROP price3;
ALTER TABLE food1 RENAME food2;
DESC food2;
DROP TABLE IF EXISTS food2;
SHOW TABLES;