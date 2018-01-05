#第2章    条件で分ける方法(分岐の基礎文法)
#リスト2.18    練習問題

weight = input('体重をkg単位で入力してください  ：')
height = input('身長をm単位で入力してください   ：')
bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    print('やせてる')
elif bmi < 25:
    print('ふつう')
elif bmi < 35:
    print('ちょっと太ってる？')
else:
    print('だいぶ太ってる！')

print(bmi)
