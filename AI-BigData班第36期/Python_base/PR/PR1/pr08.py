'''
請使用選擇敘述撰寫一程式，讓使用者輸入一個正整數，然後判斷它是3或5的倍數，
顯示【x is a multiple of 3.】或【x is a multiple of 5.】；
若此數值同時為3與5的倍數，顯示【x is a multiple of 3 and 5.】；
如此數值皆不屬於3或5的倍數，顯示【x is not a multiple of 3 or 5.】，
將使用者輸入的數值代入x。
'''
#ch5
n = eval(input())

if( n%3 == 0 and n%5 != 0):
  print(n,"is a multiple of 3.")
elif(n%3 !=0 and n%5 == 0):
  print(n,"is a multiple of 5.")
elif(n%3 == 0 and n%5 == 0):
  print(n,"is a multiple of 3 and 5.")
elif(n%3 != 0 and n%5 != 0):
  print(n,"is not a multiple of 3 or 5.")