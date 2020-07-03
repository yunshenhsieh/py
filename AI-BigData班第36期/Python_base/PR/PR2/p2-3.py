'''
請撰寫一程式，讓使用者輸入三位學生各五筆成績，接著再計算並輸出每位學生的總分及平均分數。
提示：平均分數輸出到小數點後第二位。
'''
#ch8
N = ["1st", "2nd", "3rd"]
L1 = [[0 for j in range(5)] for i in range(3)]
for i in range(3):
    print("The {} student:".format(N[i]))
    for j in range(5):
        L1[i][j] = int(input())

for i in range(3):
    print("Student %d" % (i + 1))
    print("#Sum %d" % (sum(L1[i])))
    print("#Average %.2f" % (sum(L1[i]) / 5))