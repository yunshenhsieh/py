'''
請使用選擇敘述撰寫一程式，讓使用者輸入三個邊長，檢查這三個邊長是否可以組成一個三角形。
若可以，則輸出該三角形之周長；否則顯示【Invalid】。
提示：檢查方法 = 任意兩個邊長之總和大於第三邊長。
'''
#ch5
x=eval(input())
y=eval(input())
z=eval(input())

if x+y>z and x+z>y and y+z>x:
  print(x+y+z)
else:
  print("Invalid")

