USE db01;
-- single row subquery
SELECT ename,salary FROM employee WHERE salary  > (SELECT salary FROM employee WHERE ename ='潘麗珍');
SELECT ename,title,salary FROM employee WHERE title = (SELECT title FROM employee WHERE empno = 1002) AND salary > (SELECT salary FROM employee WHERE empno =1005);
SELECT deptno,MIN(salary) 'Minimum Salary' FROM employee GROUP BY deptno HAVING MIN(salary) > (SELECT MIN(salary) FROM employee WHERE deptno =200);
SELECT ename,title,salary,ROUND(salary * 100/(SELECT SUM(salary)FROM employee WHERE deptno=100),1) 'Percentage' FROM employee WHERE deptno = 100;
SELECT ename,title,salary,ROUND(salary * 100/t.total,1) 'Percentage' FROM employee,(SELECT SUM(salary) 'total' FROM employee WHERE deptno =100) t WHERE deptno =100;

-- multiple row subquery
SELECT ename,title,salary FROM employee WHERE salary <ANY(SELECT salary FROM employee WHERE title='senior engineer') AND title <> 'senior engineer';
SELECT ename,title,salary FROM employee WHERE salary < ALL (SELECT salary FROM employee WHERE title='senior engineer') AND title <> 'senior engineer';
-- 下面這行執行沒有結果，是因為判斷式IN其實表示x=1003 or x=1004 or x=null，變NOT IN後x<>1003 and x<>1004 and x<>null，因為and中有一個回傳了null，整個subquery就回傳了null就沒有輸出資料了。
SELECT ename FROM emp WHERE empno NOT IN(SELECT DISTINCT mgrno FROM emp);
SELECT ename FROM emp WHERE empno NOT IN(SELECT DISTINCT mgrno FROM emp WHERE mgrno IS NOT NULL);

-- correlated subquery
SELECT e.ename,e.title,e.salary,ROUND(salary * 100/(SELECT SUM(salary) FROM employee WHERE deptno = e.deptno),1) 'Percentage' FROM employee e WHERE e.deptno =100;
SELECT ename,salary,deptno FROM employee e WHERE salary IN (SELECT MIN(salary) FROM employee GROUP BY deptno HAVING deptno = e.deptno);
SELECT ename,salary,deptno FROM employee e WHERE salary = (SELECT MIN(salary) FROM employee WHERE deptno = e.deptno);
-- 上面兩行執行結果相同，只是寫法不同。


