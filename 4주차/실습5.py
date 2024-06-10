'''
불린형은 참(True) 또는 거짓(False)을 나타내는 데이터형
isRight = False
print('type :', type(isRight), ', id=', id(isRight))

print(bool(0))
print(bool(1))
print(bool('test'))
print(bool(''))
print(bool(None))

문자들의 순서있는 집합(sequence of characters)으로 str형이라 함
문자를 표현하기 위한 데이터형으로 작은 따옴표, 큰따옴표로 텍스트를 감싸서 표현

name = 'Hong'
print(type(name))
print(id(name))

문자열 내에 작은 따옴표(‘)나 큰따옴표(“)가 있는 경우에는
▪ 서로 다른 따옴표로 묶어준다.
▪ 역슬래시(\)를 작은 따옴표나 큰따옴표 앞에 기술한다.

intro = '나는 "홍길동"이야'
print(intro)
print("나는 \"홍길동\"이야.")


\n = 줄바꿈
p = "본 교재는 Python을\n보다 쉽게 공부할수 있도록 한 교재입니다.\n저자"
print(p)

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래쉬 세개 출력")
print(r"\n \t \" \\를 그대로 출력")

◼ 문자열에서 지원하는 연산자
▪ 더하기(+): 문자열을 연결(병합)
• 문자열끼리는 더하기(+)를 생략 할 수 있음
▪ 곱하기(*): 문자열을 반복

함수 | 내용 
str() | 괄호 안의 데이터를 문자로 변환
int() | 괄호 안의 데이터를 정수로 변환
float() | 괄호 안의 데이터를 실수로 변환
bool() | 괄호 안의 데이터를 논리형으로 변환

print("%d" %123)

name = '홍길동'
age = 20
age2 = 200
print("%s는 %d살 입니다" % (name, age))

print('%f' % 1234)
print('%.2f' % 1.234)
print('%7.2f' % 1.234)
print('%7s' % 'hong')

◼ f-String 방법
▪ 문자열에 변수의 값을 삽입하여 출력하고 싶으면 문자열이 시작하는 따옴표 전에 f를 쓰고 문자열 안에서 중
괄호{ }안에 변수명을 입력한다.
price = 10000
print(f'상품의 가격은 {price}원입니다.')
time = '12:00pm'
message = f'현재 시간은 {time}입니다.'
print(message)

a = 1.23
b = 3.45
print(f'{a} * {b} = {a*b:.2f}')

word = 'Python'
print(word[0])
print(word[5])
print(word[-1])
print(word[-6])
print('Python'[0])
print('Python'[5])
print('Python'[-1])



s = 'Monty-python'
print(s[0])
print(s[:3]) # 0, 1, 2
print(s[5:]) # 5 ~ last

word = 'Monty Python'

print(word[:5])
print(word[5:])
print(word[6:-2])
print(word[10:5])
print(word[-3:-5])
print(word[2:10:3])
print(word[10:5:-2])

a = '대한민국만세'
print(a[1:3:1])
print(a[::-1])
print(a[::2])
print(a[1:3:])


'''
