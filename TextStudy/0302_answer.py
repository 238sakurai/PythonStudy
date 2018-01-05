#第3章    繰り返しさせる方法(反復の基礎文法)
#リスト3.6 練習問題その2 九九の演算

kuku = [1,2,3,4,5,6,7,8,9]
for x in kuku:
    for y in kuku:
        print (x*y, end=' ')
    print('')
