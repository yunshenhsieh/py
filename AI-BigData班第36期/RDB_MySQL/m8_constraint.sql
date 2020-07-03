CREATE TABLE emp1(
-- column level constraint
empno	DECIMAL(4)	PRIMARY KEY,
ename	VARCHAR(30) NOT NULL,
hiredate DATE 		NOT NULL,
email	VARCHAR(30) UNIQUE,
deptno	DECIMAL(3)	NOT NULL,
salary	INT,
title	VARCHAR(20)	NOT NULL	DEFAULT 'engineer',
-- table level constraint
CONSTRAINT emp_deptno_fk FOREIGN KEY (deptno)
REFERENCES department(deptno));

-- Explicit Default
INSERT INTO dept VALUES (600,'Public Relations',DEFAULT);
UPDATE dept SET cityno = DEFAULT WHERE deptno = 500;

-- Foreign key
INSERT INTO emp1 VALUES (1001,'李悟空','2013/11/10','lee@gmail.com',100,56000,'senior engineer');
-- Error Code: 1062. Duplicate entry 'lee@gmail.com' for key 'email'
INSERT INTO emp1 VALUES (1002,'李悟空','2013/11/10','lee@gmail.com',100,56000,'senior engineer');

INSERT INTO emp1 VALUES (1002,'李悟空','2013/11/10','lee1@gmail.com',200,56000,'senior engineer');
-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`db01`.`emp1`, CONSTRAINT `emp_deptno_fk` FOREIGN KEY (`deptno`) REFERENCES `department` (`deptno`))
INSERT INTO emp1 VALUES (1003,'李悟空','2013/11/10','lee2@gmail.com',600,56000,'senior engineer');
-- Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails (`db01`.`emp1`, CONSTRAINT `emp_deptno_fk` FOREIGN KEY (`deptno`) REFERENCES `department` (`deptno`))
UPDATE emp1 SET deptno = 600 WHERE empno = 1001;
-- Error Code: 1451. Cannot delete or update a parent row: a foreign key constraint fails (`db01`.`emp1`, CONSTRAINT `emp_deptno_fk` FOREIGN KEY (`deptno`) REFERENCES `department` (`deptno`))
DELETE FROM department WHERE deptno = 100;
-- 下面這行可以執行，因為子資料(剛新增的資料中)沒有300的，且只有emp1有設定foreign key，所以可以執行可以刪。
DELETE FROM department WHERE deptno = 300;

-- Foreign key 中UPDATE RESTRICT換成UPDATE CASCADE的方法，也可以用視窗設定。
ALTER TABLE `db01`.`emp1` 
DROP FOREIGN KEY `emp_deptno_fk`;
ALTER TABLE `db01`.`emp1` 
ADD CONSTRAINT `emp_deptno_fk`
  FOREIGN KEY (`deptno`)
  REFERENCES `db01`.`department` (`deptno`)
  ON UPDATE CASCADE;
-- 驗證上一段程式碼
UPDATE department SET deptno = 101 WHERE deptno = 100;

-- Foreign key 中DELETE RESTRICT換成DELETE CASCADE的方法，也可以用視窗設定。
ALTER TABLE `db01`.`emp1` 
DROP FOREIGN KEY `emp_deptno_fk`;
ALTER TABLE `db01`.`emp1` 
ADD CONSTRAINT `emp_deptno_fk`
  FOREIGN KEY (`deptno`)
  REFERENCES `db01`.`department` (`deptno`)
  ON DELETE CASCADE
  ON UPDATE CASCADE;
-- 驗證上一段程式碼
DELETE FROM department WHERE deptno = 101;

-- AUTO_INCREMENT
CREATE TABLE mem(memno int PRIMARY KEY AUTO_INCREMENT,mname VARCHAR(30) NOT NULL);
INSERT INTO mem (mname) VALUES ('David Ho'),('Maria Wang'),('Pam Pan'),('Tina Lee'),('Jean Tsao');
SELECT LAST_INSERT_ID();
-- 以上這行會查AUTO_INCREMENT自動編號到幾號了，但邏輯是回傳上一次加到幾號，若已有5筆，一次加5筆，會回傳6，但若又加一筆，就會回傳11，正常了。
INSERT INTO mem (mname) VALUES ('David Ho'),('Maria Wang'),('Pam Pan'),('Tina Lee'),('Jean Tsao');
-- 以上為沒有設定初始值的方法。
DROP table mem;
CREATE TABLE mem(memno int PRIMARY KEY AUTO_INCREMENT,mname VARCHAR(30) NOT NULL)AUTO_INCREMENT =100;
-- 以上這行是有設定初始值的方法。