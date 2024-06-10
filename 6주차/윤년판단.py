'''
# 사용자에게 입력을 받는 방식
year = int(input("연도를 입력하시요: "))

if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0):
    print(f'{year}년은 윤년입니다')
    
else:
    print(f'{year}년은 윤년이 아닙니다.')
'''

# 랜덤 모듈을 이용하여 하는 방식

import random

year = random.randrange(1900,2024)

if ((year % 4 == 0 and year % 100 !=0) or year % 400 == 0):
    print(f'{year}년은 윤년입니다')
    
else:
    print(f'{year}년은 윤년이 아닙니다.')