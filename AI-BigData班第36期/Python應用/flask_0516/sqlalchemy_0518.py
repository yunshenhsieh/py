import pymysql
# 建立連線
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Rootroot12@localhost:3306/TESTDB', echo=True)

# 宣告映射
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# 描述 Table
from sqlalchemy import Column, Integer, String, Date


class Staff(Base):
    __tablename__ = 'Staff'

    ID = Column(String(10), primary_key=True)
    Name = Column(String(45), nullable=False)
    DeptId = Column(String(10), nullable=False)
    Age = Column(Integer, default=None)
    Gender = Column(String(3), default=None)
    Salary = Column(Integer, default=None)
    RecordDt = Column(Date, nullable=False)

    def __repr__(self):
        return "<User(name='%s', record='%s'>" % (self.Name, self.RecordDt)

# 建立 session
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)
session = DBSession()

# 查詢
for r in session.query(Staff):
    print(r.ID, r.Name, r.Salary, r.RecordDt)

# 查詢搭配條件
for r in session.query(Staff).filter(Staff.Salary < 50000):
    print(r.ID, r.Name, r.RecordDt)

# 建立一筆資料的物件
Staff(ID='009', Name='Allen', DeptId='001', Age=25, Gender='M', Salary=80000, RecordDt='2020-05-01 21:04:52')
# 將物件 INSERT 進 Table
session.add_all([Staff(ID='009', Name='Allen', DeptId='001', Age=25, Gender='M', Salary=80000, RecordDt='2020-05-01 21:04:52')])

# 在查詢一下
for r in session.query(Staff):
    print(r.ID, r.Name, r.Salary, r.RecordDt)

# Commit 並關閉 session
session.commit()
session.close()