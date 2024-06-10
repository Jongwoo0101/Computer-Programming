'''
def f(i, mylist):
    i = i + 1
    mylist.append(0)
    
k = 10
m = [1, 2, 3]

f(k, m)

print(f'k = {k}, m = {m}')

def func1(a):
    return a + x

def func2(a):
    x = 10
    return a + x

x = 1

print('fun1(100) result : ', func1(100))
print('fun2(100) result : ', func2(100))
print('after function x result', x)

def func1(a):
    return a + x

def func2(a):
    global x
    x = 10
    return a + x

x = 1

print('fun1(100) result : ', func1(100))
print('fun2(100) result : ', func2(100))
print('after function x result', x)

pi = 3.14159265358979

def circleArea(radius):
    return pi * radius * radius

def circleCircum(radius):
    return 2 * pi * radius

r = int(input('반지름을 입력하시오: '))
print(f'반지름이 {r}인 원의 면적: {circleArea(r)}')
print(f'반지름의 {r}인 원의 둘레: {circleCircum(r)}')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiple(a, b):
    return a * b

def divide(a, b):
    return a / b

num1 = int(input('첫번째 정수를 입력: '))
num2 = int(input('두번째 정수를 입력: '))
operator = input('+, -, *, / 중에서 선택')


if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiple(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
    
print(f'{num1} {operator} {num2} = {result}')

def calc(n1, op, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    else:
        return n1 / n2
    
num1 = int(input('첫 번째 정수를 입력: '))
num2 = int(input('두 번째 정수를 입력: '))
operator = int(input('+, -, *, / 중 선택: '))

print(f'{num1} {operator} {num2} = {calc(num1, operator, num2)}')


'''

def f(x, y, /, z): # x, y는 위치전용, z는 둘 다 허용
    print(f'x: {x}, y: {y}, z: {z}')
    
f(1, 2, 3)
f(1, 2, z = 3)
# f(x = 1, y = 2, z = 3)

def f2(x, /, y, *, z): # x: 위치허용, y: 둘 다 허용, z: 키워드 전용
    print(f'x: {x}, y: {y}, z: {z}')
    
f2(1, 2, z = 3)
f2(1, y = 2, z = 3)
# f2(1, 2, 3)