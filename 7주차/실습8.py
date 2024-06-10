'''
n = int(input("정수를 입력하시오: "))

if n >= 0:
    if n == 0:
        print("0입니다.")
    else:
        print("양수입니다.")
        
else:
    print("음수 입니다.")
    
user_id = ['김철수','홍길동','김영희']

name = input('아이다: ')
if name in user_id:
    password = input('패스워드를 입력하시오.')
    if password == '12345678':
        print('환영합니다.')
    else:
        print('잘못된 패스워드 입니다.')
else:
    print('알 수 없는 사용자입니다!')
    
score = int(input("점수를 입력하세요: "))

if score >= 90:
    print("A학점 입니다.")
    
elif score >= 80:
    print('B학점 입니다.') 

elif score >= 70:
    print('C학점 입니다.') 
    
elif score >= 60:
    print('D학점 입니다.') 

else:
    print('F학점 입니다.')
    
# elif를 이용한 음수 양수 0 판병

n = int(input("정수를 입력하세요: "))

if n > 0:
    print("입력된 정수는 양수입니다.")
    
elif n == 0:
    print("입력된 정수는 0입니다.")
    
else:
    print("입력된 정수는 음수입니다.")
'''

year = int(input("태어난 년도를 입력하세요 : "))

age = 2024 - year + 1

print(age)

if 8 <= age < 14:
    print("초등학생 입니다.")
    
elif 14 <= age < 17:
    print("중학생 입니다.")
    
elif 17 <= age < 20:
    print("고등학생 입니다.")
    
elif 20 <= age < 27:
    print("대학생 입니다.") 