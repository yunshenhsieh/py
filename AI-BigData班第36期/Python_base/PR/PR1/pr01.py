
'''
請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。
提示：總和與平均數皆輸出到小數點後第1位。
'''
#ch6

a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())

Sum = a + b + c + d + e
Avg = Sum / 5

print(a,b,c,d,e)
print("Sum = %.1f" % (Sum) )
print("Average = %.1f" % (Avg) )