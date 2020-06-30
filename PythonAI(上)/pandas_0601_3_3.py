import pandas as pd

data=[{'A':1,'B':2},{'A':5,"B":10,"C":20},{"B":20,"C":5,"D":22}]

df=pd.DataFrame(data,columns=list('ABCD'),index=['r0','r1','r2'])
print(df)
print('')
print(df.loc['r0'])
print('')
print(df.iloc[1])
print('')
print(df['B'])
print('')
print(df.loc['r1':'r2','C':'D'])
print('')
print(df.shape)