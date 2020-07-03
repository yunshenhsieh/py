import jieba

s = '大家好，我叫小賀，今天來中央大學大數據班上課，覺得非常開心。'

s1_list=jieba.cut(s,cut_all=True)
s2_list=jieba.cut(s,cut_all=False)
s3_list=jieba.cut(s)
s4_list=jieba.cut_for_search(s)

print('全模式 :',' | '.join(s1_list))
print('精確模式:',' | '.join(s2_list))
print('預設模式:',' | '.join(s3_list))
print('搜尋引擎模式:',' | '.join(s4_list))

jieba.load_userdict('./mydict.txt')

s1_list=jieba.cut(s,cut_all=True)
s2_list=jieba.cut(s,cut_all=False)
s3_list=jieba.cut(s)
s4_list=jieba.cut_for_search(s)
print('全模式 :',' | '.join(s1_list))
print('精確模式:',' | '.join(s2_list))
print('預設模式:',' | '.join(s3_list))
print('搜尋引擎模式:',' | '.join(s4_list))
