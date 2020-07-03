'''
請撰寫一程式，以不定數迴圈的方式讓使用者輸入西元年份，
然後判斷它是否為閏年（leap year）或平年。
其判斷規則如下：每四年一閏，每百年不閏，但每四百年也一閏。
(假設此不定數迴圈輸入-9999則會結束此迴圈。)
'''
#ch5
Y=0
while(Y != -9999):
  Y = eval(input())
  if Y != -9999:
    if Y % 4 == 0 and Y % 100 != 0:
      print(Y,"is a leap year.")
    elif Y % 400 == 0:
      print(Y,"is a leap year.")
    else:
      print(Y,"is not a leap year.")