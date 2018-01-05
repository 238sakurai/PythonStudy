#第3章    繰り返しさせる方法(反復の基礎文法)
#リスト3.5

import random

#   自分のヒットポイント
my_hit_point = 30
#   スライムのヒットポイント
slime_hit_point = 10
#   攻撃の順番
#   ここでは自分から攻撃するものとする
index = 0
#   どちらかのヒットポイントがあるまで戦う
#   ヒットポイントが0以下になると繰り返しが終わる
while slime_hit_point > 0 and my_hit_point > 0:
    #   ランダムに与えるダメージを決定
    attack = random.randint(1,8)
    #   自分とスライムが交互に攻撃をする
    if index % 2 == 0:
        print('スライムに' + str(attack) + 'のダメージ')
        slime_hit_point -= attack
#        print('スライムの残りHP' + str(slime_hit_point))  #これは遊びで追記
    else:
        print('ゆうしゃに' + str(attack) + 'のダメージ')
        my_hit_point -= attack
#        print('ゆうしゃの残りHP' + str(my_hit_point))     #これは遊びで追記
    index += 1
#   whileを抜けたらどちらかが死んでる
#   自分のヒットポイントが残っていれば、スライム撃破！
if my_hit_point > 0:
    print('スライムをやっつけた')
else:
    print('ゆうしゃは死んでしまった')
