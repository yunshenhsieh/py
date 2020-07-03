USE homework;
INSERT INTO food VALUES ('CK001', '曲奇餅乾', '2021/01/10', 'TL', 250, '點心');
INSERT INTO food VALUES ('CK002', '蘇打餅乾', '2019/10/12', 'TW', 80, '點心');
INSERT INTO food VALUES ('DK001', '高山茶', '2021/05/23', 'TW', 780, '飲料');
INSERT INTO food VALUES ('DK002', '綠茶', '2020/06/11', 'JP', 530, '飲料');
INSERT INTO food VALUES ('OL001', '苦茶油', '2022/03/16', 'TW', 360, '調味品');
INSERT INTO food VALUES ('OL002', '橄欖油', '2021/07/25', 'TL', 420, '調味品');
INSERT INTO food VALUES ('CK003', '仙貝', '2020/11/01', 'JP', 270, '點心');
INSERT INTO food VALUES ('SG001', '醬油', '2022/05/05', 'JP', 260, '調味品');
INSERT INTO food VALUES ('OL003', '葡萄子油', '2022/05/05', 'JP', 550, '調味品');
INSERT INTO food VALUES ('CK004', '鳳梨酥', '2020/10/12', 'TW', 340, '點心');
INSERT INTO food VALUES ('CK005', '太陽餅', '2020/08/27', 'TW', 150, '點心');
INSERT INTO food VALUES ('DK003', '紅茶', '2022/11/12', 'TL', 260, '飲料');
INSERT INTO food VALUES ('SG002', '醋', '2021/09/18', 'TW', 60, '調味品');

INSERT INTO place VALUES ('TW', '台灣');
INSERT INTO place VALUES ('JP', '日本');
INSERT INTO place VALUES ('TL', '泰國');
INSERT INTO place VALUES ('US', '美國');

-- Module 4 query 
SELECT * FROM food;
SELECT w_name,expiredate,price FROM food;
SELECT w_name AS '名稱',expiredate AS '到期日',price AS '價格' FROM food;
SELECT DISTINCT catalog FROM food;
SELECT CONCAT(w_name,' ',catalog) AS 'Food name&catalog' FROM food;

-- Module 4 where
SELECT w_name,price FROM food WHERE price > 400;
SELECT w_name,price FROM food WHERE price BETWEEN 250 AND 530;
SELECT w_name,price FROM food WHERE price NOT BETWEEN 250 AND 530;
SELECT w_name,price FROM food WHERE catalog IN ('點心');
SELECT w_name,price,catalog FROM food WHERE catalog IN ('點心','飲料');
SELECT w_name,price FROM food WHERE placeid IN ('TW','JP');
SELECT w_name,expiredate,price FROM food WHERE w_name LIKE '%油%';
SELECT w_name,price,expiredate FROM food WHERE expiredate <= '2020/12/31';
SELECT w_name,price,expiredate FROM food WHERE expiredate <= '2021/06/30';
SELECT w_name,price,expiredate FROM food WHERE expiredate <= CURDATE() + INTERVAL 6 MONTH;

-- Module 4 order by
SELECT w_name,expiredate,price FROM food ORDER BY price DESC;
SELECT w_name,expiredate,price FROM food ORDER BY price DESC LIMIT 3;
SELECT w_name,price FROM food WHERE price <=250 ORDER BY price ASC;
SELECT w_name,price,(price+ROUND(price * 0.05)) AS 'NEW Price' FROM food;
SELECT w_name,price,(price+ROUND(price * 0.05)) AS 'NEW Price',(price+ROUND(price * 0.05)-price) AS 'Increase' FROM food;
SELECT w_name,price,
CASE
WHEN price<=250 THEN (price + TRUNCATE(price * 0.08,0))
WHEN price BETWEEN 251 AND 500 THEN(price + TRUNCATE(price * 0.05,0))
WHEN price >500 THEN(price + TRUNCATE(price * 0.03,0))
END AS 'NEW price' FROM food;
SELECT w_name,catalog,DATEDIFF(expiredate,CURDATE()) AS 'Days of expired',IF(DATEDIFF(expiredate,CURDATE()) > 0,'未過期','已過期') AS 'expired or not' FROM food;
SELECT w_name,catalog,DATEDIFF(expiredate,CURDATE()) AS 'Days of expired',IF(DATEDIFF(expiredate,CURDATE()) > 0,'未過期','已過期') AS 'expired or not' FROM food ORDER BY DATEDIFF(expiredate,CURDATE());

-- Module 4 group by & having
SELECT ROUND(MAX(price)) AS 'Max',ROUND(MIN(price)) AS 'Min',ROUND(SUM(price)) AS 'Sum',ROUND(AVG(price)) AS 'Avg' FROM food;
SELECT catalog AS '種類',(MAX(price)) AS 'Max',ROUND(MIN(price)) AS 'Min',ROUND(SUM(price)) AS 'Sum',ROUND(AVG(price)) AS 'Avg' FROM food GROUP BY catalog;
SELECT catalog AS '種類',(MAX(price)) AS 'Max',ROUND(MIN(price)) AS 'Min',ROUND(SUM(price)) AS 'Sum',ROUND(AVG(price)) AS 'Avg' FROM food GROUP BY catalog HAVING ROUND(AVG(price))>300 ORDER BY ROUND(AVG(price)) DESC ;
SELECT catalog,COUNT(*) AS 'COUNT' FROM food GROUP BY catalog;
SELECT catalog,placeid,COUNT(*) AS 'COUNT' FROM food GROUP BY catalog,placeid;

-- Module 5 join
SELECT w_name,placeid,place.name,price FROM food JOIN place ON food.placeid = place.id;
SELECT CONCAT(w_name,'     ',place.name)'Food name & place' FROM food JOIN place ON food.placeid = place.id;
SELECT w_name,price,place.id,place.name FROM food JOIN place ON food.placeid = place.id AND place.name='台灣';
SELECT w_name,price,place.name FROM food JOIN place ON food.placeid = place.id AND place.name='台灣';
SELECT w_name,price,place.name FROM food JOIN place ON food.placeid = place.id AND place.name IN ('台灣','日本') ORDER BY price DESC;
SELECT w_name,expiredate,price FROM food JOIN place ON food.placeid = place.id AND place.name='台灣' ORDER BY price DESC LIMIT 3;
SELECT place.name,(MAX(price)) AS '最高',(MIN(price)) AS '最低',(SUM(price)) AS '總和',ROUND((AVG(price))) AS '平均' FROM food JOIN place ON food.placeid = place.id GROUP BY place.name;
SELECT place.name,catalog,COUNT(*) FROM food JOIN place ON food.placeid = place.id GROUP BY place.name,food.catalog;