import random

tries = 0
guess = 0
answer = random.randint(1, 100)

print("1부터 100사이의 숫자를 맞추시오")

while guess != answer and tries < 10:
    guess = int(input("숫자를 입력하시오: "))
    tries += 1
    if guess < answer:
        print("정답보다 낮음!")
        
    elif guess > answer:
        print("정답보다 높음")

if guess == answer:
    print("축하합니다. 시도횟수 = ", tries)
    
else:
    print("정답은: ", answer)