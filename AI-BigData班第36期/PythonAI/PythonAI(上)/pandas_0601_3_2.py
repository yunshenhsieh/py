import pandas as pd
import numpy as np

df1=pd.DataFrame(np.random.rand(6,4),columns=list('ABCD'))
print(df1)
print('')

df2=pd.DataFrame(np.random.randn(6,4),columns=list('ABCD'))
print(df2)
print('')

df1=df1.append(df2,ignore_index=True)
print(df1)
print('')

df1=df1.drop(list(range(2,8)))
print(df1)
print('')
df1=df1.drop(columns=['A','D'])
print(df1)
print('')
df=df1.drop(11)
print(df1)