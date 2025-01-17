'''
# ◼ 파이썬은 여러 개의 값을 모아서 하나의 변수에 저장할 수 있다.
# ▪ 개별적인 값들을 하나의 변수에 담아서 처리
# ▪ 매번 변수의 이름을 작성하고 관리하는 것보다 편리하고 효율적
# ◼ 리스트는 [ ] 안에 값을 나열하고 값과 값 사이에 콤마를 찍으면 된다.
#  list_name = [ 값1, 값2, 값3, ... , 값n ]

shopping_list = ['milk', 'eggs', 'cheese', 'butter', 'cream']
print(shopping_list)
print(type(shopping_list))

nums = [10, 20, 30, 40, 50]
print(type(nums))
print(id(nums))

# ◼ 리스트는 정수, 문자열, 실수 등 서로 다른 데이터형도 하나로 묶을 수 있다.
# ◼ 리스트는 문자열과 마찬가지로 0부터 시작하는 인덱스가 있으며 슬라이싱도 가능
# ◼ 리스트는 빈 리스트를 만드는 것을 허용

a = []
b = [1,2,3]
c = [10, 20, '파이썬']
d = [2, 12.3, 'text', ['엄마', '아빠', '형', '동생']]
print(d[0])
print(d[3])
print(d[3][0])

a, b= 100, 200 # a에는 100, b에는 200을 할당하는 동시할당문
print(a==b)
print(a!=b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
# 두 개의 기호로 표현된 비교 연산자는 띄어쓰면 안된다
# 두 개 기호로 표현된 비교 연산자의 순서를 뒤집어도 안된다

# 파이썬은 복합적인 관계식도 가능
a = 5
b = 10
print(0 < a < b)
print(0 < a and a < b)

# 관계 연산자는 숫자뿐만 아니라 객체간에서도 크기를 비교할 수 있다.
# 문자열의 경우 일반적인 사전에서 나오는 단어의 순서와 동일하다.
print('abcd' > 'abc')
print([1,4,2] == [1,2,4])
# 서로 다는 데이터형 간의 값은 비교할 수 없다
# 숫자 데이터형은 예외로 비교가능(정수와 실수인 경우만)

# if - else 문
# ◼ 파이썬에서 선택 구조를 위해 if문 사용
# ◼ 들여쓰기(indent)를 주의하여 작성해야 올바르게 실행
# ▪ 들여쓰기: tab 1번 또는 space 4번
# ▪ 내어쓰기: backspace 키 이용
# ▪ 주의: 들여쓰기를 잘못하면 오류 발생

a = 200
if a < 100:
    print("100보다 작군요")

else:
    print("100과 같거나 크군요")
print("프로그램 끝")

'''
