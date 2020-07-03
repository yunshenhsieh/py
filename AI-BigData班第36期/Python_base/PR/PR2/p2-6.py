'''
請撰寫一程式，為一詞典輸入資料（以輸入鍵值"end"作為輸入結束點，詞典中將不包含鍵值"end"），
再輸入一鍵值並檢視此鍵值是否存在於該詞典中。
'''
#ch8
d1 = {}
while True:
    K = input("Key: ")
    if K == "end":
        break
    d1[K] = input("Value: ")

sc = input("Search key: ")
print(sc in d1.keys())