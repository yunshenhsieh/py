'''
請撰寫一程式，讓使用者輸入兩個整數，接著呼叫函式compute()，
此函式接收兩個參數a、b，並回傳從 a 連加到 b的和。
'''
#ch7
def compute(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s


a = eval(input())
b = eval(input())
print(compute(a, b))