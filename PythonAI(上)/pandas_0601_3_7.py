import pandas as pd
import numpy as np

d={"A":pd.Series(data=np.random.randint(10,30,5),
                 index=pd.date_range('20200101',periods=5)),
   "B":pd.Series(data=np.random.randint(50,80,5),
                 index=pd.date_range('20200101',periods=5)),
   "C":pd.Series(data=np.random.randint(100, 150, 5),
             index=pd.date_range('20200101', periods=5))
   }

df=pd.DataFrame(d,index=pd.date_range('20200101',periods=5))
print(df)
print('')
df['D']=df["B"] + df["C"]
print(df)
print('')
print(df.loc['20200102':'20200104'])
print('')
del df["A"]
print(df)
df["E"]=pd.Series(data=[10,20,30,40,50],
                 index=pd.date_range('20200101',periods=5))
print(df)
print('')
print(df["B"].values)
print('')
print(df.T)
print('')
df=df.drop(pd.date_range('20200103',periods=2))
print(df)
print('')
d={"B":10,"C":20,"D":30,"E":40,}
df=df.append(pd.DataFrame(data=d,index=pd.date_range('20200106',periods=1)),sort=True)
d=[{"B":11,"C":21,"D":31,"E":41,},
   {"B":32,"C":22,"D":32,"E":42,}]
df=df.append(pd.DataFrame(data=d,index=pd.date_range('20200107',periods=2)),sort=True)
print(df)