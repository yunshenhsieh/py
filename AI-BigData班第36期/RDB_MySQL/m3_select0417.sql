SELECT * FROM employee;
SELECT deptno,ename,salary FROM employee;

SELECT 17/4,17 div 4,17%4,17*null;

-- 20200417別名(Alias)的使用方式
SELECT ename AS '員工姓名',salary*12 AS '年薪' FROM employee;
SELECT ename '員工姓名',salary*12 '年薪' FROM employee;
SELECT ename 員工姓名,salary*12 年薪 FROM employee;
SELECT ename 'Employee name',salary*12 'Annual salary' FROM employee; -- 如果中間有空白字元，就一定要用單引號包起來。

-- String Functions:SUBSTRING(str,pos,[len])截取部份字串
SELECT SUBSTRING(ename,1,1) '姓氏' FROM employee;
SELECT SUBSTRING(ename,2) '姓名' FROM employee;
SELECT SUBSTRING('David Wang',1,5) '姓氏';
SELECT SUBSTRING('David Wang',7) '姓氏';
SELECT SUBSTRING('David Wang',-4) '姓氏';
SELECT SUBSTRING('David Wang',-4,2) '姓氏';
SELECT CONCAT(ename,' is a ',title) '員工' FROM employee;
SELECT LENGTH('我是一個student') 'length';
SELECT CHAR_LENGTH('我是一個student') 'length';

-- date functions
SELECT SYSDATE() + INTERVAL 5 DAY 'Date';
SELECT SYSDATE() - INTERVAL 3 MONTH 'Date';
SELECT SYSDATE(),SLEEP(2),SYSDATE();
SELECT NOW(),SLEEP(2),NOW(); -- NOW()取出來的當下時間是常數，再次使用時會抓之前的時間來用，需小心。
SELECT CURDATE(),CURTIME();
SELECT CONCAT(CURDATE(),' ',CURTIME())'Date';
SELECT ADDDATE(CURDATE(),5)'Date';
SELECT ADDDATE(CURDATE(),INTERVAL 2 MONTH)'Date';
SELECT SUBDATE(CURDATE(),5)'Date';
SELECT SUBDATE(CURDATE(),INTERVAL 6 HOUR)'Date'; -- 如果用日期，但用小時為間隔單位，會有問題。
SELECT SUBDATE(CURDATE(),INTERVAL 6 DAY)'Date';

-- 課堂出題練習
SELECT empno,ename,hiredate,
	DATEDIFF(NOW(),hiredate) DIV 365 'year',
    DATEDIFF(NOW(),hiredate) / 365 'year',
    ROUND(DATEDIFF(NOW(),hiredate) / 365) 'year',
    ROUND(DATEDIFF(NOW(),hiredate) / 365,1) 'year'
    FROM employee; -- 算年資用。
SELECT empno,ename,hiredate,
    DATEDIFF(NOW(),hiredate) / 365 'year',
    ROUND(DATEDIFF(NOW(),hiredate) % 365 / 30) 'month'
    FROM employee; -- 算年資用，自己寫的，需求是印出工作幾年幾用，但有bug，可能出現12個月。
    
-- 20200425條件判斷式：IF 和 CASE...WHEN...ELSE
SELECT empno,ename,salary,
  salary * IF(salary>=50000,2,1.5)'bonus'
FROM employee;

SELECT empno,ename,salary,
  CASE
    WHEN salary > 100000 THEN 'A'
    WHEN salary BETWEEN 70000 AND 100000 THEN 'B'
    WHEN salary BETWEEN 50000 AND 69999 THEN 'C'
    WHEN salary BETWEEN 30000 AND 49999 THEN 'D'
    ELSE 'E'
  END 'Grade'
FROM employee;

-- 去除重覆的資料列 DISTINCT
SELECT DISTINCT deptno FROM employee;
SELECT DISTINCT deptno,mgrno FROM department;

-- WHERE clause
SELECT * FROM employee WHERE deptno = 100;
SELECT * FROM employee WHERE title = 'engineer';
SELECT * FROM employee WHERE hiredate > '2007/07/06';
SELECT * FROM employee WHERE salary >= 50000;
SELECT * FROM employee WHERE salary BETWEEN 30000 AND 40000;
SELECT * FROM employee WHERE title IN('manager','engineer');
SELECT * FROM department WHERE mgrno IS NULL;

