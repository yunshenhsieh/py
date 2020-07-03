'''
請撰寫一程式，計算費氏數列（Fibonacci numbers），
使用者輸入一正整數num (num>=2)，並將它傳遞給名為compute()的函式，
此函式將輸出費氏數列前num個的數值。

提示：費氏數列的某一項數字是其前兩項的和，而且第0項為0，第一項為1，表示方式如下：
F0=0
F1=1
Fn=Fn−1+Fn−2
'''
#ch7

#解法一
def fib(n):

    a = 0 ; b= 1 ; i=0

    while True:
        if i == n:
            break
        yield a
        a, b , i =  b,  a+b, i+1


n = eval(input())

for x in fib(n):
    print(x, end=' ')

'''
#解法二
def fib(i):
    if i <= 1:
        return i
    else:
        return fib(i-1) + fib(i-2)


n = eval(input())
for x in range(n):
    print(fib(x), end=" ")
'''
