total = 0
ans = 'yes'

while ans == 'yes':
    n = int(input("숫자를 입력하세요: "))
    ans = input("계속? (yes/no): ")
    total += n
    
print(f'합계는 : {total}')