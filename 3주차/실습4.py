'''
# 할당 연산자 (=): 변수에 값을 대입할 때 사용

x = 100 + 200

# 100 = x + y # 등호 왼쪽이 변수가 아니면 문제 발생, 잘못된 수식

x = y = 100 # 여러 개의 변수에 동일한 값을 저장

x = y = z = 0 # 하나의 값을 여러 변수에 할당

x, y, z = 10, 20, 30 # 한번에 여러 개의 변수 초기화 (변수와 값의 개수가 일치해야 함)
 
x, y = y, x # x와 y값을 서로 교환

x = 1000
print("초기값 x = ", x)
x += 2
print("x += 2 후의 x = ", x)
x -= 2
print("x -= 2 후의 x = ", x)

string = '강남'
string += '대학교'
print(string)
print(string * 8)
string *= 3
print(string)

name = input('What is your first name? ')
print(name)

# input() 함수는 사용자의 입력을 무조건 문자열 형태로 반환
name = input("이름이 무엇인가요? ")
print("만나서 반갑습니다. " + name + "씨!")
# age = input("나이는요?")
age  = int(input("나이 입력: "))
print(age)
print("네, 그러면 당신은 이미 " + str(age) + "살이시군요," + name + "씨!")
print("네, 그러면 당신은 이미 ", age, "살이시군요," + name + "씨!")

x = input("첫 번째 정수: ")
y = input("두 번째 정수: ")
sum = x + y
print("합은 ", sum)

x = int(input("첫 번쨰 정수: "))
y = int(input("두 번째 정수: "))
sum = x + y
print("합은 ", sum)

a = 10
b = 10
print(id(a), id(b))
# 4381465520 4381465520 주소가 같은것을 확인

a = 5000
b = 5000

print(id(a)==id(b))
# False

a = 2 ** 1024
print(type(a))


a = 314e-2
print(a)
b = 0.123456789012345678901234567890
print(b)


round() 함수
▪ 숫자를 가장 가까운 정수로 반올림하는 역할을 한다.
▪ round(number, ndigits=None)
• ndigits : 생략되거나 None 이면 가장 가까운 정수를 반환
• number를 소수점 다음에 ndigits 으로 반올림
• 실수의 특성상 round() 동작이 예상과 다를 수 있다. 

print(round(3.14159))
print(round(3.74159))
print(round(3.14159, 2))
print(round(3.14859, 2))

'''