-- LIKE
SELECT * FROM employee WHERE ename LIKE '林%';
SELECT * FROM employee WHERE ename LIKE '%生';
SELECT * FROM employee WHERE ename LIKE '%麗%';
SELECT * FROM employee WHERE ename LIKE '_麗%';
SELECT * FROM employee WHERE ename LIKE '__麗%';
SELECT * FROM employee WHERE title LIKE '%SA\_%';
SELECT * FROM employee WHERE title LIKE '%SA/_%' ESCAPE '/';
-- 上面兩行的執行結果一樣，ESCAPE可以改成你想要的跳脫字元。
SELECT * FROM employee WHERE salary >= 45000 AND ename LIKE '林%';
SELECT * FROM employee WHERE salary >= 45000 OR ename LIKE '林%';
SELECT * FROM employee WHERE salary >= 30000 AND 40000; -- 同SELECT * FROM employee WHERE salary BETWEEN 30000 AND 40000;
SELECT * FROM employee WHERE title ='manager' OR title ='engineer';
-- 查詢出來後，下面有一排null，表示出來的值可以做修改、新增、刪除，這是MySQL的工具特性。

-- NOT
SELECT * FROM employee WHERE title NOT IN('manager','engineer');
SELECT * FROM department WHERE mgrno IS NOT NULL;
SELECT * FROM employee WHERE salary NOT BETWEEN 40000 AND 60000;
SELECT * FROM employee WHERE ename NOT LIKE '林%';

-- ORDER BY clause
SELECT * FROM employee ORDER BY hiredate DESC;
SELECT * FROM employee ORDER BY hiredate;
SELECT * FROM employee ORDER BY salary;
SELECT * FROM employee ORDER BY salary DESC;
SELECT ename,deptno,salary FROM employee ORDER BY deptno,salary DESC;
SELECT ename,deptno,salary FROM employee ORDER BY deptno DESC,salary DESC;
SELECT ename,salary*12 ' Annual' FROM employee ORDER BY Annual;
SELECT ename,salary*12 ' Annual' FROM employee ORDER BY salary*12;
SELECT ename,deptno,salary FROM employee ORDER BY 3;
SELECT * FROM employee ORDER BY 3;

-- LIMIT clause MySQL專有
SELECT * FROM employee LIMIT 3;
SELECT * FROM employee LIMIT 4,3;
SELECT * FROM employee ORDER BY hiredate LIMIT 3;
SELECT * FROM employee ORDER BY salary DESC LIMIT 3;

-- Aggregate Function
SELECT SUM(salary),AVG(salary),MAX(salary),MIN(salary) FROM employee;
SELECT count(salary) FROM employee;
SELECT count(empno) FROM employee;
SELECT count(deptno) FROM employee;
SELECT count(DISTINCT deptno) FROM employee;
SELECT count(*) FROM employee;
SELECT count(mgrno) FROM department;

-- GROUP BY clause
SELECT deptno,AVG(salary) 'Average' FROM employee GROUP BY deptno;
SELECT deptno,COUNT(*) 'count' ,SUM(salary) 'sum' ,AVG(salary) 'Average' FROM employee GROUP BY deptno;
SELECT deptno,COUNT(deptno) 'count' ,SUM(salary) 'sum' ,AVG(salary) 'Average' FROM employee GROUP BY deptno;
SELECT deptno,AVG(salary) 'Average' FROM employee GROUP BY deptno ORDER BY AVG(salary);
SELECT deptno,COUNT(*) 'Count' FROM employee GROUP BY deptno;
SELECT deptno,title, SUM(salary) ' Total' FROM employee GROUP BY deptno,title;

-- HAVING clause
SELECT deptno,AVG(salary) 'Average' FROM employee GROUP BY deptno HAVING AVG(salary) >50000;

-- Aggregate Function完整範例(觀念題，一次寫一點，驗證後再寫)
-- 找出不同職稱的總薪資，但不包括含有"SA"這些字的職稱，且總薪資必須超過100000，最後結果並以總薪資排序。
SELECT title,SUM(salary) 'Total'
FROM employee
WHERE title NOT LIKE '%SA%'
GROUP BY title
HAVING SUM(salary) > 100000
ORDER BY SUM(salary) DESC;
