import random

x = random.randint(1, 100)
y = random.randint(1, 100)

user_input = int(input((f'{x} - {y} = ')))

answer = x - y

if user_input == answer:
    print('맞았습니다.')
    
else:
    print('틀렸습니다.')