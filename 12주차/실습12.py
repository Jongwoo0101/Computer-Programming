'''
# 함수 작성 예시
def get_sum (start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

value = get_sum(1, 10) # func call
print(value)
print(get_sum(1, 100)) # func call

# 값 반환
def findMax(a, b):
    if a > b:
        fmax = a
        
    else:
        fmax = b
    return fmax

def findMax(a, b):
    if a > b:
        return a
    else:
        return b
        
# return many result
def sub():
    return 1, 2, 3

a, b, c = sub()
print(a, b, c)

# 함수는 호출 전에 정의되어 있어야 함
print('프로그램의 시작')
hello()
print('프로그램의 끝')

def hello():
    print('hello world!')
    
# 파이썬에서는 함수의 매개변수가 기본값을 가질 수 있다. ➔ 기본 매개변수(Default or Optional Parameters)

# 함수 인수를 보내는 방법

def calc(x, y, z):
    return x - y + z

print(calc(y= 20, x = 10, z= 10)) # -> 여기서 y x z 는 키워드 인수이다
print(calc(20, 10, 30)) # -> 여기서 20 10 30은 위치 인수이다


# call by object
def modify(n):
    n += 1
    
k = 10
print('함수 호출 전 k = ', k)
modify(k)
print('함수 호출 후 k = ', k)

# 지역 변수
def sub():
    s = 'i love banana'
    print(s)
sub()

def sub():
    s = 'i love banana'
    print(s)
    
sub()
print(s) # "s"이(가) 정의되지 않았습니다.PylancereportUndefinedVariable (function) s: Any


def sub():
    print(s)
s = 'i love apple'
sub()

def func1(a):
    return a + x

def func2(a):
    x = 10
    return a + x

x = 1

print('fun1(100) result : ', func1(100))
print('fun2(100) result : ', func2(100))
print('after function x result', x)

def func1(a):
    return a + x

def func2(a):
    global x
    x = 10
    return a + x

x = 1

print('fun1(100) result : ', func1(100))
print('fun2(100) result : ', func2(100))
print('after function x result', x)

'''

# Docstring -> Document String - 문서화
# 함수에 대한 설명을 함수 내에 넣을 수 있는 기능

# def greet(name):
#    '''
#    This function greets to the person passed in as a parameter
#    '''
#    print("Hello" + name + "Good morning")
    
# print(help(greet))
# print(greet.__doc__)



