
'''
請使用選擇敘述撰寫一程式，根據使用者輸入的分數顯示對應的等級。標準如下表所示：
分數	等級
80 ~ 100	A
70 ~ 79	B
60 ~ 69	C
<= 59	F

'''
#ch5
a=eval(input(""))
if a>=80 and a<=100:
  print("A")
elif a>=70 and a<=79:
  print("B")
elif a>=60 and a<=69:
  print("C")
elif a<=59:
  print("F")