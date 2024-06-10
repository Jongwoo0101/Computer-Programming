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