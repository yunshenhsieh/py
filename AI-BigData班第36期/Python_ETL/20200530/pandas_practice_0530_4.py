import pandas as pd

df =pd.DataFrame(columns=['Name','Age','Height'])

df.loc[0] = ['Allen','22','175']
df.loc[1] = ['Ted','25','180']
df.loc[2] = ['Jack','28','170']

df['Weight'] = ['75','80','70']

df['Age'][0] = '23'

df['Age']='123'
df.loc[0] = 'aaaa'

print(df)

df.to_csv('./test.csv')

df.to_csv('./test2.csv',index=0)

df2 = pd.read_csv('./test.csv')
print(df2)
df3 = pd.read_csv('./test2.csv')
print(df3)

colums = ['Name','Age','Height']
data = [['Allen','22','175'],['Ted','25','180']
        ]
df4=pd.DataFrame(data=data,columns=colums)
print(df4)