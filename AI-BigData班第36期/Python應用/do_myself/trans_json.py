
kv=[];kv2=[];kv3=[]
i=0;n=0;o=0
while True:
    file = open('C:\\Users\\Big data\\Desktop\\jsontest.txt','r',encoding='utf-8')
    if i < len(file.readlines()):
        f2=open('C:\\Users\\Big data\\Desktop\\jsontest.txt','r',encoding='utf-8')
        kv2.append(f2.readlines()[i])
        i+=1
    else:
        break
for j in kv2:
    kv2[n]=j.strip().split('|')[1:-1]
    n+=1

print(kv)
del kv2[1]
kv=kv2
dic1={}
for i in range(1,len(kv2)):
    dic1['00'+str(i)]=dict(zip(kv2[0],kv[i]))

print(str(dic1))
with open('C:\\Users\\Big data\\Desktop\\jsonresult.txt','w',encoding='utf-8') as f:
    for i in dic1:
        f.write(i + str(dic1[i]) + ',\n')

# print(kv)
# for j in kv[1:]:
#     m2=0;m=0
#     while True:
#         try:
#             if o<len(j):
#                 j.insert(m2,kv[0][m])
#                 m2+=2
#                 m+=1
#             else:
#                 break
#         except:
#             break

# kstr=str(kv[:][:])
# kstr=kstr.replace('[','').replace('],','\n')
# with open('C:\\Users\\Big data\\Desktop\\jsonresult.txt','w',encoding='utf-8') as f:
#     f.write(kstr)