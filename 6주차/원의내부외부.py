import random

r = 5
x = random.randrange(-10, 11)
y = random.randrange(-10, 11)

distance = (x**2 + y**2) ** 0.5 #원점과 (x,y)의 거리

if distance <= r:
    print(f'({x},{y})점은 반지름 5인 원의 내부에 있다 ')
else:
    print(f'({x},{y})점은 반지름 5인 원의 외부에 있다 ')