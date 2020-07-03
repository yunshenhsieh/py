-- Cross Join
SELECT ename,dname FROM emp,dept;
SELECT emp.ename,dept.dname FROM emp,dept;
SELECT emp.ename,dept.dname FROM emp CROSS JOIN dept;
-- 以上三行執行結果一樣，但建議用第三行寫法。

-- Inner Join:Equal join
SELECT emp.ename,dept.dname FROM emp,dept WHERE emp.deptno = dept.deptno;
SELECT emp.ename,dept.dname FROM emp JOIN dept ON emp.deptno = dept.deptno;
SELECT emp.ename,emp.deptno,dept.dname FROM emp,dept WHERE emp.deptno = dept.deptno;
SELECT emp.ename,deptno.deptno,dept.dname FROM emp,dept WHERE emp.deptno = dept.deptno;
SELECT emp.ename,dept.dname FROM emp JOIN dept USING (deptno);
SELECT emp.ename,dept.dname FROM emp NATURAL JOIN dept;
-- 以上六行執行結果一樣，但建議用第二行寫法。
SELECT ename,emp.deptno,dname FROM emp,dept WHERE emp.deptno = dept.deptno AND title='manager';
SELECT ename,emp.deptno,dname FROM emp JOIN dept ON emp.deptno = dept.deptno AND title='manager';
SELECT ename,emp.deptno,dname FROM emp JOIN dept ON emp.deptno = dept.deptno WHERE title='manager';
-- 以上三行執行結果一樣，第二行是用ANSI join的規則寫法寫的。
-- 表格別名
SELECT e.ename,e.deptno,d.dname FROM emp e,dept d WHERE e.deptno = d.deptno;
-- 以上是兩個表格別名的打寫。
SELECT e.ename,d.dname,c.cname FROM emp e,dept d,city c WHERE e.deptno=d.deptno AND d.cityno=c.cityno;
SELECT e.ename,d.dname,c.cname FROM emp e JOIN dept d ON e.deptno=d.deptno JOIN city c ON d.cityno=c.cityno;
-- 以上是三個表格別名的打寫，第二行是用ANSI的規則寫法寫的。

-- Inner join:Non-Equal join
SELECT e.ename,e.salary,g.level FROM emp e,grade g WHERE e.salary BETWEEN g.lowest AND g.highest;
SELECT e.ename,d.dname,e.salary,g.level FROM emp e,dept d,grade g WHERE e.deptno = d.deptno AND e.salary BETWEEN g.lowest AND g.highest;
SELECT e.ename,d.dname,e.salary,g.level FROM emp e JOIN dept d ON e.deptno = d.deptno JOIN grade g ON e.salary BETWEEN g.lowest AND g.highest;
-- 以上二行執行結果都一樣，第二行是用ANSI規則寫的。

-- Outer join
SELECT e.ename,e.deptno,d.dname FROM emp e LEFT JOIN dept d ON e.deptno = d.deptno;
SELECT e.ename,d.deptno,d.dname FROM emp e RIGHT JOIN dept d ON e.deptno = d.deptno;
SELECT e.ename,e.deptno,d.dname FROM emp e LEFT JOIN dept d ON e.deptno = d.deptno
UNION
SELECT e.ename,d.deptno,d.dname FROM emp e RIGHT JOIN dept d ON e.deptno = d.deptno;

-- Self join(一定要有別名)
SELECT worker.ename ' worker name',manager.ename 'manager name' FROM emp worker,emp manager WHERE worker.mgrno = manager.empno;
