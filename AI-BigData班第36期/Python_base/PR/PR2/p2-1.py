'''
請撰寫一程式，讓使用者輸入十個整數，計算並輸出偶數和奇數的個數。
'''
#ch5

A=0
B=0

for i in range(10):
  N = int(input())
  if N % 2 == 0:
    A += 1
  if N % 2 != 0:
    B+=1
print("Even numbers: %d" % A)
print("Odd numbers: %d" % B)