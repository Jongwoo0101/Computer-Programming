basic = 0
unit = 0

amount = float(input('전기 사용량을 입력하세요: '))
child = input('다자녀 가정인가요? (예 or 아니오)')

if amount <= 200:
    basic = 910
    unit = 99.3

elif amount <= 400:
    basic = 1600
    unit = 187.9

else:
    basic = 7300
    unit = 280.6
    
totalprice = basic + unit * amount

print('=' * 30)
print(f'사용량: {amount}kwh')
print(f'기본요금: {basic}원')
print(f'단가: {unit}원')
print('전기 요금', end = '')

if child == '예':
    print('(다자녀 할인 적용)', end='')
    totalprice *= 0.8
    
print(f': {totalprice:.0f}원')