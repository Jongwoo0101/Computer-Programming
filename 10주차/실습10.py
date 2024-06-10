'''
◼ 반복문에서 반복이 완료되기 전에 반복문을 빠져나오는 경우 사용
◼ 무한 루프 사용시 제어를 위해 break문을 사용
◼ break 문은 반복을 강제로 중단시키는 역할을 함


a = 1
while a <= 10:
    print(f'a = {a}')
    
    if a == 5:
        break
    a += 1
    
print('after while')
print() # change line

for a in range(1, 11):
    print(f'a = {a}')
    if a == 5:
        break
print('after for')

a = 0
while a <= 10:
    a += 1
    if a % 3 == 0:
        continue
    print(f'a = {a}')
print('종료')

s = 'I love Python'

for c in s:
    if c in 'aeiouAEIOU':
        continue
    print(c, end='')
    
print()

for c in s:
    if c not in 'aeiouAEIOU':
        print(c, end='')
        
'''

for x in range(6):
    if x == 2:
        break
    print(x, end='')
    
else:
    print("\n반복완료")