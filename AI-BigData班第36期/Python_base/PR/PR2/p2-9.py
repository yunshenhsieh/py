'''
請撰寫一程式，提示使用者輸入一個社會安全碼SSN，格式為ddd-dd-dddd，d表示數字。
若格式完全符合（正確的SSN）則顯示【Valid SSN】，否則顯示【Invalid SSN】。
'''
#ch9
SSN = list(input().split("-"))
b=0
for i in range(len(SSN)):
  if SSN[i].isdigit()==False:
    print("Invalid SSN")
    b+=1
    break
if b==0:
  print("Valid SSN")