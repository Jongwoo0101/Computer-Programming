'''
for y in range(5):
    for x in range(10):
        print("*", end="")
    print("")

for line in range(10):
    for star in range(line + 1):
        print('*', end='')
    print()


for line in range(1, 11, 1):
    for star in range(11 - line):
        print('*', end='')
    print()

for line in range(10, 0, -1):
    print('*' * line)

for line in range(1, 11, 1):
    for star in range(1, 11 - line):
        print(" ", end='')
    for i in range(1, line + 1):
        print('*', end='')
    print()

for line in range(1, 11, 1):
    print(' ' * (10 - line) + '*' * line)
'''

'''

test output
1
22
333
4444
55555


for line in range(1, 6, 1):
    for star in range(line):
        print(line, end='')
    print()

'''

'''
# check print function type
print(type(print))

# define hello function
def hello():
    print('Hello')

# check hello function's type
print(type(hello))

# check python default builtin function
print(dir(__builtins__))

'''

'''
함수의 기본구조
# 함수 정의
def 함수명 ([매개변수1, 매개변수2, ..., 매개변수 n]):
    함수내 수행할 문장1
    함수내 수행할 문장2
    ...
    return 반환값

#함수 호출
함수명(인수1, ... , 인수n)
'''

'''
def print_address():
    print('경상북도')
    print('울릉군 울릉읍')
    print('독도시 산 1-96번지')

print_address()

def get_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

value = get_sum(1, 10)
print(value)
print(get_sum(1, 100))

'''
