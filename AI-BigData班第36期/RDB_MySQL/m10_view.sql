-- 建立View
CREATE VIEW empvu100 AS SELECT empno,ename,salary FROM employee WHERE deptno = 100;
SELECT * FROM empvu100;

CREATE VIEW salvu100 AS SELECT empno id,ename name,salary*12 'Annual_salary' FROM employee WHERE deptno = 100;
SELECT * FROM salvu100;

CREATE VIEW salvu100_1(id,name,annual_salary) AS SELECT empno,ename,salary*12 FROM employee WHERE deptno = 100;
SELECT * FROM salvu100_1;

CREATE VIEW dept_sum_vw (name,minsal,maxsal,avgsal) AS SELECT d.dname,MIN(e.salary),MAX(e.salary),AVG(e.salary) FROM employee e,department d WHERE e.deptno = d.deptno GROUP BY d.dname;
SELECT * FROM dept_sum_vw;

-- View維護資料
SELECT * FROM employee;
UPDATE empvu100 SET ename='孫悟淨' WHERE empno=1009;
-- 上行可執行，table裡的資料會被更改，因為view裡有包括1009這個人的資料。
UPDATE empvu100 SET ename = 'hen大為' WHERE empno=1003;
-- 上行可執行，但不會有結果，也不會改變table裡面的資料，因為view裡沒有包括1003這個人的資料。
UPDATE empvu100 SET title='SA' WHERE empno=1009;
-- 上行不可執行，因為view裡沒有包括title這個資料。
DELETE FROM empvu100 WHERE empno=1009;
-- 上行可執行，table裡的資料也會被刪除。

-- using with check option
CREATE VIEW emp_sal_vw AS SELECT empno,ename,salary FROM employee WHERE salary<=40000 WITH CHECK OPTION;
UPDATE emp_sal_vw SET salary = 40001 WHERE empno = 1002;
-- 上行無法執行，因為不符合上面view裡面的where條件。