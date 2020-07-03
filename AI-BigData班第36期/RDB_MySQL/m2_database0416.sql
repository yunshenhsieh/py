CREATE DATABASE db01;
CREATE SCHEMA `db02` ;

USE db02; -- switch database

SHOW DATABASES;
CREATE DATABASE IF NOT EXISTS db01;
SHOW charset;
SHOW collation;
SHOW collation like 'big5%';
ALTER DATABASE db02 CHARACTER SET big5 COLLATE big5_bin; -- 資料庫內有資料就不要改character set跟collate
SELECT @@character_set_database,@@collation_database; -- 查看DB是用哪種character set跟collation
DROP DATABASE IF EXISTS db02;