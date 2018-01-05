#num = input('数字を入力してください------> ')

num = int(15)

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'Fizzbuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)
