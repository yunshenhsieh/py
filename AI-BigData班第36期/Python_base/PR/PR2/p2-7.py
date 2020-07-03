'''
請撰寫一程式，輸入X組和Y組各自的科目至集合中，
以字串"end"作為結束點（集合中不包含字串"end"）。
請依序分行顯示
(1) X組和Y組的所有科目、
(2)X組和Y組的共同科目、
(3)Y組有但X組沒有的科目，
以及(4) X組和Y組彼此沒有的科目（不包含相同科目）
'''
#ch8
x = set()
y = set()
print("Enter group X's subjects:")
while True:
    enter = input()
    if enter == "end":
        break
    x.add(enter)

print("Enter group Y's subjects:")
while True:
    enter = input()
    if enter == "end":
        break
    y.add(enter)

print(sorted(x | y))
print(sorted(x & y))
print(sorted(y - x))
print(sorted(x ^ y))