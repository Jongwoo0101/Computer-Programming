'''
fact = 1

n = int(input("정수를 입력하시오: "))

for i in range(1, n+1):
    fact = fact * i
    
print(n, "!은", fact, "이다.")
'''


# 재귀
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
        

n = int(input("정수를 입력하시오: "))

print(f'{n}!은 {factorial(n)}입니다')