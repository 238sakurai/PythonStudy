x = input('数字を入力してください')
for i in range(int(x)):
    if i % 5 == 0:
        print(str(i) + '---'  + 'ham')
    elif i % 3 == 0:
        print(str(i) + '---'  + 'eggs')
    else:
        print(str(i) + '---' + 'spam')
