import pandas as pd
import os

flist = os.listdir('C:/Users/Big data/Desktop/etl')

data = []
for textfile in flist:
    with open('C:/Users/Big data/Desktop/etl/%s' % (textfile),
              'r',encoding='utf-8')as f:
        data_str = f.read().\
            replace('作者:','作者：').replace('標題:','標題：').replace('時間:','時間：')\
            .split('---split---')[1]
        #上面這行會有replace是因為我自己爬下來的文章字元格式跟老師有不同，所以要自行整理寫上的。
        data_row = data_str.split('\n')[1:]
        data.append(data_row)
        # print(data_row)
        # print(data_str)
    # print('==========')

columns = ['推','噓','分數','作者','標題','時間']
df = pd.DataFrame(data=data,columns=columns)
# print(df)

df_copied = df.copy()
# print(df_copied)

# 下面這行要配合try:except那段使用，會寫except只是為了我用來打bug用的
def tmpfilter(datastring):
    result = datastring.split('：')[1]
    return result

# df_copied['推'] = df_copied['推'].apply(tmpfilter)
# print(df_copied)

try:
    for c in columns:
        df_copied[c] = df_copied[c].apply(tmpfilter)
except:
    print(df_copied[c]+'======')
    with open('./testlog.txt','a',encoding='utf-8')as f:
        f.write(str(df_copied[c]))

# 下面這行是用lambda寫，跟上面(tmpfilter+try:except)結果一樣
# for c in columns:
#
#     df_copied[c] = df_copied[c].apply(lambda s: s.split('：')[1])
#
# print(df_copied)

df_copied.to_csv('./test3.csv',index=False)