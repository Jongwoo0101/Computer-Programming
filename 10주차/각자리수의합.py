import random

number = random.randint(100, 10000)

total = 0

while number > 0:
    digit = number % 10
    total += digit
    number = number // 10
    
print(f'자리수의 총 합은 {total} 입니다.')