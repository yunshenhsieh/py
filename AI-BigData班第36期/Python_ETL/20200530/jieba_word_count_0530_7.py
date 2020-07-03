import jieba
import os

flist = os.listdir('C:/Users/Big data/Desktop/etl')

sb = ''
for textfile in flist:
    with open('C:/Users/Big data/Desktop/etl/%s' %(textfile),'r',encoding='utf-8')as f:
        sb += f.read().split('---split---')[0]

s_cut = jieba.cut(sb)

for w in s_cut:
    print(w)

s_cut = jieba.cut(sb)
wc = {}
for w in s_cut:
    if len(w) < 2 :
        continue
    if not w in wc:
        wc[w]=1
    else:
        wc[w] += 1

wc_list = [(w,wc[w]) for w in wc]
wc_list.sort(key=lambda t: t[1],reverse=True)
print(wc_list)