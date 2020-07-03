'''
請撰寫一程式，要求使用者輸入一個密碼（字串），檢查此密碼是否符合規則。密碼規則如下：
a. 必須至少八個字元。
b. 只包含英文字母和數字。
c. 至少要有一個大寫英文字母。
d. 若符合上述三項規則，程式將顯示檢查結果為【Valid password】，否則顯示【Invalid password】。

'''
#ch9
PW = input()
b=0
for i in range(len(PW)):
  if PW[i].isupper():
    b=1
if b==1 and len(PW)>=8 and PW.isalnum():
  print("Valid password")
else:
  print("Invalid password")