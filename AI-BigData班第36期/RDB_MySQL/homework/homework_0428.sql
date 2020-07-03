-- subquery
SELECT w_name,expiredate,price FROM food WHERE price > (SELECT price FROM food WHERE w_name='鳳梨酥') ORDER BY price DESC;
SELECT w_name,expiredate,price FROM food WHERE price < (SELECT price FROM food WHERE w_name='曲奇餅乾') AND catalog='點心';
SELECT w_name,YEAR(expiredate),price FROM food WHERE (SELECT YEAR(expiredate) FROM food WHERE w_name='鳳梨酥')=YEAR(expiredate);
SELECT w_name,expiredate,price FROM food WHERE price > (SELECT AVG(price) FROM food);
SELECT w_name,expiredate,price FROM food WHERE price < (SELECT AVG(price) FROM food WHERE placeid = 'tw');
SELECT w_name,expiredate,price FROM food WHERE catalog = (SELECT catalog FROM food WHERE w_name='仙貝') AND price < (SELECT price FROM food WHERE w_name='仙貝');
SELECT w_name,expiredate,price FROM food WHERE (SELECT placeid FROM food WHERE w_name='仙貝') AND expiredate < (SYSDATE() - INTERVAL 6 MONTH);
SELECT w_name,expiredate,MIN(price),placeid FROM food GROUP BY placeid;
SELECT w_name,price,catalog FROM food WHERE price IN (SELECT MAX(price) FROM food f GROUP BY catalog HAVING catalog=f.catalog);
SELECT w_name,price,catalog FROM food WHERE catalog <> '點心' AND price > (SELECT MAX(price) FROM food WHERE catalog='點心') ORDER BY price DESC;
SELECT w_name,price,placeid FROM food f WHERE price IN (SELECT MAX(price) FROM food GROUP BY placeid HAVING placeid=f.placeid);

-- DML (id,w_name,expiredate,placeid,price,catalog)
INSERT INTO food(id,w_name,expiredate,placeid,price,catalog) VALUES ('QQ003','雪碧','2020-04-28','UK',29,'飲料');
INSERT INTO food(w_name,id,expiredate,placeid,price,catalog) VALUES ('火碧','QQ004','2020-04-28','UK',29,'飲料');
INSERT INTO food VALUES ('QQ005','水碧','2020-012-28','US',29,'點心'),('QQ006','石油碧','2020-011-28','GG',45,'飲料');

UPDATE food SET price=123456 WHERE id = 'QQ005';
UPDATE food SET price=(SELECT 
CASE
WHEN price<=250 THEN (price + TRUNCATE(price * 0.08,0))
WHEN price BETWEEN 251 AND 500 THEN(price + TRUNCATE(price * 0.05,0))
WHEN price >500 THEN(price + TRUNCATE(price * 0.03,0))
END 
FROM (SELECT * FROM food) e WHERE id='QQ006') 
WHERE id = 'QQ004';

DELETE FROM food WHERE id = 'QQ005';