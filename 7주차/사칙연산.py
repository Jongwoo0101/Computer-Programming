n = int(input('첫번째 숫자를 입력: '))
op = input('연산자를 입력(+, -, *, /)중 선택: ')
m = int(input("두번째 숫자를 입력: "))

if op == '+':
    print(f'{n} + {m} = {n + m}')
elif op == '-':
    print(f'{n} - {m} = {n - m}')
elif op == '*':
    print(f'{n} * {m} = {n * m}')
elif op == '/':
    print(f'{n} / {m} = {n / m}')
    
else:
    print("연산자를 잘못 입력했습니다.")