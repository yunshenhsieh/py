import sys
b=input()
a=b.split(',')
sum=0
for i in a:
    sum+=int(i)
    print(sum)
print(b)
c=eval(b)
print(c)
for i in c:
    sum+=i
    print(sum)
print(sys.stdout)