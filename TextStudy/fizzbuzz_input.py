#第2章    条件で分ける方法(分岐の基礎文法)
#リスト2.16    練習問題

a = input('数字を入力してください')
a = int(a)
if a % 15 == 0:
    print('FizzBuzz')
elif a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(a)
