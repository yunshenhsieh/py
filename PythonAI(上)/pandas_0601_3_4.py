import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randint(1,100,24).reshape(6,4),columns=list("ABCD"))
print(df)
print("")
print(df[3:5])
print("")
print(df[["A","B","D"]])
print('')
print(df.loc[3,"B"])
print("")
print(df.iloc[3,1])
print("")
print(df.iloc[2:5,0:2])
print(df.loc[2:5,["A","B"]])
print("")
print(df[df>18])
print("")
df[df>18]=100
print(df)
print('')
print(df[df.C>50])