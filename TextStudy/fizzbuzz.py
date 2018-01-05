#第2章    条件で分ける方法(分岐の基礎文法)
#リスト2.14    練習問題

a = 15
if a % 3 == 0:
    print('Fizz')
elif a % 5 == 0:
    print('Buzz')
elif a % 15 == 0:
    print('FizzBuzz')
else:
    print(a)
