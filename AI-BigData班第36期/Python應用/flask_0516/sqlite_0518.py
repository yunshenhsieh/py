import sqlite3
# Connect to sqlite file
conn = sqlite3.connect('test.db')

# Execute SQL syntax
conn.execute("""CREATE TABLE IF NOT EXISTS `Staff` (
  `ID` VARCHAR(10) NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  `DeptId` VARCHAR(10) NOT NULL,
  `Age` INT NULL,
  `Gender` VARCHAR(3) NULL,
  `Salary` INT NULL,
  `recordDt` DATETIME NOT NULL,
  PRIMARY KEY (`ID`));""")

sql = """
INSERT INTO Staff (ID, Name, DeptId, Age, Gender, Salary, recordDt)
VALUES ('001', 'Jay', '001', 50, 'M', 56000, '2020-04-24 14:59:57');
"""
conn.execute(sql)
conn.commit()

# Get query data
for row in conn.execute("""SELECT * FROM Staff;"""):
    print(row)

sql = """
DELETE FROM Staff;
"""
conn.execute(sql)
conn.commit()

sql = """
INSERT INTO Staff (ID, Name, DeptId, Age, Gender, Salary, recordDt)
VALUES ('001', 'Jay', '001', 50, 'M', 56000, '2020-04-24 14:59:57');
"""
conn.execute(sql)
conn.commit()

# Close connection
conn.close()