#第2章    条件で分ける方法(分岐の基礎文法)
#リスト2.9

a = 10
if a > 1:
    print ("a")
    if a < 5:
        print("b")
    elif a <= 10:
        print("c")
        if a > 17:
            print("d")
        elif a > 30:
            print("e")
