#練習問題その2_「キーワード引数を使う」　0502_answer.py
def get_sum(**kargs):
    start = kargs['start']
    end = kargs['end']
    result = 0
    for v in range(start,end+1):
        result += v
        print('startからendまでの値:' + str(v))
    return result

val = get_sum(start=1,end=100)
print(val)
