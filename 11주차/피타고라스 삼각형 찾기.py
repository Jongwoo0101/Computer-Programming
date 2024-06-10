'''
# while 문을 이용하고 사용자에게 입력을 받는 방식으로 구현
i = 1

while(i == 1):
    
    a = int(input("a값을 입력해주세요: "))
    b = int(input("b값을 입력해주세요: "))
    c = int(input("c값을 입력해주세요: "))

    sum = a*a + b*b

    if sum == c*c:
        print('피타고라스 삼각형 입니다.')

    else:
        print("피타고라스 삼각형이 아닙니다")

    i = int(input("계속하려면 1을 입력하세요.\n종료하려면 1이외의 다른 숫자를 입력하세요."))
'''

# 정석 답
n = 0

for a in range(1, 101, 1):
    for b in range(1, 101, 1):
        for c in range(1, 101, 1):
            if (a * a + b * b == c * c):
                print(f'a = {a} b = {b} c = {c}')
                n += 1
print(f'100보다 작은 삼각형 중에서 피타고라스의 정리가 성립하는 직각 삼각형은 총 {n}개 입니다.')