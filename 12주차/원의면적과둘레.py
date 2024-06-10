pi = 3.14159265358979

def circleArea(radius):
    return pi * radius * radius

def circleCircum(radius):
    return 2 * pi * radius

r = int(input('반지름을 입력하시오: '))
print(f'반지름이 {r}인 원의 면적: {circleArea(r)}')
print(f'반지름의 {r}인 원의 둘레: {circleCircum(r)}')

