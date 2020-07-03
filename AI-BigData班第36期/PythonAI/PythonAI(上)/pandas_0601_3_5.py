import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(1,100,24).reshape(6,4),columns=list("ABCD"))
print(df)
print('')
print(df.head(3))
print('')
print(df.tail(2))
print('')
print(df.describe())
print('')
df['TAG']=["M","F","F","M","F","M"]
print(df)
print('')
print(df.groupby("TAG").sum())
print('')
print(df.groupby("TAG").mean())